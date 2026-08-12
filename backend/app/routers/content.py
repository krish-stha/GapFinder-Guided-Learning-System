import json
import random
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

from ..database import get_db
from .. import models, schemas
from .auth import get_current_student, get_current_teacher

router = APIRouter(prefix="/content", tags=["content"])


@router.get("/courses")
def list_courses(db: Session = Depends(get_db)):
    return [{"id": c.id, "name": c.name} for c in db.query(models.Course).all()]


@router.get("/sections", response_model=list[schemas.ChapterOut])
def list_sections(course_id: int, type: str | None = None, db: Session = Depends(get_db)):
    q = db.query(models.Section).filter_by(course_id=course_id)
    if type:
        q = q.filter_by(type=type)
    return q.all()


@router.get("/chapters/{chapter_id}/resources", response_model=schemas.ChapterResourcesOut)
def chapter_resources(
    chapter_id: int,
    db: Session = Depends(get_db),
    student: models.Student = Depends(get_current_student),
):
    """Chapter Learning Page: notes/videos/resources plus any
    question_type='example' worked examples linked to the chapter.
    Side-effect upserts ChapterProgress.notes_viewed_at, same idempotent-
    upsert convention as /practice/{id}/answer's pre-created Attempt rows."""
    chapter = db.get(models.Section, chapter_id)
    if not chapter or chapter.type != "Chapter":
        raise HTTPException(404, "Chapter not found")

    resources = (
        db.query(models.LearningResource)
          .filter_by(chapter_id=chapter_id)
          .order_by(models.LearningResource.order_index.asc())
          .all()
    )
    example_questions = (
        db.query(models.Question)
          .join(models.QuestionChapter, models.QuestionChapter.question_id == models.Question.id)
          .filter(models.QuestionChapter.chapter_id == chapter_id, models.Question.question_type == "example")
          .all()
    )
    examples = [
        schemas.QuestionOut(
            id=q.id, body=q.body, answers=[o["answer"] for o in json.loads(q.answers_json)],
            difficulty_label=q.difficulty_label, source=q.source, position=i,
        ) for i, q in enumerate(example_questions)
    ]

    progress = db.query(models.ChapterProgress).filter_by(student_id=student.id, chapter_id=chapter_id).first()
    if progress is None:
        progress = models.ChapterProgress(student_id=student.id, chapter_id=chapter_id)
        db.add(progress)
    progress.notes_viewed_at = datetime.utcnow()
    db.commit()

    return schemas.ChapterResourcesOut(
        chapter_id=chapter_id, chapter_name=chapter.name,
        resources=resources, examples=examples,
        progress=schemas.ChapterProgressOut(
            chapter_id=chapter_id, notes_viewed_at=progress.notes_viewed_at,
            marked_complete_at=progress.marked_complete_at,
        ),
    )


@router.get("/chapters/completed/me", response_model=list[int])
def completed_chapter_ids(
    db: Session = Depends(get_db),
    student: models.Student = Depends(get_current_student),
):
    """Chapter ids this student has marked complete on the Chapter Learning
    Page - the one place that flag is surfaced today is that page's own
    button, so a student has no way to see which chapters they'd already
    marked without revisiting each one. Feeds a small badge on the chapter-
    browsing tree (ChaptersPage) instead."""
    rows = (
        db.query(models.ChapterProgress.chapter_id)
          .filter(models.ChapterProgress.student_id == student.id,
                   models.ChapterProgress.marked_complete_at.isnot(None))
          .all()
    )
    return [r[0] for r in rows]


@router.post("/chapters/{chapter_id}/complete", response_model=schemas.ChapterProgressOut)
def mark_chapter_complete(
    chapter_id: int,
    db: Session = Depends(get_db),
    student: models.Student = Depends(get_current_student),
):
    chapter = db.get(models.Section, chapter_id)
    if not chapter or chapter.type != "Chapter":
        raise HTTPException(404, "Chapter not found")

    progress = db.query(models.ChapterProgress).filter_by(student_id=student.id, chapter_id=chapter_id).first()
    if progress is None:
        progress = models.ChapterProgress(student_id=student.id, chapter_id=chapter_id)
        db.add(progress)
    progress.marked_complete_at = datetime.utcnow()
    db.commit()
    return schemas.ChapterProgressOut(
        chapter_id=chapter_id, notes_viewed_at=progress.notes_viewed_at,
        marked_complete_at=progress.marked_complete_at,
    )


# ---------------------------------------------------- teacher content CRUD --
# Learning Content Management (notes/video-links/resources) and Assessment
# Management (chapters/questions). All teacher-gated.

@router.post("/sections", response_model=schemas.ChapterOut)
def create_section(
    payload: schemas.SectionCreate,
    db: Session = Depends(get_db),
    teacher: models.Student = Depends(get_current_teacher),
):
    if payload.parent_id is not None and not db.get(models.Section, payload.parent_id):
        raise HTTPException(404, "parent_id does not exist")
    if not db.get(models.Course, payload.course_id):
        raise HTTPException(404, "course_id does not exist")
    section = models.Section(name=payload.name, type=payload.type,
                              parent_id=payload.parent_id, course_id=payload.course_id)
    db.add(section)
    db.commit()
    db.refresh(section)
    return section


@router.put("/sections/{section_id}", response_model=schemas.ChapterOut)
def update_section(
    section_id: int,
    payload: schemas.SectionCreate,
    db: Session = Depends(get_db),
    teacher: models.Student = Depends(get_current_teacher),
):
    section = db.get(models.Section, section_id)
    if not section:
        raise HTTPException(404, "Section not found")
    section.name, section.type = payload.name, payload.type
    section.parent_id, section.course_id = payload.parent_id, payload.course_id
    db.commit()
    db.refresh(section)
    return section


@router.delete("/sections/{section_id}", response_model=schemas.MessageOut)
def delete_section(
    section_id: int,
    db: Session = Depends(get_db),
    teacher: models.Student = Depends(get_current_teacher),
):
    section = db.get(models.Section, section_id)
    if not section:
        raise HTTPException(404, "Section not found")
    if db.query(models.Section).filter_by(parent_id=section_id).first():
        raise HTTPException(400, "Section has child sections - delete those first")
    db.query(models.QuestionChapter).filter_by(chapter_id=section_id).delete()
    db.delete(section)
    db.commit()
    return schemas.MessageOut(detail="Section deleted.")


def _shuffled_options(options: list[str], correct: int) -> tuple[list[str], int]:
    """Teacher-authored questions are written with the correct option in
    whatever order the author typed it (usually first) - storage must not
    preserve that bias, same discipline as scripts/load_question_bank.py's
    identical helper (kept separate rather than imported, since app code
    shouldn't depend on the one-off scripts/ tree)."""
    order = list(range(len(options)))
    random.shuffle(order)
    new_options = [options[i] for i in order]
    return new_options, order.index(correct)


@router.post("/questions", response_model=schemas.QuestionOut)
def create_question(
    payload: schemas.QuestionCreate,
    db: Session = Depends(get_db),
    teacher: models.Student = Depends(get_current_teacher),
):
    """source='teacher_authored' - deliberately distinct from 'synthetic'
    so a future cleanup pass (see scripts/consolidate_courses.py
    phase4_cleanup, which filters on source=='synthetic') never treats
    real teacher-authored content as junk-eligible filler."""
    chapter = db.get(models.Section, payload.chapter_id)
    if not chapter or chapter.type != "Chapter":
        raise HTTPException(404, "chapter_id does not reference a Chapter")
    if not (0 <= payload.correct_index < len(payload.options)):
        raise HTTPException(400, "correct_index out of range")

    shuffled_options, shuffled_correct = _shuffled_options(payload.options, payload.correct_index)
    next_id = (db.query(func.max(models.Question.id)).scalar() or 0) + 1
    question = models.Question(
        id=next_id, body=payload.body,
        answers_json=json.dumps([{"answer": o} for o in shuffled_options]),
        correct_answer=shuffled_correct, difficulty_label=payload.difficulty_label,
        question_type=payload.question_type, source="teacher_authored",
        scoreable=(payload.question_type != "example"), explanation=payload.explanation,
    )
    db.add(question)
    db.add(models.QuestionChapter(question_id=next_id, chapter_id=payload.chapter_id))
    db.commit()
    db.refresh(question)
    return schemas.QuestionOut(
        id=question.id, body=question.body, answers=shuffled_options,
        difficulty_label=question.difficulty_label, source=question.source, position=0,
    )


@router.delete("/questions/{question_id}", response_model=schemas.MessageOut)
def delete_question(
    question_id: int,
    db: Session = Depends(get_db),
    teacher: models.Student = Depends(get_current_teacher),
):
    question = db.get(models.Question, question_id)
    if not question:
        raise HTTPException(404, "Question not found")
    db.query(models.QuestionChapter).filter_by(question_id=question_id).delete()
    db.delete(question)
    db.commit()
    return schemas.MessageOut(detail="Question deleted.")


@router.post("/resources", response_model=schemas.LearningResourceOut)
def create_resource(
    payload: schemas.LearningResourceCreate,
    db: Session = Depends(get_db),
    teacher: models.Student = Depends(get_current_teacher),
):
    chapter = db.get(models.Section, payload.chapter_id)
    if not chapter or chapter.type != "Chapter":
        raise HTTPException(404, "chapter_id does not reference a Chapter")
    resource = models.LearningResource(**payload.model_dump(), created_by=teacher.id)
    db.add(resource)
    db.commit()
    db.refresh(resource)
    return resource


@router.put("/resources/{resource_id}", response_model=schemas.LearningResourceOut)
def update_resource(
    resource_id: int,
    payload: schemas.LearningResourceUpdate,
    db: Session = Depends(get_db),
    teacher: models.Student = Depends(get_current_teacher),
):
    resource = db.get(models.LearningResource, resource_id)
    if not resource:
        raise HTTPException(404, "Resource not found")
    for k, v in payload.model_dump(exclude_unset=True).items():
        setattr(resource, k, v)
    resource.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(resource)
    return resource


@router.delete("/resources/{resource_id}", response_model=schemas.MessageOut)
def delete_resource(
    resource_id: int,
    db: Session = Depends(get_db),
    teacher: models.Student = Depends(get_current_teacher),
):
    resource = db.get(models.LearningResource, resource_id)
    if not resource:
        raise HTTPException(404, "Resource not found")
    db.delete(resource)
    db.commit()
    return schemas.MessageOut(detail="Resource deleted.")


@router.get("/quiz-templates", response_model=list[schemas.QuizTemplateOut])
def list_quiz_templates(course_id: int, db: Session = Depends(get_db)):
    """Public/student-facing list of published templates - feeds the mock-
    test picker's 'or take a teacher-set quiz' option."""
    return (
        db.query(models.QuizTemplate)
          .filter_by(course_id=course_id, is_published=True)
          .all()
    )
