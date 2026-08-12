import { useEffect, useState } from "react";
import { Flame, Target, Trophy, ClipboardCheck, ClipboardList, Award } from "lucide-react";
import { practiceApi } from "../api/practice";
import type { Achievements, Badge } from "../types";

const ICONS: Record<string, typeof Flame> = {
  flame: Flame,
  target: Target,
  trophy: Trophy,
  "clipboard-check": ClipboardCheck,
  "clipboard-list": ClipboardList,
};

// Badge ids are "<family>_<tier>" (e.g. "streak_1", "chapters_mastered_3")
// or a single untiered id ("diagnostic_taken"). Earning "1000 Questions"
// also earns "50/200/500 Questions" underneath it - showing every earned
// tier would just be redundant, so only the highest earned tier per
// family is displayed.
function highestPerFamily(badges: Badge[]): Badge[] {
  const byFamily = new Map<string, Badge>();
  for (const b of badges) {
    const family = b.id.replace(/_\d+$/, "");
    const existing = byFamily.get(family);
    if (!existing || b.tier > existing.tier) byFamily.set(family, b);
  }
  return [...byFamily.values()];
}

export default function AchievementsStrip() {
  const [data, setData] = useState<Achievements | null>(null);

  useEffect(() => {
    // Best-effort, same .catch(() => undefined) pattern the rest of the
    // dashboard uses for non-critical fetches - a failure here shouldn't
    // block the page's core recommendation.
    practiceApi.achievementsMe().then(setData).catch(() => undefined);
  }, []);

  if (data === null) return null;

  const earned = highestPerFamily(data.badges.filter((b) => b.earned));
  const teaser = data.next_milestones[0];

  return (
    <section className="achievements-strip">
      <div className="achievements-badges">
        {earned.length === 0 ? (
          <span className="badge-chip badge-chip-placeholder">
            <Award size={15} strokeWidth={2} />
            Earn your first badge
          </span>
        ) : (
          earned.map((b) => {
            const Icon = ICONS[b.icon] ?? Award;
            return (
              <span key={b.id} className="badge-chip badge-chip-earned" title={b.description}>
                <Icon size={15} strokeWidth={2} />
                {b.label}
              </span>
            );
          })
        )}
      </div>
      {teaser && <p className="milestone-banner">{teaser.message}</p>}
    </section>
  );
}
