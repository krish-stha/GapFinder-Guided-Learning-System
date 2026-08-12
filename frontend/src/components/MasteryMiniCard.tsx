import { Link } from "react-router-dom";
import type { ChapterEvidence, PriorityBand } from "../types";

export const BAND_CLASS: Record<PriorityBand, string> = {
  High: "band-high",
  Medium: "band-medium",
  Low: "band-low",
  "Insufficient evidence": "band-insufficient",
};

// colorClass is a plain string rather than PriorityBand so this can also
// color a subject-level aggregate bar (Practice page's subject cards),
// which has no real priority_band of its own - see pctColorClass below.
export function MasteryBar({ pct, colorClass }: { pct: number; colorClass: string }) {
  return (
    <div className="mastery-bar-track">
      <div className={`mastery-bar-fill ${colorClass}`} style={{ width: `${pct}%` }} />
    </div>
  );
}

// For an aggregate (e.g. average mastery across a subject's chapters) that
// isn't itself a ChapterEvidence with a real priority_band - buckets by
// raw percentage instead, using distinct pct-* classes so it's never
// confused with an actual evidence-derived band elsewhere in the UI.
export function pctColorClass(ratio: number): string {
  if (ratio < 0.4) return "pct-low";
  if (ratio < 0.7) return "pct-mid";
  return "pct-good";
}

export function ChapterMiniCard({ evidence, linkTo }: { evidence: ChapterEvidence; linkTo: string }) {
  const bandClass = BAND_CLASS[evidence.priority_band] ?? "band-insufficient";
  const pct = Math.round(evidence.mastery_estimate * 100);
  return (
    <div className={`weak-area-mini-card ${bandClass}`}>
      <h4>{evidence.chapter_name}</h4>
      <p className="weak-area-mini-pct">{pct}% mastery</p>
      <MasteryBar pct={pct} colorClass={bandClass} />
      <span className={`band-badge ${bandClass}`}>{evidence.priority_band}</span>
      <Link to={linkTo} className="cta-button-secondary weak-area-mini-cta">
        Practice
      </Link>
    </div>
  );
}
