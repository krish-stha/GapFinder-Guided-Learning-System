import { useEffect, useMemo, useState } from "react";
import { Link, useSearchParams } from "react-router-dom";
import { Info, Search, TrendingUp, TrendingDown } from "lucide-react";
import { practiceApi } from "../api/practice";
import { contentApi } from "../api/content";
import { ApiError } from "../api/client";
import { useAuth } from "../context/AuthContext";
import { matchCourseForStudent } from "../components/CoursePicker";
import { TableSkeleton } from "../components/Skeletons";
import { MasteryBar, pctColorClass } from "../components/MasteryMiniCard";
import { subjectMapFromSections } from "../utils/tree";
import { chapterStatusFor, CHAPTER_STATUS_CLASS, type ChapterStatus } from "../utils/chapterStatus";
import type { LearningPathStep } from "../types";

const STATUS_ORDER: ChapterStatus[] = ["Needs Attention", "Developing", "Strong", "Not Assessed"];

type SortPresetKey =
  | "default"
  | "lowest_mastery"
  | "lowest_accuracy"
  | "highest_priority"
  | "most_improved"
  | "most_attempted"
  | "least_attempted"
  | "name_az";

const SORT_PRESETS: Record<SortPresetKey, { label: string; getValue: (s: LearningPathStep) => number | null; ascending: boolean }> = {
  default: { label: "Priority order (default)", getValue: () => null, ascending: true },
  lowest_mastery: { label: "Lowest mastery", getValue: (s) => s.mastery_estimate, ascending: true },
  lowest_accuracy: { label: "Lowest accuracy", getValue: (s) => s.raw_accuracy, ascending: true },
  highest_priority: { label: "Highest priority", getValue: (s) => s.priority_score, ascending: false },
  most_improved: { label: "Most improved", getValue: (s) => (s.trend_significant ? s.trend_slope : null), ascending: false },
  most_attempted: { label: "Most attempted", getValue: (s) => s.n_attempts ?? 0, ascending: false },
  least_attempted: { label: "Least attempted", getValue: (s) => s.n_attempts ?? 0, ascending: true },
  name_az: { label: "Chapter name (A-Z)", getValue: () => null, ascending: true },
};

// Nulls always sort last regardless of direction - "lowest mastery" should
// never put a never-attempted chapter (no mastery estimate at all) above a
// genuinely low-scoring one, since that would misrepresent absence of
// evidence as the worst possible score.
function sortByPreset(path: LearningPathStep[], preset: SortPresetKey): LearningPathStep[] {
  if (preset === "name_az") return [...path].sort((a, b) => a.chapter_name.localeCompare(b.chapter_name));
  const { getValue, ascending } = SORT_PRESETS[preset];
  return [...path].sort((a, b) => {
    const va = getValue(a);
    const vb = getValue(b);
    if (va === null && vb === null) return 0;
    if (va === null) return 1;
    if (vb === null) return -1;
    return ascending ? va - vb : vb - va;
  });
}

function SummaryCards({ path }: { path: LearningPathStep[] }) {
  const evidenced = path.filter((s) => s.mastery_estimate !== null);
  const avgMasteryPct = evidenced.length
    ? Math.round((evidenced.reduce((sum, s) => sum + s.mastery_estimate!, 0) / evidenced.length) * 100)
    : null;
  const weakCount = path.filter((s) => s.status === "High").length;
  const improvingCount = path.filter((s) => s.trend_significant && (s.trend_slope ?? 0) > 0).length;

  return (
    <div className="dashboard-stat-tiles">
      <div className="stat-tile">
        <span className="stat-tile-value">{path.length}</span>
        <span className="stat-tile-label">Chapters</span>
      </div>
      <div className="stat-tile">
        <span className="stat-tile-value">{avgMasteryPct !== null ? `${avgMasteryPct}%` : "—"}</span>
        <span className="stat-tile-label">Avg Mastery</span>
      </div>
      <div className="stat-tile">
        <span className="stat-tile-value stat-tile-warning">{weakCount}</span>
        <span className="stat-tile-label">Weak</span>
      </div>
      <div className="stat-tile">
        <span className="stat-tile-value stat-tile-positive">{improvingCount}</span>
        <span className="stat-tile-label">Improving</span>
      </div>
    </div>
  );
}

function DistributionBars({ path }: { path: LearningPathStep[] }) {
  const counts = path.reduce(
    (acc, s) => {
      const status = chapterStatusFor(s.status);
      acc[status] = (acc[status] ?? 0) + 1;
      return acc;
    },
    {} as Record<ChapterStatus, number>,
  );
  const max = Math.max(1, ...STATUS_ORDER.map((s) => counts[s] ?? 0));

  return (
    <section className="chapter-distribution">
      <p className="distribution-heading">Your chapter mastery</p>
      <div className="chapter-distribution-rows">
        {STATUS_ORDER.map((status) => {
          const count = counts[status] ?? 0;
          return (
            <div className="chapter-distribution-row" key={status}>
              <span className={`band-badge ${CHAPTER_STATUS_CLASS[status]}`}>{status}</span>
              <div className="chapter-distribution-bar-track">
                <div
                  className={`chapter-distribution-bar-fill ${CHAPTER_STATUS_CLASS[status]}`}
                  style={{ width: `${(count / max) * 100}%` }}
                />
              </div>
              <span className="chapter-distribution-count">{count}</span>
            </div>
          );
        })}
      </div>
    </section>
  );
}

function TrendCell({ step }: { step: LearningPathStep }) {
  if (step.status === "not_started" || step.trend_slope === null) {
    return <span className="trend-cell trend-flat">—</span>;
  }
  if (!step.trend_significant) {
    return <span className="trend-cell trend-flat">→</span>;
  }
  const pct = Math.round(Math.abs(step.trend_slope) * 100);
  const up = step.trend_slope > 0;
  const Icon = up ? TrendingUp : TrendingDown;
  return (
    <span className={`trend-cell ${up ? "trend-up" : "trend-down"}`} title="Change in correctness per recent attempt">
      <Icon size={13} strokeWidth={2.25} /> {pct}%
    </span>
  );
}

function ActionCell({
  step,
  matchedCourseId,
  inMatchedCourseTree,
}: {
  step: LearningPathStep;
  matchedCourseId: number | null;
  inMatchedCourseTree: boolean;
}) {
  const status = chapterStatusFor(step.status);
  if (status === "Strong") {
    return (
      <Link to={`/chapter/${step.chapter_id}`} className="cta-button-secondary chapter-analysis-action">
        View
      </Link>
    );
  }
  const to =
    matchedCourseId !== null && inMatchedCourseTree
      ? `/quick-practice/${matchedCourseId}/${step.chapter_id}`
      : `/chapter/${step.chapter_id}`;
  return (
    <Link to={to} className="cta-button chapter-analysis-action">
      Practice
    </Link>
  );
}

function MasteryInfoPanel() {
  return (
    <div className="chapter-analysis-info-panel">
      <p>
        <strong>Mastery ≠ Accuracy.</strong> Mastery blends difficulty-adjusted accuracy (harder questions count more)
        with a recency-weighted score (recent attempts count more than older ones), and is scaled down when there
        isn't much evidence yet. Two students with the same accuracy can have different mastery scores if one
        answered harder questions, or has been improving more recently.
      </p>
    </div>
  );
}

export default function ChapterAnalysisPage() {
  const { student } = useAuth();
  const [searchParams] = useSearchParams();
  const [path, setPath] = useState<LearningPathStep[] | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [subjectMap, setSubjectMap] = useState<Map<number, string>>(new Map());
  const [matchedCourseId, setMatchedCourseId] = useState<number | null>(null);
  // Pre-selects when arriving from a "View analysis in {subject}" link
  // (e.g. My Performance's strongest-subject card) - falls back to "all"
  // when there's no ?subject= param, same as before.
  const [subjectFilter, setSubjectFilter] = useState(searchParams.get("subject") ?? "all");
  const [statusFilter, setStatusFilter] = useState<"all" | ChapterStatus>("all");
  const [query, setQuery] = useState("");
  const [sortPreset, setSortPreset] = useState<SortPresetKey>("default");
  const [showInfo, setShowInfo] = useState(false);

  useEffect(() => {
    practiceApi
      .learningPath()
      .then(setPath)
      .catch((err) => setError(err instanceof ApiError ? err.message : "Could not load chapter analysis."));
  }, []);

  useEffect(() => {
    contentApi
      .listCourses()
      .then((courses) => {
        const matched = matchCourseForStudent(courses, student?.grade ?? null, student?.stream ?? null);
        if (!matched) return;
        setMatchedCourseId(matched.id);
        return contentApi.listSections(matched.id).then((sections) => setSubjectMap(subjectMapFromSections(sections)));
      })
      .catch(() => undefined);
  }, [student]);

  const subjects = useMemo(() => [...new Set(subjectMap.values())].sort(), [subjectMap]);

  const filtered = useMemo(() => {
    if (!path) return [];
    const q = query.trim().toLowerCase();
    return path.filter((s) => {
      if (subjectFilter !== "all" && subjectMap.get(s.chapter_id) !== subjectFilter) return false;
      if (statusFilter !== "all" && chapterStatusFor(s.status) !== statusFilter) return false;
      if (q && !s.chapter_name.toLowerCase().includes(q)) return false;
      return true;
    });
  }, [path, subjectFilter, statusFilter, query, subjectMap]);

  const sorted = useMemo(() => sortByPreset(filtered, sortPreset), [filtered, sortPreset]);

  if (error) return <p className="page-error">{error}</p>;
  if (path === null)
    return (
      <div className="chapter-analysis-page">
        <h1>Chapter Analysis</h1>
        <TableSkeleton />
      </div>
    );

  if (path.length === 0) {
    return (
      <div className="empty-state">
        <h1>Chapter Analysis</h1>
        <p>You haven't practised any chapters yet.</p>
        <Link to="/chapters" className="cta-button">
          Start practising
        </Link>
      </div>
    );
  }

  return (
    <div className="chapter-analysis-page">
      <header className="chapter-analysis-header">
        <div>
          <h1>Chapter Analysis</h1>
          <p className="dashboard-subtitle">See your performance, mastery, and learning confidence across every chapter.</p>
        </div>
        <button type="button" className="chapter-analysis-info-btn" onClick={() => setShowInfo((v) => !v)}>
          <Info size={14} strokeWidth={2} /> How is mastery calculated?
        </button>
      </header>

      {showInfo && <MasteryInfoPanel />}

      <SummaryCards path={path} />
      <DistributionBars path={path} />

      <div className="chapter-analysis-filters">
        <select value={subjectFilter} onChange={(e) => setSubjectFilter(e.target.value)}>
          <option value="all">All Subjects</option>
          {subjects.map((s) => (
            <option key={s} value={s}>
              {s}
            </option>
          ))}
        </select>
        <select value={statusFilter} onChange={(e) => setStatusFilter(e.target.value as "all" | ChapterStatus)}>
          <option value="all">All Status</option>
          {STATUS_ORDER.map((s) => (
            <option key={s} value={s}>
              {s}
            </option>
          ))}
        </select>
        <select value={sortPreset} onChange={(e) => setSortPreset(e.target.value as SortPresetKey)}>
          {(Object.keys(SORT_PRESETS) as SortPresetKey[]).map((key) => (
            <option key={key} value={key}>
              Sort: {SORT_PRESETS[key].label}
            </option>
          ))}
        </select>
        <label className="chapter-drilldown-search">
          <Search size={15} strokeWidth={2} />
          <input type="search" placeholder="Search chapters…" value={query} onChange={(e) => setQuery(e.target.value)} />
        </label>
      </div>

      {sorted.length === 0 ? (
        <p className="page-loading">No chapters match.</p>
      ) : (
        <div className="chapter-analysis-table-wrap">
          <table className="teacher-table chapter-analysis-table">
            <thead>
              <tr>
                <th>Chapter</th>
                <th>Mastery</th>
                <th>Accuracy</th>
                <th>Evidence</th>
                <th>Trend</th>
                <th>Status</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              {sorted.map((s) => {
                const status = chapterStatusFor(s.status);
                const hasEvidence = s.mastery_estimate !== null;
                return (
                  <tr key={s.chapter_id}>
                    <td>
                      <Link to={`/chapter/${s.chapter_id}`} className="chapter-analysis-name">
                        <span className={`band-dot ${CHAPTER_STATUS_CLASS[status]}`} />
                        {s.chapter_name}
                      </Link>
                    </td>
                    <td>
                      {hasEvidence ? (
                        <div className="chapter-analysis-mastery-cell">
                          <span>{Math.round(s.mastery_estimate! * 100)}%</span>
                          <MasteryBar pct={Math.round(s.mastery_estimate! * 100)} colorClass={pctColorClass(s.mastery_estimate!)} />
                        </div>
                      ) : (
                        "—"
                      )}
                    </td>
                    <td>{s.raw_accuracy !== null ? `${Math.round(s.raw_accuracy * 100)}%` : "—"}</td>
                    <td>{s.n_attempts ?? 0} attempts</td>
                    <td>
                      <TrendCell step={s} />
                    </td>
                    <td>
                      <span className={`band-badge ${CHAPTER_STATUS_CLASS[status]}`}>{status}</span>
                    </td>
                    <td>
                      <ActionCell step={s} matchedCourseId={matchedCourseId} inMatchedCourseTree={subjectMap.has(s.chapter_id)} />
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
