import { useEffect, useState } from "react";
import { useAuth } from "../context/AuthContext";

function storageKey(studentId: number): string {
  return `gls_onboarding_seen_${studentId}`;
}

// One-time welcome popup, shown the first time a student lands on a
// completely empty Dashboard (zero practice attempts). Purely a first-run
// nudge - dismissing it (either way) never needs to be shown again for
// this account, tracked per student id so it doesn't leak across logins
// on a shared browser.
export default function WelcomeOnboardingModal() {
  const { student } = useAuth();
  const [open, setOpen] = useState(false);

  useEffect(() => {
    if (!student) return;
    if (!localStorage.getItem(storageKey(student.id))) setOpen(true);
  }, [student]);

  function dismiss() {
    if (student) localStorage.setItem(storageKey(student.id), "1");
    setOpen(false);
  }

  if (!open) return null;

  return (
    <div className="exam-confirm-overlay" onClick={dismiss}>
      <div className="exam-confirm-panel onboarding-modal-panel" onClick={(e) => e.stopPropagation()}>
        <button type="button" className="onboarding-modal-close" aria-label="Close" onClick={dismiss}>
          ×
        </button>
        <h2>Welcome to GapFinder</h2>
        <p className="dashboard-subtitle">Get a real, evidence-based baseline in a couple of minutes:</p>
        <ol className="onboarding-modal-steps">
          <li>
            <strong>Take a diagnostic assessment</strong> - untimed, mixed questions across every chapter in your
            course.
          </li>
          <li>
            <strong>Get your personalised weak-chapter list</strong> - ranked by priority, with a plain-English
            explanation for each one.
          </li>
        </ol>
        <div className="onboarding-modal-actions">
          <button type="button" className="cta-button-secondary" onClick={dismiss}>
            Skip for now
          </button>
          <button type="button" className="cta-button" onClick={dismiss}>
            Let's start
          </button>
        </div>
      </div>
    </div>
  );
}
