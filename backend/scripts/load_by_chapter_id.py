# -*- coding: utf-8 -*-
"""
Loader variant for chapters whose real names are Devanagari text with
subtle spacing quirks (confirmed via live query, e.g. a chapter titled
with a double space before an embedded English translation) - retyping
such strings by hand as dict keys for load_question_bank.py's exact-name
matching would risk an invisible typo silently producing an
"unmatched_chapter_names" abort, or worse, a false non-match that looks
like a real content gap. Since the chapter ids were already verified via
a live DB query (not guessed), this loader keys content by chapter_id
(int) directly instead of by name - same content-shape and safety
guarantees (validates the chapter exists and is type='Chapter' before
writing, new Question ids continue from MAX(questions.id)+1), just a
different, typo-proof matching key for this specific case.

Usage: import and call load_by_chapter_id(QUESTIONS) from a one-off
script, where QUESTIONS is {chapter_id: [ {q, options, correct,
difficulty}, ... ]}.
"""
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
    """See load_question_bank.py's identical helper - authored content
    modules write "correct" against their own option order, which is
    almost always 0; storage must not preserve that bias."""
    order = list(range(len(options)))
    random.shuffle(order)
    new_options = [options[i] for i in order]
    new_correct = order.index(correct)
    return new_options, new_correct


def load_by_chapter_id(questions_by_chapter_id: dict) -> dict:
    db = SessionLocal()
    report = {"inserted": {}, "coverage_after": {}}

    bad_ids = []
    for chapter_id in questions_by_chapter_id:
        section = db.query(models.Section).filter(models.Section.id == chapter_id).first()
        if section is None or section.type != "Chapter":
            bad_ids.append(chapter_id)
    if bad_ids:
        report["ABORTED"] = f"chapter_ids not found or not type=Chapter: {bad_ids}"
        db.close()
        return report

    next_id = (db.query(func.max(models.Question.id)).scalar() or 0) + 1

    for chapter_id, items in questions_by_chapter_id.items():
        section = db.query(models.Section).filter(models.Section.id == chapter_id).first()
        added = 0
        for item in items:
            shuffled_options, shuffled_correct = _shuffled_options(item["options"], item["correct"])
            q = models.Question(
                id=next_id,
                body=item["q"],
                answers_json=json.dumps([{"answer": a} for a in shuffled_options]),
                correct_answer=shuffled_correct,
                level=DIFFICULTY_TO_LEVEL[item["difficulty"]],
                difficulty_label=item["difficulty"],
                question_type="MCQ",
                source="synthetic",
                scoreable=True,
            )
            db.add(q)
            db.add(models.QuestionChapter(question_id=next_id, chapter_id=chapter_id))
            next_id += 1
            added += 1
        report["inserted"][f"{section.name} (id={chapter_id})"] = added

    db.commit()

    for chapter_id in questions_by_chapter_id:
        count = db.query(models.QuestionChapter).filter(models.QuestionChapter.chapter_id == chapter_id).count()
        section = db.query(models.Section).filter(models.Section.id == chapter_id).first()
        report["coverage_after"][f"{section.name} (id={chapter_id})"] = count

    report["total_questions_added"] = sum(report["inserted"].values())
    report["all_chapters_at_or_above_20"] = all(c >= 20 for c in report["coverage_after"].values())
    db.close()
    return report
