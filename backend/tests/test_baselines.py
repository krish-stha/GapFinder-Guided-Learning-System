"""
Tests for evaluation/baselines/. The DKT test is structural only (correct
shapes, no NaNs after one training step) - NOT a full training run, since
LSTM training is slow/stochastic and doesn't belong in the fast pytest
suite. Full DKT training only happens when run_predictive_benchmark.py is
invoked directly.
Run with: pytest tests/test_baselines.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import torch

from evaluation.baselines.threshold import rank_chapters_threshold, predict_next_prefix
from evaluation.baselines.dkt import DKTModel, encode_student_sequence, build_padded_batch, _masked_bce_loss
from evaluation.synthetic import GeneratorConfig, generate_dataset, attempts_by_student


def test_rank_chapters_threshold_orders_weakest_first():
    attempts_by_chapter = {
        1: [{"is_correct": True}] * 8,          # 100% accuracy
        2: [{"is_correct": False}] * 8,          # 0% accuracy
        3: [{"is_correct": True}, {"is_correct": False}] * 4,  # 50% accuracy
    }
    ranked = rank_chapters_threshold(attempts_by_chapter)
    assert ranked == [2, 3, 1]


def test_predict_next_prefix_running_accuracy():
    attempts = [{"is_correct": True}, {"is_correct": False}, {"is_correct": True}]
    assert predict_next_prefix(attempts, 0) == 0.5  # no evidence yet
    assert predict_next_prefix(attempts, 1) == 1.0  # 1/1 correct so far
    assert abs(predict_next_prefix(attempts, 2) - 0.5) < 1e-9  # 1/2 correct so far


def test_dkt_forward_pass_shape_and_no_nans():
    config = GeneratorConfig(n_students=6, n_chapters=4, seed=1)
    records = generate_dataset(config)
    by_student = attempts_by_student(records)

    sequences = [encode_student_sequence(recs, config.n_chapters)
                 for recs in by_student.values() if len(recs) >= 2]
    X, mask, next_idx, Y = build_padded_batch(sequences, config.n_chapters)

    model = DKTModel(config.n_chapters, hidden_size=8)
    output = model(X)

    assert output.shape == (len(sequences), X.shape[1], config.n_chapters)
    assert not torch.isnan(output).any()


def test_dkt_one_training_step_reduces_loss_and_stays_finite():
    config = GeneratorConfig(n_students=6, n_chapters=4, seed=1)
    records = generate_dataset(config)
    by_student = attempts_by_student(records)

    sequences = [encode_student_sequence(recs, config.n_chapters)
                 for recs in by_student.values() if len(recs) >= 2]
    X, mask, next_idx, Y = build_padded_batch(sequences, config.n_chapters)

    torch.manual_seed(0)
    model = DKTModel(config.n_chapters, hidden_size=8)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

    loss_before = _masked_bce_loss(model(X), next_idx, Y, mask)
    optimizer.zero_grad()
    loss_before.backward()
    optimizer.step()
    loss_after = _masked_bce_loss(model(X), next_idx, Y, mask)

    assert torch.isfinite(loss_before)
    assert torch.isfinite(loss_after)
