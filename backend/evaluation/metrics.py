"""
Shared metric helpers for the evaluation scripts (J.1/J.2/J.3). Pure
functions over plain lists/sets - no DB, no HTTP, no dependency on the
mastery engine or the synthetic generator.
"""
from sklearn.metrics import roc_auc_score
from scipy.stats import kendalltau


def precision_recall_f1_at_k(ranked_chapter_ids: list, ground_truth_weak: set, k: int) -> dict:
    """ranked_chapter_ids: weakest/highest-priority first. Precision/recall
    against the ground-truth weak-chapter set, evaluated at the top-k of
    the ranking."""
    top_k = ranked_chapter_ids[:k]
    if not top_k:
        return {"precision": 0.0, "recall": 0.0, "f1": 0.0}
    hits = len(set(top_k) & ground_truth_weak)
    precision = hits / len(top_k)
    recall = hits / len(ground_truth_weak) if ground_truth_weak else 0.0
    f1 = 0.0 if (precision + recall) == 0 else 2 * precision * recall / (precision + recall)
    return {"precision": precision, "recall": recall, "f1": f1}


def auc(y_true: list, y_pred: list) -> float | None:
    """Wraps sklearn's ROC-AUC. Returns None if y_true has only one class
    present (AUC is undefined in that case, e.g. a held-out slice with no
    incorrect answers at all)."""
    if len(set(y_true)) < 2:
        return None
    return float(roc_auc_score(y_true, y_pred))


def rmse(y_true: list, y_pred: list) -> float:
    n = len(y_true)
    if n == 0:
        return 0.0
    return (sum((t - p) ** 2 for t, p in zip(y_true, y_pred)) / n) ** 0.5


def kendalls_tau(ranking_a: list, ranking_b: list) -> float | None:
    """Both rankings must contain the same items. Compares rank POSITION of
    each item in a vs. in b. Returns None if either ranking has fewer than
    2 items (tau is undefined)."""
    if len(ranking_a) < 2 or len(ranking_b) < 2:
        return None
    pos_b = {item: i for i, item in enumerate(ranking_b)}
    a_positions = list(range(len(ranking_a)))
    b_positions = [pos_b[item] for item in ranking_a]
    tau, _ = kendalltau(a_positions, b_positions)
    return None if tau != tau else float(tau)  # NaN check (tau undefined for constant input)


def overlap_at_k(ranking_a: list, ranking_b: list, k: int) -> float:
    """|top_k(a) ∩ top_k(b)| / k. 0.0 if k == 0."""
    if k == 0:
        return 0.0
    top_a, top_b = set(ranking_a[:k]), set(ranking_b[:k])
    return len(top_a & top_b) / k
