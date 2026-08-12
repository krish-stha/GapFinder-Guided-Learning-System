import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { contentApi } from "../api/content";
import { ApiError } from "../api/client";
import { useAuth } from "../context/AuthContext";
import { CourseGrid, matchCourseForStudent } from "../components/CoursePicker";
import type { Course } from "../types";

type LoadState = { status: "loading" } | { status: "picking-course"; courses: Course[] } | { status: "error"; message: string };

// Reached via the plain "Quick Practice" nav CTAs, where the course isn't
// known yet - resolves the student's home course (or lets them pick one)
// and hands off to ExamPage's purpose="practice" route, which owns the
// actual question-count picker/taking/results flow. Every other "Practice"
// button in the app already knows its course_id and links straight to
// /quick-practice/:courseId(/:chapterId), skipping this resolver entirely.
export default function QuickPracticePage() {
  const { student } = useAuth();
  const navigate = useNavigate();
  const [state, setState] = useState<LoadState>({ status: "loading" });

  useEffect(() => {
    let cancelled = false;
    contentApi
      .listCourses()
      .then((courses) => {
        if (cancelled) return;
        const match = matchCourseForStudent(courses, student?.grade ?? null, student?.stream ?? null);
        if (match) {
          navigate(`/quick-practice/${match.id}`, { replace: true });
        } else {
          setState({ status: "picking-course", courses });
        }
      })
      .catch((err) => {
        if (!cancelled) setState({ status: "error", message: err instanceof ApiError ? err.message : "Could not load courses." });
      });
    return () => {
      cancelled = true;
    };
  }, [student, navigate]);

  if (state.status === "loading") return <p className="page-loading">Loading…</p>;

  if (state.status === "error") return <p className="page-error">{state.message}</p>;

  return (
    <div className="dashboard-page">
      <h1>Quick Practice</h1>
      <p className="dashboard-subtitle">Pick a course to start a quick practice round.</p>
      <CourseGrid courses={state.courses} onSelect={(id) => navigate(`/quick-practice/${id}`)} />
    </div>
  );
}
