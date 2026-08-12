# -*- coding: utf-8 -*-
"""
One-time migration: every question inserted so far by
load_question_bank.py / load_by_chapter_id.py stored its options in the
authored content module's own order, and every content module happened
to write its correct option first ("correct": 0). Neither loader
shuffled on insert (fixed in this same change), so 2,319 of 2,320
Management-course questions (course 209/210) ended up with
correct_answer=0 - a student could score 100% by always picking option A.

This script re-shuffles the options (and recomputes correct_answer) in
place for exactly those affected rows, identified the same way the audit
did: Question.source == 'synthetic', linked via QuestionChapter to a
Section under course_id in (209, 210), body NOT starting with the old
clean_and_fill.py placeholder marker (that placeholder content is a
different, already-fine population and is left untouched).

Usage (from `backend/`):
    python -m scripts.fix_correct_answer_shuffle
"""
import json
import random
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).parent.parent))

from collections import Counter

from app.database import SessionLocal
from app import models


def _shuffled_options(options: list[str], correct: int) -> tuple[list[str], int]:
    order = list(range(len(options)))
    random.shuffle(order)
    new_options = [options[i] for i in order]
    new_correct = order.index(correct)
    return new_options, new_correct


def main():
    db = SessionLocal()

    questions = (
        db.query(models.Question)
          .join(models.QuestionChapter, models.QuestionChapter.question_id == models.Question.id)
          .join(models.Section, models.Section.id == models.QuestionChapter.chapter_id)
          .filter(models.Section.course_id.in_([209, 210]))
          .filter(models.Question.source == "synthetic")
          .filter(~models.Question.body.startswith("[SYNTHETIC PLACEHOLDER]"))
          .distinct()
          .all()
    )

    before = Counter(q.correct_answer for q in questions)

    for q in questions:
        answers = json.loads(q.answers_json)
        options = [a["answer"] for a in answers]
        new_options, new_correct = _shuffled_options(options, q.correct_answer)
        q.answers_json = json.dumps([{"answer": opt} for opt in new_options], ensure_ascii=False)
        q.correct_answer = new_correct

    db.commit()

    after = Counter(q.correct_answer for q in questions)
    report = {
        "questions_migrated": len(questions),
        "correct_answer_distribution_before": dict(sorted(before.items())),
        "correct_answer_distribution_after": dict(sorted(after.items())),
    }
    db.close()
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
