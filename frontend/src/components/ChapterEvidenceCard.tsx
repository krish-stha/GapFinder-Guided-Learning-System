import { Link } from "react-router-dom";
import type { ChapterEvidence } from "../types";

const BAND_CLASS: Record<string, string> = {
  High: "band-high",
  Medium: "band-medium",
  Low: "band-low",
  "Insufficient evidence": "band-insufficient",
};

interface ChapterEvidenceCardProps {
  evidence: ChapterEvidence;
  // false = render as a non-navigating div (e.g. a teacher viewing a
  // student's evidence - /chapter/:id is a student-only route, so linking
  // there would just bounce a teacher back to /teacher via ProtectedRoute).
  linkTo?: string | false;
}

function CardContents({ evidence, bandClass }: { evidence: ChapterEvidence; bandClass: string }) {
  return (
    <>
      <header className="evidence-header">
        <h3>{evidence.chapter_name}</h3>
        <span className={`band-badge ${bandClass}`}>{evidence.priority_band}</span>
      </header>
      <p className="evidence-explanation">{evidence.explanation}</p>
      {evidence.priority_band !== "Insufficient evidence" && (
        <dl className="evidence-stats">
          <div>
            <dt>Mastery</dt>
            <dd>{Math.round(evidence.mastery_estimate * 100)}%</dd>
          </div>
          <div>
            <dt>Confidence</dt>
            <dd>{Math.round(evidence.confidence * 100)}%</dd>
          </div>
          <div>
            <dt>Attempts</dt>
            <dd>{evidence.n_attempts}</dd>
          </div>
        </dl>
      )}
    </>
  );
}

export default function ChapterEvidenceCard({ evidence, linkTo }: ChapterEvidenceCardProps) {
  const bandClass = BAND_CLASS[evidence.priority_band] ?? "band-insufficient";

  if (linkTo === false) {
    return (
      <div className={`evidence-card ${bandClass}`}>
        <CardContents evidence={evidence} bandClass={bandClass} />
      </div>
    );
  }

  return (
    <Link to={linkTo ?? `/chapter/${evidence.chapter_id}`} className={`evidence-card ${bandClass}`}>
      <CardContents evidence={evidence} bandClass={bandClass} />
    </Link>
  );
}
