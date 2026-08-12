import { api } from "./client";
import type { Role, Student, TokenResponse, MessageOut } from "../types";

export interface RegisterPayload {
  name: string;
  email: string;
  password: string;
  grade?: number;
  stream?: string;
  role?: Role;
  teacher_invite_code?: string;
  // optional - a student can register without a class and join one later
  class_join_code?: string;
}

export interface LoginPayload {
  email: string;
  password: string;
}

export const authApi = {
  register: (payload: RegisterPayload) => api.post<TokenResponse>("/auth/register", payload),
  login: (payload: LoginPayload) => api.post<TokenResponse>("/auth/login", payload),
  requestEmailVerification: () => api.post<MessageOut>("/auth/request-email-verification"),
  verifyEmail: (token: string) => api.get<MessageOut>(`/auth/verify-email?token=${encodeURIComponent(token)}`),
  forgotPassword: (email: string) => api.post<MessageOut>("/auth/forgot-password", { email }),
  resetPassword: (token: string, newPassword: string) =>
    api.post<MessageOut>("/auth/reset-password", { token, new_password: newPassword }),
  joinClass: (joinCode: string) => api.post<Student>("/auth/join-class", { join_code: joinCode }),
};
