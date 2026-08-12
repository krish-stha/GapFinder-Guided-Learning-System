import type { ReactNode } from "react";
import Logo from "./Logo";

const TAGLINES: { heading: string; body: string }[] = [
  {
    heading: "Know exactly what to study next.",
    body: "Evidence-weighted, explainable chapter recommendations built from your own practice history - not a generic percentage cutoff.",
  },
  {
    heading: "Every recommendation shows its work.",
    body: "Accuracy, difficulty, recency, and trend - the same factors a good tutor would weigh, laid out so you can see exactly why a chapter is flagged.",
  },
];

export default function AuthLayout({ children }: { children: ReactNode }) {
  const tagline = TAGLINES[Math.floor(Math.random() * TAGLINES.length)];
  return (
    <div className="auth-page">
      <div className="auth-hero" aria-hidden="true">
        <div className="auth-hero-content">
          <span className="auth-hero-brand">
            <Logo size={22} variant="solid" />
            GapFinder
          </span>
          <h2>{tagline.heading}</h2>
          <p>{tagline.body}</p>
        </div>
      </div>
      <div className="auth-panel">{children}</div>
    </div>
  );
}
