import { useEffect, useMemo, useState } from "react";
import { Link } from "react-router-dom";
import { Trophy, AlertTriangle, Lightbulb, TrendingUp, TrendingDown, Info } from "lucide-react";
import { practiceApi } from "../api/practice";
import { contentApi } from "../api/content";
import { ApiError } from "../api/client";
import { useAuth } from "../context/AuthContext";
import { matchCourseForStudent } from "../components/CoursePicker";
import { subjectMapFromSections } from "../utils/tree";
import PerformanceTrendChart from "../components/PerformanceTrendChart";
import { MasteryBar, pctColorClass } from "../components/MasteryMiniCard";
import { TableSkeleton } from "../components/Skeletons";
import type { AccuracyPoint, ChapterEvidence, Performance, SubjectPerformance } from "../types";

const RANGE_OPTIONS: { label: string; days: number | null }[] = [
  { label: "7 Days", days: 7 },
  { label: "30 Days", days: 30 },
  { label: "3 Months", days: 90 },
  { label: "All", days: null },
];

const SUBJECT_LOW_CONFIDENCE_ATTEMPTS = 10;

function weightedAvgMastery(subjects: SubjectPerformance[]): number | null {
  const totalN = subjects.reduce((sum, s) => sum + s.n_attempts, 0);
  if (totalN === 0) return null;
  return subjects.reduce((sum, s) => sum + s.avg_mastery * s.n_attempts, 0) / totalN;
}

function accuracyOf(points: AccuracyPoint[]): number | null {
  if (points.length === 0) return null;
  return Math.round((points.filter((p) => p.is_correct).length / points.length) * 100);
}

// Same "recent window vs the window before it" comparison used on the
// Dashboard, applied here to whichever set of accuracy points is currently
// in view (already range/subject filtered) - null (no delta shown) when
// there isn't a full previous window's worth of history yet, rather than
// comparing against a partial/misleading window.
function periodDelta(points: AccuracyPoint[], rangeDays: number | null): number | null {
  if (rangeDays === null) return null;
  const now = Date.now();
  const currentStart = now - rangeDays * 86_400_000;
  const previousStart = now - rangeDays * 2 * 86_400_000;
  const current = points.filter((p) => new Date(p.answered_at).getTime() >= currentStart);
  const previous = points.filter((p) => {
    const t = new Date(p.answered_at).getTime();
    return t >= previousStart && t < currentStart;
  });
  const currentAcc = accuracyOf(current);
  const previousAcc = accuracyOf(previous);
  if (currentAcc === null || previousAcc === null || previous.length < 3) return null;
  return currentAcc - previousAcc;
}

function SubjectSpotlightCard({
  kind,
  subject,
  href,
}: {
  kind: "strongest" | "weakest";
  subject: SubjectPerformance;
  href: string;
}) {
  const isStrongest = kind === "strongest";
  return (
    <Link to={href} className={`subject-spotlight-card ${isStrongest ? "subject-spotlight-strong" : "subject-spotlight-weak"}`}>
      <span className="subject-spotlight-icon">
        {isStrongest ? <Trophy size={16} strokeWidth={2} /> : <AlertTriangle size={16} strokeWidth={2} />}
      </span>
      <span className="subject-spotlight-label">{isStrongest ? "Strongest subject" : "Needs attention"}</span>
      <h3>{subject.subject_name}</h3>
      <p>{Math.round(subject.avg_mastery * 100)}% mastery</p>
      {subject.n_attempts < SUBJECT_LOW_CONFIDENCE_ATTEMPTS && (
        <span className="subject-spotlight-caveat">
          Based on {subject.n_attempts} attempt{subject.n_attempts === 1 ? "" : "s"} so far - early signal, not confirmed yet
        </span>
      )}
      <span className="subject-spotlight-cta">{isStrongest ? "View analysis →" : "See weak areas →"}</span>
    </Link>
  );
}

function GapFinderInsight({
  weakest,
  overallAvg,
  weakChapters,
}: {
  weakest: SubjectPerformance;
  overallAvg: number;
  weakChapters: string[];
}) {
  const gapPct = Math.round((overallAvg - weakest.avg_mastery) * 100);
  return (
    <section className="gapfinder-insight">
      <p className="distribution-heading">
        <Lightbulb size={14} strokeWidth={2.5} style={{ display: "inline", marginRight: 6, verticalAlign: -2 }} />
        GapFinder Insight
      </p>
      <p>
        Your <strong>{weakest.subject_name}</strong> mastery ({Math.round(weakest.avg_mastery * 100)}%) is {gapPct}% below
        your overall average ({Math.round(overallAvg * 100)}%).
        {weakChapters.length > 0 && ` We recommend focusing on ${weakChapters.join(" and ")}.`}
        {weakest.n_attempts < SUBJECT_LOW_CONFIDENCE_ATTEMPTS &&
          ` This is based on only ${weakest.n_attempts} attempt${weakest.n_attempts === 1 ? "" : "s"} so far, so treat it as an early signal rather than a confirmed weak spot.`}
      </p>
      <Link to={`/weak-areas?subject=${encodeURIComponent(weakest.subject_name)}`} className="cta-button-secondary">
        Work on {weakest.subject_name} →
      </Link>
    </section>
  );
}

export default function PerformancePage() {
  const { student } = useAuth();
  const [data, setData] = useState<Performance | null>(null);
  const [evidence, setEvidence] = useState<ChapterEvidence[]>([]);
  const [subjectMap, setSubjectMap] = useState<Map<number, string>>(new Map());
  const [error, setError] = useState<string | null>(null);
  const [rangeDays, setRangeDays] = useState<number | null>(30);
  const [subjectFilter, setSubjectFilter] = useState("all");
  const [showAllSessions, setShowAllSessions] = useState(false);
  const [showInfo, setShowInfo] = useState(false);

  useEffect(() => {
    practiceApi
      .performanceMe()
      .then(setData)
      .catch((err) => setError(err instanceof ApiError ? err.message : "Could not load your performance."));
    practiceApi.resultsMe().then(setEvidence).catch(() => undefined);
  }, []);

  useEffect(() => {
    contentApi
      .listCourses()
      .then((courses) => {
        const matched = matchCourseForStudent(courses, student?.grade ?? null, student?.stream ?? null);
        if (!matched) return;
        return contentApi.listSections(matched.id).then((sections) => setSubjectMap(subjectMapFromSections(sections)));
      })
      .catch(() => undefined);
  }, [student]);

  const subjects = useMemo(() => [...new Set(subjectMap.values())].sort(), [subjectMap]);

  const rangeFiltered = useMemo(() => {
    if (!data) return [];
    if (rangeDays === null) return data.accuracy_trend;
    const cutoff = Date.now() - rangeDays * 86_400_000;
    return data.accuracy_trend.filter((p) => new Date(p.answered_at).getTime() >= cutoff);
  }, [data, rangeDays]);

  const filteredTrend = useMemo(() => {
    if (subjectFilter === "all") return rangeFiltered;
    return rangeFiltered.filter((p) => subjectMap.get(p.chapter_id) === subjectFilter);
  }, [rangeFiltered, subjectFilter, subjectMap]);

  const subjectScopedTrend = useMemo(() => {
    if (!data) return [];
    if (subjectFilter === "all") return data.accuracy_trend;
    return data.accuracy_trend.filter((p) => subjectMap.get(p.chapter_id) === subjectFilter);
  }, [data, subjectFilter, subjectMap]);

  const currentAccuracy = accuracyOf(filteredTrend);
  const delta = periodDelta(subjectScopedTrend, rangeDays);

  const sortedSubjects = useMemo(
    () => (data ? [...data.subject_breakdown].sort((a, b) => b.avg_mastery - a.avg_mastery) : []),
    [data],
  );
  const strongest = sortedSubjects[0] ?? null;
  const weakest = sortedSubjects.length > 1 ? sortedSubjects[sortedSubjects.length - 1] : null;
  const overallAvgMastery = weightedAvgMastery(sortedSubjects);

  const insightWeakChapters = useMemo(() => {
    if (!weakest) return [];
    return evidence
      .filter((e) => subjectMap.get(e.chapter_id) === weakest.subject_name && (e.priority_band === "High" || e.priority_band === "Medium"))
      .sort((a, b) => b.priority_score - a.priority_score)
      .slice(0, 2)
      .map((e) => e.chapter_name);
  }, [evidence, weakest, subjectMap]);

  if (error) return <p className="page-error">{error}</p>;
  if (data === null)
    return (
      <div className="performance-page">
        <h1>My Performance</h1>
        <TableSkeleton />
      </div>
    );

  if (data.accuracy_trend.length === 0) {
    return (
      <div className="empty-state">
        <h1>My Performance</h1>
        <p>You haven't answered any scored questions yet.</p>
        <Link to="/chapters" className="cta-button">
          Start practising
        </Link>
      </div>
    );
  }

  const overallAccuracy = accuracyOf(data.accuracy_trend);
  const completedSessions = data.session_history.filter((s) => s.completed_at !== null);
  const recentWindow = completedSessions.slice(0, 5);
  const priorWindow = completedSessions.slice(5, 10);
  const recentSessionAvg = recentWindow.length
    ? Math.round(recentWindow.reduce((sum, s) => sum + (s.percentage ?? 0), 0) / recentWindow.length)
    : null;
  const priorSessionAvg =
    priorWindow.length >= 3 ? Math.round(priorWindow.reduce((sum, s) => sum + (s.percentage ?? 0), 0) / priorWindow.length) : null;
  const improvementDelta = recentSessionAvg !== null && priorSessionAvg !== null ? recentSessionAvg - priorSessionAvg : null;

  const visibleSessions = showAllSessions ? completedSessions : completedSessions.slice(0, 5);
  const insightGapMeaningful =
    weakest !== null && overallAvgMastery !== null && Math.round((overallAvgMastery - weakest.avg_mastery) * 100) >= 5;

  return (
    <div className="performance-page">
      <header className="chapter-analysis-header">
        <div>
          <h1>My Performance</h1>
          <p className="dashboard-subtitle">See how your learning is progressing across subjects and practice.</p>
        </div>
        <button type="button" className="chapter-analysis-info-btn" onClick={() => setShowInfo((v) => !v)}>
          <Info size={14} strokeWidth={2} /> Accuracy vs. mastery?
        </button>
      </header>

      {showInfo && (
        <div className="chapter-analysis-info-panel">
          <p>
            <strong>Accuracy</strong> is simply correct ÷ total questions. <strong>Mastery</strong> is a different,
            adjusted estimate - it blends difficulty-adjusted accuracy (harder questions count more) with a
            recency-weighted score (recent attempts count more than older ones). Two students with the same accuracy
            can have different mastery if one answered harder questions or has been improving more recently.
          </p>
        </div>
      )}

      <div className="dashboard-stat-tiles">
        <div className="stat-tile">
          <span className="stat-tile-value">{overallAccuracy !== null ? `${overallAccuracy}%` : "—"}</span>
          <span className="stat-tile-label">Overall Accuracy</span>
        </div>
        <div className="stat-tile">
          <span className="stat-tile-value">{data.accuracy_trend.length}</span>
          <span className="stat-tile-label">Questions Attempted</span>
        </div>
        <div className="stat-tile">
          <span className="stat-tile-value">{overallAvgMastery !== null ? `${Math.round(overallAvgMastery * 100)}%` : "—"}</span>
          <span className="stat-tile-label">Avg Mastery</span>
        </div>
        {improvementDelta !== null && (
          <div className="stat-tile">
            <span className={`stat-tile-value ${improvementDelta >= 0 ? "stat-tile-positive" : "stat-tile-warning"}`}>
              {improvementDelta >= 0 ? "+" : ""}
              {improvementDelta}%
            </span>
            <span className="stat-tile-label">Improvement</span>
          </div>
        )}
      </div>

      <section className="detail-section">
        <div className="performance-trend-header">
          <h2>Performance trend</h2>
          <div className="performance-trend-controls">
            <div className="range-filter">
              {RANGE_OPTIONS.map((opt) => (
                <button
                  key={opt.label}
                  type="button"
                  className={`range-filter-btn${rangeDays === opt.days ? " active" : ""}`}
                  onClick={() => setRangeDays(opt.days)}
                >
                  {opt.label}
                </button>
              ))}
            </div>
            {subjects.length > 0 && (
              <select value={subjectFilter} onChange={(e) => setSubjectFilter(e.target.value)}>
                <option value="all">All Subjects</option>
                {subjects.map((s) => (
                  <option key={s} value={s}>
                    {s}
                  </option>
                ))}
              </select>
            )}
          </div>
        </div>

        {filteredTrend.length === 0 ? (
          <p className="page-loading">No attempts in this range.</p>
        ) : (
          <>
            <PerformanceTrendChart points={filteredTrend} granularity={rangeDays !== null && rangeDays <= 7 ? "day" : "week"} />
            <p className="performance-trend-current">
              Current accuracy: <strong>{currentAccuracy}%</strong>
              {delta !== null && (
                <span className={delta >= 0 ? "stat-tile-delta stat-tile-delta-up" : "stat-tile-delta stat-tile-delta-down"}>
                  {delta >= 0 ? <TrendingUp size={12} strokeWidth={2.5} /> : <TrendingDown size={12} strokeWidth={2.5} />}
                  {delta >= 0 ? "+" : ""}
                  {delta}% vs previous period
                </span>
              )}
            </p>
          </>
        )}
      </section>

      {strongest && weakest && (
        <div className="subject-spotlight-grid">
          <SubjectSpotlightCard kind="strongest" subject={strongest} href={`/chapter-analysis?subject=${encodeURIComponent(strongest.subject_name)}`} />
          <SubjectSpotlightCard kind="weakest" subject={weakest} href={`/weak-areas?subject=${encodeURIComponent(weakest.subject_name)}`} />
        </div>
      )}

      <section className="detail-section">
        <h2>Subject performance</h2>
        {data.subject_breakdown.length === 0 ? (
          <p className="page-loading">Not enough data yet to break this down by subject.</p>
        ) : (
          <div className="subject-performance-list">
            {data.subject_breakdown
              .slice()
              .sort((a, b) => a.avg_mastery - b.avg_mastery)
              .map((s) => {
                const pct = Math.round(s.avg_mastery * 100);
                return (
                  <div className="subject-performance-row" key={s.subject_id}>
                    <span className="subject-performance-name">{s.subject_name}</span>
                    <span className="subject-performance-attempts">{s.n_attempts}</span>
                    <MasteryBar pct={pct} colorClass={pctColorClass(s.avg_mastery)} />
                    <span className="subject-performance-pct">{pct}%</span>
                  </div>
                );
              })}
          </div>
        )}
      </section>

      {weakest && overallAvgMastery !== null && insightGapMeaningful && (
        <GapFinderInsight weakest={weakest} overallAvg={overallAvgMastery} weakChapters={insightWeakChapters} />
      )}

      <section className="detail-section">
        <h2>Recent sessions</h2>
        <table className="teacher-table">
          <thead>
            <tr>
              <th>When</th>
              <th>Type</th>
              <th>Score</th>
              <th>Duration</th>
            </tr>
          </thead>
          <tbody>
            {visibleSessions.map((s) => {
              const durationMin =
                s.completed_at !== null
                  ? Math.max(1, Math.round((new Date(s.completed_at).getTime() - new Date(s.started_at).getTime()) / 60_000))
                  : null;
              return (
                <tr key={s.session_id}>
                  <td>{new Date(s.completed_at!).toLocaleDateString()}</td>
                  <td>{s.purpose}</td>
                  <td>
                    {s.correct_count} / {s.total_questions}
                    {s.percentage !== null && ` (${Math.round(s.percentage)}%)`}
                  </td>
                  <td>{durationMin !== null ? `${durationMin} min` : "—"}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
        {completedSessions.length > 5 && (
          <button type="button" className="cta-button-secondary performance-sessions-toggle" onClick={() => setShowAllSessions((v) => !v)}>
            {showAllSessions ? "Show fewer" : `View all history (${completedSessions.length})`}
          </button>
        )}
      </section>
    </div>
  );
}
