import { useEffect, useState, type FormEvent } from "react";
import { contentApi } from "../api/content";
import { teacherApi } from "../api/teacher";
import { ApiError } from "../api/client";
import ChapterTreePicker from "../components/ChapterTreePicker";
import { CourseGrid, CourseHeaderBar } from "../components/CoursePicker";
import type { Chapter, Course, QuizTemplate } from "../types";

const DIFFICULTIES = ["Easy", "Medium", "Hard"] as const;

export default function AssessmentManagementPage() {
  const [courses, setCourses] = useState<Course[] | null>(null);
  const [courseId, setCourseId] = useState<number | null>(null);
  const [sections, setSections] = useState<Chapter[]>([]);
  const [selectedChapter, setSelectedChapter] = useState<Chapter | null>(null);
  const [templates, setTemplates] = useState<QuizTemplate[]>([]);
  const [message, setMessage] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const [qBody, setQBody] = useState("");
  const [qOptions, setQOptions] = useState(["", "", "", ""]);
  const [qCorrect, setQCorrect] = useState(0);
  const [qDifficulty, setQDifficulty] = useState<(typeof DIFFICULTIES)[number]>("Medium");
  const [qExplanation, setQExplanation] = useState("");

  const [quizTitle, setQuizTitle] = useState("");
  const [quizNumQuestions, setQuizNumQuestions] = useState(20);
  const [quizDifficulty, setQuizDifficulty] = useState("");
  const [quizTimeLimit, setQuizTimeLimit] = useState("");

  useEffect(() => {
    contentApi.listCourses().then(setCourses).catch(() => setError("Could not load courses."));
  }, []);

  useEffect(() => {
    if (courseId === null) return;
    setSelectedChapter(null);
    contentApi.listSections(courseId).then(setSections).catch(() => setError("Could not load chapters."));
    contentApi.quizTemplates(courseId).then(setTemplates).catch(() => undefined);
  }, [courseId]);

  async function submitQuestion(e: FormEvent) {
    e.preventDefault();
    if (!selectedChapter) return;
    setError(null);
    setMessage(null);
    try {
      await contentApi.createQuestion({
        chapter_id: selectedChapter.id,
        body: qBody,
        options: qOptions,
        correct_index: qCorrect,
        difficulty_label: qDifficulty,
        explanation: qExplanation || null,
      });
      setMessage(`Question added to ${selectedChapter.name}.`);
      setQBody("");
      setQOptions(["", "", "", ""]);
      setQCorrect(0);
      setQExplanation("");
    } catch (err) {
      setError(err instanceof ApiError ? err.message : "Could not create the question.");
    }
  }

  async function submitQuizTemplate(e: FormEvent) {
    e.preventDefault();
    if (courseId === null) return;
    setError(null);
    setMessage(null);
    try {
      const created = await teacherApi.createQuizTemplate({
        title: quizTitle,
        course_id: courseId,
        chapter_id: selectedChapter?.id ?? null,
        difficulty_label: quizDifficulty || null,
        num_questions: quizNumQuestions,
        time_limit_seconds: quizTimeLimit ? Number(quizTimeLimit) : null,
      });
      setTemplates((t) => [...t, created]);
      setMessage(`Quiz template "${created.title}" created.`);
      setQuizTitle("");
    } catch (err) {
      setError(err instanceof ApiError ? err.message : "Could not create the quiz template.");
    }
  }

  async function deleteTemplate(id: number) {
    await teacherApi.deleteQuizTemplate(id);
    setTemplates((t) => t.filter((x) => x.id !== id));
  }

  if (courses === null) return <p className="page-loading">Loading courses…</p>;
  const selectedCourseObj = courseId !== null ? courses.find((c) => c.id === courseId) ?? null : null;

  return (
    <div className="assessment-management-page">
      <h1>Assessment Management</h1>
      <p className="dashboard-subtitle">Author questions and create quiz templates students can take.</p>

      {selectedCourseObj === null ? (
        <CourseGrid courses={courses} onSelect={setCourseId} />
      ) : (
        <CourseHeaderBar course={selectedCourseObj} onChange={() => setCourseId(null)} />
      )}

      {error && <p className="form-error">{error}</p>}
      {message && <p className="feedback-correct">{message}</p>}

      {courseId !== null && (
        <div className="assessment-layout">
          <div>
            <h2>Chapters</h2>
            <ChapterTreePicker
              sections={sections}
              selectedChapterId={selectedChapter?.id ?? null}
              onSelect={setSelectedChapter}
            />
          </div>

          <div className="assessment-forms">
            <section className="teacher-section">
              <h2>Author a question {selectedChapter ? `- ${selectedChapter.name}` : "(select a chapter)"}</h2>
              <form className="auth-form" onSubmit={submitQuestion}>
                <label>
                  Question body
                  <textarea value={qBody} onChange={(e) => setQBody(e.target.value)} required rows={3} />
                </label>
                {qOptions.map((opt, i) => (
                  <label key={i}>
                    Option {i + 1} {i === qCorrect && "(correct)"}
                    <div className="option-input-row">
                      <input
                        value={opt}
                        onChange={(e) => {
                          const next = [...qOptions];
                          next[i] = e.target.value;
                          setQOptions(next);
                        }}
                        required
                      />
                      <input type="radio" name="correct" checked={qCorrect === i} onChange={() => setQCorrect(i)} />
                    </div>
                  </label>
                ))}
                <label>
                  Difficulty
                  <select value={qDifficulty} onChange={(e) => setQDifficulty(e.target.value as typeof qDifficulty)}>
                    {DIFFICULTIES.map((d) => (
                      <option key={d} value={d}>
                        {d}
                      </option>
                    ))}
                  </select>
                </label>
                <label>
                  Explanation (optional, shown after answering)
                  <textarea value={qExplanation} onChange={(e) => setQExplanation(e.target.value)} rows={2} />
                </label>
                <button type="submit" disabled={!selectedChapter}>
                  Add question
                </button>
              </form>
            </section>

            <section className="teacher-section">
              <h2>Create a quiz template</h2>
              <form className="auth-form" onSubmit={submitQuizTemplate}>
                <label>
                  Title
                  <input value={quizTitle} onChange={(e) => setQuizTitle(e.target.value)} required />
                </label>
                <label>
                  Chapter (optional - leave unset for a mixed course-wide quiz)
                  <input value={selectedChapter?.name ?? "None selected"} disabled />
                </label>
                <label>
                  Number of questions
                  <input
                    type="number"
                    min={1}
                    value={quizNumQuestions}
                    onChange={(e) => setQuizNumQuestions(Number(e.target.value))}
                  />
                </label>
                <label>
                  Difficulty filter (optional)
                  <select value={quizDifficulty} onChange={(e) => setQuizDifficulty(e.target.value)}>
                    <option value="">Any</option>
                    {DIFFICULTIES.map((d) => (
                      <option key={d} value={d}>
                        {d}
                      </option>
                    ))}
                  </select>
                </label>
                <label>
                  Time limit in seconds (optional)
                  <input type="number" min={0} value={quizTimeLimit} onChange={(e) => setQuizTimeLimit(e.target.value)} />
                </label>
                <button type="submit">Create quiz template</button>
              </form>
            </section>

            {templates.length > 0 && (
              <section className="teacher-section">
                <h2>Existing quiz templates for this course</h2>
                <table className="teacher-table">
                  <thead>
                    <tr>
                      <th>Title</th>
                      <th>Questions</th>
                      <th>Difficulty</th>
                      <th></th>
                    </tr>
                  </thead>
                  <tbody>
                    {templates.map((t) => (
                      <tr key={t.id}>
                        <td>{t.title}</td>
                        <td>{t.num_questions}</td>
                        <td>{t.difficulty_label ?? "Any"}</td>
                        <td>
                          <button type="button" className="skip-button" onClick={() => deleteTemplate(t.id)}>
                            Delete
                          </button>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </section>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
