import { useEffect, useMemo, useState, type FormEvent } from "react";
import { Link } from "react-router-dom";
import { Target, CalendarCheck, Sparkles, School, ArrowRight, TrendingUp, TrendingDown } from "lucide-react";
import { practiceApi } from "../api/practice";
import { authApi } from "../api/auth";
import { contentApi } from "../api/content";
import { ApiError } from "../api/client";
import { useAuth } from "../context/AuthContext";
import { useStreak } from "../context/StreakContext";
import { matchCourseForStudent } from "../components/CoursePicker";
import { subjectMapFromSections } from "../utils/tree";
import ChapterEvidenceCard from "../components/ChapterEvidenceCard";
import AnimatedNumber from "../components/AnimatedNumber";
import AchievementsStrip from "../components/AchievementsStrip";
import TakeDiagnosticPrompt from "../components/TakeDiagnosticPrompt";
import WelcomeOnboardingModal from "../components/WelcomeOnboardingModal";
import ContinuePracticingRow from "../components/ContinuePracticingRow";
import { MasteryBar, pctColorClass, BAND_CLASS } from "../components/MasteryMiniCard";
import { EvidenceListSkeleton } from "../components/Skeletons";
import { isStepTwoPending, clearStepTwoPending } from "../utils/stepTwoBanner";
import type { ChapterEvidence, SessionHistoryEntry, RecentChapter, Progress, Achievements } from "../types";

function greeting(): string {
  const hour = new Date().getHours();
  if (hour < 12) return "Good morning";
  if (hour < 17) return "Good afternoon";
  return "Good evening";
}

function JoinClassPrompt() {
  const { student, updateStudent } = useAuth();
  const [code, setCode] = useState("");
  // "joined" is tracked separately from student.class_id so the success
  // message survives the re-render updateStudent() triggers below - by
  // the time that render happens, class_id is already non-null, and
  // without this the component's own "already enrolled" guard would hide
  // the form (and the message with it) before the student ever saw it.
  const [status, setStatus] = useState<"idle" | "joining" | "error" | "joined">("idle");
  const [message, setMessage] = useState<string | null>(null);

  if (!student) return null;
  if (student.class_id !== null && status !== "joined") return null;

  async function submit(e: FormEvent) {
    e.preventDefault();
    setStatus("joining");
    setMessage(null);
    try {
      const updated = await authApi.joinClass(code);
      updateStudent({ class_id: updated.class_id });
      setStatus("joined");
      setMessage("You've joined the class!");
    } catch (err) {
      setStatus("error");
      setMessage(err instanceof ApiError ? err.message : "Could not join that class.");
    }
  }

  return (
    <section className="classroom-card">
      <span className="classroom-card-icon">
        <School size={18} strokeWidth={2} />
      </span>
      <div className="classroom-card-body">
        {status === "joined" ? (
          <p className="feedback-correct join-class-success">{message}</p>
        ) : (
          <>
            <span className="join-class-label">Not part of a class yet?</span>
            <form className="join-class-prompt" onSubmit={submit}>
              <div className="option-input-row">
                <input
                  value={code}
                  onChange={(e) => setCode(e.target.value)}
                  placeholder="e.g. 4F9K2A"
                  required
                />
                <button type="submit" disabled={status === "joining"}>
                  {status === "joining" ? "Joining…" : "Join"}
                </button>
              </div>
              {status === "error" && message && <p className="form-error">{message}</p>}
            </form>
          </>
        )}
      </div>
    </section>
  );
}

// Closes the loop the welcome modal opened ("Step 1: diagnostic, Step 2:
// your weak-chapter list") - without this, finishing the diagnostic just
// silently swapped the empty state for the normal populated dashboard with
// no acknowledgement that this *is* step 2, which read as the guidance
// abandoning the student right when it mattered most. Driven by a
// persisted per-student flag (markStepTwoPending in ExamPage's doFinish),
// not react-router navigation state - state only survives the one exact
// click that set it, so closing the tab, using a sidebar link, or coming
// back later after a completed diagnostic silently lost the acknowledgement
// even though real evidence existed. The persisted flag shows this on the
// next populated-dashboard visit regardless of how the student got there,
// and is cleared for good once dismissed.
function StepTwoBanner({ onDismiss }: { onDismiss: () => void }) {
  return (
    <div className="step-two-banner">
      <span className="onboarding-step-label">Step 2 of 2 — done</span>
      <p>
        This is your personalised weak-chapter list, ranked by priority from your diagnostic. Chapters below marked
        "Insufficient evidence" just need a few more attempts before a real priority shows - Quick Practice or the
        chapter cards below are the natural next step.
      </p>
      <button type="button" className="step-two-banner-dismiss" aria-label="Dismiss" onClick={onDismiss}>
        ×
      </button>
    </div>
  );
}

// Every bullet maps to a real, already-computed field on the evidence
// object - never fabricated. Deliberately short labels (not full
// sentences) to read as a scannable checklist under the hero card.
function heroReasons(e: ChapterEvidence): string[] {
  const reasons: string[] = [];
  if (e.mastery_estimate < 0.5) reasons.push(`Low mastery (${Math.round(e.mastery_estimate * 100)}%)`);
  if (e.raw_accuracy < 0.5) reasons.push(`Low accuracy (${Math.round(e.raw_accuracy * 100)}%)`);
  if (e.confidence >= 0.7) reasons.push(`Sufficient evidence (${e.n_attempts} attempts)`);
  if (e.priority_band === "High") reasons.push("High potential for improvement");
  return reasons;
}

function HeroRecommendationCard({
  evidence,
  learnHref,
  practiceHref,
}: {
  evidence: ChapterEvidence;
  learnHref: string;
  practiceHref: string;
}) {
  const pct = Math.round(evidence.mastery_estimate * 100);
  const intro =
    evidence.priority_band === "High"
      ? "This is currently your highest-priority learning gap."
      : evidence.priority_band === "Medium"
        ? "This is a developing area worth your attention next."
        : "This is the best place to focus next, based on your evidence so far.";
  const reasons = heroReasons(evidence);
  const bandClass = BAND_CLASS[evidence.priority_band] ?? "band-insufficient";

  return (
    <section className={`hero-recommendation ${bandClass}`}>
      <p className="distribution-heading">
        <Target size={14} strokeWidth={2.5} style={{ display: "inline", marginRight: 6, verticalAlign: -2 }} />
        Your next best action
      </p>
      <h2 className="hero-recommendation-chapter">{evidence.chapter_name}</h2>
      <p className="hero-recommendation-intro">
        Your current mastery is {pct}%, and your accuracy is {Math.round(evidence.raw_accuracy * 100)}%. {intro}
      </p>

      <div className="mastery-bar-row">
        <span>Mastery</span>
        <span>{pct}%</span>
      </div>
      <MasteryBar pct={pct} colorClass={pctColorClass(evidence.mastery_estimate)} />

      <p className="hero-recommendation-meta">
        {evidence.n_attempts} question{evidence.n_attempts === 1 ? "" : "s"} attempted &middot; {evidence.priority_band}{" "}
        priority
      </p>

      {reasons.length > 0 && (
        <div className="hero-recommendation-reasons">
          <p className="hero-recommendation-reasons-label">Why GapFinder recommends this</p>
          <ul>
            {reasons.map((r) => (
              <li key={r}>{r}</li>
            ))}
          </ul>
        </div>
      )}

      <div className="hero-recommendation-actions">
        <Link to={learnHref} className="cta-button-secondary">
          Review Chapter
        </Link>
        <Link to={practiceHref} className="cta-button">
          Start Practice <ArrowRight size={16} strokeWidth={2.5} />
        </Link>
      </div>
    </section>
  );
}

function TodaysPlan({ chapterName, learnHref, practiceHref }: { chapterName: string; learnHref: string; practiceHref: string }) {
  return (
    <section className="todays-plan">
      <p className="distribution-heading">
        <CalendarCheck size={14} strokeWidth={2.5} style={{ display: "inline", marginRight: 6, verticalAlign: -2 }} />
        Today's learning plan
      </p>
      <ol className="todays-plan-steps">
        <li>
          <span className="todays-plan-num">1</span>
          <Link to={learnHref} className="todays-plan-step-label">
            Review {chapterName}
          </Link>
          <span className="todays-plan-time">~10 min</span>
        </li>
        <li>
          <span className="todays-plan-num">2</span>
          <Link to={practiceHref} className="todays-plan-step-label">
            Practice 10 questions
          </Link>
          <span className="todays-plan-time">~10 min</span>
        </li>
        <li>
          <span className="todays-plan-num">3</span>
          <Link to={practiceHref} className="todays-plan-step-label">
            Retest weak concepts
          </Link>
          <span className="todays-plan-time">~10 min</span>
        </li>
      </ol>
      <p className="todays-plan-total">Estimated time: ~30 min</p>
      <Link to={learnHref} className="cta-button">
        Start Today's Plan <ArrowRight size={16} strokeWidth={2.5} />
      </Link>
    </section>
  );
}

function NiceProgress({ progress }: { progress: Progress | null }) {
  const best = useMemo(() => {
    if (!progress) return null;
    return progress.before_after
      .filter((b) => b.mastery_before !== null && b.mastery_after !== null)
      .map((b) => ({ ...b, delta: Math.round((b.mastery_after! - b.mastery_before!) * 100) }))
      .filter((b) => b.delta > 5)
      .sort((a, b) => b.delta - a.delta)[0];
  }, [progress]);

  if (!best) return null;

  return (
    <Link to="/progress" className="nice-progress-card">
      <span className="nice-progress-icon">
        <Sparkles size={16} strokeWidth={2} />
      </span>
      <div className="nice-progress-body">
        <span className="nice-progress-label">Nice progress</span>
        <p>
          Your mastery in <strong>{best.chapter_name}</strong> improved from {Math.round(best.mastery_before! * 100)}% →{" "}
          {Math.round(best.mastery_after! * 100)}%.
        </p>
      </div>
      <span className="nice-progress-delta">+{best.delta}%</span>
    </Link>
  );
}

export default function DashboardPage() {
  const { logout, student } = useAuth();
  const { streakDays } = useStreak();
  const [showStepTwo, setShowStepTwo] = useState(false);
  const [evidence, setEvidence] = useState<ChapterEvidence[] | null>(null);
  const [sessionHistory, setSessionHistory] = useState<SessionHistoryEntry[]>([]);
  const [recentChapters, setRecentChapters] = useState<RecentChapter[]>([]);
  const [progress, setProgress] = useState<Progress | null>(null);
  const [achievements, setAchievements] = useState<Achievements | null>(null);
  const [matchedCourseId, setMatchedCourseId] = useState<number | null>(null);
  const [chapterIdsInTree, setChapterIdsInTree] = useState<Set<number>>(new Set());
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;
    practiceApi
      .resultsMe()
      .then((data) => {
        if (!cancelled) setEvidence(data);
      })
      .catch((err) => {
        if (cancelled) return;
        if (err instanceof ApiError && err.status === 401) {
          logout();
          return;
        }
        setError(err instanceof ApiError ? err.message : "Could not load your results.");
      });
    // best-effort - all of these are nice-to-haves on this page, not
    // worth blocking or erroring the whole dashboard over
    practiceApi.performanceMe().then((p) => {
      if (!cancelled) setSessionHistory(p.session_history.filter((s) => s.completed_at !== null));
    }).catch(() => undefined);
    practiceApi.recentChapters().then((c) => {
      if (!cancelled) setRecentChapters(c);
    }).catch(() => undefined);
    practiceApi.progressMe().then((p) => {
      if (!cancelled) setProgress(p);
    }).catch(() => undefined);
    practiceApi.achievementsMe().then((a) => {
      if (!cancelled) setAchievements(a);
    }).catch(() => undefined);
    return () => {
      cancelled = true;
    };
  }, [logout]);

  useEffect(() => {
    contentApi
      .listCourses()
      .then((courses) => {
        const matched = matchCourseForStudent(courses, student?.grade ?? null, student?.stream ?? null);
        if (!matched) return;
        setMatchedCourseId(matched.id);
        return contentApi
          .listSections(matched.id)
          .then((sections) => setChapterIdsInTree(new Set(subjectMapFromSections(sections).keys())));
      })
      .catch(() => undefined);
  }, [student]);

  useEffect(() => {
    if (student && evidence && evidence.length > 0 && isStepTwoPending(student.id)) {
      setShowStepTwo(true);
    }
  }, [student, evidence]);

  function dismissStepTwo() {
    if (student) clearStepTwoPending(student.id);
    setShowStepTwo(false);
  }

  if (error) return <p className="page-error">{error}</p>;
  if (evidence === null)
    return (
      <div className="dashboard-page">
        <h1>What to work on next</h1>
        <p className="dashboard-subtitle">Ranked from your recorded practice attempts, most in need of attention first.</p>
        <EvidenceListSkeleton />
      </div>
    );

  if (evidence.length === 0) {
    return (
      <div className="empty-state onboarding-empty-state">
        <WelcomeOnboardingModal />
        <h1>What to work on next</h1>
        <p className="dashboard-subtitle">You haven't practised any chapters yet.</p>

        <span className="onboarding-step-label">Step 1 of 2 — get started</span>
        <TakeDiagnosticPrompt variant="card" />

        <p className="onboarding-divider">or skip ahead</p>
        <div className="onboarding-secondary-row">
          <Link to="/quick-practice" className="cta-button-secondary">
            Quick Practice
          </Link>
          <Link to="/chapters" className="cta-button-secondary">
            Browse chapters
          </Link>
        </div>

        <div className="onboarding-demoted">
          <AchievementsStrip />
          <JoinClassPrompt />
        </div>
      </div>
    );
  }

  const highPriorityCount = evidence.filter((e) => e.priority_band === "High").length;
  const topRecommendation = evidence[0];
  const weakChapters = evidence.filter((e) => e.priority_band === "High" || e.priority_band === "Medium").slice(0, 5);

  const recentWindow = sessionHistory.slice(0, 5);
  const priorWindow = sessionHistory.slice(5, 10);
  const recentAvgScore = recentWindow.length
    ? Math.round(recentWindow.reduce((sum, s) => sum + (s.percentage ?? 0), 0) / recentWindow.length)
    : null;
  const priorAvgScore =
    priorWindow.length >= 3
      ? Math.round(priorWindow.reduce((sum, s) => sum + (s.percentage ?? 0), 0) / priorWindow.length)
      : null;
  const scoreDelta = recentAvgScore !== null && priorAvgScore !== null ? recentAvgScore - priorAvgScore : null;

  const streakMilestone = achievements?.next_milestones.find((m) => m.badge_id.startsWith("streak_")) ?? null;

  const inMatchedCourse = matchedCourseId !== null && chapterIdsInTree.has(topRecommendation.chapter_id);
  const learnHref = `/chapter/${topRecommendation.chapter_id}/learn`;
  const practiceHref = inMatchedCourse
    ? `/quick-practice/${matchedCourseId}/${topRecommendation.chapter_id}`
    : `/chapter/${topRecommendation.chapter_id}`;
  const showHero = topRecommendation.priority_band !== "Insufficient evidence";

  return (
    <div className="dashboard-page">
      <h1>
        {greeting()}, {student?.name.split(" ")[0]}
      </h1>
      <p className="dashboard-subtitle">Here's what you should focus on today.</p>

      {showStepTwo && <StepTwoBanner onDismiss={dismissStepTwo} />}

      <div className="dashboard-stat-tiles">
        <div className="stat-tile">
          <span className="stat-tile-value">
            <AnimatedNumber value={evidence.length} />
          </span>
          <span className="stat-tile-label">Chapters tracked</span>
        </div>

        <Link to="/weak-areas" className={`stat-tile stat-tile-link${highPriorityCount === 0 ? " stat-tile-disabled" : ""}`}>
          <span className="stat-tile-value stat-tile-warning">
            <AnimatedNumber value={highPriorityCount} />
          </span>
          <span className="stat-tile-label">High-priority gaps</span>
        </Link>

        {recentAvgScore !== null && (
          <Link to="/performance" className="stat-tile stat-tile-link">
            <span className="stat-tile-value">
              <AnimatedNumber value={recentAvgScore} suffix="%" />
            </span>
            <span className="stat-tile-label">Recent accuracy</span>
            {scoreDelta !== null && (
              <span className={`stat-tile-delta ${scoreDelta >= 0 ? "stat-tile-delta-up" : "stat-tile-delta-down"}`}>
                {scoreDelta >= 0 ? <TrendingUp size={12} strokeWidth={2.5} /> : <TrendingDown size={12} strokeWidth={2.5} />}
                {scoreDelta >= 0 ? "+" : ""}
                {scoreDelta}% from before
              </span>
            )}
          </Link>
        )}

        <div className="stat-tile">
          <span className="stat-tile-value">
            {streakDays !== null && streakDays > 0 ? `🔥 ${streakDays}d` : "🔥 0d"}
          </span>
          <span className="stat-tile-label">
            {streakMilestone ? streakMilestone.message : streakDays && streakDays > 0 ? "Keep it going" : "Practice today to start"}
          </span>
        </div>
      </div>

      {showHero && <HeroRecommendationCard evidence={topRecommendation} learnHref={learnHref} practiceHref={practiceHref} />}

      {showHero && <TodaysPlan chapterName={topRecommendation.chapter_name} learnHref={learnHref} practiceHref={practiceHref} />}

      <ContinuePracticingRow chapters={recentChapters} evidenceByChapter={new Map(evidence.map((e) => [e.chapter_id, e]))} />

      <AchievementsStrip />

      <NiceProgress progress={progress} />

      {weakChapters.length > 0 && (
        <section className="dashboard-priority-areas">
          <div className="dashboard-priority-areas-header">
            <p className="distribution-heading">Priority areas</p>
            <Link to="/weak-areas">See all in Weak Areas →</Link>
          </div>
          <div className="evidence-list">
            {weakChapters.map((e) => (
              <ChapterEvidenceCard key={e.chapter_id} evidence={e} />
            ))}
          </div>
        </section>
      )}

      <Link to="/chapters" className="cta-button-secondary">
        Practice more chapters
      </Link>

      <JoinClassPrompt />
    </div>
  );
}
