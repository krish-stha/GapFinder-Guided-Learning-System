import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { practiceApi } from "../api/practice";
import { ApiError } from "../api/client";
import AccuracyTrendChart from "../components/AccuracyTrendChart";
import { MasteryBar } from "../components/MasteryMiniCard";
import { chapterStatusFor, CHAPTER_STATUS_CLASS } from "../utils/chapterStatus";
import type { ChapterDetail } from "../types";

// Every bullet here maps to a real field on `detail` - never fabricated
// advice text. Framed positively for a Low-band ("Strong") chapter instead
// of reusing "needs attention" language that wouldn't make sense there.
function buildReasons(detail: ChapterDetail): string[] {
  const reasons: string[] = [];
  const isStrong = detail.priority_band === "Low";
  const diffPct =
    detail.subject_avg_mastery !== null ? Math.round((detail.mastery_estimate - detail.subject_avg_mastery) * 100) : null;

  if (diffPct !== null) {
    if (diffPct < 0) reasons.push(`Your mastery here is ${Math.abs(diffPct)}% below your average in other chapters in this subject.`);
    else if (isStrong && diffPct > 0) reasons.push(`Your mastery here is ${diffPct}% above your average in other chapters in this subject.`);
  }
  if (detail.trend_significant && detail.trend_slope !== null) {
    reasons.push(
      detail.trend_slope < 0
        ? "Your performance has been declining over recent attempts."
        : "Your performance has been improving over recent attempts.",
    );
  }
  if (detail.confidence >= 0.7) {
    reasons.push(`You have enough attempts (${detail.n_attempts}) for this estimate to be reliable.`);
  } else {
    reasons.push(`This estimate is based on a limited number of attempts (${detail.n_attempts}) so far.`);
  }
  return reasons;
}

export default function ChapterDetailPage() {
  const { chapterId } = useParams();
  const [detail, setDetail] = useState<ChapterDetail | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!chapterId) return;
    practiceApi
      .chapterDetail(Number(chapterId))
      .then(setDetail)
      .catch((err) =>
        setError(
          err instanceof ApiError && err.status === 404
            ? "No recorded attempts for this chapter yet."
            : err instanceof ApiError
              ? err.message
              : "Could not load chapter detail.",
        ),
      );
  }, [chapterId]);

  if (error)
    return (
      <div className="page-error">
        <p>{error}</p>
        <Link to="/dashboard">Back to dashboard</Link>
      </div>
    );
  if (detail === null) return <p className="page-loading">Loading chapter detail…</p>;

  const status = chapterStatusFor(detail.priority_band);
  const statusClass = CHAPTER_STATUS_CLASS[status];
  const trendLabel =
    detail.trend_significant && detail.trend_slope !== null
      ? detail.trend_slope > 0
        ? "Improving"
        : "Declining"
      : "No clear trend";
  const diffPct =
    detail.subject_avg_mastery !== null ? Math.round((detail.mastery_estimate - detail.subject_avg_mastery) * 100) : null;
  const reasons = buildReasons(detail);

  return (
    <div className="detail-page">
      <Link to="/dashboard" className="detail-back">
        ← Back to dashboard
      </Link>
      <header className="detail-header">
        <h1>{detail.chapter_name}</h1>
        <span className={`band-badge ${statusClass}`}>{status}</span>
      </header>
      <p className="evidence-explanation">{detail.explanation}</p>

      <div className="mastery-bar-row detail-mastery-row">
        <span>Mastery</span>
        <span>{Math.round(detail.mastery_estimate * 100)}%</span>
      </div>
      <MasteryBar pct={Math.round(detail.mastery_estimate * 100)} colorClass={statusClass} />

      <dl className="evidence-stats detail-stats">
        <div>
          <dt>Accuracy</dt>
          <dd>{Math.round(detail.raw_accuracy * 100)}%</dd>
        </div>
        {detail.subject_avg_mastery !== null && (
          <div>
            <dt>Subject average</dt>
            <dd>{Math.round(detail.subject_avg_mastery * 100)}%</dd>
          </div>
        )}
        {diffPct !== null && (
          <div>
            <dt>Difference</dt>
            <dd className={diffPct >= 0 ? "feedback-correct" : "feedback-neutral"}>
              {diffPct >= 0 ? "+" : ""}
              {diffPct}%
            </dd>
          </div>
        )}
        <div>
          <dt>Confidence</dt>
          <dd>{Math.round(detail.confidence * 100)}%</dd>
        </div>
        <div>
          <dt>Attempts</dt>
          <dd>{detail.n_attempts}</dd>
        </div>
        <div>
          <dt>Trend</dt>
          <dd>{trendLabel}</dd>
        </div>
      </dl>

      <section className="detail-section">
        <h2>Score history</h2>
        <AccuracyTrendChart points={detail.attempts} />
      </section>

      {reasons.length > 0 && (
        <section className="detail-section">
          <h2>{status === "Strong" ? "Why this chapter looks strong" : "Why this matters"}</h2>
          <ul className="detail-reasons">
            {reasons.map((r) => (
              <li key={r}>{r}</li>
            ))}
          </ul>
        </section>
      )}

      <section className="detail-section">
        <h2>Attempts</h2>
        <table className="teacher-table">
          <thead>
            <tr>
              <th>#</th>
              <th>Result</th>
              <th>Difficulty</th>
              <th>When</th>
            </tr>
          </thead>
          <tbody>
            {detail.attempts.map((a) => (
              <tr key={a.order}>
                <td>{a.order + 1}</td>
                <td className={a.is_correct ? "feedback-correct" : "feedback-neutral"}>
                  {a.is_correct ? "Correct" : "Incorrect"}
                </td>
                <td>{a.difficulty_label ?? "-"}</td>
                <td>{new Date(a.answered_at).toLocaleString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </section>

      <div className="detail-actions">
        <Link to={`/quick-practice/${detail.course_id}/${detail.chapter_id}`} className="cta-button">
          Practice this chapter
        </Link>
        <Link to={`/practice/${detail.course_id}/${detail.chapter_id}`} className="cta-button-secondary">
          Or take a timed chapter test
        </Link>
      </div>
    </div>
  );
}
