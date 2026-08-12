from typing import Literal
from pydantic import BaseModel, EmailStr
from datetime import datetime


class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    grade: int | None = None
    stream: str | None = None
    role: Literal["student", "teacher"] = "student"
    # required, and checked against TEACHER_INVITE_CODE, only when role="teacher"
    teacher_invite_code: str | None = None
    # optional - a student can register without a class and join one later
    # via POST /auth/join-class (see schemas.JoinClassRequest)
    class_join_code: str | None = None


class StudentOut(BaseModel):
    id: int
    name: str
    email: str
    grade: int | None
    stream: str | None
    role: str
    email_verified: bool
    class_id: int | None

    class Config:
        from_attributes = True


class StudentLogin(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    student: StudentOut


class MessageOut(BaseModel):
    detail: str


class ForgotPasswordRequest(BaseModel):
    email: EmailStr


class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str


class ChapterOut(BaseModel):
    id: int
    name: str
    type: str
    parent_id: int | None
    course_id: int

    class Config:
        from_attributes = True


class QuestionOut(BaseModel):
    """Never includes correct_answer - that would let the client cheat."""
    id: int
    body: str
    answers: list[str]
    difficulty_label: str | None
    source: str
    position: int


class StartSessionRequest(BaseModel):
    # None = mixed draw across every chapter in course_id (mock_test/diagnostic mode).
    chapter_id: int | None = None
    course_id: int
    num_questions: int = 10
    purpose: Literal["practice", "mock_test", "diagnostic"] = "practice"
    # if set, resolves the template's chapter/difficulty/count and draws
    # from that instead of the generic mixed/chapter-scoped paths
    quiz_template_id: int | None = None


class StartSessionResponse(BaseModel):
    session_id: int
    questions: list[QuestionOut]
    # None = untimed. For mock_test, ~72s/question (the 50q -> 60min ratio).
    time_limit_seconds: int | None


class AnswerRequest(BaseModel):
    question_id: int
    selected_index: int | None = None   # null = skipped
    time_taken_seconds: int | None = None


class AnswerResponse(BaseModel):
    """Always null now, regardless of purpose - every session type defers
    correctness to /finish's full review (see QuestionReviewOut), so a
    student never sees right/wrong until they submit. Kept as fields
    (not dropped) since the client still calls this endpoint on every
    answer and the shape is part of the existing contract."""
    is_correct: bool | None
    correct_answer: int | None
    explanation: str | None = None


class ReviewToggleOut(BaseModel):
    question_id: int
    marked_for_review: bool


class QuestionStateOut(BaseModel):
    """Per-question status for the exam navigator/palette, and enough to
    rehydrate an in-progress session after a page refresh. selected_index
    is safe to expose here - it's only what the student themselves chose,
    never the correct_answer, so it doesn't leak correctness."""
    question_id: int
    position: int
    answered: bool
    marked_for_review: bool
    selected_index: int | None


class SessionStateOut(BaseModel):
    session_id: int
    purpose: str
    status: str
    time_limit_seconds: int | None
    seconds_remaining: int | None  # null = untimed
    questions: list[QuestionStateOut]


class QuestionReviewOut(BaseModel):
    """One question's full review detail - only ever returned after the
    session has finished, when revealing correctness is safe."""
    question_id: int
    position: int
    body: str
    answers: list[str]
    selected_index: int | None
    correct_answer: int | None
    is_correct: bool | None
    explanation: str | None
    chapter_id: int
    chapter_name: str


class ChapterEvidenceOut(BaseModel):
    chapter_id: int
    chapter_name: str
    n_attempts: int
    raw_accuracy: float
    mastery_estimate: float
    confidence: float
    trend_slope: float | None
    trend_significant: bool
    priority_score: float
    priority_band: str
    explanation: str
    # n_attempts-weighted average mastery of this student's OTHER evidenced
    # chapters in the same subject - null when there's no such chapter yet.
    subject_avg_mastery: float | None = None


class FinishSessionOut(BaseModel):
    session_id: int
    purpose: str
    total_questions: int
    correct_count: int
    percentage: float | None
    status: str
    # Per-chapter mastery evidence (same engine/pattern as /results/me),
    # scoped to the chapters this session touched but computed from the
    # student's FULL attempt history in each - not just this session.
    chapter_breakdown: list[ChapterEvidenceOut]
    review: list[QuestionReviewOut]


class AttemptOut(BaseModel):
    """One scored attempt, oldest first - the raw material for the
    per-chapter score-history sparkline."""
    order: int
    is_correct: bool
    difficulty_label: str | None
    answered_at: datetime


class ChapterDetailOut(BaseModel):
    """Per-chapter drill-down: full evidence plus the ordered attempt
    history behind it (charter F.1 "score history sparkline, attempts,
    trend")."""
    chapter_id: int
    chapter_name: str
    course_id: int
    n_attempts: int
    raw_accuracy: float
    mastery_estimate: float
    confidence: float
    trend_slope: float | None
    trend_significant: bool
    priority_score: float
    priority_band: str
    explanation: str
    # n_attempts-weighted average mastery of this student's OTHER evidenced
    # chapters in the same subject - null when there's no such chapter yet.
    subject_avg_mastery: float | None = None
    attempts: list[AttemptOut]


# ----------------------------------------------------------- teacher/cohort --
# "Cohort" defaults to every student with recorded activity, system-wide -
# unchanged, non-breaking default. SchoolClass (see ClassOut below) now
# lets a teacher scope any of the endpoints below to one real class via an
# optional class_id, but nothing requires it.

class CohortChapterEvidenceOut(BaseModel):
    """One (student, chapter) evidence row - the raw material for a
    students x chapters heatmap on the frontend."""
    student_id: int
    student_name: str
    chapter_id: int
    chapter_name: str
    n_attempts: int
    mastery_estimate: float
    confidence: float
    priority_score: float
    priority_band: str


class ChapterWeaknessOut(BaseModel):
    """'Chapters the class is failing', aggregated across students with
    enough evidence to trust (Insufficient-evidence rows excluded)."""
    chapter_id: int
    chapter_name: str
    n_students: int
    n_students_high_priority: int
    avg_mastery: float


class StudentAttentionOut(BaseModel):
    """'Students needing attention', aggregated across their own chapters
    with enough evidence to trust."""
    student_id: int
    student_name: str
    n_chapters_tracked: int
    n_high_priority_chapters: int
    avg_priority_score: float
    weakest_chapter_name: str


class StudentSummaryOut(BaseModel):
    """One row per EVERY registered student (unlike StudentAttentionOut,
    which only lists students with at least one confidently-tracked
    chapter) - the full class roster, not just students flagged as
    needing attention. A student who registered but never practiced still
    shows up here with has_activity=False, avg_mastery=None."""
    student_id: int
    student_name: str
    grade: int | None
    stream: str | None
    has_activity: bool
    n_chapters_tracked: int
    avg_mastery: float | None
    n_high: int
    n_medium: int
    n_low: int
    weakest_chapter_name: str | None


class ClassOut(BaseModel):
    """A teacher's real class/section. student_count is computed in the
    router (COUNT of Student rows with class_id == this class), not a raw
    ORM attribute, so this is built by hand rather than via
    from_attributes - same convention as StudentSummaryOut above."""
    id: int
    name: str
    course_id: int
    join_code: str
    student_count: int
    created_at: datetime


class ClassCreate(BaseModel):
    name: str
    course_id: int


class JoinClassRequest(BaseModel):
    join_code: str


class AddStudentToClassRequest(BaseModel):
    student_id: int


# ------------------------------------------------------- learning content --
class LearningResourceOut(BaseModel):
    id: int
    chapter_id: int
    type: Literal["note", "video", "resource_link"]
    title: str
    body_markdown: str | None
    url: str | None
    order_index: int

    class Config:
        from_attributes = True


class LearningResourceCreate(BaseModel):
    chapter_id: int
    type: Literal["note", "video", "resource_link"]
    title: str
    body_markdown: str | None = None
    url: str | None = None
    order_index: int = 0


class LearningResourceUpdate(BaseModel):
    title: str | None = None
    body_markdown: str | None = None
    url: str | None = None
    order_index: int | None = None


class ChapterProgressOut(BaseModel):
    chapter_id: int
    notes_viewed_at: datetime | None
    marked_complete_at: datetime | None


class ChapterResourcesOut(BaseModel):
    """Chapter Learning Page payload: notes/videos/resources plus any
    question_type='example' worked examples linked to the chapter."""
    chapter_id: int
    chapter_name: str
    resources: list[LearningResourceOut]
    examples: list[QuestionOut]
    progress: ChapterProgressOut


# ---------------------------------------------------------- quiz templates --
class QuizTemplateOut(BaseModel):
    id: int
    title: str
    course_id: int
    chapter_id: int | None
    difficulty_label: str | None
    num_questions: int
    time_limit_seconds: int | None
    is_published: bool

    class Config:
        from_attributes = True


class QuizTemplateCreate(BaseModel):
    title: str
    course_id: int
    chapter_id: int | None = None
    difficulty_label: str | None = None
    num_questions: int = 20
    time_limit_seconds: int | None = None
    is_published: bool = True


# ------------------------------------------------------------ learning path --
class LearningPathStepOut(BaseModel):
    """One chapter in the personalized learning path. status mirrors
    priority_band for confidently-evidenced chapters (High/Medium/Low ->
    the doc's own 🔴/🟡/🟢), plus a 4th "not_started" state for chapters
    with zero attempts (which /results/me silently drops) and reuses
    "Insufficient evidence" verbatim for the sparse-data case - four
    states total, not the three the spec's emoji example implies."""
    chapter_id: int
    chapter_name: str
    status: Literal["High", "Medium", "Low", "Insufficient evidence", "not_started"]
    mastery_estimate: float | None
    explanation: str
    has_notes: bool
    has_video: bool
    # Extra structured fields (all None for not_started/no-evidence chapters)
    # so the frontend can build a real "why this is recommended" breakdown
    # instead of parsing the explanation sentence - every one of these is a
    # genuine ChapterEvidence field, not a derived/invented score.
    n_attempts: int | None = None
    raw_accuracy: float | None = None
    confidence: float | None = None
    trend_slope: float | None = None
    trend_significant: bool = False
    priority_score: float | None = None
    # n_attempts-weighted average mastery of this student's OTHER evidenced
    # chapters in the same subject - None when there's no such chapter yet,
    # never a fabricated comparison.
    subject_avg_mastery: float | None = None


# ------------------------------------------------------------- performance --
class SessionHistoryEntryOut(BaseModel):
    session_id: int
    course_id: int
    chapter_id: int | None
    purpose: str
    started_at: datetime
    completed_at: datetime | None
    total_questions: int
    correct_count: int
    percentage: float | None


class SubjectPerformanceOut(BaseModel):
    subject_id: int
    subject_name: str
    n_attempts: int
    avg_mastery: float


class AccuracyPointOut(BaseModel):
    attempt_order: int
    answered_at: datetime
    is_correct: bool
    # Lets the frontend bucket/filter the trend by subject using the same
    # chapter-tree lookup it already builds for other pages - cheaper than
    # a second subject-scoped trend endpoint.
    chapter_id: int


class PerformanceOut(BaseModel):
    accuracy_trend: list[AccuracyPointOut]
    subject_breakdown: list[SubjectPerformanceOut]
    session_history: list[SessionHistoryEntryOut]


# --------------------------------------------------------------- progress --
class BeforeAfterOut(BaseModel):
    chapter_id: int
    chapter_name: str
    mastery_before: float | None
    mastery_after: float | None


class MasteredChapterOut(BaseModel):
    """One chapter counted in chapters_completed - lets the frontend show
    exactly which chapters that number refers to instead of just a count,
    same n_attempts/confidence transparency as everywhere else in the app."""
    chapter_id: int
    chapter_name: str
    mastery_estimate: float
    n_attempts: int
    confidence: float


class ProgressOut(BaseModel):
    streak_days: int
    chapters_completed: int
    chapters_total_tracked: int
    before_after: list[BeforeAfterOut]
    mastered_chapters: list[MasteredChapterOut] = []


# ----------------------------------------------------------- achievements --
class BadgeOut(BaseModel):
    id: str
    label: str
    description: str
    tier: int
    earned: bool
    icon: str


class NextMilestoneOut(BaseModel):
    badge_id: str
    label: str
    progress_current: int
    progress_target: int
    message: str


class AchievementsOut(BaseModel):
    badges: list[BadgeOut]
    next_milestones: list[NextMilestoneOut]


# ------------------------------------------------------- recently practiced --
class RecentChapterOut(BaseModel):
    chapter_id: int
    chapter_name: str
    course_id: int
    last_practiced_at: datetime
    mastery_estimate: float | None
    priority_band: str | None


# --------------------------------------------------------------- assistant --
class AssistantAskRequest(BaseModel):
    question: str


class AssistantAskResponse(BaseModel):
    answer: str
    matched_intent: str | None  # null when the fallback response was used


# --------------------------------------------------- teacher-side analytics --
class TeacherDashboardSummaryOut(BaseModel):
    total_students: int
    total_chapters_tracked: int
    grade_distribution: dict[str, int]
    stream_distribution: dict[str, int]
    band_distribution: dict[str, int]
    avg_mastery: float | None
    alerts: list[StudentAttentionOut]


class SectionCreate(BaseModel):
    name: str
    type: Literal["Subject", "Unit", "Chapter"]
    parent_id: int | None = None
    course_id: int


class QuestionCreate(BaseModel):
    """Teacher-authored question. options[correct_index] is the correct
    answer in the AUTHOR's own order - storage shuffles it (same
    shuffle-at-insert discipline as scripts/load_question_bank.py, so an
    authored "correct index 0" bias is never preserved in the DB)."""
    chapter_id: int
    body: str
    options: list[str]
    correct_index: int
    difficulty_label: Literal["Easy", "Medium", "Hard"] = "Medium"
    question_type: Literal["MCQ", "example"] = "MCQ"
    explanation: str | None = None


class QuestionLevelStatOut(BaseModel):
    question_id: int
    body: str
    n_attempts: int
    accuracy: float


class ChapterAnalyticsOut(BaseModel):
    chapter_id: int
    chapter_name: str
    n_students_tracked: int
    pct_students_weak: float
    difficulty_breakdown: dict[str, float]  # difficulty_label -> accuracy
    question_level: list[QuestionLevelStatOut]
