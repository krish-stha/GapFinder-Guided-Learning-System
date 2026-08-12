import { createContext, useContext, useState, useCallback, useEffect, useRef, type ReactNode } from "react";
import { practiceApi } from "../api/practice";
import { useAuth } from "./AuthContext";

interface StreakContextValue {
  streakDays: number | null;
  // Called after a practice/exam session finishes so the sidebar streak
  // updates immediately instead of waiting for the next navigation (the
  // previous behaviour: Layout fetched once per mount).
  refreshStreak: () => void;
}

const StreakContext = createContext<StreakContextValue | undefined>(undefined);

export function StreakProvider({ children }: { children: ReactNode }) {
  const { student, isAuthenticated } = useAuth();
  const [streakDays, setStreakDays] = useState<number | null>(null);
  const isStudent = isAuthenticated && student?.role === "student";
  // React StrictMode (dev only) double-invokes effects, and the mount
  // effect below plus a manual refreshStreak() call can both be in flight
  // at once - without this guard, whichever request resolves LAST wins,
  // which isn't necessarily the most recently issued one. Same class of
  // bug this codebase already hit once with VerifyEmailPage's token
  // double-fire; fixed the same way there - ignore any response that
  // isn't from the latest request this provider issued.
  const requestIdRef = useRef(0);

  const refreshStreak = useCallback(() => {
    if (!isStudent) return;
    const requestId = ++requestIdRef.current;
    practiceApi
      .progressMe()
      .then((p) => {
        if (requestId === requestIdRef.current) setStreakDays(p.streak_days);
      })
      .catch(() => undefined);
  }, [isStudent]);

  useEffect(() => {
    if (isStudent) {
      refreshStreak();
    } else {
      requestIdRef.current++; // invalidate any in-flight request from the previous session
      setStreakDays(null);
    }
  }, [isStudent, refreshStreak]);

  return <StreakContext.Provider value={{ streakDays, refreshStreak }}>{children}</StreakContext.Provider>;
}

export function useStreak(): StreakContextValue {
  const ctx = useContext(StreakContext);
  if (!ctx) throw new Error("useStreak must be used within a StreakProvider");
  return ctx;
}
