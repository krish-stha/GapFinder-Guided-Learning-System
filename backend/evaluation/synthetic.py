"""
Synthetic student-response generator (project charter Section H.6). Pure
Python - no DB, no HTTP - reproducible via a fixed seed and a local
random.Random instance (never global random state).

Ground truth ("is this chapter really weak for this student?") is derived
ONLY from the latent `true_ability_at_t` value that drove response
sampling - never from the archetype label, never from sampled correctness.
That is what keeps the ground-truth-recovery experiment (J.1) non-circular:
no model, including the one under test, ever sees `true_ability_at_t`.

Every record carries two orderings:
  - `order`       : 0-based index within one (student, chapter) pair - the
                     shape app.engine.mastery.compute_chapter_evidence
                     expects.
  - `global_order`: 0-based index within one student's whole interleaved
                     cross-chapter sequence - what the DKT baseline needs,
                     since DKT models a student's full study session order,
                     not isolated per-chapter slices.
"""
import random
from dataclasses import dataclass, field
from math import exp

ARCHETYPES = ("chronically_weak", "declining", "improving", "noisy_adequate", "sparse", "healthy")
DIFFICULTY_LABELS = ("Easy", "Medium", "Hard")
_DIFFICULTY_CUTS = (-0.43, 0.43)  # ~tertiles of a standard normal -> Easy/Medium/Hard split


@dataclass(frozen=True)
class GeneratorConfig:
    seed: int = 42
    n_students: int = 120
    n_chapters: int = 10
    ability_mean: float = 0.0
    ability_sd: float = 1.0
    difficulty_mean: float = 0.0
    difficulty_sd: float = 1.0
    weak_ability_threshold: float = -0.5   # tau: used ONLY to define ground truth, never during sampling
    # deliberately kept mostly above app.engine.mastery's MIN_ATTEMPTS_FOR_CONFIDENCE
    # (10) so J.1's recovery experiment mainly tests ranking quality, not the
    # confidence gate - the dedicated `sparse` archetype below is where the
    # gate is meant to dominate
    attempts_per_chapter_range: tuple = (6, 30)
    sparse_attempts_range: tuple = (2, 4)
    archetype_weights: dict = field(default_factory=lambda: {
        "healthy": 0.35, "noisy_adequate": 0.20, "chronically_weak": 0.15,
        "declining": 0.12, "improving": 0.12, "sparse": 0.06,
    })


@dataclass(frozen=True)
class SyntheticRecord:
    student_id: int
    chapter_id: int
    order: int
    global_order: int
    is_correct: bool
    difficulty_label: str
    true_ability_at_t: float
    archetype: str          # for debugging/reporting only - never fed to a model


def _difficulty_label(x: float) -> str:
    if x < _DIFFICULTY_CUTS[0]:
        return "Easy"
    if x < _DIFFICULTY_CUTS[1]:
        return "Medium"
    return "Hard"


def true_ability(archetype: str, t: int, t_max: int, base_ability: float) -> float:
    """Deterministic per-archetype ability trajectory, relative to this
    student's own base ability. `t` is the 0-based order within the
    chapter; `t_max` is the last index in that chapter (>= 0)."""
    frac = 0.0 if t_max == 0 else t / t_max  # 0 at first attempt, 1 at last
    if archetype == "chronically_weak":
        return base_ability - 1.2
    if archetype == "healthy":
        return base_ability + 0.8
    if archetype == "noisy_adequate":
        return base_ability + 0.3  # noise enters via response sampling, not here
    if archetype == "sparse":
        return base_ability + 0.4
    if archetype == "declining":
        start, end = base_ability + 0.9, base_ability - 1.0
        return start + frac * (end - start)
    if archetype == "improving":
        start, end = base_ability - 1.0, base_ability + 0.9
        return start + frac * (end - start)
    raise ValueError(f"unknown archetype: {archetype}")


def sample_response(ability: float, difficulty: float, rng: random.Random) -> bool:
    p = 1.0 / (1.0 + exp(-(ability - difficulty)))
    return rng.random() < p


def _sample_archetype_sequence(rng: random.Random, n_chapters: int, weights: dict) -> list[str]:
    """One archetype per chapter, weighted-random, but guarantee at least
    one chronically_weak/declining/improving chapter per student (assigned
    to distinct slots, never overwriting each other) so per-student
    precision/recall@k is always computable in J.1."""
    names, probs = zip(*weights.items())
    picks = list(rng.choices(names, weights=probs, k=n_chapters))
    required = ["chronically_weak", "declining", "improving"]
    missing = [r for r in required if r not in picks]
    if missing:
        k = min(len(missing), n_chapters)  # can't guarantee more distinct archetypes than chapters
        slots = rng.sample(range(n_chapters), k=k)
        for slot, archetype in zip(slots, missing[:k]):
            picks[slot] = archetype
    return picks


def generate_dataset(config: GeneratorConfig = GeneratorConfig()) -> list[SyntheticRecord]:
    rng = random.Random(config.seed)
    records: list[SyntheticRecord] = []

    for student_id in range(config.n_students):
        base_ability = rng.gauss(config.ability_mean, config.ability_sd)
        archetypes = _sample_archetype_sequence(rng, config.n_chapters, config.archetype_weights)

        plan = []  # (chapter_id, order, archetype, t_max) - one entry per planned attempt
        for chapter_id, archetype in enumerate(archetypes):
            n = (rng.randint(*config.sparse_attempts_range) if archetype == "sparse"
                 else rng.randint(*config.attempts_per_chapter_range))
            for order in range(n):
                plan.append((chapter_id, order, archetype, n - 1))

        rng.shuffle(plan)  # interleaved study order across chapters -> global_order

        for global_order, (chapter_id, order, archetype, t_max) in enumerate(plan):
            ability = true_ability(archetype, order, t_max, base_ability)
            difficulty = rng.gauss(config.difficulty_mean, config.difficulty_sd)
            is_correct = sample_response(ability, difficulty, rng)
            records.append(SyntheticRecord(
                student_id=student_id, chapter_id=chapter_id, order=order,
                global_order=global_order, is_correct=is_correct,
                difficulty_label=_difficulty_label(difficulty),
                true_ability_at_t=ability, archetype=archetype,
            ))

    return records


def ground_truth_weak_chapters(records: list, config: GeneratorConfig) -> dict:
    """{student_id: {chapter_id, ...}} - a chapter counts as weak if
    true_ability_at_t at that chapter's LAST attempt (max `order`) is below
    weak_ability_threshold. Derived only from true_ability_at_t, never from
    is_correct or archetype - non-circular with any model's ranking."""
    last_by_pair = {}
    for r in records:
        key = (r.student_id, r.chapter_id)
        if key not in last_by_pair or r.order > last_by_pair[key].order:
            last_by_pair[key] = r

    weak: dict = {}
    for (student_id, chapter_id), r in last_by_pair.items():
        if r.true_ability_at_t < config.weak_ability_threshold:
            weak.setdefault(student_id, set()).add(chapter_id)
    return weak


def attempts_by_student_chapter(records: list) -> dict:
    """Reshape into the exact dict shape app.engine.mastery.compute_chapter_evidence
    expects, grouped by (student_id, chapter_id), sorted by local `order`."""
    grouped: dict = {}
    for r in records:
        grouped.setdefault((r.student_id, r.chapter_id), []).append(r)
    out = {}
    for key, recs in grouped.items():
        recs.sort(key=lambda r: r.order)
        out[key] = [{"is_correct": r.is_correct, "difficulty_label": r.difficulty_label, "order": r.order}
                     for r in recs]
    return out


def attempts_by_student(records: list) -> dict:
    """Group by student only, sorted by global_order - the full interleaved
    cross-chapter sequence the DKT baseline needs."""
    grouped: dict = {}
    for r in records:
        grouped.setdefault(r.student_id, []).append(r)
    for recs in grouped.values():
        recs.sort(key=lambda r: r.global_order)
    return grouped
