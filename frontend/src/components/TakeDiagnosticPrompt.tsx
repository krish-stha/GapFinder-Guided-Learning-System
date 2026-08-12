import { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { ClipboardList, ArrowRight } from "lucide-react";
import { contentApi } from "../api/content";
import { useAuth } from "../context/AuthContext";
import { CourseGrid, matchCourseForStudent } from "./CoursePicker";
import type { Course } from "../types";

// Before this existed, there was no way anywhere in the app for a real
// student to actually start a purpose="diagnostic" session - the
// Progress page's before/after comparison and the "Diagnostic Complete"
// achievement were permanently unreachable, only ever populated via the
// demo-seeding script. Reuses the exact same mixed-draw exam flow as a
// mock test (ExamPage's `purpose` prop), just under the distinct
// purpose/route the backend already keys the before/after split off.
//
// `variant="card"` is the prominent first-step hero card on the empty
// Dashboard (see the onboarding redesign); `variant="button"` (default)
// is the compact inline version used on the Progress page's empty state.
// Both share the same course-resolution logic so there's one source of
// truth for "which course does this diagnostic start in."
export default function TakeDiagnosticPrompt({ variant = "button" }: { variant?: "button" | "card" }) {
  const { student } = useAuth();
  const navigate = useNavigate();
  const [courses, setCourses] = useState<Course[] | null>(null);

  useEffect(() => {
    contentApi.listCourses().then(setCourses).catch(() => setCourses([]));
  }, []);

  if (courses === null) return null;

  const matched = matchCourseForStudent(courses, student?.grade ?? null, student?.stream ?? null);

  if (variant === "card") {
    if (matched) {
      return (
        <div className="onboarding-primary-card">
          <div className="onboarding-primary-card-icon">
            <ClipboardList size={22} strokeWidth={2} />
          </div>
          <span className="onboarding-primary-card-label">Recommended first step</span>
          <h2>Take a diagnostic assessment</h2>
          <p>Get a real, evidence-based baseline across every chapter before you start practicing.</p>
          <span className="onboarding-primary-card-meta">10-50 mixed questions · untimed · you choose the length</span>
          <Link to={`/diagnostic/${matched.id}`} className="onboarding-primary-cta">
            Start diagnostic <ArrowRight size={16} strokeWidth={2.5} />
          </Link>
        </div>
      );
    }
    if (courses.length === 0) return null;
    return (
      <div className="onboarding-primary-card">
        <div className="onboarding-primary-card-icon">
          <ClipboardList size={22} strokeWidth={2} />
        </div>
        <span className="onboarding-primary-card-label">Recommended first step</span>
        <h2>Take a diagnostic assessment</h2>
        <p>Pick a course to get a real, evidence-based baseline before you start practicing.</p>
        <CourseGrid courses={courses} onSelect={(id) => navigate(`/diagnostic/${id}`)} />
      </div>
    );
  }

  if (matched) {
    return (
      <Link to={`/diagnostic/${matched.id}`} className="cta-button">
        Take a diagnostic assessment
      </Link>
    );
  }
  if (courses.length === 0) return null;
  return (
    <div>
      <p className="dashboard-subtitle">Pick a course to take a diagnostic assessment in:</p>
      <CourseGrid courses={courses} onSelect={(id) => navigate(`/diagnostic/${id}`)} />
    </div>
  );
}
