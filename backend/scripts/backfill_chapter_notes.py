"""
One-time backfill: every Chapter-type Section currently has an empty
Chapter Learning Page (0 rows in learning_resources) - a student clicking
"Learn" sees "No learning content has been added for this chapter yet."
system-wide, 877 of 878 chapters. Teacher-authored notes/videos/links are
the real long-term fix (Learning Content Management already supports
that), but writing genuinely accurate deep subject notes for 877 chapters
spanning six streams (Physics through सामाजिक अध्ययन) in one pass isn't
something that can be done honestly without real per-chapter subject-
matter research - that would risk exactly the kind of fabricated-content
this project's academic-integrity rule exists to prevent: never fabricate,
and every synthetic data point stays clearly labelled as synthetic.

So this script inserts one `note`-type LearningResource per chapter that
combines only VERIFIABLE facts (breadcrumb, real linked-question counts
by difficulty, drawn live from the DB) with generic, subject-family-level
study guidance that is true for any chapter in that family - never a
claim about this specific chapter's content. The note is explicitly
labelled as auto-generated in its own body, same transparency discipline
already used for synthetic questions elsewhere in this project. This
closes the "page is empty" gap honestly; a teacher can still add real
notes/videos on top via Learning Content Management at any time (this
script never touches a chapter that already has at least one resource).

Run once from `backend/`:
    python -m scripts.backfill_chapter_notes
"""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.database import SessionLocal
from app import models

# Broad, defensible subject-family groupings (by exact Subject name) - used
# only to pick which generic study-strategy paragraph applies, never to
# claim anything about a specific chapter's content.
QUANTITATIVE = {
    "Physics", "Chemistry", "Chemistry Revision", "Basic Maths", "Mathematics",
    "Computer Science", "Business Maths",
}
LIFE_SCIENCE = {"Botany", "Zoology", "Botany Revision", "Science (Entrance)"}
LANGUAGE = {"नेपाली", "Compulsory English", "English"}
COMMERCE_SOCIAL = {
    "Business Studies", "Economics", "Principle of Accounting-I", "Principles of Accounting-II",
    "सामाजिक अध्ययन", "सामाजिक अध्ययन तथा जीवनोउपायोगी शिक्षा", "Social Studies",
}

STRATEGY_PARAGRAPHS = {
    "quantitative": (
        "For a numerical/problem-solving chapter like this, work formula-first: make sure you can state "
        "the key formulas and derivations from memory before timing yourself on problems. Start with Easy "
        "questions to lock in the method, then move to Medium/Hard once you're getting Easy ones right "
        "consistently - the practice draw here adapts to your mastery automatically, so sticking with it "
        "over a few sessions naturally shifts you toward harder questions."
    ),
    "life_science": (
        "This is largely a concept-and-terminology chapter - diagrams, classification, and precise "
        "vocabulary matter as much as the underlying concept. A quick self-test (can you label a diagram "
        "or define the key terms from memory?) before practicing tends to surface gaps faster than jumping "
        "straight into MCQs."
    ),
    "language": (
        "Language chapters reward active reading over passive review - read the relevant textbook section "
        "once for meaning, then again specifically looking for the grammar/vocabulary/structural points this "
        "chapter is testing. Practising a mix of questions here, then re-reading anything you got wrong, "
        "tends to stick better than re-reading the whole chapter up front."
    ),
    "commerce_social": (
        "These chapters usually combine a few core concepts with real-world application - focus on being "
        "able to explain each key concept in your own words and connect it to a concrete example, not just "
        "recognise the term. Practising application-style questions here is a good check on whether you've "
        "actually understood a concept or just memorised its definition."
    ),
}
DEFAULT_STRATEGY = (
    "Work through the practice questions for this chapter a few at a time rather than all at once - "
    "spacing attempts out tends to build stronger recall than a single long session."
)


def _family(subject_name: str) -> str:
    if subject_name in QUANTITATIVE:
        return "quantitative"
    if subject_name in LIFE_SCIENCE:
        return "life_science"
    if subject_name in LANGUAGE:
        return "language"
    if subject_name in COMMERCE_SOCIAL:
        return "commerce_social"
    return "default"


def _breadcrumb(db, chapter) -> tuple[str, str]:
    """Walk parent_id up to the top-level Subject, returning (unit_name_or_empty, subject_name)."""
    unit_name = ""
    subject_name = "this subject"
    node = chapter
    seen = set()
    while node.parent_id is not None and node.id not in seen:
        seen.add(node.id)
        parent = db.get(models.Section, node.parent_id)
        if parent is None:
            break
        if parent.type == "Unit" and not unit_name:
            unit_name = parent.name
        if parent.type == "Subject":
            subject_name = parent.name
            break
        node = parent
    return unit_name, subject_name


def _difficulty_counts(db, chapter_id: int) -> dict[str, int]:
    rows = (
        db.query(models.Question.difficulty_label)
          .join(models.QuestionChapter, models.QuestionChapter.question_id == models.Question.id)
          .filter(models.QuestionChapter.chapter_id == chapter_id, models.Question.scoreable == True)
          .all()
    )
    counts = {"Easy": 0, "Medium": 0, "Hard": 0}
    for (label,) in rows:
        if label in counts:
            counts[label] += 1
    return counts


def _build_note_body(chapter_name: str, unit_name: str, subject_name: str, diff_counts: dict[str, int]) -> str:
    total = sum(diff_counts.values())
    # Some source data (नेपाली/English) wraps each chapter in a Unit tier
    # with the identical name - showing that back reads as a redundant
    # "part of X, under Y" when X == chapter_name, so drop it in that case.
    if unit_name and unit_name != chapter_name:
        where = f'part of **{unit_name}**, under **{subject_name}**'
    else:
        where = f'part of **{subject_name}**'
    lines = [f"This chapter, **{chapter_name}**, is {where}.", ""]

    if total > 0:
        lines.append(
            f"There are **{total} practice questions** available for this chapter right now "
            f"({diff_counts['Easy']} Easy, {diff_counts['Medium']} Medium, {diff_counts['Hard']} Hard)."
        )
    else:
        lines.append(
            "No practice questions are linked to this chapter in the system yet, so mastery tracking "
            "won't have anything to compute here until some are added."
        )
    lines.append("")

    family = _family(subject_name)
    lines.append(STRATEGY_PARAGRAPHS.get(family, DEFAULT_STRATEGY))
    lines.append("")
    lines.append(
        "Once you've attempted a few questions here, this chapter will start showing up in your mastery "
        "tracking (🔴 High / 🟡 Medium / 🟢 Low priority) on the Dashboard and Weak Areas pages, so you'll "
        "know at a glance when it's worth revisiting."
    )
    lines.append("")
    lines.append(
        "*This overview was auto-generated from chapter metadata and live practice-question statistics - "
        "it's a starting guide, not a substitute for your textbook or teacher's notes. A teacher can add "
        "real notes, videos, or links to this chapter at any time from Learning Content Management.*"
    )
    return "\n".join(lines)


def backfill() -> dict:
    db = SessionLocal()
    report: dict = {}

    teacher = db.query(models.Student).filter(models.Student.role == "teacher").first()
    if teacher is None:
        report["ABORTED"] = "no teacher account exists to attribute created_by to - nothing written"
        db.close()
        return report

    all_chapters = db.query(models.Section).filter(models.Section.type == "Chapter").all()
    chapters_with_resource = {
        row[0] for row in db.query(models.LearningResource.chapter_id).distinct().all()
    }
    targets = [c for c in all_chapters if c.id not in chapters_with_resource]

    report["total_chapters"] = len(all_chapters)
    report["chapters_already_with_content"] = len(chapters_with_resource)
    report["chapters_to_backfill"] = len(targets)

    created = 0
    zero_question_chapters = 0
    for chapter in targets:
        unit_name, subject_name = _breadcrumb(db, chapter)
        diff_counts = _difficulty_counts(db, chapter.id)
        if sum(diff_counts.values()) == 0:
            zero_question_chapters += 1
        body = _build_note_body(chapter.name, unit_name, subject_name, diff_counts)
        db.add(models.LearningResource(
            chapter_id=chapter.id, type="note", title="How to approach this chapter",
            body_markdown=body, url=None, order_index=0, created_by=teacher.id,
        ))
        created += 1

    db.commit()

    total_after = db.query(models.LearningResource.chapter_id).distinct().count()
    report["notes_created"] = created
    report["backfilled_chapters_had_zero_questions"] = zero_question_chapters
    report["chapters_with_content_after"] = total_after
    report["every_chapter_covered"] = (total_after == len(all_chapters))

    db.close()
    return report


if __name__ == "__main__":
    import json
    result = backfill()
    print(json.dumps(result, indent=2, ensure_ascii=False))
