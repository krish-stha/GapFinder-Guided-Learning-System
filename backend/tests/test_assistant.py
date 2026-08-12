"""
Unit tests for the rule-based assistant's intent matcher
(app/routers/practice.py:match_intent). Pure function, no DB - same
discipline as test_mastery.py - so these test the actual pattern-matching
decision boundary in isolation from the DB-backed answer formatting.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app.routers.practice import match_intent


def test_weak_chapters_intent_matches_the_spec_example_verbatim():
    # the user's own verbatim example from the feature spec
    intent, chapter_id = match_intent("Which chapters should I study before my exam?", {})
    assert intent == "weak_chapters"
    assert chapter_id is None


def test_weak_chapters_intent_matches_variants():
    for phrasing in ["what should I focus on?", "what's weak right now", "priority chapters please"]:
        intent, _ = match_intent(phrasing, {})
        assert intent == "weak_chapters", phrasing


def test_performance_summary_intent():
    intent, chapter_id = match_intent("How am I doing overall?", {})
    assert intent == "performance_summary"
    assert chapter_id is None


def test_streak_intent():
    intent, chapter_id = match_intent("What's my streak?", {})
    assert intent == "streak"
    assert chapter_id is None


def test_specific_chapter_intent_matches_a_tracked_chapter_by_name():
    intent, chapter_id = match_intent(
        "How am I doing in Physical Quantities?", {24059: "Physical Quantities", 7924: "Circular Motion"}
    )
    assert intent == "specific_chapter"
    assert chapter_id == 24059


def test_specific_chapter_intent_is_case_insensitive():
    intent, chapter_id = match_intent("tell me about PHYSICAL QUANTITIES", {24059: "Physical Quantities"})
    assert intent == "specific_chapter"
    assert chapter_id == 24059


def test_specific_chapter_checked_before_weak_chapters_when_both_could_match():
    # "study" would trigger weak_chapters, but a named chapter is more
    # specific and should win
    intent, chapter_id = match_intent(
        "should I study Physical Quantities more?", {24059: "Physical Quantities"}
    )
    assert intent == "specific_chapter"
    assert chapter_id == 24059


def test_unrecognized_question_falls_back_to_help():
    intent, chapter_id = match_intent("what's the weather like today?", {})
    assert intent == "help"
    assert chapter_id is None


def test_no_tracked_chapters_does_not_crash_specific_chapter_check():
    intent, chapter_id = match_intent("How am I doing overall?", {})
    assert intent == "performance_summary"
    assert chapter_id is None


def test_mastery_explain_intent():
    for phrasing in ["How is mastery calculated?", "what is mastery", "mastery vs accuracy"]:
        intent, _ = match_intent(phrasing, {})
        assert intent == "mastery_explain", phrasing


def test_mastery_explain_checked_before_chapters_mastered():
    # "mastery" alone would also satisfy the looser "master" pattern, but
    # an explicit "how is X calculated" question is more specific
    intent, _ = match_intent("How is mastery calculated?", {})
    assert intent == "mastery_explain"


def test_chapters_mastered_intent():
    intent, chapter_id = match_intent("How many chapters have I mastered?", {})
    assert intent == "chapters_mastered"
    assert chapter_id is None


def test_improving_intent():
    intent, chapter_id = match_intent("Am I improving?", {})
    assert intent == "improving"
    assert chapter_id is None


def test_questions_count_intent():
    intent, chapter_id = match_intent("How many questions have I answered?", {})
    assert intent == "questions_count"
    assert chapter_id is None


def test_subject_mastery_intent_matches_a_tracked_subject_by_name():
    intent, subject_id = match_intent("How am I doing in Chemistry?", {}, {5: "Chemistry", 6: "Physics"})
    assert intent == "subject_mastery"
    assert subject_id == 5


def test_specific_chapter_checked_before_subject_mastery():
    intent, matched_id = match_intent(
        "How am I doing in Physical Quantities?",
        {24059: "Physical Quantities"}, {6: "Physics"},
    )
    assert intent == "specific_chapter"
    assert matched_id == 24059
