import { Link } from "react-router-dom";
import { ArrowRight } from "lucide-react";
import { BAND_CLASS } from "./MasteryMiniCard";
import { relativeDayLabel } from "../utils/relativeTime";
import type { ChapterEvidence, RecentChapter } from "../types";

// Shared by Dashboard (continuity on the "what to work on" surface) and
// the Practice page (continuity on the "let me improve it" surface) - same
// recent-chapters/me data, same card, so the two pages never drift.
// evidenceByChapter is optional - callers that already have the student's
// full evidence loaded (Dashboard) can pass it to show a real attempt
// count per card; callers that don't (Practice page) just omit it.
export default function ContinuePracticingRow({
  chapters,
  evidenceByChapter,
}: {
  chapters: RecentChapter[];
  evidenceByChapter?: Map<number, ChapterEvidence>;
}) {
  if (chapters.length === 0) return null;
  return (
    <section className="continue-practicing">
      <h2>Continue where you left off</h2>
      <div className="recent-chapters-list">
        {chapters.map((c) => {
          const nAttempts = evidenceByChapter?.get(c.chapter_id)?.n_attempts;
          return (
            <Link
              key={c.chapter_id}
              to={`/quick-practice/${c.course_id}/${c.chapter_id}`}
              className="recent-chapter-card"
            >
              <span className="recent-chapter-name">{c.chapter_name}</span>
              <span className="recent-chapter-meta">
                {c.priority_band && (
                  <span className={`band-badge ${BAND_CLASS[c.priority_band]}`}>{c.priority_band}</span>
                )}
                <span className="recent-chapter-time">
                  {nAttempts !== undefined ? `${nAttempts} attempts` : relativeDayLabel(c.last_practiced_at)}
                </span>
              </span>
              <span className="recent-chapter-cta">
                Continue <ArrowRight size={13} strokeWidth={2.5} />
              </span>
            </Link>
          );
        })}
      </div>
    </section>
  );
}
