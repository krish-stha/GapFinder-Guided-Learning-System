import { createContext, useContext, useState, useCallback, type ReactNode } from "react";
import { authApi, type LoginPayload, type RegisterPayload } from "../api/auth";
import { getToken, setToken as persistToken } from "../api/client";
import type { Student } from "../types";

interface AuthContextValue {
  student: Student | null;
  isAuthenticated: boolean;
  // both return the resolved Student so the caller can navigate by role
  // immediately, without waiting on a re-render to see updated context state
  login: (payload: LoginPayload) => Promise<Student>;
  register: (payload: RegisterPayload) => Promise<Student>;
  logout: () => void;
  // patches the locally-cached student (e.g. email_verified flipping true)
  // without a full re-login round trip
  updateStudent: (patch: Partial<Student>) => void;
}

const AuthContext = createContext<AuthContextValue | undefined>(undefined);
const STUDENT_KEY = "gls_student";

function loadStoredStudent(): Student | null {
  const raw = localStorage.getItem(STUDENT_KEY);
  if (!raw) return null;
  try {
    return JSON.parse(raw) as Student;
  } catch {
    return null;
  }
}

function persistStudent(student: Student | null) {
  if (student) localStorage.setItem(STUDENT_KEY, JSON.stringify(student));
  else localStorage.removeItem(STUDENT_KEY);
}

export function AuthProvider({ children }: { children: ReactNode }) {
  const [student, setStudent] = useState<Student | null>(loadStoredStudent);
  const [hasToken, setHasToken] = useState<boolean>(!!getToken());

  const login = useCallback(async (payload: LoginPayload) => {
    const res = await authApi.login(payload);
    persistToken(res.access_token);
    persistStudent(res.student);
    setStudent(res.student);
    setHasToken(true);
    return res.student;
  }, []);

  const register = useCallback(async (payload: RegisterPayload) => {
    const res = await authApi.register(payload);
    persistToken(res.access_token);
    persistStudent(res.student);
    setStudent(res.student);
    setHasToken(true);
    return res.student;
  }, []);

  const logout = useCallback(() => {
    persistToken(null);
    persistStudent(null);
    setStudent(null);
    setHasToken(false);
  }, []);

  const updateStudent = useCallback((patch: Partial<Student>) => {
    setStudent((prev) => {
      if (!prev) return prev;
      const next = { ...prev, ...patch };
      persistStudent(next);
      return next;
    });
  }, []);

  return (
    <AuthContext.Provider value={{ student, isAuthenticated: hasToken, login, register, logout, updateStudent }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth(): AuthContextValue {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used within an AuthProvider");
  return ctx;
}
