# -*- coding: utf-8 -*-
"""
Common-subjects phase: नेपाली / English / (partly) Computer Science are
compulsory for both NEB streams and already have substantial REAL
content-partner content sitting under the Science courses (91, 38). Rather
than author more synthetic content, this script reuses that real content
by creating (or reusing) matching Section rows under the Management
courses (209, 210) and adding new QuestionChapter link rows pointing at
the SAME Question ids - zero Question duplication, zero synthetic
content, exactly the "duplicate common subjects" idea from the plan.

Matching is exact-chapter-name-only, same discipline as
load_question_bank.py / create_subject.py - a chapter with no exact name
match in the source subject is simply left unlinked (not invented, not
fuzzy-matched), and is reported so it can be authored separately if it
turns out to need content (e.g. सामाजिक अध्ययन, whose "एकाइ N ..." chapter
titles differ in exact wording between the Management shell and the
Science course even though the topics are the same - confirmed NOT safe
to link this way, left for separate fresh authoring).

Two operations, both idempotent (safe to re-run):

  create_and_link(target_course_id, subject_name, source_subject_id)
      Creates a brand-new Subject+Chapter shell under target_course_id,
      chapter names copied VERBATIM (queried live, never hand-transcribed
      - this dataset includes Devanagari text where a typo would be easy
      to introduce by hand) from source_subject_id's chapters, then links
      every source chapter's questions into the new matching chapter.
      Refuses to create a duplicate subject if one already exists by that
      name (same guard as create_subject.py).

  link_existing(target_subject_id, source_subject_id)
      For a shell that already exists under the Management course (e.g.
      नेपाली, whose chapter names were already part of 209/210's original
      empty-shell structure), matches by exact chapter name and links
      questions. Chapters in target with no exact match in source are
      reported, not created.

Usage (from `backend/`), see __main__ for the exact calls made for this
session's Common-subjects phase.
"""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy import func

from app.database import SessionLocal
from app import models


def chapters_under_subject(db, subject_id):
    result = []
    stack = [subject_id]
    while stack:
        pid = stack.pop()
        children = db.query(models.Section).filter(models.Section.parent_id == pid).all()
        for c in children:
            if c.type == "Chapter":
                result.append(c)
            else:
                stack.append(c.id)
    return result


def _link_chapter_questions(db, source_chapter_id, target_chapter_id):
    source_qids = {
        row.question_id
        for row in db.query(models.QuestionChapter).filter(
            models.QuestionChapter.chapter_id == source_chapter_id
        )
    }
    already_linked = {
        row.question_id
        for row in db.query(models.QuestionChapter).filter(
            models.QuestionChapter.chapter_id == target_chapter_id
        )
    }
    to_link = source_qids - already_linked
    for qid in to_link:
        db.add(models.QuestionChapter(question_id=qid, chapter_id=target_chapter_id))
    return len(to_link), len(source_qids)


def link_existing(target_subject_id, source_subject_id):
    db = SessionLocal()
    report = {"target_subject_id": target_subject_id, "source_subject_id": source_subject_id}

    target_chapters = chapters_under_subject(db, target_subject_id)
    source_chapters = {c.name: c for c in chapters_under_subject(db, source_subject_id)}

    linked, unmatched = {}, []
    for tc in target_chapters:
        sc = source_chapters.get(tc.name)
        if sc is None:
            unmatched.append(tc.name)
            continue
        n_new, n_total = _link_chapter_questions(db, sc.id, tc.id)
        linked[tc.name] = {"target_chapter_id": tc.id, "source_chapter_id": sc.id,
                            "questions_linked_new": n_new, "questions_available": n_total}

    db.commit()
    report["linked"] = linked
    report["unmatched_target_chapters"] = unmatched
    report["chapters_linked"] = len(linked)
    report["chapters_unmatched"] = len(unmatched)
    db.close()
    return report


def create_and_link(target_course_id, subject_name, source_subject_id):
    db = SessionLocal()
    report = {"course_id": target_course_id, "subject_name": subject_name, "source_subject_id": source_subject_id}

    existing = (
        db.query(models.Section)
          .filter(models.Section.course_id == target_course_id, models.Section.type == "Subject",
                   models.Section.name == subject_name)
          .first()
    )
    if existing is not None:
        report["note"] = f"Subject {subject_name!r} already exists under course {target_course_id} (id={existing.id}) - reusing it, not creating a duplicate"
        target_subject_id = existing.id
    else:
        source_chapters = chapters_under_subject(db, source_subject_id)
        next_id = (db.query(func.max(models.Section.id)).scalar() or 0) + 1
        target_subject_id = next_id
        db.add(models.Section(id=target_subject_id, name=subject_name, type="Subject", parent_id=None, course_id=target_course_id))
        next_id += 1
        name_to_new_chapter_id = {}
        for sc in source_chapters:
            db.add(models.Section(id=next_id, name=sc.name, type="Chapter", parent_id=target_subject_id, course_id=target_course_id))
            name_to_new_chapter_id[sc.name] = next_id
            next_id += 1
        db.commit()
        report["subject_id"] = target_subject_id
        report["chapters_created"] = len(name_to_new_chapter_id)

    db.close()

    link_report = link_existing(target_subject_id, source_subject_id)
    report["link_report"] = link_report
    return report


if __name__ == "__main__":
    import json

    results = {}

    # नेपाली: shells already exist under 209/210 (original empty-shell
    # structure) - link only, no creation.
    results["209_nepali_link"] = link_existing(target_subject_id=34310, source_subject_id=23982)   # 209 नेपाली <- 91 नेपाली
    results["210_nepali_link"] = link_existing(target_subject_id=34298, source_subject_id=11494)   # 210 नेपाली <- 38 नेपाली

    # English: no shell exists under 209/210 at all - create from source
    # chapter names, then link.
    results["209_english_create_link"] = create_and_link(209, "English", source_subject_id=35113)  # 91 Compulsory English
    results["210_english_create_link"] = create_and_link(210, "English", source_subject_id=18072)  # 38 English

    # Computer Science: 209 has no shell; 91's intro-CS content is real
    # and topically coherent for grade 11 - create from source and link.
    results["209_cs_create_link"] = create_and_link(209, "Computer Science", source_subject_id=25838)  # 91 Computer Science

    print(json.dumps(results, indent=2, ensure_ascii=False, default=str))
