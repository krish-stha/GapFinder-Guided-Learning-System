"""
Unit tests for the Phase 3 mastery-engine additions (aggregate_subject_evidence,
build_learning_path, pick_adaptive_distribution) - same pure dict-in/dataclass-out
discipline and make_attempts() convention as test_mastery.py.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app.engine import mastery


def make_attempts(pattern, difficulty="Medium"):
    return [{"is_correct": c, "difficulty_label": difficulty, "order": i}
            for i, c in enumerate(pattern)]


def test_build_learning_path_appends_not_started_chapters_last():
    ev_high = mastery.compute_chapter_evidence(1, make_attempts([False] * 12))
    ranked = mastery.rank_chapters([ev_high])
    path = mastery.build_learning_path(ranked, all_chapter_ids=[1, 2, 3])
    assert [step["chapter_id"] for step in path] == [1, 2, 3]
    assert path[0]["status"] == "High"
    assert path[1]["status"] == "not_started"
    assert path[1]["evidence"] is None
    assert path[2]["status"] == "not_started"


def test_build_learning_path_with_no_attempts_at_all():
    path = mastery.build_learning_path([], all_chapter_ids=[10, 20])
    assert len(path) == 2
    assert all(step["status"] == "not_started" for step in path)


def test_aggregate_subject_evidence_weights_by_attempt_count():
    # chapter 1: 10 attempts, all correct -> high mastery
    # chapter 2: 2 attempts, all wrong -> low mastery, but Insufficient
    #   evidence chapters (n<10 by default) still carry a real mastery_estimate
    #   here since we're calling compute_chapter_evidence directly, not going
    #   through the priority_band gate - aggregate_subject_evidence just wants
    #   n_attempts-weighted numbers, not band-filtered ones.
    ev1 = mastery.compute_chapter_evidence(1, make_attempts([True] * 10))
    ev2 = mastery.compute_chapter_evidence(2, make_attempts([False] * 2))
    agg = mastery.aggregate_subject_evidence([ev1, ev2], chapter_to_subject={1: 100, 2: 100})
    assert 100 in agg
    assert agg[100]["n_attempts"] == 12
    # weighted average should sit much closer to ev1's mastery (10 attempts)
    # than ev2's (2 attempts)
    expected = (ev1.mastery_estimate * 10 + ev2.mastery_estimate * 2) / 12
    assert abs(agg[100]["avg_mastery"] - round(expected, 3)) < 0.01


def test_aggregate_subject_evidence_skips_zero_attempt_chapters():
    ev_empty = mastery.compute_chapter_evidence(1, [])
    agg = mastery.aggregate_subject_evidence([ev_empty], chapter_to_subject={1: 100})
    assert agg == {}


def test_aggregate_subject_evidence_skips_unmapped_chapters():
    ev = mastery.compute_chapter_evidence(1, make_attempts([True] * 10))
    agg = mastery.aggregate_subject_evidence([ev], chapter_to_subject={})
    assert agg == {}


def test_pick_adaptive_distribution_shifts_toward_hard_as_mastery_rises():
    low = mastery.pick_adaptive_distribution(0.0)
    mid = mastery.pick_adaptive_distribution(0.5)
    high = mastery.pick_adaptive_distribution(1.0)
    assert low["Easy"] > mid["Easy"] > high["Easy"]
    assert low["Hard"] < mid["Hard"] < high["Hard"]


def test_pick_adaptive_distribution_always_sums_to_one():
    for m in (0.0, 0.25, 0.5, 0.75, 1.0):
        dist = mastery.pick_adaptive_distribution(m)
        assert abs(sum(dist.values()) - 1.0) < 1e-9
        assert all(v > 0 for v in dist.values())


def test_pick_adaptive_distribution_clamps_out_of_range_input():
    below = mastery.pick_adaptive_distribution(-1.0)
    above = mastery.pick_adaptive_distribution(2.0)
    assert below == mastery.pick_adaptive_distribution(0.0)
    assert above == mastery.pick_adaptive_distribution(1.0)
