import { useEffect, useState, type FormEvent } from "react";
import ReactMarkdown from "react-markdown";
import { contentApi } from "../api/content";
import { ApiError } from "../api/client";
import ChapterTreePicker from "../components/ChapterTreePicker";
import { CourseGrid, CourseHeaderBar } from "../components/CoursePicker";
import type { Chapter, Course, LearningResource, ResourceType } from "../types";

export default function LearningContentManagementPage() {
  const [courses, setCourses] = useState<Course[] | null>(null);
  const [courseId, setCourseId] = useState<number | null>(null);
  const [sections, setSections] = useState<Chapter[]>([]);
  const [selectedChapter, setSelectedChapter] = useState<Chapter | null>(null);
  const [existing, setExisting] = useState<LearningResource[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [message, setMessage] = useState<string | null>(null);

  const [type, setType] = useState<ResourceType>("note");
  const [title, setTitle] = useState("");
  const [body, setBody] = useState("");
  const [url, setUrl] = useState("");

  useEffect(() => {
    contentApi.listCourses().then(setCourses).catch(() => setError("Could not load courses."));
  }, []);

  useEffect(() => {
    if (courseId === null) return;
    setSelectedChapter(null);
    setExisting([]);
    contentApi.listSections(courseId).then(setSections).catch(() => setError("Could not load chapters."));
  }, [courseId]);

  useEffect(() => {
    if (!selectedChapter) return;
    contentApi
      .chapterResources(selectedChapter.id)
      .then((r) => setExisting(r.resources))
      .catch(() => setExisting([]));
  }, [selectedChapter]);

  async function submit(e: FormEvent) {
    e.preventDefault();
    if (!selectedChapter) return;
    setError(null);
    setMessage(null);
    try {
      const created = await contentApi.createResource({
        chapter_id: selectedChapter.id,
        type,
        title,
        body_markdown: type === "note" ? body : null,
        url: type !== "note" ? url : null,
      });
      setExisting((r) => [...r, created]);
      setMessage(`"${created.title}" added to ${selectedChapter.name}.`);
      setTitle("");
      setBody("");
      setUrl("");
    } catch (err) {
      setError(err instanceof ApiError ? err.message : "Could not create the resource.");
    }
  }

  async function remove(id: number) {
    await contentApi.deleteResource(id);
    setExisting((r) => r.filter((x) => x.id !== id));
  }

  if (courses === null) return <p className="page-loading">Loading courses…</p>;
  const selectedCourseObj = courseId !== null ? courses.find((c) => c.id === courseId) ?? null : null;

  return (
    <div className="content-management-page">
      <h1>Learning Content Management</h1>
      <p className="dashboard-subtitle">Upload notes, videos (links), and resources, mapped to chapters.</p>

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
              <h2>Add content {selectedChapter ? `- ${selectedChapter.name}` : "(select a chapter)"}</h2>
              <form className="auth-form" onSubmit={submit}>
                <label>
                  Type
                  <select value={type} onChange={(e) => setType(e.target.value as ResourceType)}>
                    <option value="note">Note (markdown)</option>
                    <option value="video">Video (external link)</option>
                    <option value="resource_link">Resource link</option>
                  </select>
                </label>
                <label>
                  Title
                  <input value={title} onChange={(e) => setTitle(e.target.value)} required />
                </label>
                {type === "note" ? (
                  <>
                    <label>
                      Body (markdown)
                      <textarea value={body} onChange={(e) => setBody(e.target.value)} rows={6} required />
                    </label>
                    {body && (
                      <div className="markdown-preview">
                        <p className="distribution-heading">Preview</p>
                        <ReactMarkdown>{body}</ReactMarkdown>
                      </div>
                    )}
                  </>
                ) : (
                  <label>
                    URL
                    <input type="url" value={url} onChange={(e) => setUrl(e.target.value)} required placeholder="https://…" />
                  </label>
                )}
                <button type="submit" disabled={!selectedChapter}>
                  Add {type === "note" ? "note" : type === "video" ? "video" : "resource"}
                </button>
              </form>
            </section>

            {selectedChapter && existing.length > 0 && (
              <section className="teacher-section">
                <h2>Existing content for {selectedChapter.name}</h2>
                <table className="teacher-table">
                  <thead>
                    <tr>
                      <th>Type</th>
                      <th>Title</th>
                      <th></th>
                    </tr>
                  </thead>
                  <tbody>
                    {existing.map((r) => (
                      <tr key={r.id}>
                        <td>{r.type}</td>
                        <td>{r.title}</td>
                        <td>
                          <button type="button" className="skip-button" onClick={() => remove(r.id)}>
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
