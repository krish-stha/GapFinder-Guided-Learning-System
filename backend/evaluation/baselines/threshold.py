"""
The naive percentage-threshold baseline (project charter Section I.1) -
"the baseline to beat, not the method". No evidence-volume weighting, no
difficulty weighting, no recency weighting, no confidence gating: weakness
is just 1 - raw accuracy.
"""


def rank_chapters_threshold(attempts_by_chapter: dict) -> list:
    """attempts_by_chapter: {chapter_id: [{"is_correct": bool, ...}, ...]}.
    Returns chapter_ids sorted weakest-first (lowest raw accuracy first).
    Ties broken by chapter_id for determinism."""
    def raw_accuracy(atts):
        return sum(1 for a in atts if a["is_correct"]) / len(atts) if atts else 0.0

    return sorted(attempts_by_chapter.keys(),
                  key=lambda cid: (raw_accuracy(attempts_by_chapter[cid]), cid))


def predict_next_prefix(attempts: list, k: int) -> float:
    """Running accuracy of attempts[:k] - the walk-forward prediction for
    the attempt at position k, used by the J.2 predictive benchmark so the
    threshold baseline is scored on the same prefix-only protocol as the
    interpretable engine and DKT. Returns 0.5 (no evidence yet) if k == 0."""
    prefix = attempts[:k]
    if not prefix:
        return 0.5
    return sum(1 for a in prefix if a["is_correct"]) / len(prefix)
