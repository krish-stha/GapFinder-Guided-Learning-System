"""
Sanity tests for the synthetic generator (evaluation/synthetic.py). No DB,
no HTTP - matches the pure-function philosophy of the rest of the engine.
Run with: pytest tests/test_synthetic.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import statistics

from evaluation.synthetic import (
    GeneratorConfig, SyntheticRecord, generate_dataset, ground_truth_weak_chapters,
    attempts_by_student_chapter, attempts_by_student,
)

SMALL_CONFIG = GeneratorConfig(n_students=15, n_chapters=6, seed=123)


def test_generation_is_reproducible_with_fixed_seed():
    a = generate_dataset(SMALL_CONFIG)
    b = generate_dataset(SMALL_CONFIG)
    assert a == b


def test_different_seeds_give_different_output():
    a = generate_dataset(SMALL_CONFIG)
    b = generate_dataset(GeneratorConfig(n_students=15, n_chapters=6, seed=999))
    assert a != b


def test_covers_all_configured_students_and_chapters():
    records = generate_dataset(SMALL_CONFIG)
    assert {r.student_id for r in records} == set(range(SMALL_CONFIG.n_students))
    assert {r.chapter_id for r in records} == set(range(SMALL_CONFIG.n_chapters))


def test_chronically_weak_archetype_scores_much_lower_than_healthy():
    # statistical sanity over a larger sample, not an exact-value assertion
    config = GeneratorConfig(n_students=200, n_chapters=8, seed=7)
    records = generate_dataset(config)
    weak = [r.is_correct for r in records if r.archetype == "chronically_weak"]
    healthy = [r.is_correct for r in records if r.archetype == "healthy"]
    assert statistics.mean(weak) < statistics.mean(healthy) - 0.2


def test_declining_ends_weaker_than_it_started():
    config = GeneratorConfig(n_students=200, n_chapters=8, seed=7)
    records = generate_dataset(config)
    declining = [r for r in records if r.archetype == "declining"]
    grouped = {}
    for r in declining:
        grouped.setdefault((r.student_id, r.chapter_id), []).append(r)
    early_ability, late_ability = [], []
    for recs in grouped.values():
        recs.sort(key=lambda r: r.order)
        if len(recs) < 4:
            continue
        early_ability.append(recs[0].true_ability_at_t)
        late_ability.append(recs[-1].true_ability_at_t)
    assert statistics.mean(late_ability) < statistics.mean(early_ability)


def test_sparse_archetype_has_fewer_attempts_than_others():
    records = generate_dataset(SMALL_CONFIG)
    grouped = {}
    for r in records:
        grouped.setdefault((r.student_id, r.chapter_id, r.archetype), []).append(r)
    sparse_counts = [len(v) for k, v in grouped.items() if k[2] == "sparse"]
    other_counts = [len(v) for k, v in grouped.items() if k[2] != "sparse"]
    assert sparse_counts, "expected at least one sparse chapter in this config"
    assert max(sparse_counts) < min(other_counts)


def test_ground_truth_is_derived_only_from_final_ability_not_archetype_label():
    # two hand-built "declining"-labelled chapters: one truly ends weak,
    # one truly ends healthy. Ground truth must track the ability value at
    # the final attempt, not the archetype string, proving it's non-circular
    # with any model that only ever sees is_correct/difficulty_label.
    config = GeneratorConfig(weak_ability_threshold=-0.5)
    ends_weak = [
        SyntheticRecord(student_id=0, chapter_id=0, order=0, global_order=0,
                         is_correct=True, difficulty_label="Medium",
                         true_ability_at_t=0.9, archetype="declining"),
        SyntheticRecord(student_id=0, chapter_id=0, order=1, global_order=1,
                         is_correct=False, difficulty_label="Medium",
                         true_ability_at_t=-1.0, archetype="declining"),
    ]
    ends_healthy = [
        SyntheticRecord(student_id=1, chapter_id=0, order=0, global_order=0,
                         is_correct=False, difficulty_label="Medium",
                         true_ability_at_t=-1.0, archetype="improving"),
        SyntheticRecord(student_id=1, chapter_id=0, order=1, global_order=1,
                         is_correct=True, difficulty_label="Medium",
                         true_ability_at_t=0.9, archetype="improving"),
    ]
    gt = ground_truth_weak_chapters(ends_weak + ends_healthy, config)
    assert gt.get(0) == {0}          # student 0's chapter 0 IS weak (ends at -1.0)
    assert gt.get(1, set()) == set()  # student 1's chapter 0 is NOT weak (ends at 0.9)


def test_attempts_by_student_chapter_matches_mastery_engine_input_shape():
    records = generate_dataset(SMALL_CONFIG)
    grouped = attempts_by_student_chapter(records)
    some_key = next(iter(grouped))
    atts = grouped[some_key]
    assert all(set(a.keys()) == {"is_correct", "difficulty_label", "order"} for a in atts)
    assert [a["order"] for a in atts] == list(range(len(atts)))  # sorted, 0-based, contiguous


def test_attempts_by_student_sorted_by_global_order():
    records = generate_dataset(SMALL_CONFIG)
    grouped = attempts_by_student(records)
    for recs in grouped.values():
        orders = [r.global_order for r in recs]
        assert orders == sorted(orders)
