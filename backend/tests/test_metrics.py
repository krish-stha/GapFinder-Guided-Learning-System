"""
Known-input/known-output tests for evaluation/metrics.py.
Run with: pytest tests/test_metrics.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from evaluation.metrics import precision_recall_f1_at_k, auc, rmse, kendalls_tau, overlap_at_k


def test_precision_recall_f1_at_k_known_values():
    result = precision_recall_f1_at_k([1, 2, 3, 4], ground_truth_weak={2, 4, 5}, k=2)
    assert result["precision"] == 0.5
    assert abs(result["recall"] - 1 / 3) < 1e-9
    assert abs(result["f1"] - 0.4) < 1e-9


def test_precision_recall_f1_at_k_empty_ground_truth():
    result = precision_recall_f1_at_k([1, 2, 3], ground_truth_weak=set(), k=2)
    assert result == {"precision": 0.0, "recall": 0.0, "f1": 0.0}


def test_precision_recall_f1_at_k_perfect_recovery():
    result = precision_recall_f1_at_k([5, 6, 1, 2], ground_truth_weak={5, 6}, k=2)
    assert result == {"precision": 1.0, "recall": 1.0, "f1": 1.0}


def test_auc_perfect_separation_is_one():
    assert auc([0, 1, 0, 1], [0.1, 0.9, 0.2, 0.8]) == 1.0


def test_auc_undefined_with_single_class_returns_none():
    assert auc([1, 1, 1], [0.2, 0.5, 0.8]) is None


def test_rmse_known_values():
    assert rmse([0, 1], [0, 1]) == 0.0
    assert rmse([0, 0], [1, 1]) == 1.0


def test_kendalls_tau_identical_rankings_is_one():
    assert kendalls_tau([1, 2, 3, 4], [1, 2, 3, 4]) == 1.0


def test_kendalls_tau_fully_reversed_rankings_is_minus_one():
    tau = kendalls_tau([1, 2, 3, 4], [4, 3, 2, 1])
    assert abs(tau - (-1.0)) < 1e-9


def test_kendalls_tau_undefined_for_short_rankings():
    assert kendalls_tau([1], [1]) is None


def test_overlap_at_k_known_values():
    assert overlap_at_k([1, 2, 3], [1, 2, 4], k=2) == 1.0
    assert abs(overlap_at_k([1, 2, 3], [1, 2, 4], k=3) - 2 / 3) < 1e-9
    assert overlap_at_k([1, 2, 3], [1, 2, 4], k=0) == 0.0
