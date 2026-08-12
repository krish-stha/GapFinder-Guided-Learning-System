import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { Trophy, AlertTriangle, Brain, CheckCircle2, Circle, ArrowRight, Info } from "lucide-react";
import { practiceApi } from "../api/practice";
import { ApiError } from "../api/client";
import AnimatedNumber from "../components/AnimatedNumber";
import TakeDiagnosticPrompt from "../components/TakeDiagnosticPrompt";
import { MasteryBar, pctColorClass } from "../components/MasteryMiniCard";
import { TableSkeleton } from "../components/Skeletons";
import type { BeforeAfter, Progress } from "../types";

interface Paired {
  chapter_id: number;
  chapter_name: string;
  before: number;
  after: number;
  deltaPct: number;
}

function pairUp(rows: BeforeAfter[]): Paired[] {
  return rows
    .filter((b): b is BeforeAfter & { mastery_before: number; mastery_after: number } => b.mastery_before !== null && b.mastery_after !== null)
    .map((b) => ({
      chapter_id: b.chapter_id,
      chapter_name: b.chapter_name,
      before: b.mastery_before,
      after: b.mastery_after,
      deltaPct: Math.round((b.mastery_after - b.mastery_before) * 100),
    }));
}

function HighlightCard({ item, kind }: { item: Paired; kind: "up" | "down" }) {
  return (
    <div className={`progress-highlight-card progress-highlight-${kind}`}>
      <h4>{item.chapter_name}</h4>
      <p className="progress-highlight-change">
        {Math.round(item.before * 100)}% <ArrowRight size={13} strokeWidth={2.5} /> {Math.round(item.after * 100)}%
      </p>
      <span className={`progress-highlight-delta progress-highlight-delta-${kind}`}>
        {item.deltaPct > 0 ? "+" : ""}
        {item.deltaPct}%
      </span>
      {kind === "down" && (
        <Link to={`/chapter/${item.chapter_id}`} className="cta-button-secondary progress-highlight-cta">
          Practice this chapter →
        </Link>
      )}
    </div>
  );
}

function BeforeAfterRow({ row }: { row: BeforeAfter }) {
  const before = row.mastery_before;
  const after = row.mastery_after;
  const deltaPct = before !== null && after !== null ? Math.round((after - before) * 100) : null;
  return (
    <div className="before-after-row">
      <span className="before-after-chapter">{row.chapter_name}</span>
      <div className="before-after-bars">
        <span className="before-after-pct">{before !== null ? `${Math.round(before * 100)}%` : "—"}</span>
        {before !== null && <MasteryBar pct={Math.round(before * 100)} colorClass="band-insufficient" />}
        <ArrowRight size={13} strokeWidth={2.5} className="before-after-arrow" />
        <span className="before-after-pct">{after !== null ? `${Math.round(after * 100)}%` : "—"}</span>
        {after !== null && <MasteryBar pct={Math.round(after * 100)} colorClass={pctColorClass(after)} />}
      </div>
      <span
        className={
          deltaPct === null ? "before-after-delta" : deltaPct > 0 ? "before-after-delta up" : deltaPct < 0 ? "before-after-delta down" : "before-after-delta"
        }
      >
        {deltaPct !== null ? `${deltaPct > 0 ? "+" : ""}${deltaPct}%` : "—"}
      </span>
    </div>
  );
}

export default function ProgressPage() {
  const [data, setData] = useState<Progress | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [showMastered, setShowMastered] = useState(false);
  const [showImproved, setShowImproved] = useState(false);
  const [showInfo, setShowInfo] = useState(false);

  useEffect(() => {
    practiceApi
      .progressMe()
      .then(setData)
      .catch((err) => setError(err instanceof ApiError ? err.message : "Could not load your progress."));
  }, []);

  if (error) return <p className="page-error">{error}</p>;
  if (data === null)
    return (
      <div className="progress-page">
        <h1>Progress & Improvement</h1>
        <TableSkeleton />
      </div>
    );

  if (data.chapters_total_tracked === 0) {
    return (
      <div className="empty-state">
        <h1>Progress & Improvement</h1>
        <p>Practice a few chapters first to start tracking your progress.</p>
        <Link to="/chapters" className="cta-button">
          Start practising
        </Link>
      </div>
    );
  }

  const paired = pairUp(data.before_after);
  const improved = paired.filter((p) => p.deltaPct > 0);
  const declined = paired.filter((p) => p.deltaPct < 0);
  const avgBefore = paired.length ? paired.reduce((sum, p) => sum + p.before, 0) / paired.length : null;
  const avgAfter = paired.length ? paired.reduce((sum, p) => sum + p.after, 0) / paired.length : null;
  const overallGrowthPct = avgBefore !== null && avgAfter !== null ? Math.round((avgAfter - avgBefore) * 100) : null;

  const biggestImprovements = [...improved].sort((a, b) => b.deltaPct - a.deltaPct).slice(0, 2);
  const needsReinforcement = [...declined]
    .filter((p) => p.deltaPct <= -5)
    .sort((a, b) => a.deltaPct - b.deltaPct)
    .slice(0, 2);

  const milestones = [
    { label: "Diagnostic completed", done: data.before_after.length > 0, hint: null as string | null },
    {
      label: "5 chapters improved",
      done: improved.length >= 5,
      hint: improved.length < 5 ? `${5 - improved.length} more chapter${5 - improved.length === 1 ? "" : "s"} improved` : null,
    },
    {
      label: "10 chapters mastered",
      done: data.chapters_completed >= 10,
      hint: data.chapters_completed < 10 ? `${10 - data.chapters_completed} more chapter${10 - data.chapters_completed === 1 ? "" : "s"} mastered` : null,
    },
    {
      label: "60% overall mastery",
      done: avgAfter !== null && avgAfter >= 0.6,
      hint: avgAfter !== null && avgAfter < 0.6 ? `${Math.round((0.6 - avgAfter) * 100)}% more mastery` : null,
    },
    {
      label: "7-day streak",
      done: data.streak_days >= 7,
      hint: data.streak_days < 7 ? `${7 - data.streak_days} more day${7 - data.streak_days === 1 ? "" : "s"} streak` : null,
    },
  ];
  const nextMilestone = milestones.find((m) => !m.done) ?? null;

  const topImprovement = biggestImprovements[0];
  const worstDecline = needsReinforcement[0];
  const insightText =
    paired.length > 0
      ? `You've improved in ${improved.length} of your ${paired.length} practiced chapters since your diagnostic.` +
        (topImprovement ? ` Your biggest improvement is ${topImprovement.chapter_name} (+${topImprovement.deltaPct}%).` : "") +
        (worstDecline ? ` However, ${worstDecline.chapter_name} has declined by ${Math.abs(worstDecline.deltaPct)}% and may need reinforcement.` : "")
      : null;

  return (
    <div className="progress-page">
      <header className="chapter-analysis-header">
        <div>
          <h1>Progress & Improvement</h1>
          <p className="dashboard-subtitle">Track how your learning has changed since your diagnostic.</p>
        </div>
        <button type="button" className="chapter-analysis-info-btn" onClick={() => setShowInfo((v) => !v)}>
          <Info size={14} strokeWidth={2} /> How is this calculated?
        </button>
      </header>

      {showInfo && (
        <div className="chapter-analysis-info-panel">
          <p>
            <strong>Overall growth</strong> compares your average mastery across chapters at your diagnostic vs. now.{" "}
            <strong>Mastery</strong> isn't raw accuracy - it blends difficulty-adjusted accuracy with a recency-weighted
            score, so recent attempts and harder questions count more. A chapter is <strong>mastered</strong> at
            ≥70% mastery with enough attempts to trust the number, and <strong>improved</strong> when mastery now is
            higher than at your diagnostic.
          </p>
        </div>
      )}

      <div className="dashboard-stat-tiles">
        <div className="stat-tile">
          <span className={`stat-tile-value ${overallGrowthPct !== null && overallGrowthPct < 0 ? "stat-tile-warning" : "stat-tile-positive"}`}>
            {overallGrowthPct !== null ? `${overallGrowthPct > 0 ? "+" : ""}${overallGrowthPct}%` : "—"}
          </span>
          <span className="stat-tile-label">Overall growth</span>
        </div>
        <button
          type="button"
          className={`stat-tile stat-tile-link${data.chapters_completed === 0 ? " stat-tile-disabled" : ""}`}
          onClick={() => data.chapters_completed > 0 && setShowMastered((v) => !v)}
        >
          <span className="stat-tile-value">
            <AnimatedNumber value={data.chapters_completed} />
          </span>
          <span className="stat-tile-label">Chapters mastered{data.chapters_completed > 0 ? (showMastered ? " ▲" : " ▼") : ""}</span>
        </button>
        <button
          type="button"
          className={`stat-tile stat-tile-link${improved.length === 0 ? " stat-tile-disabled" : ""}`}
          onClick={() => improved.length > 0 && setShowImproved((v) => !v)}
        >
          <span className="stat-tile-value">
            <AnimatedNumber value={improved.length} />
          </span>
          <span className="stat-tile-label">Chapters improved{improved.length > 0 ? (showImproved ? " ▲" : " ▼") : ""}</span>
        </button>
        <div className="stat-tile">
          <span className="stat-tile-value">🔥 {data.streak_days}</span>
          <span className="stat-tile-label">Day streak</span>
        </div>
      </div>
      <p className="progress-tracked-note">
        {data.chapters_total_tracked} chapters tracked total - see the full breakdown in{" "}
        <Link to="/chapter-analysis">Chapter Analysis</Link>.
      </p>

      {showImproved && improved.length > 0 && (
        <section className="mastered-chapters-panel">
          <p className="distribution-heading">Improved = your mastery is higher now than it was at your diagnostic</p>
          <div className="before-after-list">
            {improved
              .slice()
              .sort((a, b) => b.deltaPct - a.deltaPct)
              .map((p) => (
                <div className="before-after-row" key={p.chapter_id}>
                  <span className="before-after-chapter">{p.chapter_name}</span>
                  <span className="before-after-pct">{Math.round(p.before * 100)}%</span>
                  <ArrowRight size={13} strokeWidth={2.5} className="before-after-arrow" />
                  <span className="before-after-pct">{Math.round(p.after * 100)}%</span>
                  <span className="before-after-delta up">+{p.deltaPct}%</span>
                </div>
              ))}
          </div>
        </section>
      )}

      {showMastered && data.mastered_chapters.length > 0 && (
        <section className="mastered-chapters-panel">
          <p className="distribution-heading">
            Mastered = mastery ≥ 70%, with enough attempts to trust the estimate
          </p>
          <div className="before-after-list">
            {data.mastered_chapters.map((m) => (
              <div className="before-after-row" key={m.chapter_id}>
                <span className="before-after-chapter">{m.chapter_name}</span>
                <MasteryBar pct={Math.round(m.mastery_estimate * 100)} colorClass={pctColorClass(m.mastery_estimate)} />
                <span className="before-after-pct">{Math.round(m.mastery_estimate * 100)}%</span>
                <span className="mastered-chapter-meta">
                  {m.n_attempts} attempt{m.n_attempts === 1 ? "" : "s"} &middot; {Math.round(m.confidence * 100)}% confidence
                </span>
              </div>
            ))}
          </div>
        </section>
      )}

      {avgBefore !== null && avgAfter !== null && (
        <section className="progress-hero">
          <p className="distribution-heading">Your overall improvement</p>
          <div className="progress-hero-bars">
            <div className="progress-hero-col">
              <span className="progress-hero-label">Diagnostic</span>
              <span className="progress-hero-pct">{Math.round(avgBefore * 100)}%</span>
              <MasteryBar pct={Math.round(avgBefore * 100)} colorClass="band-insufficient" />
            </div>
            <ArrowRight size={22} strokeWidth={2.5} className="progress-hero-arrow" />
            <div className="progress-hero-col">
              <span className="progress-hero-label">Now</span>
              <span className="progress-hero-pct">{Math.round(avgAfter * 100)}%</span>
              <MasteryBar pct={Math.round(avgAfter * 100)} colorClass={pctColorClass(avgAfter)} />
            </div>
          </div>
          {overallGrowthPct !== null && (
            <span className={`progress-hero-delta ${overallGrowthPct >= 0 ? "up" : "down"}`}>
              {overallGrowthPct > 0 ? "+" : ""}
              {overallGrowthPct}%
            </span>
          )}
        </section>
      )}

      {(biggestImprovements.length > 0 || needsReinforcement.length > 0) && (
        <div className="progress-highlights-grid">
          {biggestImprovements.length > 0 && (
            <section>
              <p className="distribution-heading">
                <Trophy size={14} strokeWidth={2.5} style={{ display: "inline", marginRight: 6, verticalAlign: -2 }} />
                Biggest improvements
              </p>
              <div className="progress-highlight-list">
                {biggestImprovements.map((item) => (
                  <HighlightCard key={item.chapter_id} item={item} kind="up" />
                ))}
              </div>
            </section>
          )}
          {needsReinforcement.length > 0 && (
            <section>
              <p className="distribution-heading">
                <AlertTriangle size={14} strokeWidth={2.5} style={{ display: "inline", marginRight: 6, verticalAlign: -2 }} />
                Needs reinforcement
              </p>
              <div className="progress-highlight-list">
                {needsReinforcement.map((item) => (
                  <HighlightCard key={item.chapter_id} item={item} kind="down" />
                ))}
              </div>
            </section>
          )}
        </div>
      )}

      <section className="detail-section">
        <h2>Before vs. after</h2>
        <p className="dashboard-subtitle">Since your diagnostic test - not your overall chapter mastery.</p>
        {data.before_after.length === 0 ? (
          <div>
            <p className="page-loading">
              Take a diagnostic assessment to unlock a before/after comparison as you keep practising.
            </p>
            <TakeDiagnosticPrompt />
          </div>
        ) : (
          <div className="before-after-list">
            {data.before_after.map((ba) => (
              <BeforeAfterRow key={ba.chapter_id} row={ba} />
            ))}
          </div>
        )}
      </section>

      {insightText && (
        <section className="progress-insight">
          <p className="distribution-heading">
            <Brain size={14} strokeWidth={2.5} style={{ display: "inline", marginRight: 6, verticalAlign: -2 }} />
            GapFinder Progress Insight
          </p>
          <p>{insightText}</p>
          {worstDecline && (
            <Link to={`/chapter/${worstDecline.chapter_id}`} className="cta-button-secondary">
              Work on {worstDecline.chapter_name} →
            </Link>
          )}
        </section>
      )}

      <section className="detail-section">
        <h2>Milestones</h2>
        <ul className="milestones-list">
          {milestones.map((m) => (
            <li key={m.label} className={m.done ? "milestone-done" : "milestone-pending"}>
              {m.done ? <CheckCircle2 size={16} strokeWidth={2} /> : <Circle size={16} strokeWidth={2} />}
              <span>{m.label}</span>
            </li>
          ))}
        </ul>
        {nextMilestone?.hint && <p className="milestones-next-hint">{nextMilestone.hint} to reach your next milestone.</p>}
      </section>
    </div>
  );
}
