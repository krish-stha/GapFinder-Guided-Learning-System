import { useEffect, useMemo, useState } from "react";
import { teacherApi } from "../api/teacher";
import { contentApi } from "../api/content";
import { ApiError } from "../api/client";
import { TableSkeleton } from "../components/Skeletons";
import type { CohortChapterEvidence, Course, PriorityBand } from "../types";

const BAND_CLASS: Record<PriorityBand, string> = {
  High: "band-high",
  Medium: "band-medium",
  Low: "band-low",
  "Insufficient evidence": "band-insufficient",
};

export default function CohortHeatmapPage() {
  const [courses, setCourses] = useState<Course[]>([]);
  const [courseId, setCourseId] = useState<number | null>(null);
  const [rows, setRows] = useState<CohortChapterEvidence[] | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    contentApi.listCourses().then(setCourses).catch(() => undefined);
  }, []);

  useEffect(() => {
    setRows(null);
    teacherApi
      .cohortEvidence(courseId)
      .then(setRows)
      .catch((err) => setError(err instanceof ApiError ? err.message : "Could not load the heatmap."));
  }, [courseId]);

  const { students, chapters, cellByKey } = useMemo(() => {
    const studentMap = new Map<number, string>();
    const chapterMap = new Map<number, string>();
    const cellByKey = new Map<string, CohortChapterEvidence>();
    for (const r of rows ?? []) {
      studentMap.set(r.student_id, r.student_name);
      chapterMap.set(r.chapter_id, r.chapter_name);
      cellByKey.set(`${r.student_id}:${r.chapter_id}`, r);
    }
    const students = [...studentMap.entries()].sort((a, b) => a[1].localeCompare(b[1]));
    const chapters = [...chapterMap.entries()].sort((a, b) => a[1].localeCompare(b[1]));
    return { students, chapters, cellByKey };
  }, [rows]);

  if (error) return <p className="page-error">{error}</p>;

  return (
    <div className="heatmap-page">
      <h1>Cohort heatmap</h1>
      <p className="dashboard-subtitle">Every student × every chapter they've practised, coloured by priority band.</p>

      <label className="heatmap-course-filter">
        Course
        <select value={courseId ?? ""} onChange={(e) => setCourseId(e.target.value ? Number(e.target.value) : null)}>
          <option value="">All courses</option>
          {courses.map((c) => (
            <option key={c.id} value={c.id}>
              {c.name}
            </option>
          ))}
        </select>
      </label>

      {rows === null ? (
        <TableSkeleton rows={6} cols={5} />
      ) : rows.length === 0 ? (
        <p className="page-loading">
          {courseId ? "No recorded practice attempts yet for this course." : "No recorded practice attempts yet."}
        </p>
      ) : (
        <div className="heatmap-scroll">
          <table className="heatmap-table">
            <thead>
              <tr>
                <th className="heatmap-corner">Student</th>
                {chapters.map(([id, name]) => (
                  <th key={id} className="heatmap-col-header">
                    {name}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {students.map(([sid, sname]) => (
                <tr key={sid}>
                  <th className="heatmap-row-header">{sname}</th>
                  {chapters.map(([cid]) => {
                    const cell = cellByKey.get(`${sid}:${cid}`);
                    if (!cell) return <td key={cid} className="heatmap-cell heatmap-cell-empty" />;
                    return (
                      <td
                        key={cid}
                        className={`heatmap-cell ${BAND_CLASS[cell.priority_band]}`}
                        title={`${cell.priority_band} · ${Math.round(cell.mastery_estimate * 100)}% mastery · ${cell.n_attempts} attempts`}
                      >
                        {cell.priority_band === "Insufficient evidence"
                          ? "–"
                          : `${Math.round(cell.mastery_estimate * 100)}%`}
                      </td>
                    );
                  })}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
