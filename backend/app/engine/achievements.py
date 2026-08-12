"""
Gamification engine. Pure Python - no DB/HTTP, same discipline as
app.engine.mastery: takes a plain stats dict in, returns plain dicts out.
Badges are computed on the fly from existing Attempt/PracticeSession data
every time this is called - nothing is persisted (no points/XP/badge
tables), matching this codebase's existing "never store what can be
computed" convention (see mastery.py, /practice/progress/me).

Input to compute_achievements():
    {"streak_days": int, "questions_answered": int, "chapters_mastered": int,
     "mock_tests_completed": int, "diagnostic_completed": bool}
"""
from dataclasses import dataclass

# Each tier: (threshold, label). Tiers are checked low-to-high; a stat
# earns every tier whose threshold it has reached, and the next tier not
# yet reached becomes that family's `next_milestones` candidate.
STREAK_TIERS = [(3, "3-Day Streak"), (7, "7-Day Streak"), (14, "14-Day Streak"), (30, "30-Day Streak")]
QUESTIONS_TIERS = [(50, "50 Questions"), (200, "200 Questions"), (500, "500 Questions"), (1000, "1000 Questions")]
CHAPTERS_MASTERED_TIERS = [
    (1, "First Chapter Mastered"), (5, "5 Chapters Mastered"),
    (15, "15 Chapters Mastered"), (30, "30 Chapters Mastered"),
]
MOCK_TEST_TIERS = [(1, "First Mock Test"), (5, "5 Mock Tests"), (15, "15 Mock Tests")]

_FAMILIES = [
    # (family_id, stat_key, tiers, icon, singular unit noun for the
    # next_milestone message - "2 days more to earn ...", not just "2 more")
    ("streak", "streak_days", STREAK_TIERS, "flame", "day"),
    ("questions", "questions_answered", QUESTIONS_TIERS, "target", "question"),
    ("chapters_mastered", "chapters_mastered", CHAPTERS_MASTERED_TIERS, "trophy", "chapter"),
    ("mock_tests", "mock_tests_completed", MOCK_TEST_TIERS, "clipboard-check", "mock test"),
]


@dataclass(frozen=True)
class Badge:
    id: str
    label: str
    description: str
    tier: int          # 1-based position within its family
    earned: bool
    icon: str


@dataclass(frozen=True)
class NextMilestone:
    badge_id: str
    label: str
    progress_current: int
    progress_target: int
    message: str


def compute_achievements(stats: dict) -> dict:
    """Returns {"badges": [Badge, ...], "next_milestones": [NextMilestone, ...]}.
    badges includes EVERY tier in every family (earned and unearned) so the
    caller can render a full progression, not just what's been unlocked.
    next_milestones holds one entry per family that still has an unearned
    tier (a maxed-out family contributes none), sorted smallest-remaining-
    gap-first so the caller can show the single closest one as a teaser."""
    badges: list[Badge] = []
    milestones: list[NextMilestone] = []

    for family_id, stat_key, tiers, icon, unit in _FAMILIES:
        current = stats.get(stat_key, 0)
        next_tier_found = False
        for tier_index, (threshold, label) in enumerate(tiers, start=1):
            earned = current >= threshold
            badges.append(Badge(
                id=f"{family_id}_{tier_index}", label=label,
                description=f"Reach {threshold}.", tier=tier_index,
                earned=earned, icon=icon,
            ))
            if not earned and not next_tier_found:
                next_tier_found = True
                gap = threshold - current
                unit_word = unit if gap == 1 else f"{unit}s"
                milestones.append(NextMilestone(
                    badge_id=f"{family_id}_{tier_index}", label=label,
                    progress_current=current, progress_target=threshold,
                    message=f"{gap} {unit_word} more to earn \"{label}\"!",
                ))

    diagnostic_earned = bool(stats.get("diagnostic_completed", False))
    badges.append(Badge(
        id="diagnostic_taken", label="Diagnostic Complete",
        description="Take your first diagnostic assessment.", tier=1,
        earned=diagnostic_earned, icon="clipboard-list",
    ))
    if not diagnostic_earned:
        milestones.append(NextMilestone(
            badge_id="diagnostic_taken", label="Diagnostic Complete",
            progress_current=0, progress_target=1,
            message="Take a diagnostic assessment to earn \"Diagnostic Complete\"!",
        ))

    milestones.sort(key=lambda m: m.progress_target - m.progress_current)
    return {"badges": badges, "next_milestones": milestones}
