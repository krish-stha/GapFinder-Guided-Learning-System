import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import ReactMarkdown from "react-markdown";
import { contentApi } from "../api/content";
import { ApiError } from "../api/client";
import HtmlWithKatex from "../components/HtmlWithKatex";
import type { ChapterResources } from "../types";

export default function ChapterLearningPage() {
  const { chapterId } = useParams();
  const [data, setData] = useState<ChapterResources | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [marking, setMarking] = useState(false);

  useEffect(() => {
    if (!chapterId) return;
    contentApi
      .chapterResources(Number(chapterId))
      .then(setData)
      .catch((err) => setError(err instanceof ApiError ? err.message : "Could not load this chapter's learning content."));
  }, [chapterId]);

  async function markComplete() {
    if (!chapterId || !data) return;
    setMarking(true);
    try {
      const progress = await contentApi.markChapterComplete(Number(chapterId));
      setData({ ...data, progress });
    } finally {
      setMarking(false);
    }
  }

  if (error)
    return (
      <div className="page-error">
        <p>{error}</p>
        <Link to="/chapters">Back to chapters</Link>
      </div>
    );
  if (data === null) return <p className="page-loading">Loading chapter content…</p>;

  const notes = data.resources.filter((r) => r.type === "note");
  const videos = data.resources.filter((r) => r.type === "video");
  const links = data.resources.filter((r) => r.type === "resource_link");
  const isComplete = data.progress.marked_complete_at !== null;

  return (
    <div className="detail-page">
      <Link to="/chapters" className="detail-back">
        ← Back to chapters
      </Link>
      <header className="detail-header">
        <h1>{data.chapter_name}</h1>
        <button
          type="button"
          className={isComplete ? "chapter-complete-btn chapter-complete-btn-done" : "chapter-complete-btn"}
          onClick={markComplete}
          disabled={marking || isComplete}
        >
          {isComplete ? "✓ Completed" : "Mark as complete"}
        </button>
      </header>

      {notes.length === 0 && videos.length === 0 && links.length === 0 && data.examples.length === 0 ? (
        <p className="page-loading">
          No learning content has been added for this chapter yet. Practice questions are still available from{" "}
          <Link to="/chapters">the chapter list</Link>.
        </p>
      ) : (
        <>
          {notes.map((note) => (
            <section className="detail-section" key={note.id}>
              <h2>{note.title}</h2>
              <div className="chapter-note-body">
                <ReactMarkdown>{note.body_markdown ?? ""}</ReactMarkdown>
              </div>
            </section>
          ))}

          {videos.length > 0 && (
            <section className="detail-section">
              <h2>Videos</h2>
              <ul className="resource-link-list">
                {videos.map((v) => (
                  <li key={v.id}>
                    <a href={v.url ?? "#"} target="_blank" rel="noreferrer">
                      ▶ {v.title}
                    </a>
                  </li>
                ))}
              </ul>
            </section>
          )}

          {links.length > 0 && (
            <section className="detail-section">
              <h2>Resources</h2>
              <ul className="resource-link-list">
                {links.map((r) => (
                  <li key={r.id}>
                    <a href={r.url ?? "#"} target="_blank" rel="noreferrer">
                      🔗 {r.title}
                    </a>
                  </li>
                ))}
              </ul>
            </section>
          )}

          {data.examples.length > 0 && (
            <section className="detail-section">
              <h2>Worked examples</h2>
              {data.examples.map((ex) => (
                <div className="example-card" key={ex.id}>
                  <HtmlWithKatex className="question-body" html={ex.body} />
                  <ul className="answer-list">
                    {ex.answers.map((a, i) => (
                      <li key={i} className="answer-option">
                        <HtmlWithKatex as="span" html={a} />
                      </li>
                    ))}
                  </ul>
                </div>
              ))}
            </section>
          )}
        </>
      )}

      <div className="chapter-learning-actions">
        <Link to={`/chapter/${data.chapter_id}`} className="cta-button">
          View my performance in this chapter
        </Link>
      </div>
    </div>
  );
}
