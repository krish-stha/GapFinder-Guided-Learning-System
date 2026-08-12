# -*- coding: utf-8 -*-
"""
Loads an authored question bank (see scripts/content/*.py) into the
database: creates Question rows (source='synthetic') and links them to
the matching Chapter Section under a given course/subject via
QuestionChapter. Reusable across every Management-course content batch
(Business Studies, Economics, Accounting, Business Maths, ...).

Chapter matching is by EXACT name equality against Section rows already
in the database - never fuzzy-matched (see consolidate_courses.py's
module docstring for why). If a bank's chapter name has no exact match,
the script aborts before writing anything rather than guessing.

Some subjects legitimately have two Chapter rows with the IDENTICAL name
(e.g. "Principle of Accounting-I" has two chapters both named "Book of
Original Entry- Journal, Ledgers Account and Trial Balance", ids 34353
and 34626 - a real quirk in the source curriculum data, not a bug). When
a name matches N>1 chapters, the content module's question list for that
name must be evenly divisible by N; it is split into N consecutive,
equal-sized batches and assigned one batch per chapter, ordered by
chapter id ascending, so the split is deterministic and reproducible.

Usage (from `backend/`):
    python -m scripts.load_question_bank <course_id> <subject_name> <content_module>

Example:
    python -m scripts.load_question_bank 209 "Business Studies" scripts.content.grade11_business_studies
"""
import argparse
import importlib
import json
import random
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy import func

from app.database import SessionLocal
from app import models

DIFFICULTY_TO_LEVEL = {"Easy": 1, "Medium": 3, "Hard": 5}


def _shuffled_options(options: list[str], correct: int) -> tuple[list[str], int]:
    """Shuffle option order together with the correct index, so
    correct_answer isn't predictably 0 for every authored question - every
    content/*.py file writes "correct" as an index into its own authored
    option order, which happened to be position 0 nearly always; storage
    must not preserve that bias."""
    order = list(range(len(options)))
    random.shuffle(order)
    new_options = [options[i] for i in order]
    new_correct = order.index(correct)
    return new_options, new_correct


def load_bank(course_id: int, subject_name: str, questions_by_chapter: dict) -> dict:
    db = SessionLocal()
    report: dict = {"course_id": course_id, "subject_name": subject_name}

    subject = (
        db.query(models.Section)
          .filter(models.Section.course_id == course_id, models.Section.type == "Subject",
                   models.Section.name == subject_name)
          .first()
    )
    if subject is None:
        report["ABORTED"] = f"no Subject section named {subject_name!r} under course {course_id}"
        db.close()
        return report

    # resolve every chapter name to its Section id(s) under this subject
    # first, so we abort before writing anything if a name doesn't match
    # (or doesn't split evenly across a duplicate-named pair)
    assignments = []  # list of (chapter_name, chapter_id, item_batch)
    unmatched, uneven = [], []
    for chapter_name, items in questions_by_chapter.items():
        chapters = (
            db.query(models.Section)
              .filter(models.Section.course_id == course_id, models.Section.type == "Chapter",
                       models.Section.name == chapter_name)
              .order_by(models.Section.id)
              .all()
        )
        if not chapters:
            unmatched.append(chapter_name)
            continue
        if len(items) % len(chapters) != 0:
            uneven.append({"chapter_name": chapter_name, "matches": len(chapters), "items_supplied": len(items)})
            continue
        batch_size = len(items) // len(chapters)
        for i, chapter in enumerate(chapters):
            batch = items[i * batch_size:(i + 1) * batch_size]
            assignments.append((chapter_name, chapter.id, batch))

    if unmatched or uneven:
        report["ABORTED"] = "chapter matching failed - fix the content module, nothing written"
        if unmatched:
            report["unmatched_chapter_names"] = unmatched
        if uneven:
            report["uneven_split_chapter_names"] = uneven
        db.close()
        return report

    next_id = (db.query(func.max(models.Question.id)).scalar() or 0) + 1
    inserted = {}
    for chapter_name, chapter_id, batch in assignments:
        count = 0
        for item in batch:
            shuffled_options, shuffled_correct = _shuffled_options(item["options"], item["correct"])
            answers_json = json.dumps([{"answer": opt} for opt in shuffled_options], ensure_ascii=False)
            q = models.Question(
                id=next_id, body=item["q"], answers_json=answers_json,
                correct_answer=shuffled_correct, level=DIFFICULTY_TO_LEVEL.get(item["difficulty"], 3),
                difficulty_label=item["difficulty"], question_type="MCQ",
                source="synthetic", scoreable=True,
            )
            db.add(q)
            db.add(models.QuestionChapter(question_id=next_id, chapter_id=chapter_id))
            next_id += 1
            count += 1
        inserted.setdefault(chapter_name, []).append({"chapter_id": chapter_id, "questions_added": count})

    db.commit()
    report["inserted"] = inserted
    report["total_questions_added"] = sum(b["questions_added"] for batches in inserted.values() for b in batches)

    # verify every targeted chapter now has >=20 scoreable questions
    coverage = {}
    for chapter_name, chapter_id, _ in assignments:
        n = (
            db.query(func.count(models.QuestionChapter.question_id))
              .join(models.Question, models.Question.id == models.QuestionChapter.question_id)
              .filter(models.QuestionChapter.chapter_id == chapter_id, models.Question.scoreable == True)
              .scalar()
        )
        coverage[f"{chapter_name} (id={chapter_id})"] = n
    report["coverage_after"] = coverage
    report["all_chapters_at_or_above_20"] = all(n >= 20 for n in coverage.values())

    db.close()
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("course_id", type=int)
    parser.add_argument("subject_name")
    parser.add_argument("content_module")
    args = parser.parse_args()

    module = importlib.import_module(args.content_module)
    result = load_bank(args.course_id, args.subject_name, module.QUESTIONS)
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
