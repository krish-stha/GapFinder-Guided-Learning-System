import { api } from "./client";
import type {
  CohortChapterEvidence,
  ChapterWeakness,
  StudentAttention,
  StudentSummary,
  TeacherDashboardSummary,
  ChapterEvidence,
  Performance,
  ChapterAnalytics,
  QuizTemplate,
  SchoolClass,
} from "../types";

export interface QuizTemplatePayload {
  title: string;
  course_id: number;
  chapter_id?: number | null;
  difficulty_label?: string | null;
  num_questions?: number;
  time_limit_seconds?: number | null;
  is_published?: boolean;
}

export interface ClassPayload {
  name: string;
  course_id: number;
}

// Builds "?a=1&b=2" from whichever of course_id/class_id are actually set -
// every cohort endpoint below takes the same optional pair, so this is the
// one place that conditional-query-string logic lives instead of being
// repeated per wrapper.
function cohortQuery(params: { course_id?: number | null; class_id?: number | null }): string {
  const parts: string[] = [];
  if (params.course_id != null) parts.push(`course_id=${params.course_id}`);
  if (params.class_id != null) parts.push(`class_id=${params.class_id}`);
  return parts.length ? `?${parts.join("&")}` : "";
}

export const teacherApi = {
  cohortEvidence: (courseId?: number | null, classId?: number | null) =>
    api.get<CohortChapterEvidence[]>(`/teacher/cohort-evidence${cohortQuery({ course_id: courseId, class_id: classId })}`),
  chaptersFailing: (classId?: number | null) =>
    api.get<ChapterWeakness[]>(`/teacher/chapters-failing${cohortQuery({ class_id: classId })}`),
  studentsNeedingAttention: () => api.get<StudentAttention[]>("/teacher/students-needing-attention"),
  studentsOverview: (classId?: number | null) =>
    api.get<StudentSummary[]>(`/teacher/students-overview${cohortQuery({ class_id: classId })}`),
  dashboardSummary: (classId?: number | null) =>
    api.get<TeacherDashboardSummary>(`/teacher/dashboard-summary${cohortQuery({ class_id: classId })}`),
  studentEvidence: (studentId: number) => api.get<ChapterEvidence[]>(`/teacher/students/${studentId}/evidence`),
  studentPerformance: (studentId: number) => api.get<Performance>(`/teacher/students/${studentId}/performance`),
  chapterAnalytics: (chapterId: number, classId?: number | null) =>
    api.get<ChapterAnalytics>(`/teacher/chapters/${chapterId}/analytics${cohortQuery({ class_id: classId })}`),

  createQuizTemplate: (payload: QuizTemplatePayload) => api.post<QuizTemplate>("/teacher/quiz-templates", payload),
  updateQuizTemplate: (id: number, payload: QuizTemplatePayload) =>
    api.put<QuizTemplate>(`/teacher/quiz-templates/${id}`, payload),
  deleteQuizTemplate: (id: number) => api.delete<{ detail: string }>(`/teacher/quiz-templates/${id}`),

  listClasses: () => api.get<SchoolClass[]>("/teacher/classes"),
  createClass: (payload: ClassPayload) => api.post<SchoolClass>("/teacher/classes", payload),
  deleteClass: (id: number) => api.delete<{ detail: string }>(`/teacher/classes/${id}`),
  classRoster: (id: number) => api.get<StudentSummary[]>(`/teacher/classes/${id}/roster`),
  addStudentToClass: (classId: number, studentId: number) =>
    api.post<{ detail: string }>(`/teacher/classes/${classId}/students`, { student_id: studentId }),
  removeStudentFromClass: (classId: number, studentId: number) =>
    api.delete<{ detail: string }>(`/teacher/classes/${classId}/students/${studentId}`),
};
