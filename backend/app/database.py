import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker, declarative_base

# Loaded here (not only in main.py) so every entry point that imports this
# module - scripts/, pytest, the app itself - picks up DATABASE_URL from
# .env consistently, not just the ones that happen to run through main.py
# first. Safe to call more than once (main.py also calls it before this
# module is imported); idempotent.
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

# SQLite by default for local dev/demo; set DATABASE_URL in .env to a
# postgresql:// URL to use Postgres instead - see scripts/migrate_sqlite_to_postgres.py
# for a one-time data copy when switching an existing dev DB over.
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./guided_learning.db")

# check_same_thread is a SQLite-only connect arg - psycopg2 (Postgres)
# doesn't recognize it and would error if passed.
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def run_dev_migrations():
    """Base.metadata.create_all() only creates missing TABLES, never adds
    columns to ones that already exist - there's no Alembic yet (flagged
    Further Work). For a dev DB with model changes like adding Student.role,
    patch it forward here instead of losing data by deleting/recreating.
    Each check is a no-op once the column exists - which is always true for
    a brand-new Postgres DB, since create_all() already creates every
    column current models.py defines; these blocks only matter for an
    existing DB predating a given model change. Note for future additions:
    unlike SQLite (which treats booleans as 0/1 integers), Postgres's real
    BOOLEAN type rejects `DEFAULT 0`/`DEFAULT 1` outright - use `DEFAULT
    false`/`DEFAULT true` in any new ALTER TABLE block instead."""
    inspector = inspect(engine)
    if "students" not in inspector.get_table_names():
        return
    columns = {c["name"] for c in inspector.get_columns("students")}
    if "role" not in columns:
        with engine.begin() as conn:
            conn.execute(text("ALTER TABLE students ADD COLUMN role VARCHAR DEFAULT 'student'"))
    if "email_verified" not in columns:
        with engine.begin() as conn:
            conn.execute(text("ALTER TABLE students ADD COLUMN email_verified BOOLEAN DEFAULT 0"))
    if "class_id" not in columns:
        with engine.begin() as conn:
            conn.execute(text("ALTER TABLE students ADD COLUMN class_id INTEGER"))

    if "practice_sessions" in inspector.get_table_names():
        ps_columns = {c["name"] for c in inspector.get_columns("practice_sessions")}
        if "time_limit_seconds" not in ps_columns:
            with engine.begin() as conn:
                conn.execute(text("ALTER TABLE practice_sessions ADD COLUMN time_limit_seconds INTEGER"))

    if "attempts" in inspector.get_table_names():
        att_columns = {c["name"] for c in inspector.get_columns("attempts")}
        if "marked_for_review" not in att_columns:
            with engine.begin() as conn:
                conn.execute(text("ALTER TABLE attempts ADD COLUMN marked_for_review BOOLEAN DEFAULT 0"))
        if "position" not in att_columns:
            with engine.begin() as conn:
                conn.execute(text("ALTER TABLE attempts ADD COLUMN position INTEGER"))

    if "questions" in inspector.get_table_names():
        q_columns = {c["name"] for c in inspector.get_columns("questions")}
        if "explanation" not in q_columns:
            with engine.begin() as conn:
                conn.execute(text("ALTER TABLE questions ADD COLUMN explanation TEXT"))
