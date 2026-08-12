import { useEffect, useState } from "react";
import { Link, NavLink, Outlet, useLocation, useNavigate } from "react-router-dom";
import {
  Home,
  BookOpen,
  AlertTriangle,
  Milestone,
  BarChart3,
  TrendingUp,
  Activity,
  MessageCircle,
  LayoutDashboard,
  Flame,
  ClipboardList,
  FileText,
  LogOut,
  Menu,
  X,
  Sun,
  Moon,
  BookOpenText,
  Users,
} from "lucide-react";
import { useAuth } from "../context/AuthContext";
import { useTheme, type Theme } from "../context/ThemeContext";
import { useStreak } from "../context/StreakContext";
import { authApi } from "../api/auth";
import { homePathForRole } from "../utils/roles";
import Logo from "./Logo";

function VerifyEmailBanner() {
  const [status, setStatus] = useState<"idle" | "sending" | "sent" | "error">("idle");

  async function resend() {
    setStatus("sending");
    try {
      await authApi.requestEmailVerification();
      setStatus("sent");
    } catch (err) {
      setStatus("error");
      void err;
    }
  }

  return (
    <div className="verify-banner">
      {status === "sent" ? (
        <span>Verification email sent - check your inbox.</span>
      ) : (
        <>
          <span>Your email isn't verified yet.</span>
          <button type="button" onClick={resend} disabled={status === "sending"}>
            {status === "sending" ? "Sending…" : "Resend verification email"}
          </button>
          {status === "error" && <span className="verify-banner-error">Couldn't send it - try again shortly.</span>}
        </>
      )}
    </div>
  );
}

const THEME_OPTIONS: { value: Theme; label: string; icon: typeof Sun }[] = [
  { value: "light", label: "Light", icon: Sun },
  { value: "dark", label: "Dark", icon: Moon },
  { value: "reading", label: "Reading", icon: BookOpenText },
];

function ThemeToggle() {
  const { theme, setTheme } = useTheme();
  return (
    <div className="theme-toggle" role="group" aria-label="Theme">
      {THEME_OPTIONS.map(({ value, label, icon: Icon }) => (
        <button
          key={value}
          type="button"
          className={`theme-toggle-btn${theme === value ? " active" : ""}`}
          aria-pressed={theme === value}
          title={`${label} mode`}
          onClick={() => setTheme(value)}
        >
          <Icon size={16} strokeWidth={2} />
        </button>
      ))}
    </div>
  );
}

const STUDENT_LINKS = [
  { to: "/dashboard", label: "What to work on", icon: Home },
  { to: "/chapters", label: "Practice", icon: BookOpen },
  { to: "/weak-areas", label: "Weak areas", icon: AlertTriangle },
  { to: "/learning-path", label: "Learning path", icon: Milestone },
  { to: "/chapter-analysis", label: "Chapter analysis", icon: BarChart3 },
  { to: "/performance", label: "Performance", icon: TrendingUp },
  { to: "/progress", label: "Progress", icon: Activity },
  { to: "/assistant", label: "Assistant", icon: MessageCircle },
];

const TEACHER_LINKS = [
  { to: "/teacher", label: "Class overview", icon: LayoutDashboard },
  { to: "/teacher/classes", label: "Classes", icon: Users },
  { to: "/teacher/heatmap", label: "Heatmap", icon: Flame },
  { to: "/teacher/assessments", label: "Assessments", icon: ClipboardList },
  { to: "/teacher/content", label: "Content", icon: FileText },
];

export default function Layout() {
  const { student, logout, isAuthenticated } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();
  const [mobileOpen, setMobileOpen] = useState(false);
  const { streakDays } = useStreak();

  useEffect(() => {
    setMobileOpen(false);
  }, [location.pathname]);

  function handleLogout() {
    logout();
    navigate("/login");
  }

  const links = student?.role === "teacher" ? TEACHER_LINKS : STUDENT_LINKS;

  return (
    <div className="app-shell">
      {isAuthenticated && student && (
        <>
          <header className="mobile-topbar">
            <button
              type="button"
              className="mobile-topbar-toggle"
              aria-label={mobileOpen ? "Close menu" : "Open menu"}
              onClick={() => setMobileOpen((v) => !v)}
            >
              {mobileOpen ? <X size={22} /> : <Menu size={22} />}
            </button>
            <Link to={homePathForRole(student.role)} className="nav-brand">
              <Logo size={22} />
              GapFinder
            </Link>
          </header>

          {mobileOpen && <div className="sidebar-backdrop" onClick={() => setMobileOpen(false)} />}

          <aside className={`sidebar${mobileOpen ? " sidebar-open" : ""}`}>
            <Link to={homePathForRole(student.role)} className="nav-brand sidebar-brand">
              <Logo size={24} />
              GapFinder
            </Link>

            <nav className="sidebar-nav">
              {links.map(({ to, label, icon: Icon }) => (
                <NavLink key={to} to={to} end className={({ isActive }) => `sidebar-link${isActive ? " active" : ""}`}>
                  <Icon size={18} strokeWidth={2} />
                  <span>{label}</span>
                </NavLink>
              ))}
            </nav>

            <div className="sidebar-footer">
              <ThemeToggle />
              {student.role === "student" && streakDays !== null && (
                <div className={`sidebar-streak${streakDays === 0 ? " sidebar-streak-empty" : ""}`}>
                  <Flame size={16} strokeWidth={2} />
                  {streakDays > 0 ? (
                    <span>{streakDays} day{streakDays === 1 ? "" : "s"} streak</span>
                  ) : (
                    <span>No streak yet - practice today</span>
                  )}
                </div>
              )}
              <div className="sidebar-user">{student.name}</div>
              <button type="button" className="sidebar-logout" onClick={handleLogout}>
                <LogOut size={16} strokeWidth={2} />
                Log out
              </button>
            </div>
          </aside>
        </>
      )}

      <div className="app-content">
        {isAuthenticated && student && !student.email_verified && <VerifyEmailBanner />}
        <main className="app-main">
          <Outlet />
        </main>
      </div>
    </div>
  );
}
