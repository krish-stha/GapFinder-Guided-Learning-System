import { useEffect, useMemo, useRef, useState } from "react";
import { useNavigate } from "react-router-dom";
import { Target, BookOpen, ClipboardList, Clock, ArrowRight, Search } from "lucide-react";
import { contentApi } from "../api/content";
import { practiceApi } from "../api/practice";
import { ApiError } from "../api/client";
import { useAuth } from "../context/AuthContext";
import { TreeSkeleton } from "../components/Skeletons";
import { CourseGrid, CourseHeaderBar, matchCourseForStudent, subjectIcon } from "../components/CoursePicker";
import ContinuePracticingRow from "../components/ContinuePracticingRow";
import { BAND_CLASS, MasteryBar, ChapterMiniCard, pctColorClass } from "../components/MasteryMiniCard";
import { buildTree, type TreeNode } from "../utils/tree";
import type { ChapterEvidence, Course, PriorityBand, QuizTemplate, RecentChapter } from "../types";

function flattenChapters(node: TreeNode): TreeNode[] {
  if (node.type === "Chapter") return [node];
  return node.children.flatMap(flattenChapters);
}

interface SubjectStats {
  node: TreeNode;
  chapterCount: number;
  weakCount: number;
  avgMastery: number | null;
}

function computeSubjectStats(tree: TreeNode[], evidenceByChapter: Map<number, ChapterEvidence>): SubjectStats[] {
  return tree.map((subjectNode) => {
    const chapters = flattenChapters(subjectNode);
    const evidenced = chapters.map((c) => evidenceByChapter.get(c.id)).filter((e): e is ChapterEvidence => !!e);
    const weakCount = evidenced.filter((e) => e.priority_band === "High" || e.priority_band === "Medium").length;
    const avgMastery = evidenced.length
      ? evidenced.reduce((sum, e) => sum + e.mastery_estimate, 0) / evidenced.length
      : null;
    return { node: subjectNode, chapterCount: chapters.length, weakCount, avgMastery };
  });
}

function ModeCard({
  icon: Icon,
  label,
  description,
  cta,
  onClick,
}: {
  icon: typeof Target;
  label: string;
  description: string;
  cta: string;
  onClick: () => void;
}) {
  return (
    <button type="button" className="mode-card" onClick={onClick}>
      <span className="mode-card-icon">
        <Icon size={20} strokeWidth={2} />
      </span>
      <h3>{label}</h3>
      <p>{description}</p>
      <span className="mode-card-cta">
        {cta} <ArrowRight size={14} strokeWidth={2.5} />
      </span>
    </button>
  );
}

function MockTestCard({ course, templates }: { course: Course; templates: QuizTemplate[] }) {
  const navigate = useNavigate();
  return (
    <div className="mock-test-card">
      <span className="mock-test-card-icon">
        <ClipboardList size={22} strokeWidth={2} />
      </span>
      <div className="mock-test-card-body">
        <h3>Full Mock Test</h3>
        <p>Test yourself across every subject in {course.name} with a mixed, timed exam.</p>
        <div className="mock-test-card-meta">
          <span>10-50 Questions</span>
          <span>
            <Clock size={14} strokeWidth={2} /> Up to 60 min
          </span>
          <span>
            <Target size={14} strokeWidth={2} /> All Subjects
          </span>
        </div>
      </div>
      <button type="button" className="cta-button mock-test-card-cta" onClick={() => navigate(`/mock-test/${course.id}`)}>
        Start Mock Test <ArrowRight size={16} strokeWidth={2.5} />
      </button>
      {templates.length > 0 && (
        <div className="teacher-quiz-list">
          <p className="distribution-heading">Teacher-set quizzes</p>
          {templates.map((t) => (
            <button
              key={t.id}
              type="button"
              className="teacher-quiz-btn"
              onClick={() => navigate(`/mock-test/${course.id}?template=${t.id}`)}
            >
              {t.title} ({t.num_questions} questions{t.difficulty_label ? `, ${t.difficulty_label}` : ""})
            </button>
          ))}
        </div>
      )}
    </div>
  );
}

function SubjectCard({ stats, onOpen }: { stats: SubjectStats; onOpen: () => void }) {
  const Icon = subjectIcon(stats.node.name);
  const pct = stats.avgMastery !== null ? Math.round(stats.avgMastery * 100) : null;
  return (
    <button type="button" className="subject-stat-card" onClick={onOpen}>
      <span className="subject-stat-icon">
        <Icon size={20} strokeWidth={1.75} />
      </span>
      <h3>{stats.node.name}</h3>
      {pct !== null ? (
        <>
          <p className="subject-stat-pct">{pct}% mastery</p>
          <MasteryBar pct={pct} colorClass={pctColorClass(stats.avgMastery!)} />
        </>
      ) : (
        <p className="subject-stat-pct subject-stat-muted">Not started yet</p>
      )}
      <p className="subject-stat-meta">
        {stats.chapterCount} chapter{stats.chapterCount === 1 ? "" : "s"}
        {stats.weakCount > 0 && (
          <>
            {" "}
            &middot; <span className="subject-stat-weak">{stats.weakCount} weak</span>
          </>
        )}
      </p>
      <span className="cta-button-secondary subject-stat-cta">
        Practice <ArrowRight size={14} strokeWidth={2.5} />
      </span>
    </button>
  );
}

const BAND_FILTERS: { value: string; label: string }[] = [
  { value: "all", label: "All" },
  { value: "High", label: "High priority" },
  { value: "Medium", label: "Medium priority" },
  { value: "Low", label: "Low priority" },
  { value: "not_started", label: "Not started" },
];

const BAND_RANK: Record<PriorityBand, number> = { High: 0, Medium: 1, Low: 2, "Insufficient evidence": 3 };

function ChapterRow({
  chapter,
  evidence,
  courseId,
  isCompleted,
}: {
  chapter: TreeNode;
  evidence: ChapterEvidence | undefined;
  courseId: number;
  isCompleted: boolean;
}) {
  const navigate = useNavigate();
  const bandClass = evidence ? (BAND_CLASS[evidence.priority_band] ?? "band-insufficient") : "band-insufficient";
  const pct = evidence ? Math.round(evidence.mastery_estimate * 100) : null;
  const isWeak = evidence && (evidence.priority_band === "High" || evidence.priority_band === "Medium");

  return (
    <li className={`chapter-practice-row ${bandClass}`}>
      <div className="chapter-practice-row-main">
        <span className={`band-dot ${bandClass}`} />
        <div className="chapter-practice-row-body">
          <div className="chapter-practice-row-heading">
            <h4>{chapter.name}</h4>
            {isCompleted && (
              <span className="chapter-read-badge" title="You marked this chapter's content as read">
                ✓ Read
              </span>
            )}
          </div>
          {evidence ? (
            <>
              <MasteryBar pct={pct!} colorClass={bandClass} />
              <p className="chapter-practice-row-meta">
                {pct}% mastery &middot; {evidence.n_attempts} attempts &middot; {Math.round(evidence.raw_accuracy * 100)}%
                accuracy
              </p>
              {isWeak && <p className="chapter-practice-row-reason">Recommended because this is a weak area</p>}
            </>
          ) : (
            <p className="chapter-practice-row-meta chapter-practice-row-muted">Not attempted yet</p>
          )}
        </div>
      </div>
      <div className="chapter-practice-row-actions">
        <button type="button" className="cta-button-secondary" onClick={() => navigate(`/chapter/${chapter.id}/learn`)}>
          Learn
        </button>
        <button
          type="button"
          className="cta-button"
          onClick={() => navigate(`/quick-practice/${courseId}/${chapter.id}`)}
        >
          Practice <ArrowRight size={14} strokeWidth={2.5} />
        </button>
      </div>
    </li>
  );
}

function SubjectDrilldown({
  subjectStats,
  courseId,
  evidenceByChapter,
  completedChapterIds,
  onBack,
}: {
  subjectStats: SubjectStats;
  courseId: number;
  evidenceByChapter: Map<number, ChapterEvidence>;
  completedChapterIds: Set<number>;
  onBack: () => void;
}) {
  const [query, setQuery] = useState("");
  const [bandFilter, setBandFilter] = useState("all");

  const chapters = useMemo(() => flattenChapters(subjectStats.node), [subjectStats.node]);

  const filtered = useMemo(() => {
    const q = query.trim().toLowerCase();
    return chapters
      .filter((c) => !q || c.name.toLowerCase().includes(q))
      .filter((c) => {
        if (bandFilter === "all") return true;
        const ev = evidenceByChapter.get(c.id);
        if (bandFilter === "not_started") return !ev;
        return ev?.priority_band === bandFilter;
      })
      .slice()
      .sort((a, b) => {
        const rankA = evidenceByChapter.get(a.id)?.priority_band;
        const rankB = evidenceByChapter.get(b.id)?.priority_band;
        return (rankA ? BAND_RANK[rankA] : 3) - (rankB ? BAND_RANK[rankB] : 3);
      });
  }, [chapters, query, bandFilter, evidenceByChapter]);

  return (
    <section className="chapter-drilldown">
      <button type="button" className="chapter-drilldown-back" onClick={onBack}>
        ← Back to subjects
      </button>
      <h2>{subjectStats.node.name}</h2>
      <p className="dashboard-subtitle">
        {subjectStats.avgMastery !== null
          ? `Your overall mastery: ${Math.round(subjectStats.avgMastery * 100)}%`
          : "You haven't practised any chapters in this subject yet."}
      </p>

      <div className="chapter-drilldown-controls">
        <label className="chapter-drilldown-search">
          <Search size={16} strokeWidth={2} />
          <input type="search" placeholder="Search chapters…" value={query} onChange={(e) => setQuery(e.target.value)} />
        </label>
        <select value={bandFilter} onChange={(e) => setBandFilter(e.target.value)}>
          {BAND_FILTERS.map((f) => (
            <option key={f.value} value={f.value}>
              {f.label}
            </option>
          ))}
        </select>
      </div>

      {filtered.length === 0 ? (
        <p className="page-loading">No chapters match.</p>
      ) : (
        <ul className="chapter-practice-list">
          {filtered.map((c) => (
            <ChapterRow
              key={c.id}
              chapter={c}
              evidence={evidenceByChapter.get(c.id)}
              courseId={courseId}
              isCompleted={completedChapterIds.has(c.id)}
            />
          ))}
        </ul>
      )}
    </section>
  );
}

export default function ChaptersPage() {
  const { student } = useAuth();
  const navigate = useNavigate();
  const [courses, setCourses] = useState<Course[] | null>(null);
  const [selectedCourse, setSelectedCourse] = useState<number | null>(null);
  const [showAllCourses, setShowAllCourses] = useState(false);
  const [tree, setTree] = useState<TreeNode[] | null>(null);
  const [evidence, setEvidence] = useState<ChapterEvidence[]>([]);
  const [completedChapterIds, setCompletedChapterIds] = useState<Set<number>>(new Set());
  const [recentChapters, setRecentChapters] = useState<RecentChapter[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [templates, setTemplates] = useState<QuizTemplate[]>([]);
  const [openSubjectId, setOpenSubjectId] = useState<number | null>(null);
  const subjectsRef = useRef<HTMLDivElement>(null);
  const mockTestRef = useRef<HTMLDivElement>(null);

  function scrollToBrowse() {
    setOpenSubjectId(null);
    // Deferred a tick so the subject grid (hidden while a drilldown is
    // open) has re-mounted before we measure/scroll to it.
    setTimeout(() => subjectsRef.current?.scrollIntoView({ behavior: "smooth", block: "start" }), 0);
  }

  function scrollToMockTest() {
    mockTestRef.current?.scrollIntoView({ behavior: "smooth", block: "start" });
  }

  useEffect(() => {
    contentApi
      .listCourses()
      .then(setCourses)
      .catch((err) => setError(err instanceof ApiError ? err.message : "Could not load courses."));
    // evidence/recent-chapters are best-effort - a fresh account with none
    // yet is a normal state, not an error worth surfacing here
    practiceApi.resultsMe().then(setEvidence).catch(() => undefined);
    practiceApi.recentChapters().then(setRecentChapters).catch(() => undefined);
    contentApi.completedChapterIds().then((ids) => setCompletedChapterIds(new Set(ids))).catch(() => undefined);
  }, []);

  const matchedCourse = useMemo(
    () => (courses ? matchCourseForStudent(courses, student?.grade ?? null, student?.stream ?? null) : null),
    [courses, student],
  );

  useEffect(() => {
    if (selectedCourse === null && matchedCourse !== null && !showAllCourses) {
      setSelectedCourse(matchedCourse.id);
    }
  }, [matchedCourse, selectedCourse, showAllCourses]);

  useEffect(() => {
    if (selectedCourse === null) return;
    setTree(null);
    setOpenSubjectId(null);
    contentApi
      .listSections(selectedCourse)
      .then((sections) => setTree(buildTree(sections)))
      .catch((err) => setError(err instanceof ApiError ? err.message : "Could not load chapters."));
    contentApi.quizTemplates(selectedCourse).then(setTemplates).catch(() => setTemplates([]));
  }, [selectedCourse]);

  const evidenceByChapter = useMemo(() => {
    const map = new Map<number, ChapterEvidence>();
    evidence.forEach((e) => map.set(e.chapter_id, e));
    return map;
  }, [evidence]);

  // The Recommended-for-you panel draws from the student's FULL evidence
  // (every course they've ever practiced in), not just the selected course -
  // this set lets it know which of those chapters can link straight into a
  // quick-practice session for the currently selected course vs falling
  // back to the chapter detail page.
  const chapterIdsInTree = useMemo(() => {
    if (!tree) return new Set<number>();
    return new Set(tree.flatMap(flattenChapters).map((c) => c.id));
  }, [tree]);

  function recommendedLinkFor(chapterId: number): string {
    return selectedCourse !== null && chapterIdsInTree.has(chapterId)
      ? `/quick-practice/${selectedCourse}/${chapterId}`
      : `/chapter/${chapterId}`;
  }

  const recommended = useMemo(
    () => evidence.filter((e) => e.priority_band === "High" || e.priority_band === "Medium").slice(0, 3),
    [evidence],
  );

  const subjectStats = useMemo(() => (tree ? computeSubjectStats(tree, evidenceByChapter) : []), [tree, evidenceByChapter]);
  const openSubject = openSubjectId !== null ? subjectStats.find((s) => s.node.id === openSubjectId) ?? null : null;

  if (error) return <p className="page-error">{error}</p>;
  if (courses === null) return <p className="page-loading">Loading courses…</p>;

  const selectedCourseObj = selectedCourse !== null ? courses.find((c) => c.id === selectedCourse) ?? null : null;

  function chooseCourse(id: number) {
    setShowAllCourses(false);
    setSelectedCourse(id);
  }

  return (
    <div className="chapters-page">
      <header className="practice-header">
        <div>
          <h1>Practice</h1>
          <p className="dashboard-subtitle">Strengthen weak areas, master chapters, and track your progress.</p>
        </div>
        {selectedCourseObj !== null && (
          <CourseHeaderBar
            course={selectedCourseObj}
            onChange={() => {
              setShowAllCourses(true);
              setSelectedCourse(null);
            }}
          />
        )}
      </header>

      {selectedCourseObj === null ? (
        <>
          <p className="distribution-heading">Choose what you want to improve</p>
          <CourseGrid courses={courses} onSelect={chooseCourse} />
        </>
      ) : (
        <>
          {recommended.length > 0 && (
            <section className="recommended-panel">
              <div className="recommended-panel-header">
                <span className="recommended-panel-icon">
                  <Target size={18} strokeWidth={2} />
                </span>
                <div>
                  <p className="recommended-panel-title">Recommended for you</p>
                  <p className="recommended-panel-desc">
                    Based on your recent performance, these chapters need the most attention.
                  </p>
                </div>
              </div>
              <div className="recommended-panel-grid">
                {recommended.map((e) => (
                  <ChapterMiniCard key={e.chapter_id} evidence={e} linkTo={recommendedLinkFor(e.chapter_id)} />
                ))}
              </div>
            </section>
          )}

          <ContinuePracticingRow chapters={recentChapters} />

          <p className="distribution-heading">What do you want to do?</p>
          <div className="practice-mode-grid">
            <ModeCard
              icon={Target}
              label="Weak Areas"
              description="Focus on what needs work."
              cta="Start"
              onClick={() => navigate("/weak-areas")}
            />
            <ModeCard
              icon={BookOpen}
              label="By Chapter"
              description="Choose exactly what to study."
              cta="Browse"
              onClick={scrollToBrowse}
            />
            <ModeCard
              icon={ClipboardList}
              label="Mock Test"
              description="Test yourself under pressure."
              cta="Jump to"
              onClick={scrollToMockTest}
            />
          </div>

          <div ref={mockTestRef}>
            <MockTestCard course={selectedCourseObj} templates={templates} />
          </div>

          {tree === null && <TreeSkeleton />}

          {tree !== null && openSubject === null && (
            <div ref={subjectsRef}>
              <p className="distribution-heading">Your subjects</p>
              <div className="subject-card-grid">
                {subjectStats.map((s) => (
                  <SubjectCard key={s.node.id} stats={s} onOpen={() => setOpenSubjectId(s.node.id)} />
                ))}
              </div>
            </div>
          )}

          {openSubject && (
            <SubjectDrilldown
              subjectStats={openSubject}
              courseId={selectedCourse!}
              evidenceByChapter={evidenceByChapter}
              completedChapterIds={completedChapterIds}
              onBack={() => setOpenSubjectId(null)}
            />
          )}
        </>
      )}
    </div>
  );
}
