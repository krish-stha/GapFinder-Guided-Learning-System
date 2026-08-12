"""
Unit tests for the analytics engine (app/engine/mastery.py).

These run against plain dicts - no database, no API - which is the whole
point of keeping the engine pure. Run with: pytest tests/test_mastery.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app.engine import mastery


def make_attempts(pattern, difficulty="Medium"):
    """pattern: list of bool, oldest first."""
    return [{"is_correct": c, "difficulty_label": difficulty, "order": i}
            for i, c in enumerate(pattern)]


def test_zero_attempts_gives_insufficient_evidence():
    ev = mastery.compute_chapter_evidence(1, [])
    assert ev.priority_band == "Insufficient evidence"
    assert ev.n_attempts == 0


def test_sparse_attempts_lowers_confidence_even_if_all_wrong():
    # only 2 attempts, both wrong - should NOT be confidently "High" priority,
    # because we don't have enough evidence yet. This is the core sparsity
    # requirement from the project brief.
    ev = mastery.compute_chapter_evidence(1, make_attempts([False, False]))
    assert ev.confidence < 0.3
    assert ev.priority_band == "Insufficient evidence"


def test_consistent_high_accuracy_is_low_priority():
    ev = mastery.compute_chapter_evidence(1, make_attempts([True] * 12))
    assert ev.raw_accuracy == 1.0
    assert ev.priority_band == "Low"
    assert ev.confidence == 1.0


def test_consistent_low_accuracy_with_volume_is_high_priority():
    ev = mastery.compute_chapter_evidence(1, make_attempts([False] * 12))
    assert ev.raw_accuracy == 0.0
    assert ev.priority_band == "High"
    assert ev.confidence == 1.0


def test_declining_trend_is_detected_and_penalised():
    # starts correct, ends wrong - clear decline
    pattern = [True, True, True, True, False, False, False, False, False, False]
    ev = mastery.compute_chapter_evidence(1, make_attempts(pattern))
    assert ev.trend_slope is not None
    assert ev.trend_slope < 0
    assert ev.trend_significant is True


def test_improving_trend_is_detected_and_not_penalised():
    pattern = [False, False, False, False, True, True, True, True, True, True]
    ev = mastery.compute_chapter_evidence(1, make_attempts(pattern))
    assert ev.trend_slope > 0
    assert ev.trend_significant is True
    # improving trend should NOT add the decline penalty
    flat_same_avg = mastery.compute_chapter_evidence(1, make_attempts([True, False] * 5))
    assert ev.priority_score <= flat_same_avg.priority_score + 0.5  # sanity bound, not exact


def test_difficulty_weighting_rewards_hard_correct_answers():
    easy_right = mastery.compute_chapter_evidence(
        1, make_attempts([True] * 6 + [False] * 4, difficulty="Easy"))
    hard_right = mastery.compute_chapter_evidence(
        1, make_attempts([True] * 6 + [False] * 4, difficulty="Hard"))
    # same raw accuracy (60%), but hard-question correctness should score higher
    assert easy_right.raw_accuracy == hard_right.raw_accuracy == 0.6
    assert hard_right.difficulty_weighted_score >= easy_right.difficulty_weighted_score


def test_rank_chapters_orders_high_before_low_and_insufficient_last():
    high = mastery.compute_chapter_evidence(1, make_attempts([False] * 12))
    low = mastery.compute_chapter_evidence(2, make_attempts([True] * 12))
    insufficient = mastery.compute_chapter_evidence(3, make_attempts([False, False]))
    ranked = mastery.rank_chapters([low, insufficient, high])
    assert [e.chapter_id for e in ranked] == [1, 2, 3]


def test_explain_is_factually_consistent_with_evidence():
    ev = mastery.compute_chapter_evidence(1, make_attempts([True, False, False, False] * 3))
    text = mastery.explain(ev, "Thermodynamics")
    assert "Thermodynamics" in text
    assert f"{ev.n_attempts}" in text
    assert f"{round(ev.raw_accuracy*100):.0f}".split(".")[0] in text or f"{ev.raw_accuracy*100:.0f}" in text


def test_explain_insufficient_evidence_says_so():
    ev = mastery.compute_chapter_evidence(1, make_attempts([False]))
    text = mastery.explain(ev, "Optics")
    assert "Not enough attempts" in text


def test_subject_comparison_map_excludes_self_and_weights_by_attempts():
    # chapter 1: weak, chapter 2 and 3: strong, all same subject (10)
    weak = mastery.compute_chapter_evidence(1, make_attempts([False] * 12))
    strong_a = mastery.compute_chapter_evidence(2, make_attempts([True] * 12))
    strong_b = mastery.compute_chapter_evidence(3, make_attempts([True] * 8))
    chapter_to_subject = {1: 10, 2: 10, 3: 10}
    cmp = mastery.subject_comparison_map([weak, strong_a, strong_b], chapter_to_subject)
    # chapter 1's comparison excludes itself - just the (weighted) average of 2 and 3
    expected_for_1 = (strong_a.mastery_estimate * 12 + strong_b.mastery_estimate * 8) / 20
    assert abs(cmp[1] - expected_for_1) < 0.01
    # chapter 2's comparison excludes itself too - averages 1 and 3, not 2's own score
    expected_for_2 = (weak.mastery_estimate * 12 + strong_b.mastery_estimate * 8) / 20
    assert abs(cmp[2] - expected_for_2) < 0.01


def test_subject_comparison_map_omits_chapter_with_no_sibling_evidence():
    only = mastery.compute_chapter_evidence(1, make_attempts([True] * 12))
    other_subject = mastery.compute_chapter_evidence(2, make_attempts([False] * 12))
    cmp = mastery.subject_comparison_map([only, other_subject], {1: 10, 2: 20})
    assert 1 not in cmp
    assert 2 not in cmp


def test_custom_weights_change_recency_weighted_score():
    # a short half-life should discount older (early) attempts harder than
    # the default, so a chapter that started wrong and ended right should
    # score higher recency-weighted accuracy under a shorter half-life
    pattern = [False, False, False, True, True, True]
    atts = make_attempts(pattern)
    default_ev = mastery.compute_chapter_evidence(1, atts)
    short_half_life_ev = mastery.compute_chapter_evidence(
        1, atts, weights=mastery.MasteryWeights(recency_half_life=1))
    assert short_half_life_ev.recency_weighted_score > default_ev.recency_weighted_score


def test_custom_weights_change_confidence_and_band():
    # 2 attempts is "insufficient evidence" under the default volume prior
    # (min_attempts_for_confidence=10) but should read as fully confident
    # under a lower prior that only needs 2 attempts
    atts = make_attempts([False] * 2)
    default_ev = mastery.compute_chapter_evidence(1, atts)
    lenient_ev = mastery.compute_chapter_evidence(
        1, atts, weights=mastery.MasteryWeights(min_attempts_for_confidence=2))
    assert default_ev.priority_band == "Insufficient evidence"
    assert lenient_ev.confidence == 1.0
    assert lenient_ev.priority_band == "High"
