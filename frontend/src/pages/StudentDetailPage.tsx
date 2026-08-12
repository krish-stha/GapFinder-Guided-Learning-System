import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { teacherApi } from "../api/teacher";
import { ApiError } from "../api/client";
import ChapterEvidenceCard from "../components/ChapterEvidenceCard";
import AccuracyTrendChart from "../components/AccuracyTrendChart";
import { TableSkeleton } from "../components/Skeletons";
import type { ChapterEvidence, Performance } from "../types";

export default function StudentDetailPage() {
  const { studentId } = useParams();
  const [evidence, setEvidence] = useState<ChapterEvidence[] | null>(null);
  const [performance, setPerformance] = useState<Performance | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!studentId) return;
    const id = Number(studentId);
    Promise.all([teacherApi.studentEvidence(id), teacherApi.studentPerformance(id)])
      .then(([ev, perf]) => {
        setEvidence(ev);
        setPerformance(perf);
      })
      .catch((err) => setError(err instanceof ApiError ? err.message : "Could not load this student's performance."));
  }, [studentId]);

  if (error)
    return (
      <div className="page-error">
        <p>{error}</p>
        <Link to="/teacher">Back to class overview</Link>
      </div>
    );
  if (evidence === null || performance === null)
    return (
      <div className="student-detail-page">
        <h1>Student Performance</h1>
        <TableSkeleton />
      </div>
    );

  return (
    <div className="student-detail-page">
      <Link to="/teacher" className="detail-back">
        ← Back to class overview
      </Link>
      <h1>Student Performance</h1>

      {performance.accuracy_trend.length > 0 && (
        <section className="detail-section">
          <h2>Scores over time</h2>
          <AccuracyTrendChart points={performance.accuracy_trend} />
        </section>
      )}

      <section className="detail-section">
        <h2>Chapter-by-chapter evidence</h2>
        {evidence.length === 0 ? (
          <p className="page-loading">No recorded attempts for this student yet.</p>
        ) : (
          <div className="evidence-list">
            {evidence.map((e) => (
              <ChapterEvidenceCard key={e.chapter_id} evidence={e} linkTo={false} />
            ))}
          </div>
        )}
      </section>

      {performance.subject_breakdown.length > 0 && (
        <section className="detail-section">
          <h2>Subject-wise performance</h2>
          <table className="teacher-table">
            <thead>
              <tr>
                <th>Subject</th>
                <th>Attempts</th>
                <th>Avg. mastery</th>
              </tr>
            </thead>
            <tbody>
              {performance.subject_breakdown.map((s) => (
                <tr key={s.subject_id}>
                  <td>{s.subject_name}</td>
                  <td>{s.n_attempts}</td>
                  <td>{Math.round(s.avg_mastery * 100)}%</td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>
      )}
    </div>
  );
}
