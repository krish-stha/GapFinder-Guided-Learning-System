import { useCallback, useEffect, useRef, useState } from "react";
import { useParams, useNavigate, useSearchParams, Link } from "react-router-dom";
import { practiceApi } from "../api/practice";
import { ApiError } from "../api/client";
import { useStreak } from "../context/StreakContext";
import { useAuth } from "../context/AuthContext";
import ChapterEvidenceCard from "../components/ChapterEvidenceCard";
import AnimatedNumber from "../components/AnimatedNumber";
import HtmlWithKatex from "../components/HtmlWithKatex";
import { markStepTwoPending } from "../utils/stepTwoBanner";
import type { Question, QuestionState, FinishSessionResult } from "../types";

// Both the course-wide mock test and a single-chapter test share the exact
// same "timed, mark-for-review, deferred feedback" pattern - a chapter
// with fewer scoreable questions than requested just gets however many it
// has (the backend computes the timer off the actual drawn count, not the
// request, so a shorter draw gets a proportionally shorter clock
// automatically).
// Ignored server-side once a quiz_template_id is set - /start overrides
// whatever num_questions is sent with the template's own fixed count.
const TEMPLATE_PLACEHOLDER_QUESTIONS = 50;
// Chapter tests let the student pick how many questions before starting,
// since a single chapter's pool is usually much smaller than a course-wide
// test's and 50 can be overkill for a quick check.
const CHAPTER_TEST_QUESTION_COUNTS = [10, 20, 30, 50];
// Course-wide mixed draw (mock test and diagnostic both use this) - same
// picker either way, up to the full 50-question length the "Full Mock
// Test"/diagnostic cards advertise as their max.
const COURSE_WIDE_QUESTION_COUNTS = [10, 20, 30, 40, 50];
// Quick Practice - deliberately shorter options than a full test, whether
// it's scoped to one chapter or a mixed draw across the course.
const QUICK_PRACTICE_COUNTS = [5, 10, 15, 20];
// Resync the countdown against the server periodically to correct client
// clock drift and to notice if the deadline already passed server-side
// (e.g. another tab, or the tab was backgrounded past the limit).
const RESYNC_INTERVAL_MS = 20_000;
const LOW_TIME_WARNING_SECONDS = 5 * 60;

// Question bodies/options only ever come from /start, and /state doesn't
// re-send them - so a refresh mid-exam needs the original question list
// cached client-side to resume without starting an entirely new session
// (which would silently abandon the in-progress one). selected_index and
// marked_for_review are safe to trust from a fresh /state call instead.
interface StoredSession {
  sessionId: number;
  questions: Question[];
  timeLimitSeconds: number | null;
}

// Keyed by purpose too, not just course/chapter - a mock test and a
// diagnostic for the same course-wide (chapterId=null) draw would otherwise
// share one storage slot, so resuming after a refresh could silently pick
// up an abandoned mock test under the "Diagnostic assessment" heading
// instead of actually starting a diagnostic (defeating the whole point of
// purpose="diagnostic" existing as a distinct thing to complete).
function storageKey(purpose: string, courseId: string, chapterId: string | null): string {
  return `gls_exam_${purpose}_${courseId}_${chapterId ?? "mixed"}`;
}

function loadStoredSession(purpose: string, courseId: string, chapterId: string | null): StoredSession | null {
  try {
    const raw = sessionStorage.getItem(storageKey(purpose, courseId, chapterId));
    return raw ? (JSON.parse(raw) as StoredSession) : null;
  } catch {
    return null;
  }
}

function saveStoredSession(purpose: string, courseId: string, chapterId: string | null, stored: StoredSession) {
  try {
    sessionStorage.setItem(storageKey(purpose, courseId, chapterId), JSON.stringify(stored));
  } catch {
    // storage unavailable (e.g. private browsing) - resume-on-refresh just won't work
  }
}

function clearStoredSession(purpose: string, courseId: string, chapterId: string | null) {
  try {
    sessionStorage.removeItem(storageKey(purpose, courseId, chapterId));
  } catch {
    // ignore
  }
}

type LoadState =
  | { status: "loading" }
  | { status: "picking-count" }
  | { status: "error"; message: string }
  | { status: "active" }
  | { status: "finished"; result: FinishSessionResult };

interface ExamPageProps {
  // "diagnostic" powers the one-time baseline assessment that Progress &
  // Improvement's before/after comparison and the "Diagnostic Complete"
  // achievement are keyed off - reuses this exact same mixed-draw/deferred-
  // feedback/untimed-vs-timed machinery (the backend already treats
  // "diagnostic" identically to "mock_test" except for the timer), just
  // under a distinct purpose value and route.
  // "practice" powers Quick Practice - same question-tracking/mark-for-
  // review/prev-next/deferred-feedback/submit experience as a mock test,
  // just untimed and with its own (shorter) length options, reached via
  // /quick-practice/:courseId(/:chapterId).
  purpose?: "mock_test" | "diagnostic" | "practice";
}

export default function ExamPage({ purpose = "mock_test" }: ExamPageProps) {
  const { courseId, chapterId: chapterIdParam } = useParams();
  const chapterId = chapterIdParam ?? null;
  const isChapterTest = chapterId !== null;
  const isDiagnostic = purpose === "diagnostic";
  const isPractice = purpose === "practice";
  const [searchParams] = useSearchParams();
  const templateId = searchParams.get("template");
  const { refreshStreak } = useStreak();
  const { student } = useAuth();

  const [state, setState] = useState<LoadState>({ status: "loading" });
  const [sessionId, setSessionId] = useState<number | null>(null);
  const [questions, setQuestions] = useState<Question[]>([]);
  const [answers, setAnswers] = useState<Record<number, number | null>>({});
  const [statusByQuestion, setStatusByQuestion] = useState<Record<number, QuestionState>>({});
  const [current, setCurrent] = useState(0);
  const [secondsRemaining, setSecondsRemaining] = useState<number | null>(null);
  const [confirmingSubmit, setConfirmingSubmit] = useState(false);
  const [submitting, setSubmitting] = useState(false);

  const finishingRef = useRef(false);

  const doFinish = useCallback(
    async (sid: number) => {
      if (finishingRef.current) return;
      finishingRef.current = true;
      try {
        const result = await practiceApi.finish(sid);
        if (courseId) clearStoredSession(purpose, courseId, chapterId);
        if (isDiagnostic && student) markStepTwoPending(student.id);
        setState({ status: "finished", result });
        refreshStreak();
      } catch (err) {
        setState({
          status: "error",
          message: err instanceof ApiError ? err.message : "Could not submit the test.",
        });
      } finally {
        finishingRef.current = false;
      }
    },
    [courseId, chapterId, purpose, isDiagnostic, student, refreshStreak],
  );

  const startSession = useCallback(
    async (numQuestions: number) => {
      if (!courseId) return;
      setState({ status: "loading" });
      try {
        const res = await practiceApi.start({
          course_id: Number(courseId),
          chapter_id: chapterId ? Number(chapterId) : null,
          num_questions: numQuestions,
          purpose,
          ...(templateId ? { quiz_template_id: Number(templateId) } : {}),
        });
        saveStoredSession(purpose, courseId, chapterId, {
          sessionId: res.session_id, questions: res.questions, timeLimitSeconds: res.time_limit_seconds,
        });
        setSessionId(res.session_id);
        setQuestions(res.questions);
        setSecondsRemaining(res.time_limit_seconds);
        setState({ status: "active" });
      } catch (err) {
        setState({
          status: "error",
          message: err instanceof ApiError ? err.message : "Could not start this test.",
        });
      }
    },
    [courseId, chapterId, purpose, templateId],
  );

  // On mount: resume an already-in-progress session if one is stored,
  // otherwise either start immediately (course-wide mock test/diagnostic,
  // or a quiz template which already fixes its own question count) or -
  // for a fresh chapter test - stop and let the student pick how many
  // questions first, via the "picking-count" screen below.
  useEffect(() => {
    if (!courseId) return;
    let cancelled = false;

    async function init() {
      const stored = loadStoredSession(purpose, courseId!, chapterId);
      if (stored) {
        try {
          const s = await practiceApi.state(stored.sessionId);
          if (cancelled) return;
          if (s.status === "in_progress") {
            const nextAnswers: Record<number, number | null> = {};
            const byQ: Record<number, QuestionState> = {};
            s.questions.forEach((q) => {
              byQ[q.question_id] = q;
              if (q.selected_index !== null) nextAnswers[q.question_id] = q.selected_index;
            });
            setSessionId(stored.sessionId);
            setQuestions(stored.questions);
            setSecondsRemaining(s.seconds_remaining);
            setAnswers(nextAnswers);
            setStatusByQuestion(byQ);
            setState({ status: "active" });
            return;
          }
          clearStoredSession(purpose, courseId!, chapterId);
        } catch {
          clearStoredSession(purpose, courseId!, chapterId);
        }
      }

      if (cancelled) return;
      // A quiz template already fixes its own count - everything else
      // (chapter tests, the course-wide mock test, and the diagnostic) lets
      // the student pick a length first.
      if (!templateId) {
        setState({ status: "picking-count" });
        return;
      }
      await startSession(TEMPLATE_PLACEHOLDER_QUESTIONS);
    }

    void init();
    return () => {
      cancelled = true;
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [courseId, chapterId, purpose, templateId]);

  // Local 1s countdown tick.
  useEffect(() => {
    if (state.status !== "active" || secondsRemaining === null) return;
    if (secondsRemaining <= 0) {
      if (sessionId !== null) void doFinish(sessionId);
      return;
    }
    const id = setTimeout(() => setSecondsRemaining((s) => (s !== null ? s - 1 : s)), 1000);
    return () => clearTimeout(id);
  }, [state.status, secondsRemaining, sessionId, doFinish]);

  // Periodic server resync - corrects drift and catches a deadline that
  // already passed server-side (the server is the real authority, this
  // countdown is purely cosmetic).
  useEffect(() => {
    if (state.status !== "active" || sessionId === null) return;
    const id = setInterval(async () => {
      try {
        const s = await practiceApi.state(sessionId);
        if (s.status !== "in_progress") {
          void doFinish(sessionId);
          return;
        }
        setSecondsRemaining(s.seconds_remaining);
        const byQ: Record<number, QuestionState> = {};
        s.questions.forEach((q) => (byQ[q.question_id] = q));
        setStatusByQuestion(byQ);
      } catch {
        // transient network issue - next tick will retry
      }
    }, RESYNC_INTERVAL_MS);
    return () => clearInterval(id);
  }, [state.status, sessionId, doFinish]);

  const pageTitle = isDiagnostic
    ? "Diagnostic assessment"
    : isPractice
      ? "Quick Practice"
      : isChapterTest
        ? "Chapter test"
        : "Mock test";
  const startingLabel = isDiagnostic
    ? "Starting your diagnostic assessment…"
    : isPractice
      ? "Starting your quick practice…"
      : isChapterTest
        ? "Starting your chapter test…"
        : "Starting your mock test…";

  if (state.status === "loading") return <p className="page-loading">{startingLabel}</p>;

  if (state.status === "picking-count")
    return (
      <div className="question-count-picker">
        <h1>{pageTitle}</h1>
        <p className="dashboard-subtitle">How many questions do you want in this test?</p>
        <div className="question-count-options">
          {(isPractice ? QUICK_PRACTICE_COUNTS : isChapterTest ? CHAPTER_TEST_QUESTION_COUNTS : COURSE_WIDE_QUESTION_COUNTS).map((n) => (
            <button key={n} type="button" className="question-count-btn" onClick={() => void startSession(n)}>
              {n} questions
            </button>
          ))}
        </div>
        <Link to="/chapters">Cancel</Link>
      </div>
    );

  if (state.status === "error")
    return (
      <div className="page-error">
        <p>{state.message}</p>
        <Link to="/chapters">Back to chapters</Link>
      </div>
    );

  if (state.status === "finished")
    return <ExamResults result={state.result} isChapterTest={isChapterTest} isDiagnostic={isDiagnostic} isPractice={isPractice} />;

  const question = questions[current];
  const answeredCount = Object.values(answers).filter((v) => v !== undefined).length;
  const unansweredCount = questions.length - answeredCount;

  async function selectAnswer(selectedIndex: number) {
    if (sessionId === null || !question) return;
    setAnswers((prev) => ({ ...prev, [question.id]: selectedIndex }));
    setStatusByQuestion((prev) => ({
      ...prev,
      [question.id]: {
        question_id: question.id, position: question.position, answered: true,
        marked_for_review: prev[question.id]?.marked_for_review ?? false,
        selected_index: selectedIndex,
      },
    }));
    try {
      await practiceApi.answer(sessionId, { question_id: question.id, selected_index: selectedIndex });
    } catch (err) {
      if (err instanceof ApiError && err.status === 409) void doFinish(sessionId);
    }
  }

  async function toggleMarked() {
    if (sessionId === null || !question) return;
    try {
      const res = await practiceApi.toggleReview(sessionId, question.id);
      setStatusByQuestion((prev) => ({
        ...prev,
        [question.id]: {
          question_id: question.id,
          position: question.position,
          answered: prev[question.id]?.answered ?? answers[question.id] !== undefined,
          marked_for_review: res.marked_for_review,
          selected_index: prev[question.id]?.selected_index ?? answers[question.id] ?? null,
        },
      }));
    } catch (err) {
      if (err instanceof ApiError && err.status === 409) void doFinish(sessionId);
    }
  }

  function paletteClass(q: Question): string {
    const st = statusByQuestion[q.id];
    const marked = st?.marked_for_review ?? false;
    const answered = st?.answered ?? answers[q.id] !== undefined;
    const classes = ["palette-btn"];
    if (q.position === current) classes.push("current");
    if (marked) classes.push("marked");
    else if (answered) classes.push("answered");
    else classes.push("unanswered");
    return classes.join(" ");
  }

  const lowTime = secondsRemaining !== null && secondsRemaining <= LOW_TIME_WARNING_SECONDS;

  return (
    <div className="exam-page">
      <header className="exam-header">
        <h1>{pageTitle}</h1>
        {secondsRemaining !== null && (
          <span className={`exam-timer${lowTime ? " exam-timer-low" : ""}`}>{formatClock(secondsRemaining)}</span>
        )}
      </header>

      <div className="exam-layout">
        <nav className="exam-palette" aria-label="Question navigator">
          {questions.map((q) => (
            <button key={q.id} type="button" className={paletteClass(q)} onClick={() => setCurrent(q.position)}>
              {q.position + 1}
            </button>
          ))}
          <div className="exam-palette-legend">
            <span><i className="legend-dot legend-answered" /> Answered</span>
            <span><i className="legend-dot legend-marked" /> Marked</span>
            <span><i className="legend-dot legend-unanswered" /> Unanswered</span>
          </div>
        </nav>

        <div className="exam-question-panel">
          <p className="practice-progress">
            Question {current + 1} of {questions.length}
          </p>
          {question && (
            <>
              <HtmlWithKatex className="question-body" html={question.body} />
              <ul className="answer-list">
                {question.answers.map((answer, i) => (
                  <li key={i} className={`answer-option${answers[question.id] === i ? " selected" : ""}`}>
                    <label>
                      <input
                        type="radio"
                        name={`q-${question.id}`}
                        checked={answers[question.id] === i}
                        onChange={() => selectAnswer(i)}
                      />
                      <HtmlWithKatex as="span" html={answer} />
                    </label>
                  </li>
                ))}
              </ul>
            </>
          )}

          <div className="exam-nav">
            <button type="button" disabled={current === 0} onClick={() => setCurrent((c) => c - 1)}>
              Previous
            </button>
            <button
              type="button"
              className={(question && statusByQuestion[question.id]?.marked_for_review) ? "exam-mark-btn active" : "exam-mark-btn"}
              onClick={toggleMarked}
            >
              {(question && statusByQuestion[question.id]?.marked_for_review) ? "Unmark" : "Mark for review"}
            </button>
            <button type="button" disabled={current === questions.length - 1} onClick={() => setCurrent((c) => c + 1)}>
              Next
            </button>
            <button type="button" className="exam-submit-btn" onClick={() => setConfirmingSubmit(true)}>
              Submit test
            </button>
          </div>
        </div>
      </div>

      {confirmingSubmit && (
        <div className="exam-confirm-overlay">
          <div className="exam-confirm-panel">
            <h2>
              Submit{" "}
              {isDiagnostic
                ? "diagnostic assessment"
                : isPractice
                  ? "quick practice"
                  : isChapterTest
                    ? "chapter test"
                    : "mock test"}
              ?
            </h2>
            <p>
              {answeredCount} of {questions.length} answered
              {unansweredCount > 0 && ` - ${unansweredCount} left unanswered`}. Once submitted you can't go back and
              change any answers.
            </p>
            <div className="exam-confirm-actions">
              <button type="button" className="skip-button" onClick={() => setConfirmingSubmit(false)} disabled={submitting}>
                Keep working
              </button>
              <button
                type="button"
                className="exam-submit-btn"
                disabled={submitting}
                onClick={async () => {
                  if (sessionId === null) return;
                  setSubmitting(true);
                  await doFinish(sessionId);
                  setSubmitting(false);
                }}
              >
                Submit
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

function formatClock(totalSeconds: number): string {
  const m = Math.floor(totalSeconds / 60);
  const s = totalSeconds % 60;
  return `${m}:${s.toString().padStart(2, "0")}`;
}

function ExamResults({
  result,
  isChapterTest,
  isDiagnostic,
  isPractice,
}: {
  result: FinishSessionResult;
  isChapterTest: boolean;
  isDiagnostic: boolean;
  isPractice: boolean;
}) {
  const navigate = useNavigate();
  const title = isDiagnostic
    ? "Diagnostic assessment complete"
    : isPractice
      ? "Quick practice complete"
      : isChapterTest
        ? "Chapter test complete"
        : "Mock test complete";
  return (
    <div className="session-summary exam-results">
      <h1>{title}</h1>
      <p className="summary-score">
        <AnimatedNumber value={result.correct_count} /> / {result.total_questions} correct
        {result.percentage !== null && (
          <>
            {" "}
            (<AnimatedNumber value={Math.round(result.percentage)} suffix="%" />)
          </>
        )}
      </p>

      {result.chapter_breakdown.length > 0 && (
        <section className="detail-section exam-breakdown">
          <h2>How you did, by chapter</h2>
          <p className="dashboard-subtitle">
            Reflects your full history in each chapter this test covered, not just today's answers.
          </p>
          <div className="evidence-list">
            {result.chapter_breakdown.map((e) => (
              <ChapterEvidenceCard key={e.chapter_id} evidence={e} />
            ))}
          </div>
        </section>
      )}

      <section className="detail-section exam-review">
        <h2>Question review</h2>
        <ul className="exam-review-list">
          {result.review.map((q) => (
            <li key={q.question_id} className={q.is_correct ? "exam-review-item correct" : "exam-review-item incorrect"}>
              <p className="exam-review-meta">
                Q{q.position + 1} · {q.chapter_name} · {q.is_correct ? "Correct" : q.selected_index === null ? "Unanswered" : "Incorrect"}
              </p>
              <HtmlWithKatex className="question-body" html={q.body} />
              <ul className="answer-list">
                {q.answers.map((answer, i) => {
                  const isSelected = q.selected_index === i;
                  const isCorrectAnswer = q.correct_answer === i;
                  const classes = [
                    "answer-option",
                    isCorrectAnswer ? "correct" : "",
                    isSelected && !isCorrectAnswer ? "incorrect" : "",
                  ].filter(Boolean).join(" ");
                  return (
                    <li key={i} className={classes}>
                      <label>
                        <input type="radio" checked={isSelected} disabled readOnly />
                        <HtmlWithKatex as="span" html={answer} />
                      </label>
                    </li>
                  );
                })}
              </ul>
              {q.explanation && <p className="exam-review-explanation">{q.explanation}</p>}
            </li>
          ))}
        </ul>
      </section>

      <div className="summary-actions">
        <button type="button" className="cta-button" onClick={() => navigate("/dashboard")}>
          {isDiagnostic ? "See your personalised weak-chapter list →" : "View updated recommendations"}
        </button>
        <Link to="/chapters">Back to chapters</Link>
      </div>
    </div>
  );
}
