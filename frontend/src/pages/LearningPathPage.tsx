import { Link, useNavigate } from "react-router-dom";
import { useEffect, useMemo, useState } from "react";
import {
  Target,
  ArrowRight,
  CheckCircle2,
  TrendingUp,
  TrendingDown,
  CircleDot,
  Circle,
  Repeat,
} from "lucide-react";
import { practiceApi } from "../api/practice";
import { ApiError } from "../api/client";
import { EvidenceListSkeleton } from "../components/Skeletons";
import { MasteryBar, pctColorClass } from "../components/MasteryMiniCard";
import type { LearningPathStatus, LearningPathStep } from "../types";

// Matches mastery.py's MasteryWeights.mastery_complete_threshold - the
// same real threshold Progress & Achievements already use for "chapter
// completed"/"chapter mastered", reused here as the goal target rather
// than inventing a separate number.
const MASTERY_TARGET = 0.7;

const STATUS_LABEL: Record<LearningPathStatus, string> = {
  High: "High priority",
  Medium: "Medium priority",
  Low: "Low priority",
  "Insufficient evidence": "Not enough data yet",
  not_started: "Not started",
};
const STATUS_CLASS: Record<LearningPathStatus, string> = {
  High: "band-high",
  Medium: "band-medium",
  Low: "band-low",
  "Insufficient evidence": "band-insufficient",
  not_started: "band-insufficient",
};

type RoadmapState = "Not Started" | "In Progress" | "Improving" | "Declining" | "Mastered";

// A journey state, distinct from priority_band - "how far along am I with
// this chapter" rather than "how urgently does it need attention". This is
// what makes the roadmap read differently from Weak Areas' band list, per
// the product-architecture goal: Weak Areas = where am I weak, Learning
// Path = what's my progress through the plan.
function roadmapState(step: LearningPathStep): RoadmapState {
  if (step.status === "not_started") return "Not Started";
  if (step.mastery_estimate !== null && step.mastery_estimate >= MASTERY_TARGET) return "Mastered";
  if (step.trend_significant && step.trend_slope !== null) return step.trend_slope > 0 ? "Improving" : "Declining";
  return "In Progress";
}

const ROADMAP_STATE_ICON: Record<RoadmapState, typeof Circle> = {
  "Not Started": Circle,
  "In Progress": CircleDot,
  Improving: TrendingUp,
  Declining: TrendingDown,
  Mastered: CheckCircle2,
};
const ROADMAP_STATE_CLASS: Record<RoadmapState, string> = {
  "Not Started": "roadmap-state-neutral",
  "In Progress": "roadmap-state-progress",
  Improving: "roadmap-state-improving",
  Declining: "roadmap-state-declining",
  Mastered: "roadmap-state-mastered",
};

function evidenceLabel(n: number): string {
  if (n >= 20) return "Strong evidence base";
  if (n >= 10) return "Solid evidence base";
  return "Growing evidence base";
}

function impactLevel(priorityScore: number): "High" | "Medium" | "Low" {
  if (priorityScore >= 0.5) return "High";
  if (priorityScore >= 0.25) return "Medium";
  return "Low";
}

function GoalCard({ path }: { path: LearningPathStep[] }) {
  const evidenced = path.filter((s) => s.mastery_estimate !== null);
  if (evidenced.length === 0) return null;
  const avgMastery = evidenced.reduce((sum, s) => sum + s.mastery_estimate!, 0) / evidenced.length;
  const pct = Math.round(avgMastery * 100);
  const areasToImprove = path.filter((s) => s.status === "High" || s.status === "Medium").length;

  return (
    <div className="learning-goal-card">
      <div className="learning-goal-header">
        <span className="learning-goal-icon">
          <Target size={18} strokeWidth={2} />
        </span>
        <div>
          <p className="learning-goal-title">Your learning goal</p>
          <p className="learning-goal-desc">
            {avgMastery >= MASTERY_TARGET
              ? `You're averaging ${pct}% mastery, already above the ${Math.round(MASTERY_TARGET * 100)}% threshold - keep reinforcing the areas below to stay there.`
              : `Build your average mastery from ${pct}% toward the ${Math.round(MASTERY_TARGET * 100)}% mastery threshold.`}
          </p>
        </div>
      </div>
      <MasteryBar pct={pct} colorClass={pctColorClass(avgMastery)} />
      {areasToImprove > 0 && (
        <p className="learning-goal-meta">
          {areasToImprove} area{areasToImprove === 1 ? "" : "s"} to improve
        </p>
      )}
    </div>
  );
}

function ReasonChip({ label, value }: { label: string; value: string }) {
  return (
    <div className="reason-chip">
      <span className="reason-chip-value">{value}</span>
      <span className="reason-chip-label">{label}</span>
    </div>
  );
}

function StartHereCard({ step, courseId }: { step: LearningPathStep; courseId: number | null }) {
  const navigate = useNavigate();
  const bandClass = STATUS_CLASS[step.status];
  const pct = Math.round((step.mastery_estimate ?? 0) * 100);
  const delta =
    step.subject_avg_mastery !== null && step.mastery_estimate !== null
      ? Math.round((step.mastery_estimate - step.subject_avg_mastery) * 100)
      : null;
  const impact = step.priority_score !== null ? impactLevel(step.priority_score) : null;

  return (
    <section>
      <p className="distribution-heading">🎯 Start here</p>
      <div className={`weak-priority-card learning-path-hero ${bandClass}`}>
        <div className="weak-priority-card-header">
          <span className="learning-path-hero-index">01</span>
          <span className={`band-dot ${bandClass}`} />
          <h3>{step.chapter_name}</h3>
          <span className={`band-badge ${bandClass}`}>{STATUS_LABEL[step.status].toUpperCase()}</span>
        </div>

        <div className="mastery-bar-row">
          <span>Your mastery</span>
          <span>{pct}%</span>
        </div>
        <MasteryBar pct={pct} colorClass={bandClass} />

        <p className="weak-priority-meta">
          {step.n_attempts} question{step.n_attempts === 1 ? "" : "s"} &middot;{" "}
          {Math.round((step.raw_accuracy ?? 0) * 100)}% accuracy
        </p>

        <div className="reason-chip-row">
          <ReasonChip label="Mastery" value={`${pct}%`} />
          {step.n_attempts !== null && <ReasonChip label={evidenceLabel(step.n_attempts)} value={`${step.n_attempts}q`} />}
          {delta !== null && (
            <ReasonChip label="vs. subject average" value={`${delta > 0 ? "↑" : "↓"} ${Math.abs(delta)}%`} />
          )}
          {impact && <ReasonChip label="Improvement potential" value={impact} />}
        </div>

        <div className="learning-path-recommendation">
          <p className="learning-path-recommendation-label">Why this is recommended</p>
          <p>{step.explanation}</p>
        </div>

        <div className="learning-path-hero-actions">
          {(step.has_notes || step.has_video) && (
            <button
              type="button"
              className="cta-button-secondary"
              onClick={() => navigate(`/chapter/${step.chapter_id}/learn`)}
            >
              Review Notes
            </button>
          )}
          <button
            type="button"
            className="cta-button"
            onClick={() =>
              navigate(
                courseId !== null
                  ? `/quick-practice/${courseId}/${step.chapter_id}`
                  : `/chapter/${step.chapter_id}`,
              )
            }
          >
            Start Practice <ArrowRight size={16} strokeWidth={2.5} />
          </button>
        </div>
      </div>
    </section>
  );
}

function RoadmapRow({
  step,
  index,
  isLast,
  courseId,
}: {
  step: LearningPathStep;
  index: number;
  isLast: boolean;
  courseId: number | null;
}) {
  const navigate = useNavigate();
  const state = roadmapState(step);
  const StateIcon = ROADMAP_STATE_ICON[state];
  const bandClass = STATUS_CLASS[step.status];

  return (
    <li className="roadmap-item">
      <div className="roadmap-connector">
        <span className={`roadmap-dot ${bandClass}`} />
        {!isLast && <span className="roadmap-line" />}
      </div>
      <div className="roadmap-item-body">
        <span className="roadmap-index">{String(index + 1).padStart(2, "0")}</span>
        <div className="roadmap-item-main">
          <Link to={`/chapter/${step.chapter_id}`} className="roadmap-chapter-name">
            {step.chapter_name}
          </Link>
          <span className={`roadmap-state-badge ${ROADMAP_STATE_CLASS[state]}`}>
            <StateIcon size={13} strokeWidth={2.25} />
            {state}
          </span>
        </div>
        <button
          type="button"
          className="cta-button-secondary roadmap-start-btn"
          onClick={() =>
            navigate(
              courseId !== null
                ? `/quick-practice/${courseId}/${step.chapter_id}`
                : `/chapter/${step.chapter_id}`,
            )
          }
        >
          Start <ArrowRight size={13} strokeWidth={2.5} />
        </button>
      </div>
    </li>
  );
}

const CYCLE_STEPS = ["Review", "Practice", "Retest", "Analyze", "Path updated"];

function LearningCycle() {
  return (
    <section className="learning-cycle-section">
      <p className="distribution-heading">How your path works</p>
      <div className="learning-cycle">
        {CYCLE_STEPS.map((label, i) => (
          <div key={label} className="learning-cycle-step-wrap">
            <span className="learning-cycle-step">{label}</span>
            {i < CYCLE_STEPS.length - 1 && <ArrowRight size={14} strokeWidth={2} className="learning-cycle-arrow" />}
          </div>
        ))}
      </div>
      <p className="learning-cycle-note">
        <Repeat size={13} strokeWidth={2} /> Every practice session updates your evidence, so this path re-ranks itself
        the next time you visit.
      </p>
    </section>
  );
}

export default function LearningPathPage() {
  const [path, setPath] = useState<LearningPathStep[] | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [courseId, setCourseId] = useState<number | null>(null);

  useEffect(() => {
    practiceApi
      .learningPath()
      .then(setPath)
      .catch((err) => setError(err instanceof ApiError ? err.message : "Could not load your learning path."));
    // Best-effort: resolves which course to send "Start Practice" links to
    // via recent session history - if this fails, links fall back to the
    // chapter detail page instead of jumping straight into practice.
    practiceApi
      .performanceMe()
      .then((p) => {
        const recent = p.session_history[0];
        if (recent) setCourseId(recent.course_id);
      })
      .catch(() => undefined);
  }, []);

  const evidencedSteps = useMemo(() => (path ?? []).filter((s) => s.status !== "not_started"), [path]);
  const notStartedCount = useMemo(() => (path ?? []).filter((s) => s.status === "not_started").length, [path]);
  const startHere = evidencedSteps[0]?.status === "High" || evidencedSteps[0]?.status === "Medium" ? evidencedSteps[0] : null;
  // The roadmap is a near-term study plan, not an exhaustive audit - that's
  // what Weak Areas is for. Capping it keeps it a "here's what's next"
  // sequence instead of a scroll through every chapter ever attempted.
  const visibleRoadmap = evidencedSteps.slice(0, 10);
  const remainingRoadmapCount = evidencedSteps.length - visibleRoadmap.length;

  if (error) return <p className="page-error">{error}</p>;
  if (path === null)
    return (
      <div className="dashboard-page">
        <h1>Your Learning Path</h1>
        <EvidenceListSkeleton />
      </div>
    );

  if (path.length === 0) {
    return (
      <div className="empty-state">
        <h1>Your Learning Path</h1>
        <p>Practice a chapter first to unlock a personalized learning sequence.</p>
        <Link to="/chapters" className="cta-button">
          Start practising
        </Link>
      </div>
    );
  }

  return (
    <div className="dashboard-page">
      <h1>Your Learning Path</h1>
      <p className="dashboard-subtitle">
        A personalized roadmap based on your performance. Start with the areas that will make the biggest difference.
      </p>

      <GoalCard path={path} />

      {startHere && <StartHereCard step={startHere} courseId={courseId} />}

      {evidencedSteps.length > 0 && (
        <section className="roadmap-section">
          <p className="distribution-heading">Your roadmap</p>
          <ol className="roadmap-list">
            {visibleRoadmap.map((step, i) => (
              <RoadmapRow key={step.chapter_id} step={step} index={i} isLast={i === visibleRoadmap.length - 1} courseId={courseId} />
            ))}
          </ol>
          {remainingRoadmapCount > 0 && (
            <p className="roadmap-not-started-note">
              +{remainingRoadmapCount} more chapter{remainingRoadmapCount === 1 ? "" : "s"} you've practised - see the
              full sortable list in <Link to="/chapter-analysis">Chapter Analysis</Link>.
            </p>
          )}
          {notStartedCount > 0 && (
            <p className="roadmap-not-started-note">
              {notStartedCount} more chapter{notStartedCount === 1 ? "" : "s"} in your course{notStartedCount === 1 ? "" : "s"}{" "}
              {notStartedCount === 1 ? "hasn't" : "haven't"} been attempted yet -{" "}
              <Link to="/chapters">browse them in Practice</Link>.
            </p>
          )}
        </section>
      )}

      <LearningCycle />
    </div>
  );
}
