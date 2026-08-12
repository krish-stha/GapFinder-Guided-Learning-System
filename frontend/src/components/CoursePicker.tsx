import {
  FlaskConical,
  Briefcase,
  GraduationCap,
  TrendingUp,
  BookOpen,
  Atom,
  Calculator,
  Dna,
  Globe2,
  Landmark,
  Languages,
  MonitorSmartphone,
  Sprout,
  Wallet,
  type LucideIcon,
} from "lucide-react";
import type { Course } from "../types";

// Best-effort icon per course, matched by name keyword rather than a
// dedicated backend field - the course catalogue is small and named
// predictably ("NEB Grade 11 Science", "NEB Grade 12 Management", ...),
// so a keyword match is simpler than adding a schema column for this.
export function courseIcon(name: string): LucideIcon {
  const n = name.toLowerCase();
  if (n.includes("management")) return Briefcase;
  if (n.includes("science")) return FlaskConical;
  if (n.includes("foundation")) return GraduationCap;
  if (n.includes("improvement")) return TrendingUp;
  return BookOpen;
}

// Best-effort icon per subject, matched by name keyword the same way
// courseIcon works - purely decorative on the Practice page's subject
// cards, no schema field for it.
export function subjectIcon(name: string): LucideIcon {
  const n = name.toLowerCase();
  if (n.includes("physic")) return Atom;
  if (n.includes("chemistry")) return FlaskConical;
  if (n.includes("botany") || n.includes("biology")) return Sprout;
  if (n.includes("zoology")) return Dna;
  if (n.includes("maths") || n.includes("math")) return Calculator;
  if (n.includes("comput")) return MonitorSmartphone;
  if (n.includes("english") || n.includes("नेपाली") || n.includes("nepali")) return Languages;
  if (n.includes("social") || n.includes("सामाजिक")) return Globe2;
  if (n.includes("account")) return Wallet;
  if (n.includes("business") || n.includes("economic")) return Landmark;
  return BookOpen;
}

// A course named "NEB Grade {11,12} {Science,Management}" is the exact
// course a student's own registration (grade + stream) implies - matched
// by name rather than a dedicated FK since there's no course-enrollment
// field on Student. Streams without a matching course yet (e.g.
// Humanities) simply don't match, and the caller falls back to showing
// every course.
export function matchCourseForStudent(courses: Course[], grade: number | null, stream: string | null): Course | null {
  if (!grade || !stream) return null;
  const target = `neb grade ${grade} ${stream}`.toLowerCase();
  return courses.find((c) => c.name.toLowerCase() === target) ?? null;
}

export function CourseGrid({ courses, onSelect }: { courses: Course[]; onSelect: (id: number) => void }) {
  return (
    <div className="course-grid">
      {courses.map((c) => {
        const Icon = courseIcon(c.name);
        return (
          <button key={c.id} type="button" className="course-card" onClick={() => onSelect(c.id)}>
            <span className="course-card-icon">
              <Icon size={28} strokeWidth={1.75} />
            </span>
            <span className="course-card-name">{c.name}</span>
          </button>
        );
      })}
    </div>
  );
}

export function CourseHeaderBar({
  course,
  onChange,
  changeLabel = "Change course",
}: {
  course: Course;
  onChange: () => void;
  changeLabel?: string;
}) {
  const Icon = courseIcon(course.name);
  return (
    <div className="course-header-bar">
      <span className="course-header-icon">
        <Icon size={20} strokeWidth={1.75} />
      </span>
      <span className="course-header-name">{course.name}</span>
      <button type="button" className="change-course-btn" onClick={onChange}>
        {changeLabel}
      </button>
    </div>
  );
}
