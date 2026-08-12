import { api } from "./client";
import type {
  StartSessionResponse,
  AnswerResponse,
  FinishSessionResult,
  ChapterEvidence,
  ChapterDetail,
  ReviewToggle,
  SessionState,
  SessionPurpose,
  LearningPathStep,
  Performance,
  Progress,
  AssistantAskResponse,
  Achievements,
  RecentChapter,
} from "../types";

export interface StartSessionPayload {
  // null = mixed draw across every chapter in course_id (mock_test/diagnostic mode).
  chapter_id: number | null;
  course_id: number;
  num_questions?: number;
  purpose?: SessionPurpose;
  quiz_template_id?: number;
}

export interface AnswerPayload {
  question_id: number;
  selected_index: number | null;
  time_taken_seconds?: number;
}

export const practiceApi = {
  start: (payload: StartSessionPayload) => api.post<StartSessionResponse>("/practice/start", payload),
  answer: (sessionId: number, payload: AnswerPayload) =>
    api.post<AnswerResponse>(`/practice/${sessionId}/answer`, payload),
  toggleReview: (sessionId: number, questionId: number) =>
    api.put<ReviewToggle>(`/practice/${sessionId}/review/${questionId}`),
  state: (sessionId: number) => api.get<SessionState>(`/practice/${sessionId}/state`),
  finish: (sessionId: number) => api.post<FinishSessionResult>(`/practice/${sessionId}/finish`, {}),
  resultsMe: () => api.get<ChapterEvidence[]>("/practice/results/me"),
  chapterDetail: (chapterId: number) => api.get<ChapterDetail>(`/practice/chapters/${chapterId}/detail`),
  learningPath: () => api.get<LearningPathStep[]>("/practice/learning-path/me"),
  performanceMe: () => api.get<Performance>("/practice/performance/me"),
  progressMe: () => api.get<Progress>("/practice/progress/me"),
  askAssistant: (question: string) => api.post<AssistantAskResponse>("/practice/assistant/ask", { question }),
  achievementsMe: () => api.get<Achievements>("/practice/achievements/me"),
  recentChapters: (limit = 3) => api.get<RecentChapter[]>(`/practice/recent-chapters/me?limit=${limit}`),
};
