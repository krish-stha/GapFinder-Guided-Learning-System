# -*- coding: utf-8 -*-
"""
Creates a new Subject Section (and flat Chapter children, Subject ->
Chapter, no intermediate Unit level - functionally equivalent, simpler)
under a course, for cases where the target course has no existing
scaffolding for a legitimate subject. Used when a Management-course
shell (209/210) is missing a subject its sibling Science/generic course
has (e.g. course 209 "NEB Grade 11 Management" has no Business Maths
subject at all). New Section ids continue from MAX(sections.id)+1.

Refuses to create a subject that already exists by that exact name under
the given course, so it's safe to re-run without creating duplicates.

Usage (from `backend/`):
    python -m scripts.create_subject <course_id> "<Subject Name>" <content_module>

<content_module> must expose a QUESTIONS dict (see scripts/content/*.py)
- its keys become the new chapter names, one Chapter Section per key.
"""
import argparse
import importlib
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy import func

from app.database import SessionLocal
from app import models


def create_subject(course_id: int, subject_name: str, chapter_names: list) -> dict:
    db = SessionLocal()
    report: dict = {"course_id": course_id, "subject_name": subject_name}

    existing = (
        db.query(models.Section)
          .filter(models.Section.course_id == course_id, models.Section.type == "Subject",
                   models.Section.name == subject_name)
          .first()
    )
    if existing is not None:
        report["ABORTED"] = f"Subject {subject_name!r} already exists under course {course_id} (id={existing.id}) - not creating a duplicate"
        db.close()
        return report

    next_id = (db.query(func.max(models.Section.id)).scalar() or 0) + 1

    subject_id = next_id
    db.add(models.Section(id=subject_id, name=subject_name, type="Subject", parent_id=None, course_id=course_id))
    next_id += 1

    chapter_ids = {}
    for chapter_name in chapter_names:
        db.add(models.Section(id=next_id, name=chapter_name, type="Chapter", parent_id=subject_id, course_id=course_id))
        chapter_ids[chapter_name] = next_id
        next_id += 1

    db.commit()
    report["subject_id"] = subject_id
    report["chapter_ids"] = chapter_ids
    report["chapters_created"] = len(chapter_ids)
    db.close()
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("course_id", type=int)
    parser.add_argument("subject_name")
    parser.add_argument("content_module")
    args = parser.parse_args()

    module = importlib.import_module(args.content_module)
    result = create_subject(args.course_id, args.subject_name, list(module.QUESTIONS.keys()))
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
