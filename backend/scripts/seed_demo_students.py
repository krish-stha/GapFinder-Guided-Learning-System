"""
Wipes all ACTIVITY data (students, sessions, attempts, verification tokens)
and replaces it with three demo student accounts - a topper, a moderate
performer, and a low performer - each with 25-28 completed test sessions
(one diagnostic, several chapter tests, a few mixed mock tests) spread over
the last ~35 days. Every attempt answers a REAL question from course 91
("NEB Grade 11 Science") using each persona's target accuracy per chapter;
nothing here touches CONTENT (Course/Section/Question/QuestionChapter) -
only the ACTIVITY zone this system itself generates.

Purpose: give the dashboard/performance/learning-path/weak-areas/progress/
assistant pages real, varied evidence to render against, so the app can be
demoed at "lots of real use" rather than an empty fresh account. This is
demo/dev data for showing the software - NOT survey or research data, and
must never be cited as such in the dissertation.

Run: python -m scripts.seed_demo_students
"""
import json
import random
import sys
from datetime import datetime, timedelta, time

sys.path.insert(0, ".")
sys.stdout.reconfigure(encoding="utf-8")

from app.database import SessionLocal
from app import models
from app.routers.auth import hash_password

random.seed(42)

COURSE_ID = 91  # NEB Grade 11 Science - richest real content, matches grade=11/stream=Science auto-scoping
NUM_QUESTIONS_PER_TEST = 50  # same "up to 50" pattern the live app now uses everywhere

# 12 real, well-stocked chapters (100+ real scoreable questions each) across
# the four Science subjects, found live against the DB (see chat for the
# discovery query) rather than guessed.
CHAPTERS = {
    "physics_dynamics": 7927,
    "physics_work_energy": 7928,
    "physics_quantities": 7924,
    "chem_bonding": 7956,
    "chem_stoichiometry": 7954,
    "chem_alkanes": 7965,
    "botany_angiosperms": 8000,
    "botany_cell_biology": 7990,
    "botany_ecology": 8005,
    "zoology_animalia": 8023,
    "zoology_protista": 8026,
    "zoology_frog": 8024,
}


def chapter_config(base: dict, sparse_key: str | None = None, sparse_questions: int = 2) -> dict:
    """base: {chapter_key: (accuracy, trend)}. trend in {"flat","improving","declining"}.
    sparse_key (if given) gets deliberately touched by only ONE tiny session
    instead of two full ones, to also demonstrate the "Insufficient evidence"
    band for at least one chapter per persona that isn't a topper."""
    cfg = {}
    for key, (acc, trend) in base.items():
        cfg[key] = {"accuracy": acc, "trend": trend, "sparse": key == sparse_key, "sparse_n": sparse_questions}
    return cfg


PERSONAS = {
    "topper": {
        "name": "Aarav Sharma",
        "email": "aarav.topper@gapfinder.demo",
        "overall_accuracy": 0.87,
        "diagnostic_accuracy": 0.66,  # deliberately lower, to show before/after improvement
        "streak_days": 14,            # consecutive recent days touched
        "gap_after_streak": True,
        "chapters": chapter_config({
            "physics_dynamics":      (0.90, "flat"),
            "physics_work_energy":   (0.88, "flat"),
            "physics_quantities":    (0.92, "flat"),
            "chem_bonding":          (0.85, "flat"),
            "chem_stoichiometry":    (0.78, "improving"),
            "chem_alkanes":          (0.88, "flat"),
            "botany_angiosperms":    (0.93, "flat"),
            "botany_cell_biology":   (0.90, "flat"),
            "botany_ecology":        (0.87, "flat"),
            "zoology_animalia":      (0.91, "flat"),
            "zoology_protista":      (0.89, "flat"),
            "zoology_frog":          (0.84, "improving"),
        }),
        "mock_test_accuracy": 0.85,
    },
    "moderate": {
        "name": "Priya Gurung",
        "email": "priya.moderate@gapfinder.demo",
        "overall_accuracy": 0.55,
        "diagnostic_accuracy": 0.50,
        "streak_days": 5,
        "gap_after_streak": True,
        "chapters": chapter_config({
            "physics_dynamics":      (0.75, "improving"),
            "physics_work_energy":   (0.70, "flat"),
            "physics_quantities":    (0.65, "flat"),
            "chem_bonding":          (0.40, "flat"),
            "chem_stoichiometry":    (0.35, "declining"),
            "chem_alkanes":          (0.45, "flat"),
            "botany_angiosperms":    (0.60, "flat"),
            "botany_cell_biology":   (0.55, "flat"),
            "botany_ecology":        (0.50, "flat"),
            "zoology_animalia":      (0.68, "flat"),
            "zoology_protista":      (0.42, "flat"),
            "zoology_frog":          (0.50, "flat"),
        }, sparse_key="zoology_frog"),
        "mock_test_accuracy": 0.55,
    },
    "low_performer": {
        "name": "Bibek Thapa",
        "email": "bibek.learner@gapfinder.demo",
        "overall_accuracy": 0.31,
        "diagnostic_accuracy": 0.33,
        "streak_days": 2,
        "gap_after_streak": True,
        "chapters": chapter_config({
            "physics_dynamics":      (0.35, "flat"),
            "physics_work_energy":   (0.30, "declining"),
            "physics_quantities":    (0.45, "improving"),
            "chem_bonding":          (0.25, "flat"),
            "chem_stoichiometry":    (0.20, "flat"),
            "chem_alkanes":          (0.28, "flat"),
            "botany_angiosperms":    (0.32, "flat"),
            "botany_cell_biology":   (0.30, "flat"),
            "botany_ecology":        (0.38, "flat"),
            "zoology_animalia":      (0.40, "flat"),
            "zoology_protista":      (0.22, "flat"),
            "zoology_frog":          (0.33, "flat"),
        }, sparse_key="chem_alkanes"),
        "mock_test_accuracy": 0.30,
    },
}

TREND_DELTA = 0.15  # how much lower ("improving") / higher ("declining") the OLDER session's accuracy is
SKIP_PROB = {"topper": 0.01, "moderate": 0.04, "low_performer": 0.08}


def day_start(now: datetime, day_offset: int, hour: int, minute: int = 0) -> datetime:
    """Anchors to the CALENDAR DATE `day_offset` days before `now` first,
    then applies the given time-of-day - subtracting `days=` and `hours=`
    from `now` in one timedelta can push day_offset=0 into yesterday's date
    whenever `now`'s own time-of-day is earlier than the random hour being
    subtracted, which silently breaks the streak/before-after scheduling
    below (every date shifts by however many hours were subtracted)."""
    target_date = (now - timedelta(days=day_offset)).date()
    return datetime.combine(target_date, time(hour=hour, minute=minute))


def wipe_activity_data(db):
    n_attempts = db.query(models.Attempt).delete()
    n_sessions = db.query(models.PracticeSession).delete()
    n_tokens = db.query(models.VerificationToken).delete()
    n_students = db.query(models.Student).delete()
    db.commit()
    print(f"Wiped: {n_attempts} attempts, {n_sessions} sessions, {n_tokens} tokens, {n_students} students")


def load_chapter_pool(db, chapter_id: int) -> list[dict]:
    rows = (
        db.query(models.Question)
          .join(models.QuestionChapter, models.QuestionChapter.question_id == models.Question.id)
          .filter(models.QuestionChapter.chapter_id == chapter_id,
                   models.Question.source == "real", models.Question.scoreable == True)
          .all()
    )
    return [
        {"id": q.id, "chapter_id": chapter_id, "difficulty_label": q.difficulty_label,
         "correct_answer": q.correct_answer, "n_options": len(json.loads(q.answers_json))}
        for q in rows
    ]


def load_mixed_pool(db, course_id: int) -> list[dict]:
    chapter_ids = [row[0] for row in (
        db.query(models.Section.id).filter(models.Section.course_id == course_id, models.Section.type == "Chapter").all()
    )]
    rows = (
        db.query(models.QuestionChapter.question_id, models.QuestionChapter.chapter_id, models.Question)
          .join(models.Question, models.Question.id == models.QuestionChapter.question_id)
          .filter(models.QuestionChapter.chapter_id.in_(chapter_ids),
                   models.Question.source == "real", models.Question.scoreable == True)
          .all()
    )
    # lowest chapter_id per question, same attribution rule /start uses
    best_chapter: dict[int, int] = {}
    q_by_id: dict[int, models.Question] = {}
    for qid, cid, q in rows:
        q_by_id[qid] = q
        if qid not in best_chapter or cid < best_chapter[qid]:
            best_chapter[qid] = cid
    return [
        {"id": qid, "chapter_id": cid, "difficulty_label": q_by_id[qid].difficulty_label,
         "correct_answer": q_by_id[qid].correct_answer, "n_options": len(json.loads(q_by_id[qid].answers_json))}
        for qid, cid in best_chapter.items()
    ]


def build_session(db, student, course_id, chapter_id, purpose, pool, num_questions, accuracy,
                   started_at, skip_prob, persona_default_accuracy):
    n = min(num_questions, len(pool))
    chosen = random.sample(pool, n)
    session = models.PracticeSession(
        student_id=student.id, course_id=course_id, chapter_id=chapter_id, purpose=purpose,
        status="completed", started_at=started_at, total_questions=n,
        time_limit_seconds=n * 72 if purpose == "mock_test" else None,
    )
    db.add(session)
    db.flush()

    correct_count = 0
    t = started_at
    for position, q in enumerate(chosen):
        t = t + timedelta(seconds=random.randint(40, 110))
        roll = random.random()
        if roll < skip_prob:
            selected_index, is_correct = None, None
        else:
            acc = accuracy if accuracy is not None else persona_default_accuracy
            if random.random() < acc:
                selected_index, is_correct = q["correct_answer"], True
            else:
                options = [i for i in range(q["n_options"]) if i != q["correct_answer"]]
                selected_index = random.choice(options) if options else q["correct_answer"]
                is_correct = selected_index == q["correct_answer"]
        if is_correct:
            correct_count += 1
        db.add(models.Attempt(
            session_id=session.id, student_id=student.id, question_id=q["id"],
            chapter_id=q["chapter_id"], position=position, selected_index=selected_index,
            is_correct=is_correct, difficulty_label=q["difficulty_label"],
            answered_at=t, time_taken_seconds=random.randint(15, 90),
        ))

    session.correct_count = correct_count
    session.percentage = round(100 * correct_count / n, 2) if n else 0.0
    session.completed_at = t + timedelta(seconds=30)
    db.commit()
    return session


def seed_persona(db, key: str, persona: dict, pools: dict[str, list[dict]], mixed_pool: list[dict]):
    now = datetime.utcnow()
    student = models.Student(
        name=persona["name"], email=persona["email"],
        password_hash=hash_password("Demo@1234"),
        grade=11, stream="Science", role="student", email_verified=True,
    )
    db.add(student)
    db.commit()
    db.refresh(student)

    skip_prob = SKIP_PROB[key]

    # 1) diagnostic - oldest session, deliberately a bit weaker for the
    #    topper/moderate personas so Progress's before/after has something
    #    real to show ("mastery_after" > "mastery_before").
    diag_day = 34
    build_session(
        db, student, COURSE_ID, None, "diagnostic", mixed_pool, NUM_QUESTIONS_PER_TEST,
        persona["diagnostic_accuracy"], day_start(now, diag_day, hour=9), skip_prob,
        persona["overall_accuracy"],
    )

    # 2) recent-streak days (0..streak_days-1) each get exactly one chapter
    #    session, then a deliberate gap day, then older scattered sessions -
    #    this is what makes Progress's streak counter show a real number
    #    instead of 0 or an unrealistically perfect one.
    chapter_keys = list(persona["chapters"].keys())
    streak_days = list(range(0, persona["streak_days"]))
    n_older_sessions = 2 * len(chapter_keys) - len(streak_days)
    gap_start = persona["streak_days"] + 1  # leave one empty day right after the streak
    older_days = sorted(random.sample(range(gap_start, 35), min(n_older_sessions, 35 - gap_start)))
    while len(older_days) < n_older_sessions:  # pad if the range was too small
        older_days.append(older_days[-1] + 1 if older_days else gap_start)

    day_queue = streak_days + older_days
    random.shuffle(day_queue)

    session_plan = []  # (chapter_key, day_offset, is_recent)
    for ck in chapter_keys:
        cfg = persona["chapters"][ck]
        if cfg["sparse"]:
            session_plan.append((ck, day_queue.pop(), "single", cfg))
            continue
        d1, d2 = day_queue.pop(), day_queue.pop()
        older_day, recent_day = max(d1, d2), min(d1, d2)
        session_plan.append((ck, older_day, "older", cfg))
        session_plan.append((ck, recent_day, "recent", cfg))

    for ck, day_offset, kind, cfg in session_plan:
        chapter_id = CHAPTERS[ck]
        pool = pools[ck]
        base_acc = cfg["accuracy"]
        if cfg["trend"] == "improving":
            acc = base_acc - TREND_DELTA if kind == "older" else base_acc
        elif cfg["trend"] == "declining":
            acc = base_acc + TREND_DELTA if kind == "older" else base_acc
        else:
            acc = base_acc
        acc = max(0.05, min(0.98, acc))
        n_q = cfg["sparse_n"] if kind == "single" else NUM_QUESTIONS_PER_TEST
        started_at = day_start(now, day_offset, hour=random.randint(7, 21), minute=random.randint(0, 59))
        build_session(db, student, COURSE_ID, chapter_id, "mock_test", pool, n_q, acc, started_at, skip_prob, acc)

    # 3) a few mixed (course-wide) mock tests, spread through the timeline
    mock_days = [1, 12, 26] if persona["streak_days"] >= 5 else [0, 15, 30]
    for d in mock_days:
        started_at = day_start(now, d, hour=random.randint(7, 21))
        build_session(
            db, student, COURSE_ID, None, "mock_test", mixed_pool, NUM_QUESTIONS_PER_TEST,
            persona["mock_test_accuracy"], started_at, skip_prob, persona["mock_test_accuracy"],
        )

    n_sessions = db.query(models.PracticeSession).filter_by(student_id=student.id).count()
    n_attempts = db.query(models.Attempt).filter_by(student_id=student.id).count()
    print(f"{key}: {student.name} <{student.email}> - {n_sessions} sessions, {n_attempts} attempts")


def main():
    db = SessionLocal()
    try:
        wipe_activity_data(db)

        print("Loading real question pools for 12 curated chapters...")
        pools = {key: load_chapter_pool(db, cid) for key, cid in CHAPTERS.items()}
        for key, pool in pools.items():
            if len(pool) < 20:
                print(f"  WARNING: {key} (chapter {CHAPTERS[key]}) only has {len(pool)} real scoreable questions")

        print(f"Loading mixed (course-wide) pool for course {COURSE_ID}...")
        mixed_pool = load_mixed_pool(db, COURSE_ID)
        print(f"  {len(mixed_pool)} distinct real scoreable questions available course-wide")

        for key, persona in PERSONAS.items():
            seed_persona(db, key, persona, pools, mixed_pool)

        print("\nLogin with any of the above using password: Demo@1234")
    finally:
        db.close()


if __name__ == "__main__":
    main()
