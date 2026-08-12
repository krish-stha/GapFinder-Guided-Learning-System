import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { teacherApi } from "../api/teacher";
import { ApiError } from "../api/client";
import { TableSkeleton } from "../components/Skeletons";
import type { ChapterWeakness, PriorityBand, SchoolClass, StudentSummary, TeacherDashboardSummary } from "../types";

const BAND_ORDER: PriorityBand[] = ["High", "Medium", "Low", "Insufficient evidence"];
const BAND_CLASS: Record<PriorityBand, string> = {
  High: "band-high",
  Medium: "band-medium",
  Low: "band-low",
  "Insufficient evidence": "band-insufficient",
};

function buildInsight(summary: TeacherDashboardSummary): string {
  if (summary.total_students === 0) return "No students have registered yet.";
  const totalRows = BAND_ORDER.reduce((sum, b) => sum + (summary.band_distribution[b] ?? 0), 0);
  if (totalRows === 0) {
    return `${summary.total_students} student(s) registered, but none have recorded a practice attempt yet.`;
  }
  const pctHigh = Math.round(((summary.band_distribution.High ?? 0) / totalRows) * 100);
  const parts = [
    `${summary.total_students} student${summary.total_students === 1 ? "" : "s"} tracked across ${summary.total_chapters_tracked} chapter(s)`,
  ];
  if (summary.avg_mastery !== null) parts.push(`, averaging ${Math.round(summary.avg_mastery * 100)}% mastery`);
  parts.push(".");
  if (pctHigh > 0) parts.push(` ${pctHigh}% of tracked chapter-evidence is High priority.`);
  if (summary.alerts.length > 0) {
    parts.push(
      ` ${summary.alerts.length} student${summary.alerts.length === 1 ? " has" : "s have"} a High-priority chapter that's been significantly declining - see Alerts below.`,
    );
  }
  return parts.join("");
}

// Same 0.7 "mastered" cutoff Progress & Improvement already uses for its
// chapters_completed count - reusing it here keeps "needs support"
// meaning the same thing everywhere in the app, not a second private
// threshold. Below 0.5 gets the stronger High-band styling so the
// weakest students are unmistakable, not just faintly different.
function masteryStatus(avgMastery: number | null): { label: string; band: "High" | "Medium" } | null {
  if (avgMastery === null) return null;
  if (avgMastery < 0.5) return { label: "Needs support", band: "High" };
  if (avgMastery < 0.7) return { label: "Needs practice", band: "Medium" };
  return null;
}

function BandDistributionBar({ distribution }: { distribution: Record<string, number> }) {
  const total = BAND_ORDER.reduce((sum, b) => sum + (distribution[b] ?? 0), 0);
  if (total === 0) return null;
  return (
    <div className="band-dist">
      <div className="band-dist-bar">
        {BAND_ORDER.map((band) => {
          const count = distribution[band] ?? 0;
          if (count === 0) return null;
          return (
            <div
              key={band}
              className={`band-dist-segment ${BAND_CLASS[band]}`}
              style={{ flex: count }}
              title={`${band}: ${count} (${Math.round((count / total) * 100)}%)`}
            />
          );
        })}
      </div>
      <div className="band-dist-legend">
        {BAND_ORDER.map((band) => (
          <span key={band} className="band-dist-legend-item">
            <i className={`legend-dot ${BAND_CLASS[band]}`} />
            {band} ({distribution[band] ?? 0})
          </span>
        ))}
      </div>
    </div>
  );
}

export default function TeacherDashboardPage() {
  const [classes, setClasses] = useState<SchoolClass[]>([]);
  const [classId, setClassId] = useState<number | null>(null);
  const [chapters, setChapters] = useState<ChapterWeakness[] | null>(null);
  const [roster, setRoster] = useState<StudentSummary[] | null>(null);
  const [summary, setSummary] = useState<TeacherDashboardSummary | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    teacherApi.listClasses().then(setClasses).catch(() => undefined);
  }, []);

  useEffect(() => {
    setChapters(null);
    setRoster(null);
    setSummary(null);
    Promise.all([
      teacherApi.chaptersFailing(classId),
      teacherApi.studentsOverview(classId),
      teacherApi.dashboardSummary(classId),
    ])
      .then(([c, r, sum]) => {
        setChapters(c);
        setRoster(r);
        setSummary(sum);
      })
      .catch((err) => setError(err instanceof ApiError ? err.message : "Could not load class overview."));
  }, [classId]);

  if (error) return <p className="page-error">{error}</p>;

  const classFilter = classes.length > 0 && (
    <label className="heatmap-course-filter">
      Class
      <select value={classId ?? ""} onChange={(e) => setClassId(e.target.value ? Number(e.target.value) : null)}>
        <option value="">All classes</option>
        {classes.map((c) => (
          <option key={c.id} value={c.id}>{c.name}</option>
        ))}
      </select>
    </label>
  );

  if (chapters === null || roster === null || summary === null)
    return (
      <div className="teacher-page">
        <h1>Class overview</h1>
        {classFilter}
        <p className="dashboard-subtitle">
          {classId ? "Computed from this class's recorded practice attempts." : "Computed from every student's recorded practice attempts, system-wide."}
        </p>
        <section className="teacher-section">
          <h2>All students</h2>
          <TableSkeleton />
        </section>
        <section className="teacher-section">
          <h2>Chapters the class is failing</h2>
          <TableSkeleton />
        </section>
      </div>
    );

  return (
    <div className="teacher-page">
      <h1>Class overview</h1>
      {classFilter}
      <p className="dashboard-insight">{buildInsight(summary)}</p>

      <div className="dashboard-stat-tiles">
        <a href="#all-students" className="stat-tile stat-tile-link">
          <span className="stat-tile-value">{summary.total_students}</span>
          <span className="stat-tile-label">Students → see all</span>
        </a>
        <a href="#chapters-failing" className="stat-tile stat-tile-link">
          <span className="stat-tile-value">{summary.total_chapters_tracked}</span>
          <span className="stat-tile-label">Chapters tracked</span>
        </a>
        <a
          href="#alerts"
          className={`stat-tile stat-tile-link${summary.alerts.length === 0 ? " stat-tile-disabled" : ""}`}
          onClick={(e) => summary.alerts.length === 0 && e.preventDefault()}
        >
          <span className="stat-tile-value stat-tile-warning">{summary.alerts.length}</span>
          <span className="stat-tile-label">Alerts (declining)</span>
        </a>
      </div>

      <section className="teacher-section">
        <h2>Chapter evidence, by priority band</h2>
        <p className="dashboard-subtitle">
          Every (student × chapter) pair with recorded attempts, cohort-wide - this is the fastest read on how the
          class is doing overall.
        </p>
        <BandDistributionBar distribution={summary.band_distribution} />
      </section>

      <section id="all-students" className="teacher-section">
        <h2>All students</h2>
        <p className="dashboard-subtitle">
          {classId ? "Every student in this class, weakest mastery first." : "Every registered student, weakest mastery first."}
        </p>
        {roster.length === 0 ? (
          <p className="page-loading">No students have registered yet.</p>
        ) : (
          <table className="teacher-table">
            <thead>
              <tr>
                <th>Student</th>
                <th>Grade / Stream</th>
                <th>Chapters tracked</th>
                <th>Avg. mastery</th>
                <th>High</th>
                <th>Medium</th>
                <th>Low</th>
                <th>Weakest chapter</th>
              </tr>
            </thead>
            <tbody>
              {roster.map((s) => {
                const status = masteryStatus(s.avg_mastery);
                return (
                  <tr key={s.student_id} className={status ? `roster-row-${BAND_CLASS[status.band]}` : undefined}>
                    <td>
                      <Link to={`/teacher/students/${s.student_id}`}>{s.student_name}</Link>
                      {status && <span className={`band-badge ${BAND_CLASS[status.band]} roster-status-badge`}>{status.label}</span>}
                    </td>
                    <td>{s.grade ? `Grade ${s.grade}` : "-"}{s.stream ? ` · ${s.stream}` : ""}</td>
                    {s.has_activity ? (
                      <>
                        <td>{s.n_chapters_tracked}</td>
                        <td>
                          {s.avg_mastery !== null ? (
                            <>
                              <span className="mastery-inline-bar">
                                <span
                                  className="mastery-inline-fill"
                                  style={{ width: `${Math.round(s.avg_mastery * 100)}%` }}
                                />
                              </span>
                              {Math.round(s.avg_mastery * 100)}%
                            </>
                          ) : (
                            "Not enough evidence yet"
                          )}
                        </td>
                        <td className={s.n_high > 0 ? "cell-warning" : undefined}>{s.n_high}</td>
                        <td>{s.n_medium}</td>
                        <td>{s.n_low}</td>
                        <td>{s.weakest_chapter_name ?? "-"}</td>
                      </>
                    ) : (
                      <td colSpan={5} className="dashboard-subtitle">
                        No recorded practice attempts yet.
                      </td>
                    )}
                  </tr>
                );
              })}
            </tbody>
          </table>
        )}
      </section>

      {(Object.keys(summary.grade_distribution).length > 0 || Object.keys(summary.stream_distribution).length > 0) && (
        <section className="teacher-section">
          <h2>Student distribution</h2>
          <div className="distribution-row">
            <div>
              <h3 className="distribution-heading">By grade</h3>
              {Object.entries(summary.grade_distribution).map(([k, v]) => (
                <p key={k} className="distribution-line">{k}: {v}</p>
              ))}
            </div>
            <div>
              <h3 className="distribution-heading">By stream</h3>
              {Object.entries(summary.stream_distribution).map(([k, v]) => (
                <p key={k} className="distribution-line">{k}: {v}</p>
              ))}
            </div>
          </div>
        </section>
      )}

      {summary.alerts.length > 0 && (
        <section id="alerts" className="teacher-section">
          <h2>Alerts</h2>
          <p className="dashboard-subtitle">Students with a High-priority chapter that's been significantly declining.</p>
          <table className="teacher-table">
            <thead>
              <tr>
                <th>Student</th>
                <th>High priority</th>
                <th>Weakest chapter</th>
              </tr>
            </thead>
            <tbody>
              {summary.alerts.map((a) => (
                <tr key={a.student_id}>
                  <td>
                    <Link to={`/teacher/students/${a.student_id}`}>{a.student_name}</Link>
                  </td>
                  <td className="cell-warning">{a.n_high_priority_chapters}</td>
                  <td>{a.weakest_chapter_name}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>
      )}

      <section id="chapters-failing" className="teacher-section">
        <h2>Chapters the class is failing</h2>
        {chapters.length === 0 ? (
          <p className="page-loading">No chapter has enough recorded attempts yet.</p>
        ) : (
          <table className="teacher-table">
            <thead>
              <tr>
                <th>Chapter</th>
                <th>Students tracked</th>
                <th>High priority</th>
                <th>Avg. mastery</th>
              </tr>
            </thead>
            <tbody>
              {chapters.map((c) => (
                <tr key={c.chapter_id}>
                  <td>
                    <Link to={`/teacher/chapters/${c.chapter_id}`}>{c.chapter_name}</Link>
                  </td>
                  <td>{c.n_students}</td>
                  <td className={c.n_students_high_priority > 0 ? "cell-warning" : undefined}>
                    {c.n_students_high_priority}
                  </td>
                  <td>
                    <span className="mastery-inline-bar">
                      <span className="mastery-inline-fill" style={{ width: `${Math.round(c.avg_mastery * 100)}%` }} />
                    </span>
                    {Math.round(c.avg_mastery * 100)}%
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </section>
    </div>
  );
}
