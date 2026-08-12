"""
The analytics engine. Pure Python - no DB session, no HTTP, no ORM objects
in or out. Takes plain dicts, returns plain dicts. This is deliberate (see
project charter, Section G.3): it is what makes this module unit-testable
in isolation and reusable from a script for the sensitivity-analysis
experiment later, without spinning up the API.

Input to compute_chapter_evidence(): a list of attempts for ONE
(student, chapter) pair, oldest first:

    [{"is_correct": bool, "difficulty_label": "Easy"|"Medium"|"Hard",
      "order": int}, ...]

`order` is just a 0-based sequence index (session order), used for recency
and trend - we don't need wall-clock time for this to work.
"""
from dataclasses import dataclass, field
from statistics import pstdev

DIFFICULTY_WEIGHT = {"Easy": 1.0, "Medium": 1.5, "Hard": 2.0}
RECENCY_HALF_LIFE = 5          # attempts; how fast older evidence decays
MIN_ATTEMPTS_FOR_CONFIDENCE = 10
MIN_ATTEMPTS_FOR_TREND = 3


@dataclass(frozen=True)
class MasteryWeights:
    """Every tunable constant the model uses, gathered in one place so the
    sensitivity analysis (RQ3) can sweep them without duplicating the model
    logic. Defaults exactly reproduce the historical hardcoded behaviour -
    compute_chapter_evidence(chapter_id, attempts) with no weights arg is
    unaffected by this refactor."""
    difficulty_weight: dict = field(default_factory=lambda: dict(DIFFICULTY_WEIGHT))
    recency_half_life: float = RECENCY_HALF_LIFE
    min_attempts_for_confidence: float = MIN_ATTEMPTS_FOR_CONFIDENCE
    min_attempts_for_trend: int = MIN_ATTEMPTS_FOR_TREND
    mastery_recency_blend: float = 0.5   # weight on recency_weighted_score; (1-x) on difficulty_weighted_score
    trend_penalty: float = 0.15
    trend_significance_min_slope: float = 0.02
    high_priority_threshold: float = 0.5
    medium_priority_threshold: float = 0.25
    insufficient_confidence_threshold: float = 0.3
    # mastery_estimate at/above this = "chapter completed" for the
    # Progress & Improvement page's chapters_completed count.
    mastery_complete_threshold: float = 0.7


DEFAULT_WEIGHTS = MasteryWeights()


@dataclass
class ChapterEvidence:
    chapter_id: int
    n_attempts: int
    raw_accuracy: float
    difficulty_weighted_score: float
    recency_weighted_score: float
    consistency: float          # 0-1, higher = more consistent
    trend_slope: float | None   # positive = improving, negative = declining
    trend_significant: bool
    confidence: float           # 0-1, based on volume
    mastery_estimate: float     # 0-1 headline number
    priority_score: float       # higher = needs more attention
    priority_band: str          # High / Medium / Low / Insufficient evidence


def _weighted_accuracy(attempts, weights: MasteryWeights = DEFAULT_WEIGHTS):
    total_w = sum(weights.difficulty_weight.get(a["difficulty_label"], 1.0) for a in attempts)
    if total_w == 0:
        return 0.0
    correct_w = sum(weights.difficulty_weight.get(a["difficulty_label"], 1.0)
                     for a in attempts if a["is_correct"])
    return correct_w / total_w


def _recency_weighted_accuracy(attempts, weights: MasteryWeights = DEFAULT_WEIGHTS):
    n = len(attempts)
    if n == 0:
        return 0.0
    w_list, scores = [], []
    for a in attempts:
        age = (n - 1) - a["order"]  # 0 = most recent
        w = 0.5 ** (age / weights.recency_half_life)
        w_list.append(w)
        scores.append(w * (1.0 if a["is_correct"] else 0.0))
    return sum(scores) / sum(w_list)


def _trend(attempts, weights: MasteryWeights = DEFAULT_WEIGHTS):
    """Simple linear regression of correctness (0/1) over order. Returns
    (slope, is_significant). Significance here is a cheap heuristic - slope
    magnitude relative to noise - not a formal hypothesis test, and that
    limitation should be stated in the report."""
    n = len(attempts)
    if n < weights.min_attempts_for_trend:
        return None, False
    xs = [a["order"] for a in attempts]
    ys = [1.0 if a["is_correct"] else 0.0 for a in attempts]
    xm = sum(xs) / n
    ym = sum(ys) / n
    num = sum((x - xm) * (y - ym) for x, y in zip(xs, ys))
    den = sum((x - xm) ** 2 for x in xs)
    if den == 0:
        return 0.0, False
    slope = num / den
    noise = pstdev(ys) if n > 1 else 0.0
    significant = abs(slope) > (noise / n) and abs(slope) > weights.trend_significance_min_slope
    return slope, significant


def compute_chapter_evidence(chapter_id: int, attempts: list[dict],
                              weights: MasteryWeights = DEFAULT_WEIGHTS) -> ChapterEvidence:
    n = len(attempts)
    if n == 0:
        return ChapterEvidence(chapter_id, 0, 0, 0, 0, 0, None, False, 0, 0, 0, "Insufficient evidence")

    raw_acc = sum(1 for a in attempts if a["is_correct"]) / n
    diff_w = _weighted_accuracy(attempts, weights)
    rec_w = _recency_weighted_accuracy(attempts, weights)
    slope, significant = _trend(attempts, weights)

    correctness = [1.0 if a["is_correct"] else 0.0 for a in attempts]
    consistency = 1.0 - (pstdev(correctness) if n > 1 else 0.0)

    confidence = min(1.0, n / weights.min_attempts_for_confidence)

    # mastery blends difficulty-adjusted accuracy with recency, since a
    # recent improvement or decline should move the headline number
    mastery = (1 - weights.mastery_recency_blend) * diff_w + weights.mastery_recency_blend * rec_w

    # priority: weakness itself, scaled down when we don't have enough
    # evidence to trust the number, bumped up further if declining
    weakness = 1.0 - mastery
    trend_penalty = weights.trend_penalty if (significant and slope is not None and slope < 0) else 0.0
    priority = (weakness + trend_penalty) * confidence

    if confidence < weights.insufficient_confidence_threshold:
        band = "Insufficient evidence"
    elif priority >= weights.high_priority_threshold:
        band = "High"
    elif priority >= weights.medium_priority_threshold:
        band = "Medium"
    else:
        band = "Low"

    return ChapterEvidence(
        chapter_id=chapter_id, n_attempts=n, raw_accuracy=round(raw_acc, 3),
        difficulty_weighted_score=round(diff_w, 3), recency_weighted_score=round(rec_w, 3),
        consistency=round(consistency, 3),
        trend_slope=None if slope is None else round(slope, 4),
        trend_significant=significant, confidence=round(confidence, 3),
        mastery_estimate=round(mastery, 3), priority_score=round(priority, 3),
        priority_band=band,
    )


def rank_chapters(evidence_list: list[ChapterEvidence]) -> list[ChapterEvidence]:
    """Highest priority (most in need of attention) first. 'Insufficient
    evidence' chapters are sorted to the bottom - we don't want to tell a
    student to prioritise a chapter we're not confident about."""
    order = {"High": 0, "Medium": 1, "Low": 2, "Insufficient evidence": 3}
    return sorted(evidence_list, key=lambda e: (order[e.priority_band], -e.priority_score))


def aggregate_subject_evidence(chapter_evidences: list[ChapterEvidence],
                                chapter_to_subject: dict[int, int]) -> dict[int, dict]:
    """n_attempts-weighted average mastery per subject, for My Performance's
    subject-wise breakdown. Chapters with no entry in chapter_to_subject
    (e.g. a chapter whose subject lookup failed) are skipped rather than
    guessed at. Insufficient-evidence chapters (n_attempts=0 in practice,
    since compute_chapter_evidence returns that band for n=0) contribute
    zero weight, which is correct - they shouldn't drag a subject average
    down when there's no real evidence."""
    totals: dict[int, list[float]] = {}
    for ev in chapter_evidences:
        subject_id = chapter_to_subject.get(ev.chapter_id)
        if subject_id is None or ev.n_attempts == 0:
            continue
        totals.setdefault(subject_id, [0.0, 0])
        totals[subject_id][0] += ev.mastery_estimate * ev.n_attempts
        totals[subject_id][1] += ev.n_attempts
    return {
        subject_id: {"n_attempts": n, "avg_mastery": round(weighted_sum / n, 3)}
        for subject_id, (weighted_sum, n) in totals.items() if n > 0
    }


def subject_comparison_map(chapter_evidences: list[ChapterEvidence],
                            chapter_to_subject: dict[int, int]) -> dict[int, float]:
    """For each chapter, the n_attempts-weighted average mastery of the
    student's OTHER evidenced chapters in the same subject (excluding the
    chapter itself) - the number explain()'s "compared with your other
    chapters in this subject" sentence needs to actually be about the
    subject, not the whole account. A chapter with no other evidenced
    sibling in its subject yet gets no entry here, and explain() falls
    back to the plain sentence rather than fabricating a comparison."""
    by_subject: dict[int, list[ChapterEvidence]] = {}
    for ev in chapter_evidences:
        subject_id = chapter_to_subject.get(ev.chapter_id)
        if subject_id is None or ev.n_attempts == 0:
            continue
        by_subject.setdefault(subject_id, []).append(ev)

    result: dict[int, float] = {}
    for evs in by_subject.values():
        for ev in evs:
            others = [o for o in evs if o.chapter_id != ev.chapter_id]
            total_n = sum(o.n_attempts for o in others)
            if total_n == 0:
                continue
            weighted = sum(o.mastery_estimate * o.n_attempts for o in others) / total_n
            result[ev.chapter_id] = round(weighted, 3)
    return result


def build_learning_path(ranked_evidence: list[ChapterEvidence], all_chapter_ids: list[int]) -> list[dict]:
    """Appends never-attempted chapters (status="not_started") after
    rank_chapters()'s own ordering - results/me-style endpoints silently
    drop chapters with zero attempts, but a learning path needs to show
    them too (nothing to recommend studying "next" if untouched chapters
    are invisible). Pure/dict-out like the rest of this module - the
    caller (a router, which has chapter names) turns these into
    LearningPathStepOut."""
    seen = {e.chapter_id for e in ranked_evidence}
    steps = [{"chapter_id": e.chapter_id, "status": e.priority_band, "evidence": e} for e in ranked_evidence]
    for cid in all_chapter_ids:
        if cid not in seen:
            steps.append({"chapter_id": cid, "status": "not_started", "evidence": None})
    return steps


def pick_adaptive_distribution(mastery_estimate: float) -> dict[str, float]:
    """Easy/Medium/Hard sampling weights for /start's question draw when
    prior evidence exists for the target chapter - biased toward easier
    questions at low mastery, harder ones at high mastery. Between-session
    adaptation only: true within-session per-question adaptation would
    require restructuring the pre-created-Attempt-rows-at-/start
    architecture that free navigation depends on (see project plan)."""
    m = max(0.0, min(1.0, mastery_estimate))
    easy = max(0.1, 0.6 - 0.5 * m)
    hard = max(0.1, 0.1 + 0.6 * m)
    medium = max(0.1, 1.0 - easy - hard)
    total = easy + medium + hard
    return {"Easy": easy / total, "Medium": medium / total, "Hard": hard / total}


def explain(evidence: ChapterEvidence, chapter_name: str, subject_overall_accuracy: float | None = None) -> str:
    """Deterministic, template-based explanation - every clause traces to a
    field on the evidence object, so this can be unit-tested for factual
    consistency against the record it was generated from."""
    if evidence.priority_band == "Insufficient evidence":
        return (f"Not enough attempts yet in {chapter_name} ({evidence.n_attempts} so far) "
                f"to confidently assess your level. Attempt more questions to unlock a recommendation.")

    parts = [f"Your accuracy in {chapter_name} is {evidence.raw_accuracy*100:.0f}% "
             f"across {evidence.n_attempts} questions"]
    if subject_overall_accuracy is not None:
        parts.append(f", compared with {subject_overall_accuracy*100:.0f}% across your other chapters in this subject")
    parts.append(".")
    if evidence.trend_significant and evidence.trend_slope is not None:
        direction = "declined" if evidence.trend_slope < 0 else "improved"
        parts.append(f" Performance has {direction} over your recent attempts.")
    if evidence.consistency < 0.6:
        parts.append(" Your results here have been inconsistent, which lowers confidence in this estimate.")
    return "".join(parts)
