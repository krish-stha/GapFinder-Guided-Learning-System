"""
Unit tests for app.engine.achievements - pure dict-in/dict-out, no DB,
same discipline and convention as test_mastery.py / test_learning_path.py.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app.engine import achievements

ZERO_STATS = {
    "streak_days": 0, "questions_answered": 0, "chapters_mastered": 0,
    "mock_tests_completed": 0, "diagnostic_completed": False,
}


def badges_by_id(result):
    return {b.id: b for b in result["badges"]}


def milestones_by_id(result):
    return {m.badge_id: m for m in result["next_milestones"]}


def test_zero_stats_earns_nothing():
    result = achievements.compute_achievements(ZERO_STATS)
    assert all(not b.earned for b in result["badges"])
    # every family's first tier should be the next milestone
    ms = milestones_by_id(result)
    assert "streak_1" in ms
    assert ms["streak_1"].progress_current == 0
    assert ms["streak_1"].progress_target == 3


def test_exactly_at_threshold_is_earned():
    stats = dict(ZERO_STATS, streak_days=3)
    result = achievements.compute_achievements(stats)
    b = badges_by_id(result)
    assert b["streak_1"].earned is True
    assert b["streak_2"].earned is False


def test_one_below_threshold_not_earned_with_correct_progress():
    stats = dict(ZERO_STATS, streak_days=2)
    result = achievements.compute_achievements(stats)
    b = badges_by_id(result)
    assert b["streak_1"].earned is False
    ms = milestones_by_id(result)
    assert ms["streak_1"].progress_current == 2
    assert ms["streak_1"].progress_target == 3


def test_maxed_family_contributes_no_next_milestone():
    stats = dict(ZERO_STATS, streak_days=30)
    result = achievements.compute_achievements(stats)
    b = badges_by_id(result)
    assert all(b[f"streak_{i}"].earned for i in range(1, 5))
    ms = milestones_by_id(result)
    assert not any(k.startswith("streak_") for k in ms)


def test_diagnostic_boolean_toggles_correctly():
    result_false = achievements.compute_achievements(ZERO_STATS)
    assert badges_by_id(result_false)["diagnostic_taken"].earned is False
    assert "diagnostic_taken" in milestones_by_id(result_false)

    result_true = achievements.compute_achievements(dict(ZERO_STATS, diagnostic_completed=True))
    assert badges_by_id(result_true)["diagnostic_taken"].earned is True
    assert "diagnostic_taken" not in milestones_by_id(result_true)


def test_milestones_sorted_smallest_gap_first():
    stats = dict(ZERO_STATS, streak_days=2, questions_answered=0)
    result = achievements.compute_achievements(stats)
    gaps = [m.progress_target - m.progress_current for m in result["next_milestones"]]
    assert gaps == sorted(gaps)
    # streak (gap=1) should be the very first milestone
    assert result["next_milestones"][0].badge_id == "streak_1"


def test_every_tier_present_regardless_of_earned_state():
    result = achievements.compute_achievements(ZERO_STATS)
    ids = {b.id for b in result["badges"]}
    assert "streak_1" in ids and "streak_4" in ids
    assert "questions_1" in ids and "questions_4" in ids
    assert "chapters_mastered_1" in ids and "chapters_mastered_4" in ids
    assert "mock_tests_1" in ids and "mock_tests_3" in ids
    assert "diagnostic_taken" in ids
