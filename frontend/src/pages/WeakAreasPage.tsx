import { useEffect, useMemo, useState } from "react";
import { Link, useSearchParams } from "react-router-dom";
import { AlertTriangle, ArrowRight } from "lucide-react";
import { practiceApi } from "../api/practice";
import { contentApi } from "../api/content";
import { ApiError } from "../api/client";
import { useAuth } from "../context/AuthContext";
import { matchCourseForStudent } from "../components/CoursePicker";
import { EvidenceListSkeleton } from "../components/Skeletons";
import { BAND_CLASS, MasteryBar, ChapterMiniCard } from "../components/MasteryMiniCard";
import { subjectMapFromSections } from "../utils/tree";
import type { ChapterEvidence } from "../types";

function confidenceLabel(confidence: number): string {
  if (confidence >= 0.7) return "High confidence";
  if (confidence >= 0.4) return "Medium confidence";
  return "Low confidence";
}

function practiceLink(chapterId: number, matchedCourseId: number | null, inMatchedCourse: boolean): string {
  return inMatchedCourse && matchedCourseId !== null
    ? `/quick-practice/${matchedCourseId}/${chapterId}`
    : `/chapter/${chapterId}`;
}

function TopPriorityCard({ evidence, linkTo }: { evidence: ChapterEvidence; linkTo: string }) {
  const bandClass = BAND_CLASS[evidence.priority_band] ?? "band-insufficient";
  const pct = Math.round(evidence.mastery_estimate * 100);
  return (
    <div className={`weak-priority-card ${bandClass}`}>
      <div className="weak-priority-card-header">
        <span className={`band-dot ${bandClass}`} />
        <h3>{evidence.chapter_name}</h3>
        <span className={`band-badge ${bandClass}`}>{evidence.priority_band.toUpperCase()} PRIORITY</span>
      </div>

      <div className="mastery-bar-row">
        <span>Mastery</span>
        <span>{pct}%</span>
      </div>
      <MasteryBar pct={pct} colorClass={bandClass} />

      <p className="weak-priority-meta">
        {evidence.n_attempts} attempts &middot; {Math.round(evidence.raw_accuracy * 100)}% accuracy &middot;{" "}
        {confidenceLabel(evidence.confidence)}
      </p>

      <p className="weak-priority-warning">
        <AlertTriangle size={16} strokeWidth={2} />
        {evidence.explanation}
      </p>

      <Link to={linkTo} className="cta-button">
        Start Recommended Practice <ArrowRight size={16} strokeWidth={2.5} />
      </Link>
    </div>
  );
}

/**
 * Weak Areas: automatically detected weak chapters (High/Medium priority
 * band), a headline summary, a subject filter, and a single spotlighted
 * top-priority chapter above the rest - all derived from ChapterEvidence
 * (results/me), no new backend needed. The subject filter and practice
 * links both reuse the student's matched course's chapter tree (same
 * lookup TakeDiagnosticPrompt uses) rather than adding an endpoint.
 */
export default function WeakAreasPage() {
  const { student } = useAuth();
  const [searchParams] = useSearchParams();
  const [evidence, setEvidence] = useState<ChapterEvidence[] | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [subjectMap, setSubjectMap] = useState<Map<number, string>>(new Map());
  const [matchedCourseId, setMatchedCourseId] = useState<number | null>(null);
  // Pre-selects when arriving from a "See weak areas in {subject}" link
  // (e.g. My Performance's weakest-subject card) - falls back to "all"
  // when there's no ?subject= param, same as before.
  const [subjectFilter, setSubjectFilter] = useState<string>(searchParams.get("subject") ?? "all");

  useEffect(() => {
    practiceApi
      .resultsMe()
      .then(setEvidence)
      .catch((err) => setError(err instanceof ApiError ? err.message : "Could not load weak areas."));
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
    if (evidence === null) return null;
    if (subjectFilter === "all") return evidence;
    return evidence.filter((e) => subjectMap.get(e.chapter_id) === subjectFilter);
  }, [evidence, subjectFilter, subjectMap]);

  if (error) return <p className="page-error">{error}</p>;
  if (evidence === null)
    return (
      <div className="dashboard-page">
        <h1>Weak Areas</h1>
        <EvidenceListSkeleton />
      </div>
    );

  if (evidence.length === 0) {
    return (
      <div className="empty-state">
        <h1>Weak Areas</h1>
        <p>You haven't practised any chapters yet, so there's nothing to flag as weak.</p>
        <Link to="/dashboard" className="cta-button">
          Go to dashboard
        </Link>
      </div>
    );
  }

  const weak = (filtered ?? []).filter((e) => e.priority_band === "High" || e.priority_band === "Medium");
  const highCount = weak.filter((e) => e.priority_band === "High").length;
  const mediumCount = weak.filter((e) => e.priority_band === "Medium").length;
  const improvingCount = weak.filter((e) => e.trend_significant && (e.trend_slope ?? 0) > 0).length;
  const [top, ...others] = weak;

  return (
    <div className="dashboard-page weak-areas-page">
      <header className="weak-areas-header">
        <div>
          <h1>Weak Areas</h1>
          <p className="dashboard-subtitle">Let's identify what needs your attention.</p>
        </div>
        {subjects.length > 0 && (
          <label className="weak-areas-subject-filter">
            Subject
            <select value={subjectFilter} onChange={(e) => setSubjectFilter(e.target.value)}>
              <option value="all">All Subjects</option>
              {subjects.map((s) => (
                <option key={s} value={s}>
                  {s}
                </option>
              ))}
            </select>
          </label>
        )}
      </header>

      <div className="dashboard-stat-tiles">
        <div className="stat-tile">
          <span className="stat-tile-value">{weak.length}</span>
          <span className="stat-tile-label">Weak Chapters</span>
        </div>
        <div className="stat-tile">
          <span className="stat-tile-value stat-tile-warning">{highCount}</span>
          <span className="stat-tile-label">High Priority</span>
        </div>
        <div className="stat-tile">
          <span className="stat-tile-value">{mediumCount}</span>
          <span className="stat-tile-label">Medium Priority</span>
        </div>
        <div className="stat-tile">
          <span className="stat-tile-value stat-tile-positive">{improvingCount}</span>
          <span className="stat-tile-label">Improving</span>
        </div>
      </div>

      {weak.length === 0 ? (
        <p className="page-loading">
          {subjectFilter === "all"
            ? "No chapters are currently flagged High or Medium priority - nice work, or keep practising to build up evidence."
            : `No High or Medium priority chapters in ${subjectFilter}.`}
        </p>
      ) : (
        <>
          {top && (
            <section>
              <p className="distribution-heading">Your top priority</p>
              <TopPriorityCard
                evidence={top}
                linkTo={practiceLink(top.chapter_id, matchedCourseId, subjectMap.has(top.chapter_id))}
              />
            </section>
          )}

          {others.length > 0 && (
            <section>
              <p className="distribution-heading">Other areas to improve</p>
              <div className="weak-areas-grid">
                {others.map((e) => (
                  <ChapterMiniCard
                    key={e.chapter_id}
                    evidence={e}
                    linkTo={practiceLink(e.chapter_id, matchedCourseId, subjectMap.has(e.chapter_id))}
                  />
                ))}
              </div>
            </section>
          )}
        </>
      )}
    </div>
  );
}
