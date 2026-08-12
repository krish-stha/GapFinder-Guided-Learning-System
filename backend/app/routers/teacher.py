import secrets

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas
from ..engine import mastery
from .auth import get_current_teacher
from .practice import _student_by_chapter_evidence, _chapter_to_top_subject

router = APIRouter(prefix="/teacher", tags=["teacher"])

# a chapter/student only counts toward the aggregate views once the
# mastery engine itself trusts the evidence - keeps "the class is failing
# X" from being driven by one or two barely-attempted rows
CONFIDENT_BANDS = {"High", "Medium", "Low"}


def _compute_all_evidence(db: Session, course_id: int | None = None, class_id: int | None = None) -> list[dict]:
    """Every (student, chapter) evidence row across the whole system - or,
    when `class_id` is given, scoped to just that SchoolClass's enrolled
    students. Default (class_id=None) stays "cohort = every student with
    recorded activity", unchanged from before SchoolClass existed - this
    is an additive filter, not a behavior change. Reuses app.engine.mastery
    exactly as the student-facing endpoint does, just fanned out over
    every relevant student instead of one.

    `course_id`, when given, scopes to chapters under that course only -
    filtered by chapter (not by the session's own course_id) so a mixed
    mock test's per-question chapter attribution still counts correctly
    even though the session itself was started against one course."""
    query = db.query(models.Attempt).filter(models.Attempt.is_correct.isnot(None))
    if class_id is not None:
        class_student_ids = [
            row[0] for row in db.query(models.Student.id).filter(models.Student.class_id == class_id).all()
        ]
        query = query.filter(models.Attempt.student_id.in_(class_student_ids))
    attempts = query.order_by(models.Attempt.student_id, models.Attempt.chapter_id, models.Attempt.answered_at.asc()).all()
    if not attempts:
        return []

    by_student_chapter: dict[tuple[int, int], list[dict]] = {}
    for a in attempts:
        key = (a.student_id, a.chapter_id)
        atts = by_student_chapter.setdefault(key, [])
        atts.append({
            "is_correct": bool(a.is_correct),
            "difficulty_label": a.difficulty_label or "Medium",
            "order": len(atts),
        })

    student_ids = {sid for sid, _ in by_student_chapter}
    chapter_ids = {cid for _, cid in by_student_chapter}
    students = {s.id: s for s in db.query(models.Student).filter(models.Student.id.in_(student_ids))}
    chapters = {c.id: c for c in db.query(models.Section).filter(models.Section.id.in_(chapter_ids))}

    results = []
    for (sid, cid), atts in by_student_chapter.items():
        chapter = chapters.get(cid)
        if course_id is not None and (chapter is None or chapter.course_id != course_id):
            continue
        evidence = mastery.compute_chapter_evidence(cid, atts)
        student = students.get(sid)
        results.append({
            "student_id": sid, "student_name": student.name if student else f"Student {sid}",
            "chapter_id": cid, "chapter_name": chapter.name if chapter else f"Chapter {cid}",
            "evidence": evidence,
        })
    return results


@router.get("/cohort-evidence", response_model=list[schemas.CohortChapterEvidenceOut])
def cohort_evidence(
    course_id: int | None = None,
    class_id: int | None = None,
    db: Session = Depends(get_db),
    teacher: models.Student = Depends(get_current_teacher),
):
    """Raw material for a students x chapters heatmap - one row per
    (student, chapter) pair with recorded attempts. Optionally scoped to
    one course and/or one class; students with no activity in scope simply
    have no rows and disappear from the heatmap along with it."""
    return [
        schemas.CohortChapterEvidenceOut(
            student_id=r["student_id"], student_name=r["student_name"],
            chapter_id=r["chapter_id"], chapter_name=r["chapter_name"],
            n_attempts=r["evidence"].n_attempts, mastery_estimate=r["evidence"].mastery_estimate,
            confidence=r["evidence"].confidence, priority_score=r["evidence"].priority_score,
            priority_band=r["evidence"].priority_band,
        )
        for r in _compute_all_evidence(db, course_id, class_id)
    ]


@router.get("/chapters-failing", response_model=list[schemas.ChapterWeaknessOut])
def chapters_failing(
    class_id: int | None = None,
    db: Session = Depends(get_db),
    teacher: models.Student = Depends(get_current_teacher),
):
    """Ranked by how many students are in the High-priority band for that
    chapter (most first), tie-broken by lowest average mastery. Optionally
    scoped to one class."""
    by_chapter: dict[int, list[dict]] = {}
    for r in _compute_all_evidence(db, class_id=class_id):
        by_chapter.setdefault(r["chapter_id"], []).append(r)

    out = []
    for cid, rows in by_chapter.items():
        confident = [r for r in rows if r["evidence"].priority_band in CONFIDENT_BANDS]
        if not confident:
            continue
        n_high = sum(1 for r in confident if r["evidence"].priority_band == "High")
        avg_mastery = sum(r["evidence"].mastery_estimate for r in confident) / len(confident)
        out.append(schemas.ChapterWeaknessOut(
            chapter_id=cid, chapter_name=rows[0]["chapter_name"],
            n_students=len(confident), n_students_high_priority=n_high,
            avg_mastery=round(avg_mastery, 3),
        ))

    out.sort(key=lambda c: (-c.n_students_high_priority, c.avg_mastery))
    return out


@router.get("/students-needing-attention", response_model=list[schemas.StudentAttentionOut])
def students_needing_attention(db: Session = Depends(get_db), teacher: models.Student = Depends(get_current_teacher)):
    """Ranked by how many of a student's own chapters are High-priority
    (most first), tie-broken by highest average priority score."""
    by_student: dict[int, list[dict]] = {}
    for r in _compute_all_evidence(db):
        by_student.setdefault(r["student_id"], []).append(r)

    out = []
    for sid, rows in by_student.items():
        confident = [r for r in rows if r["evidence"].priority_band in CONFIDENT_BANDS]
        if not confident:
            continue
        n_high = sum(1 for r in confident if r["evidence"].priority_band == "High")
        avg_priority = sum(r["evidence"].priority_score for r in confident) / len(confident)
        weakest = max(confident, key=lambda r: r["evidence"].priority_score)
        out.append(schemas.StudentAttentionOut(
            student_id=sid, student_name=rows[0]["student_name"],
            n_chapters_tracked=len(confident), n_high_priority_chapters=n_high,
            avg_priority_score=round(avg_priority, 3), weakest_chapter_name=weakest["chapter_name"],
        ))

    out.sort(key=lambda s: (-s.n_high_priority_chapters, -s.avg_priority_score))
    return out


@router.get("/students-overview", response_model=list[schemas.StudentSummaryOut])
def students_overview(
    class_id: int | None = None,
    db: Session = Depends(get_db),
    teacher: models.Student = Depends(get_current_teacher),
):
    """The full roster - every registered student by default, or (when
    class_id is given) just that SchoolClass's enrolled students - not
    just the ones with enough confidently-tracked evidence to appear in
    /students-needing-attention (superseded by this endpoint on the Class
    overview page - it silently dropped anyone with zero confident
    chapters, which includes both a student who's never practiced at all
    AND, subtly, one whose only activity so far is too sparse to trust;
    neither should be invisible to a teacher who just wants to see how
    everyone is doing, not only the problem cases). /students-needing-
    attention itself is left in place as a standalone API, just no longer
    called from this page now that this endpoint fully covers it plus
    everyone else. Sorted weakest-mastery-first - the students most likely
    to need attention belong at the top, not buried below everyone doing
    fine. No-activity students (nothing to rank) sort last."""
    all_evidence = _compute_all_evidence(db, class_id=class_id)
    by_student: dict[int, list[dict]] = {}
    for r in all_evidence:
        by_student.setdefault(r["student_id"], []).append(r)

    students_query = db.query(models.Student).filter(models.Student.role == "student")
    if class_id is not None:
        students_query = students_query.filter(models.Student.class_id == class_id)
    students = students_query.all()
    out = []
    for s in students:
        rows = by_student.get(s.id, [])
        confident = [r for r in rows if r["evidence"].priority_band in CONFIDENT_BANDS]
        band_counts = {"High": 0, "Medium": 0, "Low": 0}
        for r in confident:
            band_counts[r["evidence"].priority_band] += 1
        avg_mastery = (
            round(sum(r["evidence"].mastery_estimate for r in confident) / len(confident), 3)
            if confident else None
        )
        weakest = max(confident, key=lambda r: r["evidence"].priority_score) if confident else None
        out.append(schemas.StudentSummaryOut(
            student_id=s.id, student_name=s.name, grade=s.grade, stream=s.stream,
            has_activity=len(rows) > 0, n_chapters_tracked=len(confident), avg_mastery=avg_mastery,
            n_high=band_counts["High"], n_medium=band_counts["Medium"], n_low=band_counts["Low"],
            weakest_chapter_name=weakest["chapter_name"] if weakest else None,
        ))

    out.sort(key=lambda s: (s.avg_mastery is None, s.avg_mastery if s.avg_mastery is not None else 0))
    return out


@router.get("/dashboard-summary", response_model=schemas.TeacherDashboardSummaryOut)
def dashboard_summary(
    class_id: int | None = None,
    db: Session = Depends(get_db),
    teacher: models.Student = Depends(get_current_teacher),
):
    """Teacher Dashboard: class performance, weakest chapters (already
    covered by /chapters-failing), student distribution, alerts. Optionally
    scoped to one class."""
    all_evidence = _compute_all_evidence(db, class_id=class_id)
    confident_rows = [r for r in all_evidence if r["evidence"].priority_band in CONFIDENT_BANDS]
    total_chapters_tracked = len({r["chapter_id"] for r in confident_rows})

    # Cohort-wide priority-band split, over every confidently-tracked
    # (student, chapter) row - the single "how's the class doing overall"
    # number the dashboard's headline sentence and band-distribution bar
    # are built from. Insufficient-evidence rows are counted too (unlike
    # confident_rows above) since "we don't know yet" is itself a real,
    # meaningful share of the cohort's coverage worth surfacing.
    band_distribution: dict[str, int] = {"High": 0, "Medium": 0, "Low": 0, "Insufficient evidence": 0}
    for r in all_evidence:
        band_distribution[r["evidence"].priority_band] = band_distribution.get(r["evidence"].priority_band, 0) + 1
    avg_mastery = (
        round(sum(r["evidence"].mastery_estimate for r in confident_rows) / len(confident_rows), 3)
        if confident_rows else None
    )

    students_query = db.query(models.Student).filter(models.Student.role == "student")
    if class_id is not None:
        students_query = students_query.filter(models.Student.class_id == class_id)
    students = students_query.all()
    grade_distribution: dict[str, int] = {}
    stream_distribution: dict[str, int] = {}
    for s in students:
        gkey = str(s.grade) if s.grade is not None else "Unspecified"
        skey = s.stream if s.stream else "Unspecified"
        grade_distribution[gkey] = grade_distribution.get(gkey, 0) + 1
        stream_distribution[skey] = stream_distribution.get(skey, 0) + 1

    by_student: dict[int, list[dict]] = {}
    for r in all_evidence:
        by_student.setdefault(r["student_id"], []).append(r)

    alerts = []
    for sid, rows in by_student.items():
        confident = [r for r in rows if r["evidence"].priority_band in CONFIDENT_BANDS]
        declining_high = [r for r in confident if r["evidence"].priority_band == "High"
                           and r["evidence"].trend_significant and (r["evidence"].trend_slope or 0) < 0]
        if not declining_high or not confident:
            continue
        n_high = sum(1 for r in confident if r["evidence"].priority_band == "High")
        avg_priority = sum(r["evidence"].priority_score for r in confident) / len(confident)
        weakest = max(confident, key=lambda r: r["evidence"].priority_score)
        alerts.append(schemas.StudentAttentionOut(
            student_id=sid, student_name=rows[0]["student_name"],
            n_chapters_tracked=len(confident), n_high_priority_chapters=n_high,
            avg_priority_score=round(avg_priority, 3), weakest_chapter_name=weakest["chapter_name"],
        ))
    alerts.sort(key=lambda a: -a.avg_priority_score)

    return schemas.TeacherDashboardSummaryOut(
        total_students=len(students), total_chapters_tracked=total_chapters_tracked,
        grade_distribution=grade_distribution, stream_distribution=stream_distribution,
        band_distribution=band_distribution, avg_mastery=avg_mastery,
        alerts=alerts[:10],
    )


def _get_student_target(db: Session, student_id: int) -> models.Student:
    """Both /students/{id} detail endpoints below intentionally stay
    visible to any teacher for any student - the teacher dashboard is
    system-wide by default (SchoolClass narrows the roster views, it
    doesn't gate them), and these are reached by clicking any student in
    that unscoped roster. What they were missing was even a basic role
    check: student_id used to accept ANY id at all - a teacher's own id,
    another teacher's id - and just silently return empty data instead of
    a clean 404. This closes that input-validation gap without changing
    behavior for the actual intended use (viewing a real student)."""
    target = db.get(models.Student, student_id)
    if not target or target.role != "student":
        raise HTTPException(404, "Student not found")
    return target


@router.get("/students/{student_id}/evidence", response_model=list[schemas.ChapterEvidenceOut])
def student_evidence(
    student_id: int,
    db: Session = Depends(get_db),
    teacher: models.Student = Depends(get_current_teacher),
):
    """Student Performance: teacher-scoped version of /practice/results/me,
    same compute_chapter_evidence -> rank_chapters -> explain pipeline."""
    _get_student_target(db, student_id)

    all_evidence, _ = _student_by_chapter_evidence(student_id, db)
    ranked = mastery.rank_chapters(all_evidence)
    chapters = {c.id: c for c in db.query(models.Section).filter(
        models.Section.id.in_([ev.chapter_id for ev in ranked])
    ).all()}
    chapter_to_subject = _chapter_to_top_subject([ev.chapter_id for ev in all_evidence], db)
    subj_cmp = mastery.subject_comparison_map(all_evidence, chapter_to_subject)

    out = []
    for ev in ranked:
        chapter = chapters.get(ev.chapter_id)
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


@router.get("/students/{student_id}/performance", response_model=schemas.PerformanceOut)
def student_performance(
    student_id: int,
    db: Session = Depends(get_db),
    teacher: models.Student = Depends(get_current_teacher),
):
    """Student Performance: teacher-scoped version of /practice/performance/me."""
    _get_student_target(db, student_id)

    sessions = (
        db.query(models.PracticeSession)
          .filter_by(student_id=student_id)
          .order_by(models.PracticeSession.started_at.desc())
          .limit(50)
          .all()
    )
    session_history = [
        schemas.SessionHistoryEntryOut(
            session_id=s.id, course_id=s.course_id, chapter_id=s.chapter_id, purpose=s.purpose,
            completed_at=s.completed_at, total_questions=s.total_questions,
            correct_count=s.correct_count, percentage=s.percentage,
        ) for s in sessions
    ]

    scored_attempts = (
        db.query(models.Attempt)
          .filter(models.Attempt.student_id == student_id, models.Attempt.is_correct.isnot(None))
          .order_by(models.Attempt.answered_at.asc())
          .all()
    )
    accuracy_trend = [
        schemas.AccuracyPointOut(attempt_order=i, answered_at=a.answered_at, is_correct=bool(a.is_correct))
        for i, a in enumerate(scored_attempts)
    ]

    all_evidence, _ = _student_by_chapter_evidence(student_id, db)
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


@router.get("/chapters/{chapter_id}/analytics", response_model=schemas.ChapterAnalyticsOut)
def chapter_analytics(
    chapter_id: int,
    class_id: int | None = None,
    db: Session = Depends(get_db),
    teacher: models.Student = Depends(get_current_teacher),
):
    """Chapter Analytics: "X% of students are weak in this chapter",
    difficulty distribution, question-level breakdown (worst-accuracy-
    first) - the one genuinely new SQL aggregation shape in this router,
    built directly off Attempt rather than reusing _compute_all_evidence's
    per-(student,chapter) shape. n_students_tracked/pct_students_weak are
    optionally scoped to one class; the difficulty/question-level breakdown
    below stays system-wide regardless (it's about the question bank's own
    difficulty, not which students attempted it)."""
    chapter = db.get(models.Section, chapter_id)
    if not chapter:
        raise HTTPException(404, "Chapter not found")

    all_evidence = _compute_all_evidence(db, class_id=class_id)
    rows_for_chapter = [r for r in all_evidence if r["chapter_id"] == chapter_id and r["evidence"].priority_band in CONFIDENT_BANDS]
    n_students_tracked = len(rows_for_chapter)
    n_weak = sum(1 for r in rows_for_chapter if r["evidence"].priority_band == "High")
    pct_weak = round(100 * n_weak / n_students_tracked, 1) if n_students_tracked else 0.0

    attempts = (
        db.query(models.Attempt)
          .filter(models.Attempt.chapter_id == chapter_id, models.Attempt.is_correct.isnot(None))
          .all()
    )
    diff_totals: dict[str, list[int]] = {}
    by_question: dict[int, list[int]] = {}
    for a in attempts:
        d = a.difficulty_label or "Medium"
        dt = diff_totals.setdefault(d, [0, 0])
        dt[0] += 1
        dt[1] += 1 if a.is_correct else 0
        qt = by_question.setdefault(a.question_id, [0, 0])
        qt[0] += 1
        qt[1] += 1 if a.is_correct else 0

    difficulty_breakdown = {d: round(correct / total, 3) for d, (total, correct) in diff_totals.items() if total}

    questions = {q.id: q for q in db.query(models.Question).filter(models.Question.id.in_(list(by_question.keys()))).all()}
    question_level = [
        schemas.QuestionLevelStatOut(
            question_id=qid, body=questions[qid].body if qid in questions else "",
            n_attempts=total, accuracy=round(correct / total, 3),
        ) for qid, (total, correct) in by_question.items() if total
    ]
    question_level.sort(key=lambda q: q.accuracy)

    return schemas.ChapterAnalyticsOut(
        chapter_id=chapter_id, chapter_name=chapter.name,
        n_students_tracked=n_students_tracked, pct_students_weak=pct_weak,
        difficulty_breakdown=difficulty_breakdown, question_level=question_level,
    )


# ------------------------------------------------------------- classes --
def _owned_class(db: Session, class_id: int, teacher: models.Student) -> models.SchoolClass:
    class_ = db.get(models.SchoolClass, class_id)
    if not class_:
        raise HTTPException(404, "Class not found")
    if class_.teacher_id != teacher.id:
        raise HTTPException(403, "Not your class")
    return class_


def _class_out(db: Session, class_: models.SchoolClass) -> schemas.ClassOut:
    student_count = db.query(models.Student).filter(models.Student.class_id == class_.id).count()
    return schemas.ClassOut(
        id=class_.id, name=class_.name, course_id=class_.course_id,
        join_code=class_.join_code, student_count=student_count, created_at=class_.created_at,
    )


@router.get("/classes", response_model=list[schemas.ClassOut])
def list_classes(db: Session = Depends(get_db), teacher: models.Student = Depends(get_current_teacher)):
    classes = db.query(models.SchoolClass).filter(models.SchoolClass.teacher_id == teacher.id).all()
    return [_class_out(db, c) for c in classes]


@router.post("/classes", response_model=schemas.ClassOut)
def create_class(
    payload: schemas.ClassCreate,
    db: Session = Depends(get_db),
    teacher: models.Student = Depends(get_current_teacher),
):
    if not db.get(models.Course, payload.course_id):
        raise HTTPException(404, "course_id does not exist")
    # 6 uppercase hex chars - same `secrets` module this codebase already
    # uses for VerificationToken/the teacher-invite check, just per-class
    # and DB-backed instead of one global env var (there are N classes,
    # each needing its own code, unlike TEACHER_INVITE_CODE).
    join_code = secrets.token_hex(3).upper()
    class_ = models.SchoolClass(
        name=payload.name, teacher_id=teacher.id, course_id=payload.course_id, join_code=join_code,
    )
    db.add(class_)
    db.commit()
    db.refresh(class_)
    return _class_out(db, class_)


@router.delete("/classes/{class_id}", response_model=schemas.MessageOut)
def delete_class(
    class_id: int,
    db: Session = Depends(get_db),
    teacher: models.Student = Depends(get_current_teacher),
):
    class_ = _owned_class(db, class_id, teacher)
    # un-enroll members rather than blocking the delete - a teacher
    # deleting a class is a real, authorized action; students just become
    # unenrolled again, same as if they'd never joined.
    db.query(models.Student).filter(models.Student.class_id == class_id).update(
        {models.Student.class_id: None}, synchronize_session=False)
    db.delete(class_)
    db.commit()
    return schemas.MessageOut(detail="Class deleted.")


@router.get("/classes/{class_id}/roster", response_model=list[schemas.StudentSummaryOut])
def class_roster(
    class_id: int,
    db: Session = Depends(get_db),
    teacher: models.Student = Depends(get_current_teacher),
):
    """Ownership-enforced version of GET /students-overview?class_id= -
    that endpoint stays open (any teacher can already see the full
    unscoped roster, so narrowing it to a class_id they don't own leaks
    nothing new), but this one 403s on someone else's class, which is what
    the Classes management page actually needs."""
    _owned_class(db, class_id, teacher)
    return students_overview(class_id=class_id, db=db, teacher=teacher)


@router.post("/classes/{class_id}/students", response_model=schemas.MessageOut)
def add_student_to_class(
    class_id: int,
    payload: schemas.AddStudentToClassRequest,
    db: Session = Depends(get_db),
    teacher: models.Student = Depends(get_current_teacher),
):
    """Teacher-adds path (alongside self-serve join-by-code) - covers
    already-registered students who can't/won't log in individually to
    enter a code. Silently reassigns if the student was already in another
    class (one class per student) - a teacher-authorized action, not
    something that needs a confirmation flow."""
    _owned_class(db, class_id, teacher)
    student = db.get(models.Student, payload.student_id)
    if not student or student.role != "student":
        raise HTTPException(404, "Student not found")
    student.class_id = class_id
    db.commit()
    return schemas.MessageOut(detail=f"{student.name} added to class.")


@router.delete("/classes/{class_id}/students/{student_id}", response_model=schemas.MessageOut)
def remove_student_from_class(
    class_id: int,
    student_id: int,
    db: Session = Depends(get_db),
    teacher: models.Student = Depends(get_current_teacher),
):
    _owned_class(db, class_id, teacher)
    student = db.get(models.Student, student_id)
    if not student or student.class_id != class_id:
        raise HTTPException(404, "Student not in this class")
    student.class_id = None
    db.commit()
    return schemas.MessageOut(detail=f"{student.name} removed from class.")


@router.post("/quiz-templates", response_model=schemas.QuizTemplateOut)
def create_quiz_template(
    payload: schemas.QuizTemplateCreate,
    db: Session = Depends(get_db),
    teacher: models.Student = Depends(get_current_teacher),
):
    """Assessment Management: create a named question-selection recipe.
    Visible to every student in the course rather than scoped to one
    class - same deliberate deferral noted on models.QuizTemplate, not a
    narrower scope decision made silently here."""
    qt = models.QuizTemplate(**payload.model_dump(), created_by=teacher.id)
    db.add(qt)
    db.commit()
    db.refresh(qt)
    return qt


@router.put("/quiz-templates/{template_id}", response_model=schemas.QuizTemplateOut)
def update_quiz_template(
    template_id: int,
    payload: schemas.QuizTemplateCreate,
    db: Session = Depends(get_db),
    teacher: models.Student = Depends(get_current_teacher),
):
    qt = db.get(models.QuizTemplate, template_id)
    if not qt:
        raise HTTPException(404, "Quiz template not found")
    for k, v in payload.model_dump().items():
        setattr(qt, k, v)
    db.commit()
    db.refresh(qt)
    return qt


@router.delete("/quiz-templates/{template_id}", response_model=schemas.MessageOut)
def delete_quiz_template(
    template_id: int,
    db: Session = Depends(get_db),
    teacher: models.Student = Depends(get_current_teacher),
):
    qt = db.get(models.QuizTemplate, template_id)
    if not qt:
        raise HTTPException(404, "Quiz template not found")
    db.delete(qt)
    db.commit()
    return schemas.MessageOut(detail="Quiz template deleted.")
