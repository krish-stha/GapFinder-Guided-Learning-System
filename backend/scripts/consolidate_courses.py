"""
One-time course-consolidation migration (project feedback: merge 9
overlapping courses down to 6, remove the off-topic one). Run manually,
phase by phase, from `backend/`:

    python -m scripts.consolidate_courses verify

Each phase is its own function with its own verification query, meant to
be run once in order, reading the printed report between phases rather
than trusting the earlier planning-time numbers blindly - this script
re-derives everything live against the actual database.

Design rule this script follows throughout: real (`source='real'`)
content is NEVER auto-matched or merged by heuristic (e.g. fuzzy chapter
name matching) - only by exact `question_id`, or by a human-reviewed fixed
subject classification table. A false-positive heuristic match would
silently misattribute real academic content to the wrong chapter, which
is a correctness bug that could undermine the whole analytics pipeline
built on top of it if discovered later.

ALWAYS back up guided_learning.db before running any phase past `verify`
(this repo's convention: `guided_learning.db.pre-migration-<timestamp>`,
gitignored).
"""
import argparse
import json
import sys
from pathlib import Path

# Windows consoles default to a codepage that can't print Devanagari
# (नेपाली / सामाजिक अध्ययन subject names show up in the report) - force UTF-8.
sys.stdout.reconfigure(encoding="utf-8")

sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy import func

from app.database import SessionLocal
from app import models

SCIENCE_11, MGMT_11_SHELL = 91, 209
SCIENCE_12, MGMT_12_SHELL = 38, 210
LMS_SCI_11, LMS_SCI_12 = 194, 195
PRE_ENG = 203
EXPECTED_COURSE_IDS = {24, 38, 72, 91, 194, 195, 203, 209, 210}


def _chapter_ids(db, course_id):
    return [
        row[0] for row in
        db.query(models.Section.id)
          .filter(models.Section.course_id == course_id, models.Section.type == "Chapter")
          .all()
    ]


def _question_ids_for_chapters(db, chapter_ids):
    if not chapter_ids:
        return set()
    rows = (
        db.query(models.QuestionChapter.question_id)
          .filter(models.QuestionChapter.chapter_id.in_(chapter_ids))
          .distinct()
          .all()
    )
    return {r[0] for r in rows}


def verify() -> dict:
    """Phase 1 - read-only. Re-derives every figure the migration plan
    depends on directly from the live database, rather than trusting the
    earlier one-off audit's numbers."""
    db = SessionLocal()
    report: dict = {}

    courses = {c.id: c.name for c in db.query(models.Course).all()}
    report["courses"] = courses
    actual_ids = set(courses.keys())
    report["course_ids_match_expected"] = actual_ids == EXPECTED_COURSE_IDS
    report["unexpected_course_ids"] = sorted(actual_ids - EXPECTED_COURSE_IDS)
    report["missing_course_ids"] = sorted(EXPECTED_COURSE_IDS - actual_ids)

    totals = {}
    for cid in sorted(actual_ids):
        chs = _chapter_ids(db, cid)
        qids = _question_ids_for_chapters(db, chs)
        totals[cid] = {"name": courses[cid], "chapters": len(chs), "distinct_questions": len(qids)}
    report["course_totals"] = totals

    # true 203-orphan set: questions linked ONLY to chapters under 203
    chapters_203 = _chapter_ids(db, PRE_ENG)
    qids_203 = _question_ids_for_chapters(db, chapters_203)
    orphan_qids = []
    for qid in qids_203:
        other = (
            db.query(models.QuestionChapter.chapter_id)
              .filter(models.QuestionChapter.question_id == qid,
                      ~models.QuestionChapter.chapter_id.in_(chapters_203))
              .first()
        )
        if other is None:
            orphan_qids.append(qid)
    report["pre_eng_203_chapter_count"] = len(chapters_203)
    report["pre_eng_203_total_distinct_questions"] = len(qids_203)
    report["pre_eng_203_orphan_question_ids"] = sorted(orphan_qids)
    report["pre_eng_203_orphan_count"] = len(orphan_qids)

    # activity-table exposure - do any recorded attempts/sessions already
    # reference the courses/chapters this migration will delete or re-home?
    report["attempts_referencing_203_chapters"] = (
        db.query(func.count(models.Attempt.id))
          .filter(models.Attempt.chapter_id.in_(chapters_203))
          .scalar()
    )
    for cid in (LMS_SCI_11, LMS_SCI_12, PRE_ENG):
        report[f"practice_sessions_course_{cid}"] = (
            db.query(func.count(models.PracticeSession.id))
              .filter(models.PracticeSession.course_id == cid)
              .scalar()
        )

    report["total_questions_system_wide"] = db.query(func.count(models.Question.id)).scalar()
    report["total_sections_system_wide"] = db.query(func.count(models.Section.id)).scalar()

    # subject-level listing for 91/38 (needed to build the Phase-4
    # classification table) and 209/210 (needed to scope content authoring)
    subjects = {}
    for cid in (SCIENCE_11, SCIENCE_12, MGMT_11_SHELL, MGMT_12_SHELL):
        rows = (
            db.query(models.Section.id, models.Section.name)
              .filter(models.Section.course_id == cid, models.Section.type == "Subject")
              .all()
        )
        subject_list = []
        for sid, sname in rows:
            # chapters under this subject may be nested under intermediate
            # "Unit" sections, so walk the whole subtree, not just direct children
            stack, chapter_ids = [sid], []
            seen = set()
            while stack:
                pid = stack.pop()
                if pid in seen:
                    continue
                seen.add(pid)
                children = db.query(models.Section.id, models.Section.type).filter(models.Section.parent_id == pid).all()
                for child_id, child_type in children:
                    if child_type == "Chapter":
                        chapter_ids.append(child_id)
                    else:
                        stack.append(child_id)
            qids = _question_ids_for_chapters(db, chapter_ids)
            subject_list.append({"subject_id": sid, "name": sname, "chapters": len(chapter_ids), "distinct_questions": len(qids)})
        subjects[cid] = subject_list
    report["subjects"] = subjects

    db.close()
    return report


def rescue_203() -> dict:
    """Phase 2 - link course 203's 33 orphan questions (real content unique
    to 203, not reachable from any other course) into the chapter with the
    EXACT SAME NAME under course 194 (or 91, for the one chapter 194 lacks
    but 91 already has) - not a generic catch-all, an exact-name match,
    verified live. This is the only kind of "matching" this migration does
    without a human-reviewed fixed table, because it's a name equality
    check against real curriculum chapters already known to be the same
    topic (203 is 99.6% the same content as 194 to begin with)."""
    db = SessionLocal()
    report: dict = {}

    chapters_203 = _chapter_ids(db, PRE_ENG)
    qids_203 = _question_ids_for_chapters(db, chapters_203)
    orphan_qids = []
    for qid in qids_203:
        other = (
            db.query(models.QuestionChapter.chapter_id)
              .filter(models.QuestionChapter.question_id == qid,
                      ~models.QuestionChapter.chapter_id.in_(chapters_203))
              .first()
        )
        if other is None:
            orphan_qids.append(qid)

    report["orphan_count_found"] = len(orphan_qids)
    if len(orphan_qids) != 33:
        report["ABORTED"] = f"expected 33 orphans, found {len(orphan_qids)} - stopping without writing anything"
        db.close()
        return report

    linked, skipped = [], []
    for qid in orphan_qids:
        # the (possibly several) chapter(s) this question sits under in 203
        source_chapter_ids = [
            row[0] for row in
            db.query(models.QuestionChapter.chapter_id)
              .filter(models.QuestionChapter.question_id == qid, models.QuestionChapter.chapter_id.in_(chapters_203))
              .all()
        ]
        for source_cid in source_chapter_ids:
            source_chapter = db.get(models.Section, source_cid)
            target = (
                db.query(models.Section)
                  .filter(models.Section.name == source_chapter.name,
                          models.Section.type == "Chapter",
                          models.Section.course_id.in_([LMS_SCI_11, SCIENCE_11]))
                  .first()
            )
            if target is None:
                skipped.append({"question_id": qid, "source_chapter": source_chapter.name, "reason": "no exact-name match found under 194 or 91"})
                continue
            exists = (
                db.query(models.QuestionChapter)
                  .filter(models.QuestionChapter.question_id == qid, models.QuestionChapter.chapter_id == target.id)
                  .first()
            )
            if exists:
                linked.append({"question_id": qid, "target_chapter": target.name, "target_chapter_id": target.id, "note": "link already existed"})
                continue
            db.add(models.QuestionChapter(question_id=qid, chapter_id=target.id))
            linked.append({"question_id": qid, "target_chapter": target.name, "target_chapter_id": target.id})

    if skipped:
        report["ABORTED"] = f"{len(skipped)} orphan(s) had no exact-name match target - rolling back, nothing written"
        report["skipped"] = skipped
        db.rollback()
        db.close()
        return report

    db.commit()
    report["linked"] = linked
    report["linked_count"] = len(linked)

    # re-verify: 0 orphans should remain
    qids_203_after = _question_ids_for_chapters(db, chapters_203)
    remaining_orphans = []
    for qid in qids_203_after:
        other = (
            db.query(models.QuestionChapter.chapter_id)
              .filter(models.QuestionChapter.question_id == qid,
                      ~models.QuestionChapter.chapter_id.in_(chapters_203))
              .first()
        )
        if other is None:
            remaining_orphans.append(qid)
    report["remaining_orphans_after_rescue"] = remaining_orphans
    report["rescue_verified"] = len(remaining_orphans) == 0

    db.close()
    return report


def _merge_course_into(db, source_id: int, target_id: int) -> dict:
    """Administrative merge: re-point every Section under `source_id` to
    `target_id` and remap any PracticeSession rows, then delete the
    now-empty source Course. No Section id, parent_id, or QuestionChapter
    row is touched - chapter ids and their question links are completely
    stable, only which Course row owns them changes. See module docstring
    for why this is safe (real content already shares question_ids across
    both trees) and why no chapter-name matching happens here."""
    before_sections = db.query(func.count(models.Section.id)).filter(models.Section.course_id == source_id).scalar()
    before_sessions = db.query(func.count(models.PracticeSession.id)).filter(models.PracticeSession.course_id == source_id).scalar()

    db.query(models.Section).filter(models.Section.course_id == source_id).update(
        {models.Section.course_id: target_id}, synchronize_session=False)
    db.query(models.PracticeSession).filter(models.PracticeSession.course_id == source_id).update(
        {models.PracticeSession.course_id: target_id}, synchronize_session=False)

    after_sections = db.query(func.count(models.Section.id)).filter(models.Section.course_id == source_id).scalar()
    after_sessions = db.query(func.count(models.PracticeSession.id)).filter(models.PracticeSession.course_id == source_id).scalar()

    result = {
        "source_id": source_id, "target_id": target_id,
        "sections_repointed": before_sections, "sections_remaining_under_source": after_sections,
        "sessions_repointed": before_sessions, "sessions_remaining_under_source": after_sessions,
    }
    if after_sections != 0 or after_sessions != 0:
        result["ABORTED"] = "repoint did not fully clear the source course - not deleting it"
        return result

    source_course = db.get(models.Course, source_id)
    db.delete(source_course)
    result["source_course_deleted"] = True
    return result


def _delete_course_203(db) -> dict:
    """Hard-delete course 203 entirely. Safe only because Phase 1 confirmed
    0 Attempt/PracticeSession rows reference it, and Phase 2 already
    rescued its 33 unique questions elsewhere - every other question under
    203 is already reachable via course 194 (now merged into 91)."""
    chapter_ids = _chapter_ids(db, PRE_ENG)
    result: dict = {"chapters_to_delete": len(chapter_ids)}

    attempts = db.query(func.count(models.Attempt.id)).filter(models.Attempt.chapter_id.in_(chapter_ids)).scalar()
    sessions = db.query(func.count(models.PracticeSession.id)).filter(models.PracticeSession.course_id == PRE_ENG).scalar()
    if attempts or sessions:
        result["ABORTED"] = f"found {attempts} attempts / {sessions} sessions referencing course 203 - not deleting"
        return result

    qc_deleted = db.query(models.QuestionChapter).filter(models.QuestionChapter.chapter_id.in_(chapter_ids)).delete(synchronize_session=False)
    result["question_chapter_rows_deleted"] = qc_deleted

    # children (Chapter) before parents (Unit/Subject) - self-referencing FK
    for section_type in ("Chapter", "Unit", "Subject"):
        deleted = (
            db.query(models.Section)
              .filter(models.Section.course_id == PRE_ENG, models.Section.type == section_type)
              .delete(synchronize_session=False)
        )
        result[f"sections_deleted_{section_type.lower()}"] = deleted

    remaining_sections = db.query(func.count(models.Section.id)).filter(models.Section.course_id == PRE_ENG).scalar()
    result["sections_remaining_under_203"] = remaining_sections
    if remaining_sections:
        result["ABORTED"] = "sections remain under 203 after delete - not deleting the Course row"
        return result

    db.delete(db.get(models.Course, PRE_ENG))
    result["course_203_deleted"] = True
    return result


def merge_science() -> dict:
    """Phase 3 - rename 91->\"NEB Grade 11 Science\" absorbing 194,
    38->\"NEB Grade 12 Science\" absorbing 195, then permanently delete
    course 203 (its unique content was already rescued in Phase 2)."""
    db = SessionLocal()
    report: dict = {}

    total_before = db.query(func.count(models.Question.id)).scalar()
    report["total_questions_before"] = total_before

    course_91 = db.get(models.Course, SCIENCE_11)
    course_38 = db.get(models.Course, SCIENCE_12)
    report["renamed"] = {SCIENCE_11: {"from": course_91.name, "to": "NEB Grade 11 Science"},
                          SCIENCE_12: {"from": course_38.name, "to": "NEB Grade 12 Science"}}
    course_91.name = "NEB Grade 11 Science"
    course_38.name = "NEB Grade 12 Science"

    report["merge_194_into_91"] = _merge_course_into(db, LMS_SCI_11, SCIENCE_11)
    report["merge_195_into_38"] = _merge_course_into(db, LMS_SCI_12, SCIENCE_12)

    if report["merge_194_into_91"].get("ABORTED") or report["merge_195_into_38"].get("ABORTED"):
        db.rollback()
        report["ABORTED"] = "one or both merges failed precondition - rolled back, nothing committed"
        db.close()
        return report

    report["delete_203"] = _delete_course_203(db)
    if report["delete_203"].get("ABORTED"):
        db.rollback()
        report["ABORTED"] = "course 203 deletion failed precondition - rolled back, nothing committed"
        db.close()
        return report

    db.commit()

    total_after = db.query(func.count(models.Question.id)).scalar()
    report["total_questions_after"] = total_after
    report["zero_question_loss"] = (total_after == total_before)
    report["remaining_courses"] = {c.id: c.name for c in db.query(models.Course).all()}

    db.close()
    return report


def _subjects_with_chapters(db, course_id):
    """Every Subject-type Section directly under `course_id`, with the full
    set of Chapter ids in its subtree (walking through any intermediate
    "Unit" sections) - shared by `verify()`'s reporting and `phase4_cleanup`'s
    classification, since both need the same subject->chapters walk."""
    rows = (
        db.query(models.Section.id, models.Section.name)
          .filter(models.Section.course_id == course_id, models.Section.type == "Subject")
          .all()
    )
    result = []
    for sid, sname in rows:
        stack, chapter_ids = [sid], []
        seen = set()
        while stack:
            pid = stack.pop()
            if pid in seen:
                continue
            seen.add(pid)
            children = db.query(models.Section.id, models.Section.type).filter(models.Section.parent_id == pid).all()
            for child_id, child_type in children:
                if child_type == "Chapter":
                    chapter_ids.append(child_id)
                else:
                    stack.append(child_id)
        result.append({"subject_id": sid, "name": sname, "chapter_ids": chapter_ids})
    return result


# Phase 4 classification table - human-reviewed, matched by exact subject
# name only (same "no heuristic matching" rule as the rest of this script).
# Any subject name found live under 91/38 that isn't in one of these three
# sets makes phase4_cleanup abort rather than guess at its category.
#
# DELETE: Management-only content (or non-curriculum junk) with real
# equivalents already authored under 209/210 - the whole subtree goes.
# SCIENCE_STRIP_SYNTHETIC: real Science subjects with abundant real content
# already (post 194/195 merge) - only the synthetic filler is removed, the
# chapter/subject structure and real questions are untouched.
# COMPULSORY_STRIP_SYNTHETIC: compulsory-across-streams subjects that will
# get freshly authored content in Phase 1b - synthetic junk is removed but
# the chapter/subject structure stays as the load target for that content.
PHASE4_DELETE_SUBJECTS = {
    "Account", "Business Studies", "Business Maths", "Economics",
    "MODEL SETS", "Kritagya's Handwritten Note", "Accounting- Crash Course",
    "Orientation class",
}
# Live `verify` (2026-08-09) showed Physics/Chemistry/Botany/Zoology/
# Mathematics/Basic Maths/Computer Science all already carry substantial
# REAL content under 91/38 (not just synthetic filler, contrary to the
# original plan's assumption for Basic Maths/Computer Science) - all seven
# get the same strip-synthetic-only treatment, keep structure + real content.
PHASE4_SCIENCE_STRIP_SYNTHETIC_SUBJECTS = {
    "Physics", "Chemistry", "Botany", "Zoology", "Mathematics",
    "Basic Maths", "Computer Science",
}
# ~100% synthetic (verified live: each subject's total distinct_questions
# matches its synthetic-only count almost exactly) - structure kept as the
# Phase 1b load target for freshly authored content. Note "Social Studies"
# (English name) under course 38 vs "सामाजिक अध्ययन" (Devanagari) under 91 -
# a genuine naming inconsistency between the two grade trees, not a typo.
PHASE4_COMPULSORY_STRIP_SYNTHETIC_SUBJECTS = {
    "Compulsory English", "English", "नेपाली", "सामाजिक अध्ययन", "Social Studies",
}
# Human-reviewed (2026-08-09, live inspection of both question bodies) exact
# exceptions to the exact-name-rescue rule: two single-question edge cases
# with genuinely no safe rescue target, not a blanket threshold relaxation.
#   130346: real Physics mechanics/friction question, but its only chapter
#     is "Physics Handwritten Notes" under "Kritagya's Handwritten Note" -
#     an informal student notes-dump, not a real curriculum chapter, so no
#     exact-name Physics chapter exists to rescue it into without guessing.
#   147663: real Nepal-economics-policy question ("which body is responsible
#     for developing sample textbooks?"), but Economics isn't part of the
#     NEB Science curriculum at all - there is no legitimate kept Economics
#     subject under 91/38 for it to belong to.
# Both accepted as a documented, tiny (2-question) loss rather than forcing
# a fuzzy match that could misattribute real content - exactly the kind of
# case this module's docstring says needs a human-reviewed call, not a
# heuristic.
PHASE4_ACCEPTED_UNRESCUABLE_QUESTION_IDS = {130346, 147663}


def _question_source_counts(db, chapter_ids):
    if not chapter_ids:
        return {"real": 0, "synthetic": 0, "other": 0}
    qids = _question_ids_for_chapters(db, chapter_ids)
    if not qids:
        return {"real": 0, "synthetic": 0, "other": 0}
    rows = db.query(models.Question.id, models.Question.source).filter(models.Question.id.in_(qids)).all()
    counts = {"real": 0, "synthetic": 0, "other": 0}
    for _, source in rows:
        key = source if source in ("real", "synthetic") else "other"
        counts[key] += 1
    return counts


def _delete_subject_subtree(db, subject_id: int, chapter_ids: list[int]) -> dict:
    """Hard-delete a Subject's entire subtree (children-before-parents, same
    order as `_delete_course_203`) plus every QuestionChapter row into it.
    Does NOT delete the underlying Question rows - a synthetic question
    might still be linked elsewhere (e.g. under a kept Science chapter),
    and `phase4_cleanup`'s final sweep separately deletes any synthetic
    Question left with zero remaining links, system-wide, after all
    subjects have been processed."""
    result: dict = {"subject_id": subject_id}
    qc_deleted = (
        db.query(models.QuestionChapter)
          .filter(models.QuestionChapter.chapter_id.in_(chapter_ids))
          .delete(synchronize_session=False)
    ) if chapter_ids else 0
    result["question_chapter_rows_deleted"] = qc_deleted

    # walk down from the subject through Unit sections to find everything
    # under it (chapters were already collected by the caller, but Unit
    # nodes in between also need deleting) - collect all descendant ids first
    all_ids, stack = [], [subject_id]
    while stack:
        pid = stack.pop()
        children = db.query(models.Section.id).filter(models.Section.parent_id == pid).all()
        for (cid,) in children:
            all_ids.append(cid)
            stack.append(cid)

    for section_type in ("Chapter", "Unit"):
        deleted = (
            db.query(models.Section)
              .filter(models.Section.id.in_(all_ids), models.Section.type == section_type)
              .delete(synchronize_session=False)
        )
        result[f"sections_deleted_{section_type.lower()}"] = deleted

    remaining_children = db.query(func.count(models.Section.id)).filter(models.Section.id.in_(all_ids)).scalar()
    if remaining_children:
        result["ABORTED"] = f"{remaining_children} descendant section(s) survived the Chapter/Unit sweep - not deleting the Subject"
        return result

    db.query(models.Section).filter(models.Section.id == subject_id).delete(synchronize_session=False)
    result["subject_deleted"] = True
    return result


def phase4_cleanup() -> dict:
    """Phase 4 - the deferred step named in this module's own docstring
    when 91/38 were renamed to Science courses: their old generic-course
    subject subtrees (Accounting, Business Studies, ...) and 9,081
    `[SYNTHETIC PLACEHOLDER]` filler questions were never actually removed,
    so a Science-stream student could still be served wrong-subject
    template garbage. This phase:
      1. classifies every Subject under 91/38 against a fixed, human-
         reviewed table (never a heuristic - same rule as the rest of this
         script), aborting if any subject name is unrecognized;
      2. verifies live that DELETE-category subjects have no unexpected
         real content before touching them (real content must never be
         silently destroyed by an assumption);
      3. hard-deletes DELETE-category subtrees entirely;
      4. strips only the `source='synthetic'` links (keeping structure and
         all real content) from Science and compulsory-subject chapters;
      5. sweeps up any synthetic Question left with zero remaining
         QuestionChapter links anywhere in the system.
    SQLite FK enforcement is off in this project (`database.py` never sets
    PRAGMA foreign_keys), so any Attempt row referencing a chapter/question
    this phase removes becomes a harmless dangling reference, not a crash -
    counted and reported below rather than silently ignored, and accepted
    per this session's plan since the counts are small (1-21 per subject)
    and almost certainly the coordinator's own QA accounts, not real
    student data."""
    db = SessionLocal()
    report: dict = {}

    subjects_91 = _subjects_with_chapters(db, SCIENCE_11)
    subjects_38 = _subjects_with_chapters(db, SCIENCE_12)

    unrecognized = []
    for subj in subjects_91 + subjects_38:
        name = subj["name"]
        if name not in (PHASE4_DELETE_SUBJECTS | PHASE4_SCIENCE_STRIP_SYNTHETIC_SUBJECTS | PHASE4_COMPULSORY_STRIP_SYNTHETIC_SUBJECTS):
            unrecognized.append(name)
    if unrecognized:
        report["ABORTED"] = f"unrecognized subject name(s) under 91/38, not in the classification table - stopping without writing anything: {sorted(set(unrecognized))}"
        db.close()
        return report

    # precondition: DELETE-category subjects must have negligible real
    # content - report every one's real/synthetic split before touching
    # anything. A stray real question or two doesn't change the fact these
    # subjects don't belong under a Science course, but before writing
    # anything off, attempt an exact-chapter-name rescue (same rule as
    # `rescue_203`: only exact name matches, never fuzzy) into a KEPT
    # subject in the same course - e.g. a "Business Maths" chapter that's
    # actually mislabeled real calculus content with an exact-name sibling
    # under "Mathematics". Only abort if real content remains that can't be
    # matched this way.
    delete_precheck = {}
    rescued = []
    unmatched_real_content = []
    for subj in subjects_91 + subjects_38:
        if subj["name"] not in PHASE4_DELETE_SUBJECTS:
            continue
        counts = _question_source_counts(db, subj["chapter_ids"])
        key = f"{subj['name']} (subject_id={subj['subject_id']})"
        delete_precheck[key] = counts
        if counts["real"] == 0:
            continue

        course_id = db.query(models.Section.course_id).filter(models.Section.id == subj["subject_id"]).scalar()
        kept_subject_ids = [
            s["subject_id"] for s in (subjects_91 if course_id == SCIENCE_11 else subjects_38)
            if s["name"] in (PHASE4_SCIENCE_STRIP_SYNTHETIC_SUBJECTS | PHASE4_COMPULSORY_STRIP_SYNTHETIC_SUBJECTS)
        ]
        real_qids = [
            r[0] for r in
            db.query(models.QuestionChapter.question_id)
              .join(models.Question, models.Question.id == models.QuestionChapter.question_id)
              .filter(models.QuestionChapter.chapter_id.in_(subj["chapter_ids"]), models.Question.source != "synthetic")
              .distinct().all()
        ]
        for qid in real_qids:
            source_chapter_ids = [
                r[0] for r in
                db.query(models.QuestionChapter.chapter_id)
                  .filter(models.QuestionChapter.question_id == qid, models.QuestionChapter.chapter_id.in_(subj["chapter_ids"]))
                  .all()
            ]
            for source_cid in source_chapter_ids:
                source_chapter = db.get(models.Section, source_cid)
                candidates = (
                    db.query(models.Section)
                      .filter(models.Section.name == source_chapter.name, models.Section.type == "Chapter",
                              models.Section.course_id == course_id,
                              models.Section.id.notin_(subj["chapter_ids"]))
                      .all()
                )
                target = None
                for candidate in candidates:
                    # walk up the parent chain (through any Unit nodes) to
                    # confirm this candidate sits under a KEPT subject, not
                    # e.g. another DELETE-category subject that happens to
                    # share a chapter name
                    walk, is_under_kept = candidate.id, False
                    for _ in range(8):
                        parent_id = db.query(models.Section.parent_id).filter(models.Section.id == walk).scalar()
                        if parent_id is None:
                            break
                        if parent_id in kept_subject_ids:
                            is_under_kept = True
                            break
                        walk = parent_id
                    if is_under_kept:
                        target = candidate
                        break
                if target is None:
                    unmatched_real_content.append({"question_id": qid, "source_chapter": source_chapter.name, "subject": key})
                    continue
                exists = (
                    db.query(models.QuestionChapter)
                      .filter(models.QuestionChapter.question_id == qid, models.QuestionChapter.chapter_id == target.id)
                      .first()
                )
                if not exists:
                    db.add(models.QuestionChapter(question_id=qid, chapter_id=target.id))
                rescued.append({"question_id": qid, "from_chapter": source_chapter.name, "to_chapter_id": target.id, "already_linked": bool(exists)})
    report["delete_precheck_source_counts"] = delete_precheck
    report["rescued_real_content"] = rescued
    truly_unmatched = [u for u in unmatched_real_content if u["question_id"] not in PHASE4_ACCEPTED_UNRESCUABLE_QUESTION_IDS]
    accepted_loss = [u for u in unmatched_real_content if u["question_id"] in PHASE4_ACCEPTED_UNRESCUABLE_QUESTION_IDS]
    report["accepted_loss_real_content"] = accepted_loss
    if truly_unmatched:
        db.rollback()
        report["ABORTED"] = "real content in a DELETE-category subject had no exact-name rescue target and is not on the reviewed accepted-loss list - rolling back, nothing written"
        report["unmatched_real_content"] = truly_unmatched
        db.close()
        return report

    # precondition: check Attempt/PracticeSession exposure for every
    # chapter about to be touched (deleted OR unlinked), report the counts
    attempts_by_subject = {}
    for subj in subjects_91 + subjects_38:
        if subj["name"] not in PHASE4_DELETE_SUBJECTS:
            continue
        n = db.query(func.count(models.Attempt.id)).filter(models.Attempt.chapter_id.in_(subj["chapter_ids"])).scalar() if subj["chapter_ids"] else 0
        if n:
            attempts_by_subject[f"{subj['name']} (subject_id={subj['subject_id']})"] = n
    report["attempts_orphaned_by_subject_deletion"] = attempts_by_subject
    report["attempts_orphaned_total"] = sum(attempts_by_subject.values())

    # --- writes start here ---
    deleted_subjects = {}
    for subj in subjects_91 + subjects_38:
        if subj["name"] not in PHASE4_DELETE_SUBJECTS:
            continue
        key = f"{subj['name']} (subject_id={subj['subject_id']})"
        result = _delete_subject_subtree(db, subj["subject_id"], subj["chapter_ids"])
        deleted_subjects[key] = result
        if result.get("ABORTED"):
            db.rollback()
            report["ABORTED"] = f"subject deletion failed for {key} - rolled back, nothing committed"
            report["deleted_subjects"] = deleted_subjects
            db.close()
            return report
    report["deleted_subjects"] = deleted_subjects

    stripped_synthetic = {}
    for subj in subjects_91 + subjects_38:
        if subj["name"] not in (PHASE4_SCIENCE_STRIP_SYNTHETIC_SUBJECTS | PHASE4_COMPULSORY_STRIP_SYNTHETIC_SUBJECTS):
            continue
        key = f"{subj['name']} (subject_id={subj['subject_id']})"
        chapter_ids = subj["chapter_ids"]
        if not chapter_ids:
            stripped_synthetic[key] = {"question_chapter_rows_deleted": 0}
            continue
        synthetic_qids = [
            r[0] for r in
            db.query(models.QuestionChapter.question_id)
              .join(models.Question, models.Question.id == models.QuestionChapter.question_id)
              .filter(models.QuestionChapter.chapter_id.in_(chapter_ids), models.Question.source == "synthetic")
              .distinct().all()
        ]
        qc_deleted = (
            db.query(models.QuestionChapter)
              .filter(models.QuestionChapter.chapter_id.in_(chapter_ids),
                      models.QuestionChapter.question_id.in_(synthetic_qids))
              .delete(synchronize_session=False)
        ) if synthetic_qids else 0
        stripped_synthetic[key] = {"question_chapter_rows_deleted": qc_deleted, "distinct_synthetic_questions_unlinked": len(synthetic_qids)}
    report["stripped_synthetic_links"] = stripped_synthetic

    # sweep: delete any synthetic Question with zero remaining QuestionChapter
    # links anywhere in the system (system-wide, not per-subject, since a
    # synthetic question could in principle have been linked to more than
    # one chapter before this phase touched anything)
    orphaned_synthetic_qids = [
        r[0] for r in
        db.query(models.Question.id)
          .outerjoin(models.QuestionChapter, models.QuestionChapter.question_id == models.Question.id)
          .filter(models.Question.source == "synthetic", models.QuestionChapter.question_id.is_(None))
          .all()
    ]
    attempts_on_orphaned = (
        db.query(func.count(models.Attempt.id)).filter(models.Attempt.question_id.in_(orphaned_synthetic_qids)).scalar()
        if orphaned_synthetic_qids else 0
    )
    report["orphaned_synthetic_questions_found"] = len(orphaned_synthetic_qids)
    report["attempts_referencing_orphaned_synthetic_questions"] = attempts_on_orphaned
    if orphaned_synthetic_qids:
        deleted_q = (
            db.query(models.Question)
              .filter(models.Question.id.in_(orphaned_synthetic_qids))
              .delete(synchronize_session=False)
        )
        report["orphaned_synthetic_questions_deleted"] = deleted_q

    db.commit()

    # final audit
    remaining_junk = (
        db.query(func.count(models.Question.id))
          .join(models.QuestionChapter, models.QuestionChapter.question_id == models.Question.id)
          .join(models.Section, models.Section.id == models.QuestionChapter.chapter_id)
          .filter(models.Section.course_id.in_([SCIENCE_11, SCIENCE_12]), models.Question.source == "synthetic")
          .scalar()
    )
    report["remaining_synthetic_questions_under_science_courses"] = remaining_junk
    report["cleanup_verified"] = remaining_junk == 0

    science_science_counts = {}
    for cid, subj_names in ((SCIENCE_11, PHASE4_SCIENCE_STRIP_SYNTHETIC_SUBJECTS), (SCIENCE_12, PHASE4_SCIENCE_STRIP_SYNTHETIC_SUBJECTS)):
        for subj in _subjects_with_chapters(db, cid):
            if subj["name"] in subj_names:
                counts = _question_source_counts(db, subj["chapter_ids"])
                science_science_counts[f"course_{cid}: {subj['name']}"] = counts
    report["real_science_content_after"] = science_science_counts

    report["remaining_subjects_under_91_38"] = {
        cid: sorted(s["name"] for s in _subjects_with_chapters(db, cid)) for cid in (SCIENCE_11, SCIENCE_12)
    }

    db.close()
    return report


def dedupe_subjects() -> dict:
    """Phase 5 - collapse the duplicate-named Subject shells that
    `_merge_course_into` (Phase 3) necessarily left behind: it re-points
    Section.course_id only, by design never matching by name (see module
    docstring), so course 91 ended up with two "Physics" Subject nodes
    (one from the original 91, one from the absorbed 194) instead of one -
    same for Chemistry/Botany/Zoology under 91, and all four under 38.

    This merge is a strictly safer operation than the Phase 3 name-
    matching this module deliberately avoids: it only re-parents Unit-type
    children (Section.parent_id) from the duplicate Subject onto the
    keeper Subject, then deletes the now-empty duplicate. No Chapter row,
    no QuestionChapter link, and no Question is ever touched - every
    Attempt/PracticeSession/ChapterProgress/QuizTemplate row keys off
    chapter_id, which never changes, so this is 100% safe for recorded
    activity regardless of which duplicate is kept. Matching is by exact
    Subject name only (never fuzzy), scoped to Subject-level nodes only -
    it does not recurse into deduplicating same-named Units/Chapters
    *within* the merged subject, which would reintroduce the exact
    chapter-level misattribution risk this module's own rule exists to
    avoid.

    Keeper is the lower Section id in each duplicate pair (the original
    91/38 subject predates the absorbed 194/195 one, since the content
    partner's ids were assigned in creation order) - same lowest-id tie-break
    convention already used for many-to-many QuestionChapter attribution
    in practice.py's `chapter_for_question`."""
    db = SessionLocal()
    report: dict = {}

    by_course_name: dict[tuple[int, str], list[int]] = {}
    for cid in (SCIENCE_11, SCIENCE_12):
        for s in db.query(models.Section).filter(models.Section.course_id == cid, models.Section.type == "Subject").all():
            by_course_name.setdefault((cid, s.name), []).append(s.id)

    dupe_pairs = {k: sorted(v) for k, v in by_course_name.items() if len(v) > 1}
    report["duplicate_subject_pairs_found"] = {f"course {cid}: {name}": ids for (cid, name), ids in dupe_pairs.items()}
    if not dupe_pairs:
        report["nothing_to_do"] = True
        db.close()
        return report

    total_questions_before = db.query(func.count(models.Question.id)).scalar()
    total_chapters_before = db.query(func.count(models.Section.id)).filter(models.Section.type == "Chapter").scalar()
    report["total_questions_before"] = total_questions_before
    report["total_chapters_before"] = total_chapters_before

    merges = {}
    for (cid, name), ids in dupe_pairs.items():
        keeper_id, *donor_ids = ids
        key = f"course {cid}: {name}"
        merges[key] = {"keeper_id": keeper_id, "donor_ids": donor_ids, "donors": []}
        for donor_id in donor_ids:
            before_children = db.query(func.count(models.Section.id)).filter(models.Section.parent_id == donor_id).scalar()
            db.query(models.Section).filter(models.Section.parent_id == donor_id).update(
                {models.Section.parent_id: keeper_id}, synchronize_session=False)
            after_children = db.query(func.count(models.Section.id)).filter(models.Section.parent_id == donor_id).scalar()
            donor_result = {"donor_id": donor_id, "children_repointed": before_children, "children_remaining_under_donor": after_children}
            if after_children != 0:
                db.rollback()
                report["ABORTED"] = f"{key}: donor {donor_id} still has children after repoint - rolled back, nothing committed"
                report["merges_attempted"] = merges
                db.close()
                return report
            db.delete(db.get(models.Section, donor_id))
            donor_result["donor_subject_deleted"] = True
            merges[key]["donors"].append(donor_result)
    report["merges"] = merges

    db.commit()

    total_questions_after = db.query(func.count(models.Question.id)).scalar()
    total_chapters_after = db.query(func.count(models.Section.id)).filter(models.Section.type == "Chapter").scalar()
    report["total_questions_after"] = total_questions_after
    report["total_chapters_after"] = total_chapters_after
    report["zero_question_loss"] = (total_questions_after == total_questions_before)
    report["zero_chapter_loss"] = (total_chapters_after == total_chapters_before)

    remaining_dupes = {}
    for cid in (SCIENCE_11, SCIENCE_12):
        names = [s.name for s in db.query(models.Section).filter(models.Section.course_id == cid, models.Section.type == "Subject").all()]
        seen_twice = sorted({n for n in names if names.count(n) > 1})
        if seen_twice:
            remaining_dupes[cid] = seen_twice
    report["remaining_duplicate_subject_names"] = remaining_dupes
    report["dedupe_verified"] = not remaining_dupes

    db.close()
    return report


REPORT_DIR = Path(__file__).parent / "reports"


def print_report(report: dict, save_as: str | None = None):
    text = json.dumps(report, indent=2, ensure_ascii=False, default=str)
    print(text)
    if save_as:
        REPORT_DIR.mkdir(exist_ok=True)
        (REPORT_DIR / save_as).write_text(text, encoding="utf-8")
        print(f"\nSaved to {REPORT_DIR / save_as}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("phase", choices=["verify", "rescue-203", "merge-science", "cleanup-junk", "dedupe-subjects"])
    args = parser.parse_args()

    if args.phase == "verify":
        print_report(verify(), save_as="phase1_verify.json")
    elif args.phase == "rescue-203":
        print_report(rescue_203(), save_as="phase2_rescue_203.json")
    elif args.phase == "merge-science":
        print_report(merge_science(), save_as="phase3_merge_science.json")
    elif args.phase == "cleanup-junk":
        print_report(phase4_cleanup(), save_as="phase4_cleanup.json")
    elif args.phase == "dedupe-subjects":
        print_report(dedupe_subjects(), save_as="phase5_dedupe_subjects.json")
