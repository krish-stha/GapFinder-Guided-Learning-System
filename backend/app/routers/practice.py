import json, random, re
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas
from ..engine import mastery, achievements
from .auth import get_current_student

router = APIRouter(prefix="/practice", tags=["practice"])

# ~72 seconds/question reproduces the reference 50-question -> 60-minute
# mock exam ratio; scales linearly with num_questions for any exam size.
SECONDS_PER_MOCK_QUESTION = 72


def _compute_time_limit(purpose: str, num_questions: int) -> int | None:
    if purpose != "mock_test":
        return None
    return round(num_questions * SECONDS_PER_MOCK_QUESTION)


def _deadline(session: models.PracticeSession) -> datetime | None:
    if session.time_limit_seconds is None:
        return None
    return session.started_at + timedelta(seconds=session.time_limit_seconds)


def _get_owned_session(session_id: int, student: models.Student, db: Session) -> models.PracticeSession:
    session = db.get(models.PracticeSession, session_id)
    if not session:
        raise HTTPException(404, "Session not found")
    if session.student_id != student.id:
        raise HTTPException(403, "Not your session")
    return session


def _score_and_complete(session: models.PracticeSession, db: Session) -> None:
    """Idempotent - a no-op if already completed. Unanswered/skipped
    questions simply don't count as correct, so percentage is always
    correct_count / total_questions (the exam-realistic denominator, not
    just the count of questions actually answered)."""
    if session.status == "completed":
        return
    attempts = db.query(models.Attempt).filter_by(session_id=session.id).all()
    correct = sum(1 for a in attempts if a.is_correct)
    session.correct_count = correct
    session.percentage = round(100 * correct / session.total_questions, 2) if session.total_questions else 0.0
    session.status = "completed"
    session.completed_at = datetime.utcnow()
    db.commit()


def _weighted_sample_by_difficulty(pool: list[tuple[int, str]], num_questions: int,
                                    distribution: dict[str, float]) -> list[int]:
    """pool: list of (question_id, difficulty_label). Allocates
    num_questions across difficulty buckets proportional to `distribution`
    (from mastery.pick_adaptive_distribution), filling any shortfall (a
    bucket running dry, or rounding) from the remaining pool at random -
    so this always returns up to num_questions ids regardless of how the
    chapter's difficulty mix compares to the target distribution."""
    by_diff: dict[str, list[int]] = {}
    for qid, diff in pool:
        by_diff.setdefault(diff or "Medium", []).append(qid)
    for bucket in by_diff.values():
        random.shuffle(bucket)

    chosen: list[int] = []
    chosen_ids: set[int] = set()
    for diff, weight in distribution.items():
        target = round(num_questions * weight)
        take = by_diff.get(diff, [])[:target]
        chosen.extend(take)
        chosen_ids.update(take)

    if len(chosen) < num_questions:
        remaining = [qid for qid, _ in pool if qid not in chosen_ids]
        random.shuffle(remaining)
        chosen.extend(remaining[: num_questions - len(chosen)])

    return chosen[:num_questions]


def _student_chapter_mastery(student_id: int, chapter_id: int, db: Session) -> float | None:
    """Current mastery_estimate for (student, chapter), or None if there's
    no prior evidence yet - used to bias /start's question draw. A light
    read, not the full engine call graph used by /results/me."""
    attempts = (
        db.query(models.Attempt)
          .filter(models.Attempt.student_id == student_id, models.Attempt.chapter_id == chapter_id,
                   models.Attempt.is_correct.isnot(None))
          .order_by(models.Attempt.answered_at.asc())
          .all()
    )
    if not attempts:
        return None
    atts_for_engine = [
        {"is_correct": bool(a.is_correct), "difficulty_label": a.difficulty_label or "Medium", "order": i}
        for i, a in enumerate(attempts)
    ]
    evidence = mastery.compute_chapter_evidence(chapter_id, atts_for_engine)
    return evidence.mastery_estimate if evidence.n_attempts > 0 else None


def _compute_streak(student_id: int, db: Session) -> int:
    """Consecutive days (ending today or yesterday - "yesterday" still
    counts as an active streak so a student doesn't lose it just for not
    having practiced yet today) with at least one recorded attempt.
    Shared by /progress/me, the assistant's streak intent, and
    /achievements/me - was duplicated verbatim in the first two before
    this extraction."""
    dates = {
        row[0].date() for row in db.query(models.Attempt.answered_at).filter(
            models.Attempt.student_id == student_id, models.Attempt.answered_at.isnot(None)
        ).all()
    }
    streak = 0
    day = datetime.utcnow().date()
    if day not in dates:
        day -= timedelta(days=1)
    while day in dates:
        streak += 1
        day -= timedelta(days=1)
    return streak


def _maybe_expire(session: models.PracticeSession, db: Session) -> None:
    """Server-side time enforcement: every endpoint that touches a session
    calls this first. If the deadline has passed while still in_progress,
    the session is auto-finished (scored as of the deadline moment, using
    whatever was already recorded - not the late-request moment) rather
    than left dangling. This also finalizes abandoned sessions the next
    time anything reads them, with no background job needed."""
    if session.status != "in_progress":
        return
    deadline = _deadline(session)
    if deadline is not None and datetime.utcnow() > deadline:
        _score_and_complete(session, db)


@router.post("/start", response_model=schemas.StartSessionResponse)
def start_session(
    payload: schemas.StartSessionRequest,
    db: Session = Depends(get_db),
    student: models.Student = Depends(get_current_student),
):
    # Resolving a quiz_template_id overrides chapter_id/course_id/
    # num_questions/difficulty with the template's own recipe, then reuses
    # the exact same downstream draw/Attempt-pre-creation/answer/finish
    # pipeline as any other session - "create quizzes" needs no new
    # session-lifecycle code, just a different question-*selection* recipe.
    course_id = payload.course_id
    chapter_id = payload.chapter_id
    num_questions = payload.num_questions
    template_difficulty = None
    template_time_limit = None
    if payload.quiz_template_id is not None:
        template = db.get(models.QuizTemplate, payload.quiz_template_id)
        if not template or not template.is_published:
            raise HTTPException(404, "Quiz template not found or not published")
        course_id, chapter_id = template.course_id, template.chapter_id
        num_questions = template.num_questions
        template_difficulty = template.difficulty_label
        template_time_limit = template.time_limit_seconds

    if chapter_id is not None:
        q_query = (
            db.query(models.QuestionChapter.question_id, models.QuestionChapter.chapter_id)
              .join(models.Question)
              .filter(models.QuestionChapter.chapter_id == chapter_id, models.Question.scoreable == True)
        )
    else:
        # Mixed draw across every chapter in the course (mock_test/diagnostic mode).
        chapter_ids = [row[0] for row in (
            db.query(models.Section.id)
              .filter(models.Section.course_id == course_id, models.Section.type == "Chapter")
              .all()
        )]
        q_query = (
            db.query(models.QuestionChapter.question_id, models.QuestionChapter.chapter_id)
              .join(models.Question)
              .filter(models.QuestionChapter.chapter_id.in_(chapter_ids), models.Question.scoreable == True)
        )
    if template_difficulty:
        q_query = q_query.filter(models.Question.difficulty_label == template_difficulty)
    q_rows = q_query.all()
    if not q_rows:
        raise HTTPException(404, "No scoreable questions available")

    # A question can legitimately link to more than one chapter (schema is
    # many-to-many by design). Pick one chapter per question deterministically
    # (lowest chapter_id) for attribution in the per-chapter breakdown.
    chapter_for_question: dict[int, int] = {}
    for qid, cid in q_rows:
        if qid not in chapter_for_question or cid < chapter_for_question[qid]:
            chapter_for_question[qid] = cid

    q_ids = list(chapter_for_question.keys())

    # Adaptive difficulty (between-session only, see mastery.pick_adaptive_distribution's
    # own docstring for why not within-session): a single-chapter practice
    # draw is biased toward the student's current mastery in that chapter,
    # when there's prior evidence. Mixed/mock/diagnostic draws and a
    # student's first-ever attempt at a chapter stay uniform random.
    prior_mastery = (
        _student_chapter_mastery(student.id, chapter_id, db)
        if chapter_id is not None and payload.purpose == "practice" and payload.quiz_template_id is None
        else None
    )
    if prior_mastery is not None:
        difficulty_by_qid = dict(
            db.query(models.Question.id, models.Question.difficulty_label)
              .filter(models.Question.id.in_(q_ids)).all()
        )
        pool = [(qid, difficulty_by_qid.get(qid)) for qid in q_ids]
        distribution = mastery.pick_adaptive_distribution(prior_mastery)
        chosen_ids = _weighted_sample_by_difficulty(pool, num_questions, distribution)
    else:
        random.shuffle(q_ids)
        chosen_ids = q_ids[:num_questions]

    questions_by_id = {q.id: q for q in db.query(models.Question).filter(models.Question.id.in_(chosen_ids)).all()}
    ordered_questions = [questions_by_id[qid] for qid in chosen_ids if qid in questions_by_id]

    time_limit = template_time_limit if template_time_limit is not None else _compute_time_limit(payload.purpose, len(ordered_questions))

    session = models.PracticeSession(
        student_id=student.id, course_id=course_id,
        chapter_id=chapter_id, purpose=payload.purpose,
        total_questions=len(ordered_questions),
        time_limit_seconds=time_limit,
    )
    db.add(session)
    db.flush()  # assigns session.id within the transaction

    for position, q in enumerate(ordered_questions):
        db.add(models.Attempt(
            session_id=session.id, student_id=student.id,
            question_id=q.id, chapter_id=chapter_for_question[q.id],
            position=position, difficulty_label=q.difficulty_label,
        ))
    db.commit()
    db.refresh(session)

    out_questions = [
        schemas.QuestionOut(
            id=q.id, body=q.body,
            answers=[o["answer"] for o in json.loads(q.answers_json)],
            difficulty_label=q.difficulty_label, source=q.source, position=position,
        ) for position, q in enumerate(ordered_questions)
    ]
    return schemas.StartSessionResponse(session_id=session.id, questions=out_questions, time_limit_seconds=time_limit)


@router.post("/{session_id}/answer", response_model=schemas.AnswerResponse)
def answer_question(
    session_id: int,
    payload: schemas.AnswerRequest,
    db: Session = Depends(get_db),
    student: models.Student = Depends(get_current_student),
):
    session = _get_owned_session(session_id, student, db)
    _maybe_expire(session, db)
    if session.status != "in_progress":
        raise HTTPException(409, "Session is not active (already finished or time expired)")

    attempt = db.query(models.Attempt).filter_by(session_id=session_id, question_id=payload.question_id).first()
    if attempt is None:
        raise HTTPException(404, "Question not part of this session")

    question = db.get(models.Question, payload.question_id)
    if not question:
        raise HTTPException(404, "Question not found")

    is_correct = None
    if question.scoreable and payload.selected_index is not None:
        is_correct = (payload.selected_index == question.correct_answer)

    attempt.selected_index = payload.selected_index
    attempt.is_correct = is_correct
    attempt.time_taken_seconds = payload.time_taken_seconds
    attempt.answered_at = datetime.utcnow()
    db.commit()

    # Every session type now defers correctness to /finish's full review -
    # Quick Practice used to reveal it per-question, but the "answer at
    # last, then submit" flow is now consistent everywhere a student
    # answers questions, not just mock tests/diagnostics.
    return schemas.AnswerResponse(is_correct=None, correct_answer=None, explanation=None)


@router.put("/{session_id}/review/{question_id}", response_model=schemas.ReviewToggleOut)
def toggle_review(
    session_id: int,
    question_id: int,
    db: Session = Depends(get_db),
    student: models.Student = Depends(get_current_student),
):
    session = _get_owned_session(session_id, student, db)
    _maybe_expire(session, db)
    if session.status != "in_progress":
        raise HTTPException(409, "Session is not active (already finished or time expired)")

    attempt = db.query(models.Attempt).filter_by(session_id=session_id, question_id=question_id).first()
    if attempt is None:
        raise HTTPException(404, "Question not part of this session")

    attempt.marked_for_review = not attempt.marked_for_review
    db.commit()
    return schemas.ReviewToggleOut(question_id=question_id, marked_for_review=attempt.marked_for_review)


@router.get("/{session_id}/state", response_model=schemas.SessionStateOut)
def session_state(
    session_id: int,
    db: Session = Depends(get_db),
    student: models.Student = Depends(get_current_student),
):
    """Polled by the exam-taking UI for the question navigator/palette and
    countdown - never leaks correctness while the session is in progress."""
    session = _get_owned_session(session_id, student, db)
    _maybe_expire(session, db)

    if session.status != "in_progress":
        seconds_remaining = 0
    else:
        deadline = _deadline(session)
        seconds_remaining = None if deadline is None else max(0, int((deadline - datetime.utcnow()).total_seconds()))

    attempts = (
        db.query(models.Attempt)
          .filter_by(session_id=session_id)
          .order_by(models.Attempt.position.asc())
          .all()
    )
    return schemas.SessionStateOut(
        session_id=session.id, purpose=session.purpose, status=session.status,
        time_limit_seconds=session.time_limit_seconds, seconds_remaining=seconds_remaining,
        questions=[
            schemas.QuestionStateOut(
                question_id=a.question_id, position=a.position or 0,
                answered=a.answered_at is not None, marked_for_review=a.marked_for_review,
                selected_index=a.selected_index,
            ) for a in attempts
        ],
    )


@router.post("/{session_id}/finish", response_model=schemas.FinishSessionOut)
def finish_session(
    session_id: int,
    db: Session = Depends(get_db),
    student: models.Student = Depends(get_current_student),
):
    session = _get_owned_session(session_id, student, db)
    _maybe_expire(session, db)
    if session.status == "in_progress":
        _score_and_complete(session, db)

    attempts = (
        db.query(models.Attempt)
          .filter_by(session_id=session_id)
          .order_by(models.Attempt.position.asc())
          .all()
    )
    questions = {q.id: q for q in db.query(models.Question).filter(
        models.Question.id.in_([a.question_id for a in attempts])
    ).all()}
    chapter_ids_in_session = sorted({a.chapter_id for a in attempts})
    chapters = {c.id: c for c in db.query(models.Section).filter(
        models.Section.id.in_(chapter_ids_in_session)
    ).all()}

    review = []
    for a in attempts:
        q = questions.get(a.question_id)
        chapter = chapters.get(a.chapter_id)
        review.append(schemas.QuestionReviewOut(
            question_id=a.question_id, position=a.position or 0,
            body=q.body if q else "",
            answers=[o["answer"] for o in json.loads(q.answers_json)] if q else [],
            selected_index=a.selected_index, correct_answer=q.correct_answer if q else None,
            is_correct=a.is_correct, chapter_id=a.chapter_id,
            chapter_name=chapter.name if chapter else f"Chapter {a.chapter_id}",
            explanation=q.explanation if q else None,
        ))

    # Per-chapter mastery evidence, same engine/pattern as /results/me -
    # computed from the student's FULL history in each chapter this
    # session touched, not just this session's own attempts.
    all_scored = (
        db.query(models.Attempt)
          .filter(models.Attempt.student_id == student.id, models.Attempt.is_correct.isnot(None))
          .order_by(models.Attempt.answered_at.asc())
          .all()
    )
    by_chapter: dict[int, list[dict]] = {}
    for a in all_scored:
        by_chapter.setdefault(a.chapter_id, []).append({
            "is_correct": bool(a.is_correct),
            "difficulty_label": a.difficulty_label or "Medium",
            "order": len(by_chapter.get(a.chapter_id, [])),
        })
    evidence_by_chapter = {cid: mastery.compute_chapter_evidence(cid, atts) for cid, atts in by_chapter.items()}
    chapter_to_subject = _chapter_to_top_subject(list(by_chapter.keys()), db)
    subj_cmp = mastery.subject_comparison_map(list(evidence_by_chapter.values()), chapter_to_subject)

    chapter_breakdown = []
    for cid in chapter_ids_in_session:
        if cid not in by_chapter:
            continue
        evidence = evidence_by_chapter[cid]
        chapter = chapters.get(cid)
        name = chapter.name if chapter else f"Chapter {cid}"
        chapter_breakdown.append(schemas.ChapterEvidenceOut(
            chapter_id=cid, chapter_name=name,
            n_attempts=evidence.n_attempts, raw_accuracy=evidence.raw_accuracy,
            mastery_estimate=evidence.mastery_estimate, confidence=evidence.confidence,
            trend_slope=evidence.trend_slope, trend_significant=evidence.trend_significant,
            priority_score=evidence.priority_score, priority_band=evidence.priority_band,
            explanation=mastery.explain(evidence, name, subj_cmp.get(cid)),
            subject_avg_mastery=subj_cmp.get(cid),
        ))

    return schemas.FinishSessionOut(
        session_id=session.id, purpose=session.purpose,
        total_questions=session.total_questions, correct_count=session.correct_count,
        percentage=session.percentage, status=session.status,
        chapter_breakdown=chapter_breakdown, review=review,
    )


@router.get("/chapters/{chapter_id}/detail", response_model=schemas.ChapterDetailOut)
def chapter_detail(
    chapter_id: int,
    db: Session = Depends(get_db),
    student: models.Student = Depends(get_current_student),
):
    """Per-chapter drill-down for the authenticated student: full evidence
    plus the ordered attempt history behind it (charter F.1 "per-chapter
    detail: score history sparkline, attempts, trend")."""
    attempts = (
        db.query(models.Attempt)
          .filter(models.Attempt.student_id == student.id,
                   models.Attempt.chapter_id == chapter_id,
                   models.Attempt.is_correct.isnot(None))
          .order_by(models.Attempt.answered_at.asc())
          .all()
    )
    if not attempts:
        raise HTTPException(404, "No recorded attempts for this chapter yet")

    atts_for_engine = [
        {"is_correct": bool(a.is_correct), "difficulty_label": a.difficulty_label or "Medium", "order": i}
        for i, a in enumerate(attempts)
    ]
    evidence = mastery.compute_chapter_evidence(chapter_id, atts_for_engine)

    chapter = db.get(models.Section, chapter_id)
    name = chapter.name if chapter else f"Chapter {chapter_id}"
    course_id = chapter.course_id if chapter else 0

    # Same "compared with your other chapters in this subject" comparison
    # every other explain() call site uses - needs the student's full
    # evidence set (not just this chapter) to compute honestly.
    all_evidence, _ = _student_by_chapter_evidence(student.id, db)
    chapter_to_subject = _chapter_to_top_subject([ev.chapter_id for ev in all_evidence], db)
    subj_cmp = mastery.subject_comparison_map(all_evidence, chapter_to_subject)

    return schemas.ChapterDetailOut(
        chapter_id=chapter_id, chapter_name=name, course_id=course_id,
        n_attempts=evidence.n_attempts, raw_accuracy=evidence.raw_accuracy,
        mastery_estimate=evidence.mastery_estimate, confidence=evidence.confidence,
        trend_slope=evidence.trend_slope, trend_significant=evidence.trend_significant,
        priority_score=evidence.priority_score, priority_band=evidence.priority_band,
        explanation=mastery.explain(evidence, name, subj_cmp.get(chapter_id)),
        subject_avg_mastery=subj_cmp.get(chapter_id),
        attempts=[
            schemas.AttemptOut(order=i, is_correct=bool(a.is_correct),
                                difficulty_label=a.difficulty_label, answered_at=a.answered_at)
            for i, a in enumerate(attempts)
        ],
    )


def _chapter_to_top_subject(chapter_ids: list[int], db: Session) -> dict[int, int]:
    """Walks Section.parent_id up from each chapter to its top-level
    Subject ancestor. Used by /performance/me's subject-wise breakdown -
    a small bulk helper rather than a per-chapter N+1 query loop."""
    if not chapter_ids:
        return {}
    all_sections = {s.id: s for s in db.query(models.Section).all()}
    result: dict[int, int] = {}
    for cid in chapter_ids:
        node = all_sections.get(cid)
        seen = set()
        while node is not None and node.parent_id is not None and node.id not in seen:
            seen.add(node.id)
            node = all_sections.get(node.parent_id)
        if node is not None:
            result[cid] = node.id
    return result


def _student_by_chapter_evidence(student_id: int, db: Session) -> tuple[list, float]:
    """Shared by /results/me, /learning-path/me and /progress/me - full
    scored-attempt history grouped by chapter, and overall accuracy."""
    attempts = (
        db.query(models.Attempt)
          .filter(models.Attempt.student_id == student_id, models.Attempt.is_correct.isnot(None))
          .order_by(models.Attempt.answered_at.asc())
          .all()
    )
    by_chapter: dict[int, list[dict]] = {}
    for a in attempts:
        by_chapter.setdefault(a.chapter_id, []).append({
            "is_correct": bool(a.is_correct),
            "difficulty_label": a.difficulty_label or "Medium",
            "order": len(by_chapter.get(a.chapter_id, [])),
        })
    all_evidence = [mastery.compute_chapter_evidence(cid, atts) for cid, atts in by_chapter.items()]
    overall_acc = sum(1 for a in attempts if a.is_correct) / len(attempts) if attempts else 0.0
    return all_evidence, overall_acc


@router.get("/learning-path/me", response_model=list[schemas.LearningPathStepOut])
def learning_path(
    db: Session = Depends(get_db),
    student: models.Student = Depends(get_current_student),
):
    """Personalized Learning Path / Learning Recommendations: reuses the
    same compute_chapter_evidence -> rank_chapters -> explain pipeline as
    /results/me, extended with build_learning_path's not-started tail.
    Scoped to courses the student has actually practiced in at least once
    (derived from their PracticeSession history) - there's no separate
    course-enrollment field on Student to seed this from otherwise, and a
    student with zero sessions has nothing to build a path from yet
    (the frontend shows a "take a diagnostic" prompt in that case)."""
    course_ids = {row[0] for row in db.query(models.PracticeSession.course_id).filter_by(student_id=student.id).distinct()}
    if not course_ids:
        return []

    all_evidence, _ = _student_by_chapter_evidence(student.id, db)
    ranked = mastery.rank_chapters(all_evidence)
    chapter_to_subject = _chapter_to_top_subject([ev.chapter_id for ev in all_evidence], db)
    subj_cmp = mastery.subject_comparison_map(all_evidence, chapter_to_subject)

    all_chapter_ids = [row[0] for row in (
        db.query(models.Section.id)
          .filter(models.Section.course_id.in_(course_ids), models.Section.type == "Chapter")
          .all()
    )]
    path = mastery.build_learning_path(ranked, all_chapter_ids)

    chapters = {c.id: c for c in db.query(models.Section).filter(
        models.Section.id.in_([step["chapter_id"] for step in path])
    ).all()}
    resource_chapter_ids = {
        row[0] for row in db.query(models.LearningResource.chapter_id).filter(
            models.LearningResource.chapter_id.in_(list(chapters.keys()))
        ).distinct()
    }
    resource_types_by_chapter: dict[int, set[str]] = {}
    for cid, rtype in (
        db.query(models.LearningResource.chapter_id, models.LearningResource.type)
          .filter(models.LearningResource.chapter_id.in_(list(chapters.keys())))
          .all()
    ):
        resource_types_by_chapter.setdefault(cid, set()).add(rtype)

    out = []
    for step in path:
        cid = step["chapter_id"]
        chapter = chapters.get(cid)
        name = chapter.name if chapter else f"Chapter {cid}"
        evidence = step["evidence"]
        types = resource_types_by_chapter.get(cid, set())
        if evidence is None:
            out.append(schemas.LearningPathStepOut(
                chapter_id=cid, chapter_name=name, status=step["status"],
                mastery_estimate=None, explanation=f"You haven't attempted any questions in {name} yet.",
                has_notes="note" in types or "resource_link" in types, has_video="video" in types,
            ))
            continue
        out.append(schemas.LearningPathStepOut(
            chapter_id=cid, chapter_name=name, status=step["status"],
            mastery_estimate=evidence.mastery_estimate,
            explanation=mastery.explain(evidence, name, subj_cmp.get(cid)),
            has_notes="note" in types or "resource_link" in types, has_video="video" in types,
            n_attempts=evidence.n_attempts, raw_accuracy=evidence.raw_accuracy,
            confidence=evidence.confidence, trend_slope=evidence.trend_slope,
            trend_significant=evidence.trend_significant, priority_score=evidence.priority_score,
            subject_avg_mastery=subj_cmp.get(cid),
        ))
    return out


@router.get("/performance/me", response_model=schemas.PerformanceOut)
def performance_me(
    db: Session = Depends(get_db),
    student: models.Student = Depends(get_current_student),
):
    """My Performance: scores over time, subject-wise performance,
    session history."""
    # Only completed sessions - an abandoned in_progress session (e.g. a
    # Quick Practice tab closed mid-run, which has no resume mechanism and
    # no server-side expiry the way mock tests do) has a meaningless
    # correct_count/percentage (still 0/None) and would otherwise show up
    # as a misleading "0/5, In progress" row forever.
    sessions = (
        db.query(models.PracticeSession)
          .filter_by(student_id=student.id, status="completed")
          .order_by(models.PracticeSession.started_at.desc())
          .limit(50)
          .all()
    )
    session_history = [
        schemas.SessionHistoryEntryOut(
            session_id=s.id, course_id=s.course_id, chapter_id=s.chapter_id, purpose=s.purpose,
            started_at=s.started_at, completed_at=s.completed_at, total_questions=s.total_questions,
            correct_count=s.correct_count, percentage=s.percentage,
        ) for s in sessions
    ]

    scored_attempts = (
        db.query(models.Attempt)
          .filter(models.Attempt.student_id == student.id, models.Attempt.is_correct.isnot(None))
          .order_by(models.Attempt.answered_at.asc())
          .all()
    )
    accuracy_trend = [
        schemas.AccuracyPointOut(
            attempt_order=i, answered_at=a.answered_at, is_correct=bool(a.is_correct), chapter_id=a.chapter_id,
        )
        for i, a in enumerate(scored_attempts)
    ]

    all_evidence, _ = _student_by_chapter_evidence(student.id, db)
    chapter_to_subject = _chapter_to_top_subject([ev.chapter_id for ev in all_evidence], db)
    subject_agg = mastery.aggregate_subject_evidence(all_evidence, chapter_to_subject)
    subjects = {s.id: s for s in db.query(models.Section).filter(models.Section.id.in_(list(subject_agg.keys()))).all()}
    subject_breakdown = [
        schemas.SubjectPerformanceOut(
            subject_id=sid, subject_name=subjects[sid].name if sid in subjects else f"Subject {sid}",
            n_attempts=data["n_attempts"], avg_mastery=data["avg_mastery"],
        ) for sid, data in subject_agg.items()
    ]

    return schemas.PerformanceOut(
        accuracy_trend=accuracy_trend, subject_breakdown=subject_breakdown, session_history=session_history,
    )


@router.get("/progress/me", response_model=schemas.ProgressOut)
def progress_me(
    db: Session = Depends(get_db),
    student: models.Student = Depends(get_current_student),
):
    """Progress & Improvement: streak, chapters completed, before/after
    comparison split at the student's first completed diagnostic session."""
    streak = _compute_streak(student.id, db)

    all_evidence, _ = _student_by_chapter_evidence(student.id, db)
    # priority_band != "Insufficient evidence" (not just mastery_estimate
    # crossing the threshold) - a chapter with only 1-2 lucky attempts can
    # already show mastery_estimate >= 0.7 despite the engine's own
    # confidence field being far too low to trust that number (see
    # teacher.py's CONFIDENT_BANDS, which every other aggregate in this app
    # already gates on - this endpoint and achievements_me below were the
    # two places that didn't, letting a "mastered" claim slip through on
    # evidence the app itself doesn't consider sufficient).
    mastered_evidence = [
        ev for ev in all_evidence
        if ev.priority_band != "Insufficient evidence"
        and ev.mastery_estimate >= mastery.DEFAULT_WEIGHTS.mastery_complete_threshold
    ]
    chapters_completed = len(mastered_evidence)
    chapters_total_tracked = sum(1 for ev in all_evidence if ev.n_attempts > 0)

    mastered_chapter_names = {c.id: c.name for c in db.query(models.Section).filter(
        models.Section.id.in_([ev.chapter_id for ev in mastered_evidence])
    ).all()}
    mastered_chapters = sorted(
        [
            schemas.MasteredChapterOut(
                chapter_id=ev.chapter_id,
                chapter_name=mastered_chapter_names.get(ev.chapter_id, f"Chapter {ev.chapter_id}"),
                mastery_estimate=ev.mastery_estimate, n_attempts=ev.n_attempts, confidence=ev.confidence,
            )
            for ev in mastered_evidence
        ],
        key=lambda m: -m.mastery_estimate,
    )

    first_diagnostic = (
        db.query(models.PracticeSession)
          .filter_by(student_id=student.id, purpose="diagnostic", status="completed")
          .order_by(models.PracticeSession.completed_at.asc())
          .first()
    )
    before_after = []
    if first_diagnostic is not None and first_diagnostic.completed_at is not None:
        split_at = first_diagnostic.completed_at
        all_attempts = (
            db.query(models.Attempt)
              .filter(models.Attempt.student_id == student.id, models.Attempt.is_correct.isnot(None))
              .order_by(models.Attempt.answered_at.asc())
              .all()
        )
        by_chapter_before: dict[int, list[dict]] = {}
        by_chapter_after: dict[int, list[dict]] = {}
        for a in all_attempts:
            bucket = by_chapter_before if a.answered_at <= split_at else by_chapter_after
            lst = bucket.setdefault(a.chapter_id, [])
            lst.append({"is_correct": bool(a.is_correct), "difficulty_label": a.difficulty_label or "Medium", "order": len(lst)})

        touched_chapters = set(by_chapter_before) | set(by_chapter_after)
        chapters = {c.id: c for c in db.query(models.Section).filter(models.Section.id.in_(list(touched_chapters))).all()}
        for cid in touched_chapters:
            before_ev = mastery.compute_chapter_evidence(cid, by_chapter_before.get(cid, [])) if by_chapter_before.get(cid) else None
            after_ev = mastery.compute_chapter_evidence(cid, by_chapter_after.get(cid, [])) if by_chapter_after.get(cid) else None
            chapter = chapters.get(cid)
            before_after.append(schemas.BeforeAfterOut(
                chapter_id=cid, chapter_name=chapter.name if chapter else f"Chapter {cid}",
                mastery_before=before_ev.mastery_estimate if before_ev else None,
                mastery_after=after_ev.mastery_estimate if after_ev else None,
            ))

    return schemas.ProgressOut(
        streak_days=streak, chapters_completed=chapters_completed,
        chapters_total_tracked=chapters_total_tracked, before_after=before_after,
        mastered_chapters=mastered_chapters,
    )


@router.get("/achievements/me", response_model=schemas.AchievementsOut)
def achievements_me(
    db: Session = Depends(get_db),
    student: models.Student = Depends(get_current_student),
):
    """Gamification strip: badges + the single closest next milestone per
    family. Everything here is derived live from Attempt/PracticeSession
    rows - no badge/points state is ever persisted, same "compute, don't
    store" discipline as mastery.py and /progress/me."""
    streak_days = _compute_streak(student.id, db)
    questions_answered = (
        db.query(models.Attempt)
          .filter(models.Attempt.student_id == student.id, models.Attempt.is_correct.isnot(None))
          .count()
    )
    all_evidence, _ = _student_by_chapter_evidence(student.id, db)
    # Same confidence gate as /progress/me's chapters_completed - a
    # "Chapters Mastered" badge earned off 1-2 lucky attempts would be a
    # real, checkable false claim, not just an edge case.
    chapters_mastered = sum(
        1 for ev in all_evidence
        if ev.priority_band != "Insufficient evidence"
        and ev.mastery_estimate >= mastery.DEFAULT_WEIGHTS.mastery_complete_threshold
    )
    mock_tests_completed = (
        db.query(models.PracticeSession)
          .filter_by(student_id=student.id, purpose="mock_test", status="completed")
          .count()
    )
    diagnostic_completed = (
        db.query(models.PracticeSession)
          .filter_by(student_id=student.id, purpose="diagnostic", status="completed")
          .first()
        is not None
    )

    result = achievements.compute_achievements({
        "streak_days": streak_days,
        "questions_answered": questions_answered,
        "chapters_mastered": chapters_mastered,
        "mock_tests_completed": mock_tests_completed,
        "diagnostic_completed": diagnostic_completed,
    })
    return schemas.AchievementsOut(
        badges=[schemas.BadgeOut(**vars(b)) for b in result["badges"]],
        next_milestones=[schemas.NextMilestoneOut(**vars(m)) for m in result["next_milestones"]],
    )


@router.get("/recent-chapters/me", response_model=list[schemas.RecentChapterOut])
def recent_chapters_me(
    limit: int = 3,
    db: Session = Depends(get_db),
    student: models.Student = Depends(get_current_student),
):
    """'Continue practicing' shortcut list: the student's most recently
    touched chapters, most-recent-first, joined with current evidence via
    the same helper /results/me and /learning-path/me already share."""
    rows = (
        db.query(models.Attempt.chapter_id, func.max(models.Attempt.answered_at).label("last_at"))
          .filter(models.Attempt.student_id == student.id, models.Attempt.answered_at.isnot(None))
          .group_by(models.Attempt.chapter_id)
          .order_by(func.max(models.Attempt.answered_at).desc())
          .limit(limit)
          .all()
    )
    if not rows:
        return []

    all_evidence, _ = _student_by_chapter_evidence(student.id, db)
    evidence_by_chapter = {ev.chapter_id: ev for ev in all_evidence}
    chapters = {c.id: c for c in db.query(models.Section).filter(
        models.Section.id.in_([r.chapter_id for r in rows])
    ).all()}

    out = []
    for r in rows:
        chapter = chapters.get(r.chapter_id)
        ev = evidence_by_chapter.get(r.chapter_id)
        out.append(schemas.RecentChapterOut(
            chapter_id=r.chapter_id,
            chapter_name=chapter.name if chapter else f"Chapter {r.chapter_id}",
            course_id=chapter.course_id if chapter else 0,
            last_practiced_at=r.last_at,
            mastery_estimate=ev.mastery_estimate if ev else None,
            priority_band=ev.priority_band if ev else None,
        ))
    return out


@router.get("/results/me", response_model=list[schemas.ChapterEvidenceOut])
def student_results(
    db: Session = Depends(get_db),
    student: models.Student = Depends(get_current_student),
):
    """The core deliverable: ranked, explained weak-chapter list for the
    authenticated student, computed from attempts THIS system recorded."""
    attempts = (
        db.query(models.Attempt)
          .filter(models.Attempt.student_id == student.id, models.Attempt.is_correct.isnot(None))
          .order_by(models.Attempt.answered_at.asc())
          .all()
    )
    if not attempts:
        return []

    by_chapter: dict[int, list[dict]] = {}
    for i, a in enumerate(attempts):
        by_chapter.setdefault(a.chapter_id, []).append({
            "is_correct": bool(a.is_correct),
            "difficulty_label": a.difficulty_label or "Medium",
            "order": len(by_chapter.get(a.chapter_id, [])),
        })

    all_evidence = [mastery.compute_chapter_evidence(cid, atts) for cid, atts in by_chapter.items()]
    ranked = mastery.rank_chapters(all_evidence)
    chapter_to_subject = _chapter_to_top_subject([ev.chapter_id for ev in all_evidence], db)
    subj_cmp = mastery.subject_comparison_map(all_evidence, chapter_to_subject)

    out = []
    for ev in ranked:
        chapter = db.get(models.Section, ev.chapter_id)
        name = chapter.name if chapter else f"Chapter {ev.chapter_id}"
        out.append(schemas.ChapterEvidenceOut(
            chapter_id=ev.chapter_id, chapter_name=name,
            n_attempts=ev.n_attempts, raw_accuracy=ev.raw_accuracy,
            mastery_estimate=ev.mastery_estimate, confidence=ev.confidence,
            trend_slope=ev.trend_slope, trend_significant=ev.trend_significant,
            priority_score=ev.priority_score, priority_band=ev.priority_band,
            explanation=mastery.explain(ev, name, subj_cmp.get(ev.chapter_id)),
            subject_avg_mastery=subj_cmp.get(ev.chapter_id),
        ))
    return out


# --------------------------------------------------------------- assistant --
# Fixed intent patterns dispatch directly into the same mastery-engine
# pipeline every other endpoint here uses, formatting templated responses
# with real substituted numbers - nothing generated or invented. Same
# discipline mastery.explain() already uses and is unit-tested for: every
# clause traces to a real evidence field.

ASSISTANT_HELP = (
    "I can answer questions like:\n"
    '- "Which chapters should I study before my exam?"\n'
    '- "How am I doing overall?"\n'
    '- "How am I doing in <chapter name>?"\n'
    '- "How am I doing in <subject name>?"\n'
    '- "How many chapters have I mastered?"\n'
    '- "Am I improving?"\n'
    '- "How many questions have I answered?"\n'
    '- "How is mastery calculated?"\n'
    '- "What\'s my streak?"'
)

_MASTERY_EXPLAIN_PATTERN = re.compile(r"\b(how is mastery|what is mastery|mastery (calculat\w*|mean\w*|differ\w*|vs\.? accuracy))\b", re.I)
_CHAPTERS_MASTERED_PATTERN = re.compile(r"\bmaster(ed)?\b", re.I)
_IMPROVING_PATTERN = re.compile(r"\b(improv\w*|getting better|am i (doing )?better)\b", re.I)
_QUESTIONS_COUNT_PATTERN = re.compile(r"\b(how many questions|questions (have i|answered|attempted))\b", re.I)
_WEAK_CHAPTERS_PATTERN = re.compile(r"\b(weak|study|focus|priorit\w*|should i|what.*(study|work on)|exam)\b", re.I)
_PERFORMANCE_PATTERN = re.compile(r"\b(how am i doing|performance|overall|summary)\b", re.I)
_STREAK_PATTERN = re.compile(r"\b(streak|consistency|how many days)\b", re.I)


def match_intent(
    question: str, chapter_names: dict[int, str], subject_names: dict[int, str] | None = None,
) -> tuple[str, int | None]:
    """Pure (no DB/HTTP) - same discipline as app.engine.mastery, so the
    actual pattern-matching decision is unit-testable in isolation.
    `chapter_names`/`subject_names` are the student's own tracked names,
    passed in already-resolved rather than queried here. Checked in this
    order: a named chapter or subject is the most specific match, so those
    are checked first; "help" means none of the fixed patterns matched."""
    q = question.lower()
    for chapter_id, name in chapter_names.items():
        if name.lower() in q:
            return "specific_chapter", chapter_id
    for subject_id, name in (subject_names or {}).items():
        if name.lower() in q:
            return "subject_mastery", subject_id
    if _MASTERY_EXPLAIN_PATTERN.search(q):
        return "mastery_explain", None
    if _CHAPTERS_MASTERED_PATTERN.search(q):
        return "chapters_mastered", None
    if _IMPROVING_PATTERN.search(q):
        return "improving", None
    if _QUESTIONS_COUNT_PATTERN.search(q):
        return "questions_count", None
    if _WEAK_CHAPTERS_PATTERN.search(q):
        return "weak_chapters", None
    if _PERFORMANCE_PATTERN.search(q):
        return "performance_summary", None
    if _STREAK_PATTERN.search(q):
        return "streak", None
    return "help", None


def _assistant_answer(question: str, student_id: int, db: Session) -> tuple[str, str | None]:
    all_evidence, overall_acc = _student_by_chapter_evidence(student_id, db)
    ranked = mastery.rank_chapters(all_evidence)
    chapters = {
        c.id: c for c in db.query(models.Section).filter(
            models.Section.id.in_([ev.chapter_id for ev in all_evidence])
        ).all()
    }
    chapter_names = {cid: c.name for cid, c in chapters.items()}
    chapter_to_subject = _chapter_to_top_subject([ev.chapter_id for ev in all_evidence], db)
    subject_agg = mastery.aggregate_subject_evidence(all_evidence, chapter_to_subject)
    subject_names = {
        s.id: s.name for s in db.query(models.Section).filter(models.Section.id.in_(list(subject_agg.keys()))).all()
    }

    intent, matched_id = match_intent(question, chapter_names, subject_names)

    if intent == "specific_chapter":
        ev = next(e for e in ranked if e.chapter_id == matched_id)
        subj_cmp = mastery.subject_comparison_map(all_evidence, chapter_to_subject)
        return mastery.explain(ev, chapters[matched_id].name, subj_cmp.get(matched_id)), intent

    if intent == "subject_mastery":
        agg = subject_agg.get(matched_id)
        name = subject_names.get(matched_id, f"Subject {matched_id}")
        if agg is None:
            return f"You haven't answered any scored questions in {name} yet.", intent
        return (
            f"Your average mastery in {name} is {round(agg['avg_mastery'] * 100)}% across "
            f"{agg['n_attempts']} question(s)."
        ), intent

    if intent == "mastery_explain":
        return (
            "Mastery isn't the same as accuracy. Accuracy is just correct ÷ total questions. Mastery blends "
            "difficulty-adjusted accuracy (harder questions count more) with a recency-weighted score (recent "
            "attempts count more than older ones), so it can move differently than raw accuracy - especially if "
            "you've recently improved or declined, or tackled harder questions."
        ), intent

    if intent == "chapters_mastered":
        mastered = [
            ev for ev in all_evidence
            if ev.priority_band != "Insufficient evidence"
            and ev.mastery_estimate >= mastery.DEFAULT_WEIGHTS.mastery_complete_threshold
        ]
        if not mastered:
            return "You haven't mastered any chapters yet (mastery ≥ 70% with enough attempts to trust it).", intent
        names = ", ".join(chapter_names.get(ev.chapter_id, f"Chapter {ev.chapter_id}") for ev in mastered[:5])
        more = f" and {len(mastered) - 5} more" if len(mastered) > 5 else ""
        return f"You've mastered {len(mastered)} chapter(s): {names}{more}.", intent

    if intent == "improving":
        improving = [ev for ev in all_evidence if ev.trend_significant and ev.trend_slope is not None and ev.trend_slope > 0]
        declining = [ev for ev in all_evidence if ev.trend_significant and ev.trend_slope is not None and ev.trend_slope < 0]
        if not improving and not declining:
            return "Your recent attempts don't show a clear trend yet in either direction - keep practicing to build up evidence.", intent
        parts = []
        if improving:
            parts.append(f"improving in {len(improving)} chapter(s)")
        if declining:
            parts.append(f"declining in {len(declining)} chapter(s)")
        return f"Based on your recent attempts, you're {' and '.join(parts)}.", intent

    if intent == "questions_count":
        n = sum(ev.n_attempts for ev in all_evidence)
        return f"You've answered {n} scored question(s) across {len(all_evidence)} chapter(s).", intent

    if intent == "weak_chapters":
        if not ranked:
            return (
                "You haven't practiced any chapters yet, so I don't have evidence to base a "
                "recommendation on. Try a diagnostic assessment or practice a chapter first."
            ), intent
        lines = []
        for i, ev in enumerate(ranked[:3]):
            chapter = chapters.get(ev.chapter_id)
            name = chapter.name if chapter else f"Chapter {ev.chapter_id}"
            lines.append(f"Priority {i + 1}: {name} - {round(ev.mastery_estimate * 100)}% mastery")
        return "Based on your practice history:\n" + "\n".join(lines), intent

    if intent == "performance_summary":
        if not all_evidence:
            return "You haven't answered any scored questions yet, so there's no performance data to summarize.", intent
        n_high = sum(1 for ev in all_evidence if ev.priority_band == "High")
        return (
            f"You've tracked {len(all_evidence)} chapter(s) with an overall accuracy of "
            f"{round(overall_acc * 100)}%. {n_high} chapter(s) are currently High priority."
        ), intent

    if intent == "streak":
        streak = _compute_streak(student_id, db)
        return f"Your current streak is {streak} day{'s' if streak != 1 else ''}.", intent

    return ASSISTANT_HELP, None


@router.post("/assistant/ask", response_model=schemas.AssistantAskResponse)
def ask_assistant(
    payload: schemas.AssistantAskRequest,
    db: Session = Depends(get_db),
    student: models.Student = Depends(get_current_student),
):
    answer, matched_intent = _assistant_answer(payload.question, student.id, db)
    return schemas.AssistantAskResponse(answer=answer, matched_intent=matched_intent)
    return out
