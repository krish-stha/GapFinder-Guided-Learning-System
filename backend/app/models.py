"""
Core schema.

Two clear zones:

1. CONTENT (imported from the cleaned content-partner export - Course,
   Section, Question, QuestionChapter). Read-mostly, refreshed by re-running
   the import pipeline.

2. ACTIVITY (generated entirely by this system - Student, PracticeSession,
   Attempt). This is the real ground-truth data the analytics engine runs
   on. Nothing here comes from the content partner.
"""
from sqlalchemy import (
    Column, Integer, String, Float, Boolean, ForeignKey, DateTime, Text,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base


# --------------------------------------------------------------- CONTENT --
class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    slug = Column(String)

    sections = relationship("Section", back_populates="course")


class Section(Base):
    """Subject -> Unit -> Chapter, self-referencing tree."""
    __tablename__ = "sections"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)  # Subject | Unit | Chapter
    parent_id = Column(Integer, ForeignKey("sections.id"), nullable=True)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)

    course = relationship("Course", back_populates="sections")
    children = relationship("Section", backref="parent", remote_side=[id])
    questions = relationship("QuestionChapter", back_populates="chapter")


class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    body = Column(Text, nullable=False)
    answers_json = Column(Text, nullable=False)   # JSON list: [{"answer": "..."}]
    correct_answer = Column(Integer, nullable=True)  # 0-based index into answers_json
    level = Column(Integer)                        # 1 / 3 / 5 raw AG scale
    difficulty_label = Column(String)               # Easy / Medium / Hard
    # MCQ | example (worked example, scoreable=False)
    question_type = Column(String, default="MCQ")
    # real | synthetic | teacher_authored - kept distinct from "synthetic"
    # deliberately: cleanup scripts (see scripts/consolidate_courses.py
    # phase4_cleanup) filter on source == "synthetic" to find junk-eligible
    # filler; conflating real teacher-authored content with that value
    # would make a future cleanup pass silently delete it.
    source = Column(String, default="real")
    scoreable = Column(Boolean, default=True)
    # shown after the student answers (Practice/Quiz "explanation after
    # answers") - nullable since most existing questions have none.
    explanation = Column(Text, nullable=True)

    chapters = relationship("QuestionChapter", back_populates="question")


class QuestionChapter(Base):
    """Many-to-many bridge, exactly as it exists in the source data -
    a question may legitimately belong to more than one chapter."""
    __tablename__ = "question_chapter_map"
    question_id = Column(Integer, ForeignKey("questions.id"), primary_key=True)
    chapter_id = Column(Integer, ForeignKey("sections.id"), primary_key=True)

    question = relationship("Question", back_populates="chapters")
    chapter = relationship("Section", back_populates="questions")


# --------------------------------------------------------------- ACTIVITY --
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    grade = Column(Integer)          # 11 or 12
    stream = Column(String)          # Science / Management / Humanities
    role = Column(String, default="student")  # student | teacher - see auth.get_current_teacher
    email_verified = Column(Boolean, default=False)
    # null = not enrolled in any class yet. One class per student (not a
    # many-to-many junction table like QuestionChapter) - a real NEB
    # student is practically in one physical class, so this stays as
    # simple as the problem actually is. See SchoolClass below.
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    sessions = relationship("PracticeSession", back_populates="student")


class SchoolClass(Base):
    """A teacher's real class/section - what "cohort" should have meant
    all along (see the pre-existing docstring on QuizTemplate below, which
    documents the gap this closes). join_code is DB-backed and per-class,
    unlike the single global TEACHER_INVITE_CODE env var auth.py already
    uses for teacher registration - that pattern only works for one
    system-wide secret, not N classes each needing their own."""
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    join_code = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class VerificationToken(Base):
    """Single-use tokens backing both email verification and password
    reset - one shared table rather than duplicating columns on Student,
    since both flows are structurally identical (issue a random token,
    email a link, redeem once before expiry)."""
    __tablename__ = "verification_tokens"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    token = Column(String, unique=True, nullable=False, index=True)
    purpose = Column(String, nullable=False)  # email_verify | password_reset
    expires_at = Column(DateTime, nullable=False)
    used_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class PracticeSession(Base):
    """One test/practice run taken inside OUR system."""
    __tablename__ = "practice_sessions"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    chapter_id = Column(Integer, ForeignKey("sections.id"), nullable=True)  # null = mixed/mock
    purpose = Column(String, default="practice")   # practice | mock_test | diagnostic
    status = Column(String, default="in_progress")  # in_progress | completed
    started_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)

    # NULL = untimed (practice mode). Deadline is computed on read as
    # started_at + time_limit_seconds, never stored separately - the
    # server, not the client countdown, is the authority on expiry.
    time_limit_seconds = Column(Integer, nullable=True)

    total_questions = Column(Integer, default=0)
    correct_count = Column(Integer, default=0)
    percentage = Column(Float, nullable=True)

    student = relationship("Student", back_populates="sessions")
    attempts = relationship("Attempt", back_populates="session")


class Attempt(Base):
    """One question slot inside a session. This table is the ground
    truth the whole analytics engine is built on.

    A row is pre-created (unanswered) for every question a session
    selects at /start time, keyed by position, so /answer can always
    UPDATE rather than INSERT - free navigation and edit-a-previous-
    answer fall out of that naturally without loosening the
    (session_id, question_id) uniqueness guarantee below. `answered_at`
    is only set when the student actually submits (or explicitly skips)
    an answer via /answer - it is NOT set at row-creation time, so
    `answered_at IS NOT NULL` is the authoritative "has this question
    been touched" signal (distinct from `selected_index IS NULL`, which
    is ambiguous between "never answered" and "explicitly skipped")."""
    __tablename__ = "attempts"
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey("practice_sessions.id"), nullable=False)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
    chapter_id = Column(Integer, ForeignKey("sections.id"), nullable=False)

    # stable 0-based order within the session, for "question 7 of 50" /
    # jump-to-question navigation and the results-page review list.
    position = Column(Integer, nullable=True)
    marked_for_review = Column(Boolean, default=False)

    selected_index = Column(Integer, nullable=True)
    is_correct = Column(Boolean, nullable=True)
    difficulty_label = Column(String)   # denormalised at answer-time for fast queries
    answered_at = Column(DateTime, nullable=True)
    time_taken_seconds = Column(Integer, nullable=True)

    session = relationship("PracticeSession", back_populates="attempts")

    __table_args__ = (UniqueConstraint("session_id", "question_id", name="uq_session_question"),)


class LearningResource(Base):
    """Teacher-authored notes/video-links/resource-links attached to a
    chapter - backs the Chapter Learning Page and Learning Content
    Management. Videos are external URLs (YouTube/Drive), not uploaded
    files - no storage/hosting infra needed for this to be fully
    functional from a teacher's point of view (paste a link, write notes)."""
    __tablename__ = "learning_resources"
    id = Column(Integer, primary_key=True)
    chapter_id = Column(Integer, ForeignKey("sections.id"), nullable=False)
    type = Column(String, nullable=False)  # note | video | resource_link
    title = Column(String, nullable=False)
    body_markdown = Column(Text, nullable=True)  # for type=note
    url = Column(String, nullable=True)           # for type=video | resource_link
    order_index = Column(Integer, default=0)
    created_by = Column(Integer, ForeignKey("students.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class ChapterProgress(Base):
    """Per-student, per-chapter learning-content progress (distinct from
    Attempt/mastery, which tracks quiz performance) - backs the "mark
    complete" / progress-indicator part of the Chapter Learning Page."""
    __tablename__ = "chapter_progress"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    chapter_id = Column(Integer, ForeignKey("sections.id"), nullable=False)
    notes_viewed_at = Column(DateTime, nullable=True)
    marked_complete_at = Column(DateTime, nullable=True)

    __table_args__ = (UniqueConstraint("student_id", "chapter_id", name="uq_student_chapter_progress"),)


class QuizTemplate(Base):
    """A named, teacher-curated question-selection recipe ("Assessment
    Management: create quizzes/tests"). SchoolClass now exists, but a
    template is still visible to every student in the course rather than
    scoped to one class - a deliberate, documented deferral (see the
    enrollment-model plan), not an oversight. Revisit once real per-class
    assignment is worth the added complexity."""
    __tablename__ = "quiz_templates"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    chapter_id = Column(Integer, ForeignKey("sections.id"), nullable=True)  # null = mixed across course
    difficulty_label = Column(String, nullable=True)  # null = any difficulty
    num_questions = Column(Integer, nullable=False)
    time_limit_seconds = Column(Integer, nullable=True)
    created_by = Column(Integer, ForeignKey("students.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_published = Column(Boolean, default=True)
