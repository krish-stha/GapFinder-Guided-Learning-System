"""
One-time copy of every row from the existing SQLite dev DB into a fresh
Postgres database, for the SQLite -> Postgres upgrade (`DATABASE_URL` in
.env). Run once, after DATABASE_URL is already pointed at Postgres and
before the app has written anything real to it - the target is assumed
empty (this creates the schema itself via Base.metadata.create_all(),
doesn't merge into an already-populated one).

    python -m scripts.migrate_sqlite_to_postgres

Two things this handles that a naive per-table copy would get wrong:

1. Insertion order across foreign keys. Student.class_id -> classes.id and
   SchoolClass.teacher_id -> students.id form a genuine cycle (a class
   references its teacher, a teacher-as-student row can reference a
   class), on top of Section's own self-reference (parent_id -> sections.id).
   Rather than hand-solving a topological order for every table (and
   re-solving it again next time a model changes), this wraps the whole
   bulk load in Postgres's `session_replication_role = replica`, which
   suspends FK enforcement for the current session the same way pg_dump's
   own restore does - insert everything in whatever order, since every
   row is a byte-for-byte copy of already-valid source data, then restore
   normal enforcement.

2. Sequence drift. Every plain `Column(Integer, primary_key=True)` in
   models.py becomes a Postgres SERIAL/IDENTITY column with its own
   sequence - but inserting rows with explicit ids (as this script does,
   to preserve every foreign key relationship exactly) never advances
   that sequence. Skip this and the ceiling looks fine until the first
   real INSERT after migration (a new registration, a new attempt, ...)
   collides with an id that already exists. Every table's sequence is
   reset to MAX(id)+1 (or left at 1 for an empty table) after the copy.

ALWAYS back up the target if it's not genuinely empty before running this -
same convention as every other migration script in this directory.
"""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy import create_engine, text

from app.database import Base, DATABASE_URL
from app import models  # noqa: F401 - registers every table on Base.metadata

SQLITE_URL = "sqlite:///./guided_learning.db"


def migrate() -> dict:
    report: dict = {}

    if not DATABASE_URL.startswith("postgresql"):
        report["ABORTED"] = (
            f"DATABASE_URL is not a postgresql:// URL ({DATABASE_URL!r}) - "
            "set it in .env and re-run, nothing was touched"
        )
        return report

    sqlite_engine = create_engine(SQLITE_URL)
    pg_engine = create_engine(DATABASE_URL)

    # target-empty precondition - refuse to run into a DB with real data
    # already in it, rather than silently duplicating or half-overwriting
    Base.metadata.create_all(bind=pg_engine)
    with pg_engine.connect() as conn:
        existing_students = conn.execute(text("SELECT COUNT(*) FROM students")).scalar()
    if existing_students:
        report["ABORTED"] = (
            f"target Postgres DB already has {existing_students} student row(s) - "
            "refusing to run against a non-empty target, nothing was written"
        )
        return report

    row_counts: dict[str, int] = {}
    with sqlite_engine.connect() as src, pg_engine.begin() as dst:
        dst.execute(text("SET session_replication_role = 'replica'"))
        for table in Base.metadata.sorted_tables:
            rows = [dict(r) for r in src.execute(table.select()).mappings().all()]
            row_counts[table.name] = len(rows)
            if rows:
                dst.execute(table.insert(), rows)
        dst.execute(text("SET session_replication_role = 'origin'"))

        # advance every SERIAL sequence past the explicit ids just inserted
        sequences_reset = []
        for table in Base.metadata.sorted_tables:
            if "id" not in table.c:
                continue
            seq_row = dst.execute(text("SELECT pg_get_serial_sequence(:t, 'id')"), {"t": table.name}).scalar()
            if not seq_row:
                continue
            dst.execute(text(
                f"SELECT setval(:seq, COALESCE((SELECT MAX(id) FROM {table.name}), 1), "
                f"(SELECT MAX(id) FROM {table.name}) IS NOT NULL)"
            ), {"seq": seq_row})
            sequences_reset.append(table.name)

    report["row_counts"] = row_counts
    report["total_rows_copied"] = sum(row_counts.values())
    report["sequences_reset"] = sequences_reset

    # verify: every table's Postgres count matches its SQLite source count
    mismatches = {}
    with pg_engine.connect() as conn:
        for table_name, expected in row_counts.items():
            actual = conn.execute(text(f"SELECT COUNT(*) FROM {table_name}")).scalar()
            if actual != expected:
                mismatches[table_name] = {"expected": expected, "actual": actual}
    report["row_count_mismatches"] = mismatches
    report["verified"] = not mismatches

    return report


if __name__ == "__main__":
    import json
    print(json.dumps(migrate(), indent=2, ensure_ascii=False))
