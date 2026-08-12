// Mirrors backend/app/schemas.py exactly - keep these two in sync by hand,
// there's no shared codegen between the FastAPI backend and this frontend.

export type Role = "student" | "teacher";

export interface Student {
  id: number;
  name: string;
  email: string;
  grade: number | null;
  stream: string | null;
  role: Role;
  email_verified: boolean;
  class_id: number | null;
}

export interface MessageOut {
  detail: string;
}

export interface TokenResponse {
  access_token: string;
  token_type: string;
  student: Student;
}

export interface Course {
  id: number;
  name: string;
}

export interface Chapter {
  id: number;
  name: string;
  type: string; // "Subject" | "Unit" | "Chapter"
  parent_id: number | null;
  course_id: number;
}

export type SessionPurpose = "practice" | "mock_test" | "diagnostic";

export interface Question {
  id: number;
  body: string; // HTML
  answers: string[]; // HTML per option
  difficulty_label: string | null;
  source: string; // "real" | "synthetic"
  position: number;
}

export interface StartSessionResponse {
  session_id: number;
  questions: Question[];
  time_limit_seconds: number | null; // null = untimed
}

export interface AnswerResponse {
  // Always null - every session type defers correctness to /finish's
  // full review, never revealed per-question.
  is_correct: boolean | null;
  correct_answer: number | null;
  explanation: string | null;
}

export interface ReviewToggle {
  question_id: number;
  marked_for_review: boolean;
}

export interface QuestionState {
  question_id: number;
  position: number;
  answered: boolean;
  marked_for_review: boolean;
  selected_index: number | null;
}

export interface SessionState {
  session_id: number;
  purpose: SessionPurpose;
  status: "in_progress" | "completed";
  time_limit_seconds: number | null;
  seconds_remaining: number | null; // null = untimed
  questions: QuestionState[];
}

export interface QuestionReview {
  question_id: number;
  position: number;
  body: string;
  answers: string[];
  selected_index: number | null;
  correct_answer: number | null;
  is_correct: boolean | null;
  explanation: string | null;
  chapter_id: number;
  chapter_name: string;
}

export type PriorityBand = "High" | "Medium" | "Low" | "Insufficient evidence";

export interface ChapterEvidence {
  chapter_id: number;
  chapter_name: string;
  n_attempts: number;
  raw_accuracy: number;
  mastery_estimate: number;
  confidence: number;
  trend_slope: number | null;
  trend_significant: boolean;
  priority_score: number;
  priority_band: PriorityBand;
  explanation: string;
  // n_attempts-weighted average mastery of this student's OTHER evidenced
  // chapters in the same subject - null when there's no such chapter yet.
  subject_avg_mastery: number | null;
}

export interface Attempt {
  order: number;
  is_correct: boolean;
  difficulty_label: string | null;
  answered_at: string; // ISO datetime
}

export interface ChapterDetail {
  chapter_id: number;
  chapter_name: string;
  course_id: number;
  n_attempts: number;
  raw_accuracy: number;
  mastery_estimate: number;
  confidence: number;
  trend_slope: number | null;
  trend_significant: boolean;
  priority_score: number;
  priority_band: PriorityBand;
  explanation: string;
  subject_avg_mastery: number | null;
  attempts: Attempt[];
}

export interface FinishSessionResult {
  session_id: number;
  purpose: SessionPurpose;
  total_questions: number;
  correct_count: number;
  percentage: number | null;
  status: string;
  // Per-chapter mastery evidence for the chapters this session touched,
  // computed from the student's full history in each (not just this
  // session) - same engine/pattern as the dashboard's ChapterEvidence.
  chapter_breakdown: ChapterEvidence[];
  review: QuestionReview[];
}

// ----------------------------------------------------------- teacher/cohort --

export interface CohortChapterEvidence {
  student_id: number;
  student_name: string;
  chapter_id: number;
  chapter_name: string;
  n_attempts: number;
  mastery_estimate: number;
  confidence: number;
  priority_score: number;
  priority_band: PriorityBand;
}

export interface ChapterWeakness {
  chapter_id: number;
  chapter_name: string;
  n_students: number;
  n_students_high_priority: number;
  avg_mastery: number;
}

export interface StudentAttention {
  student_id: number;
  student_name: string;
  n_chapters_tracked: number;
  n_high_priority_chapters: number;
  avg_priority_score: number;
  weakest_chapter_name: string;
}

export interface StudentSummary {
  student_id: number;
  student_name: string;
  grade: number | null;
  stream: string | null;
  has_activity: boolean;
  n_chapters_tracked: number;
  avg_mastery: number | null;
  n_high: number;
  n_medium: number;
  n_low: number;
  weakest_chapter_name: string | null;
}

export interface SchoolClass {
  id: number;
  name: string;
  course_id: number;
  join_code: string;
  student_count: number;
  created_at: string; // ISO datetime
}

// ------------------------------------------------------- learning content --

export type ResourceType = "note" | "video" | "resource_link";

export interface LearningResource {
  id: number;
  chapter_id: number;
  type: ResourceType;
  title: string;
  body_markdown: string | null;
  url: string | null;
  order_index: number;
}

export interface ChapterProgress {
  chapter_id: number;
  notes_viewed_at: string | null;
  marked_complete_at: string | null;
}

export interface ChapterResources {
  chapter_id: number;
  chapter_name: string;
  resources: LearningResource[];
  examples: Question[];
  progress: ChapterProgress;
}

// ---------------------------------------------------------- quiz templates --

export interface QuizTemplate {
  id: number;
  title: string;
  course_id: number;
  chapter_id: number | null;
  difficulty_label: string | null;
  num_questions: number;
  time_limit_seconds: number | null;
  is_published: boolean;
}

// ------------------------------------------------------------ learning path --

export type LearningPathStatus = PriorityBand | "not_started";

export interface LearningPathStep {
  chapter_id: number;
  chapter_name: string;
  status: LearningPathStatus;
  mastery_estimate: number | null;
  explanation: string;
  has_notes: boolean;
  has_video: boolean;
  // All null for not-started/no-evidence chapters. Every one of these is a
  // real ChapterEvidence field, not a derived/invented score.
  n_attempts: number | null;
  raw_accuracy: number | null;
  confidence: number | null;
  trend_slope: number | null;
  trend_significant: boolean;
  priority_score: number | null;
  // n_attempts-weighted average mastery of this student's OTHER evidenced
  // chapters in the same subject - null when there's no such chapter yet.
  subject_avg_mastery: number | null;
}

// ------------------------------------------------------------- performance --

export interface SessionHistoryEntry {
  session_id: number;
  course_id: number;
  chapter_id: number | null;
  purpose: string;
  started_at: string; // ISO datetime
  completed_at: string | null;
  total_questions: number;
  correct_count: number;
  percentage: number | null;
}

export interface SubjectPerformance {
  subject_id: number;
  subject_name: string;
  n_attempts: number;
  avg_mastery: number;
}

export interface AccuracyPoint {
  attempt_order: number;
  answered_at: string;
  is_correct: boolean;
  chapter_id: number;
}

export interface Performance {
  accuracy_trend: AccuracyPoint[];
  subject_breakdown: SubjectPerformance[];
  session_history: SessionHistoryEntry[];
}

// --------------------------------------------------------------- progress --

export interface BeforeAfter {
  chapter_id: number;
  chapter_name: string;
  mastery_before: number | null;
  mastery_after: number | null;
}

export interface MasteredChapter {
  chapter_id: number;
  chapter_name: string;
  mastery_estimate: number;
  n_attempts: number;
  confidence: number;
}

export interface Progress {
  streak_days: number;
  chapters_completed: number;
  chapters_total_tracked: number;
  before_after: BeforeAfter[];
  mastered_chapters: MasteredChapter[];
}

// ----------------------------------------------------------- achievements --

export interface Badge {
  id: string;
  label: string;
  description: string;
  tier: number;
  earned: boolean;
  icon: string;
}

export interface NextMilestone {
  badge_id: string;
  label: string;
  progress_current: number;
  progress_target: number;
  message: string;
}

export interface Achievements {
  badges: Badge[];
  next_milestones: NextMilestone[];
}

// ------------------------------------------------------- recently practiced --

export interface RecentChapter {
  chapter_id: number;
  chapter_name: string;
  course_id: number;
  last_practiced_at: string; // ISO datetime
  mastery_estimate: number | null;
  priority_band: PriorityBand | null;
}

// --------------------------------------------------------------- assistant --

export interface AssistantAskResponse {
  answer: string;
  matched_intent: string | null;
}

// --------------------------------------------------- teacher-side analytics --

export interface TeacherDashboardSummary {
  total_students: number;
  total_chapters_tracked: number;
  grade_distribution: Record<string, number>;
  stream_distribution: Record<string, number>;
  band_distribution: Record<string, number>;
  avg_mastery: number | null;
  alerts: StudentAttention[];
}

export interface QuestionLevelStat {
  question_id: number;
  body: string;
  n_attempts: number;
  accuracy: number;
}

export interface ChapterAnalytics {
  chapter_id: number;
  chapter_name: string;
  n_students_tracked: number;
  pct_students_weak: number;
  difficulty_breakdown: Record<string, number>;
  question_level: QuestionLevelStat[];
}
