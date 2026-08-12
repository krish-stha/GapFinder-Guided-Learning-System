import { api } from "./client";
import type {
  Course,
  Chapter,
  ChapterResources,
  ChapterProgress,
  LearningResource,
  QuizTemplate,
} from "../types";

export interface SectionPayload {
  name: string;
  type: "Subject" | "Unit" | "Chapter";
  parent_id: number | null;
  course_id: number;
}

export interface QuestionPayload {
  chapter_id: number;
  body: string;
  options: string[];
  correct_index: number;
  difficulty_label?: "Easy" | "Medium" | "Hard";
  question_type?: "MCQ" | "example";
  explanation?: string | null;
}

export interface ResourcePayload {
  chapter_id: number;
  type: "note" | "video" | "resource_link";
  title: string;
  body_markdown?: string | null;
  url?: string | null;
  order_index?: number;
}

export const contentApi = {
  listCourses: () => api.get<Course[]>("/content/courses"),
  // no `type` filter passed - fetch the whole Subject/Unit/Chapter tree for
  // the course in one call and build the tree client-side (see ChaptersPage)
  listSections: (courseId: number) => api.get<Chapter[]>(`/content/sections?course_id=${courseId}`),
  chapterResources: (chapterId: number) => api.get<ChapterResources>(`/content/chapters/${chapterId}/resources`),
  markChapterComplete: (chapterId: number) => api.post<ChapterProgress>(`/content/chapters/${chapterId}/complete`),
  completedChapterIds: () => api.get<number[]>("/content/chapters/completed/me"),
  quizTemplates: (courseId: number) => api.get<QuizTemplate[]>(`/content/quiz-templates?course_id=${courseId}`),

  createSection: (payload: SectionPayload) => api.post<Chapter>("/content/sections", payload),
  updateSection: (id: number, payload: SectionPayload) => api.put<Chapter>(`/content/sections/${id}`, payload),
  deleteSection: (id: number) => api.delete<{ detail: string }>(`/content/sections/${id}`),

  createQuestion: (payload: QuestionPayload) => api.post<unknown>("/content/questions", payload),
  deleteQuestion: (id: number) => api.delete<{ detail: string }>(`/content/questions/${id}`),

  createResource: (payload: ResourcePayload) => api.post<LearningResource>("/content/resources", payload),
  updateResource: (id: number, payload: Partial<ResourcePayload>) =>
    api.put<LearningResource>(`/content/resources/${id}`, payload),
  deleteResource: (id: number) => api.delete<{ detail: string }>(`/content/resources/${id}`),
};
