import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { teacherApi } from "../api/teacher";
import { ApiError } from "../api/client";
import HtmlWithKatex from "../components/HtmlWithKatex";
import { TableSkeleton } from "../components/Skeletons";
import type { ChapterAnalytics } from "../types";

export default function ChapterAnalyticsPage() {
  const { chapterId } = useParams();
  const [data, setData] = useState<ChapterAnalytics | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!chapterId) return;
    teacherApi
      .chapterAnalytics(Number(chapterId))
      .then(setData)
      .catch((err) => setError(err instanceof ApiError ? err.message : "Could not load chapter analytics."));
  }, [chapterId]);

  if (error)
    return (
      <div className="page-error">
        <p>{error}</p>
        <Link to="/teacher">Back to class overview</Link>
      </div>
    );
  if (data === null)
    return (
      <div className="chapter-analytics-page">
        <h1>Chapter Analytics</h1>
        <TableSkeleton />
      </div>
    );

  const worstFirst = data.question_level.slice().sort((a, b) => a.accuracy - b.accuracy);

  return (
    <div className="chapter-analytics-page">
      <Link to="/teacher" className="detail-back">
        ← Back to class overview
      </Link>
      <h1>{data.chapter_name}</h1>

      <div className="dashboard-stat-tiles">
        <div className="stat-tile">
          <span className="stat-tile-value">{data.n_students_tracked}</span>
          <span className="stat-tile-label">Students tracked</span>
        </div>
        <div className="stat-tile">
          <span className="stat-tile-value stat-tile-warning">{data.pct_students_weak}%</span>
          <span className="stat-tile-label">Weak (High priority)</span>
        </div>
      </div>

      {Object.keys(data.difficulty_breakdown).length > 0 && (
        <section className="detail-section">
          <h2>Difficulty distribution</h2>
          <table className="teacher-table">
            <thead>
              <tr>
                <th>Difficulty</th>
                <th>Accuracy</th>
              </tr>
            </thead>
            <tbody>
              {Object.entries(data.difficulty_breakdown).map(([d, acc]) => (
                <tr key={d}>
                  <td>{d}</td>
                  <td>{Math.round(acc * 100)}%</td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>
      )}

      {worstFirst.length > 0 && (
        <section className="detail-section">
          <h2>Question-level analysis</h2>
          <p className="dashboard-subtitle">Worst-accuracy questions first - candidates for review or a content fix.</p>
          <table className="teacher-table">
            <thead>
              <tr>
                <th>Question</th>
                <th>Attempts</th>
                <th>Accuracy</th>
              </tr>
            </thead>
            <tbody>
              {worstFirst.map((q) => (
                <tr key={q.question_id}>
                  <td>
                    <HtmlWithKatex as="span" html={q.body} />
                  </td>
                  <td>{q.n_attempts}</td>
                  <td className={q.accuracy < 0.3 ? "cell-warning" : undefined}>{Math.round(q.accuracy * 100)}%</td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>
      )}
    </div>
  );
}
