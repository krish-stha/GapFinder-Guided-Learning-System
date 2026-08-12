"""
Minimal DKT baseline (Piech et al. 2015 one-hot encoding): a single-layer
LSTM over a student's whole interleaved cross-chapter attempt sequence,
predicting P(correct) per chapter at every step from the history seen so
far.

Deliberately small (~100-150 lines) rather than an off-the-shelf benchmark
library (pyKT) - full control over the data format (this project's own
attempt schema, no adapter layer), lower integration risk, easier to keep
deterministic given the project's timeline. See project charter Section
G.2 ("DKT baseline") for the alternatives considered.

Train/eval protocol: split by STUDENT, not by attempt - splitting by
attempt would leak a held-out student's own future responses into their
own evaluation through the recurrent hidden state. Within a held-out
student's sequence, the prediction at position t uses only the recurrent
state built from attempts [0..t-1]; a single forward pass gives this at
every position for free, which is what makes it directly comparable to the
walk-forward protocol used for the threshold baseline and the interpretable
engine (see run_predictive_benchmark.py).
"""
import random

import torch
import torch.nn as nn


class DKTModel(nn.Module):
    def __init__(self, n_chapters: int, hidden_size: int = 64, n_layers: int = 1):
        super().__init__()
        self.n_chapters = n_chapters
        self.lstm = nn.LSTM(2 * n_chapters, hidden_size, n_layers, batch_first=True)
        self.output = nn.Linear(hidden_size, n_chapters)

    def forward(self, x):
        # x: (batch, seq_len, 2*n_chapters) one-hot -> (batch, seq_len, n_chapters) sigmoid probs
        h, _ = self.lstm(x)
        return torch.sigmoid(self.output(h))


def encode_student_sequence(records: list, n_chapters: int):
    """records: one student's attempts, sorted by global_order. Returns
    (x, next_chapter_idx, y) as plain Python lists, length len(records)-1
    (the last attempt has nothing after it to predict):
        x[t]                : one-hot(2*n_chapters) for attempt t (input at step t)
        next_chapter_idx[t]  : chapter_id of attempt t+1 (what's being predicted from x[0..t])
        y[t]                 : correctness (0.0/1.0) of attempt t+1
    """
    x, next_chapter_idx, y = [], [], []
    for t in range(len(records) - 1):
        r = records[t]
        vec = [0.0] * (2 * n_chapters)
        vec[r.chapter_id * 2 + (1 if r.is_correct else 0)] = 1.0
        x.append(vec)
        nxt = records[t + 1]
        next_chapter_idx.append(nxt.chapter_id)
        y.append(1.0 if nxt.is_correct else 0.0)
    return x, next_chapter_idx, y


def build_padded_batch(sequences: list, n_chapters: int):
    """sequences: list of (x, next_chapter_idx, y) tuples from
    encode_student_sequence, possibly different lengths. Returns padded
    tensors: X (batch, max_len, 2*n_chapters), mask (batch, max_len) of
    1.0/0.0, next_idx (batch, max_len) long, Y (batch, max_len) float."""
    max_len = max(len(x) for x, _, _ in sequences)
    input_size = 2 * n_chapters
    batch = len(sequences)

    X = torch.zeros(batch, max_len, input_size)
    mask = torch.zeros(batch, max_len)
    next_idx = torch.zeros(batch, max_len, dtype=torch.long)
    Y = torch.zeros(batch, max_len)

    for i, (x, nxt, y) in enumerate(sequences):
        L = len(x)
        if L == 0:
            continue
        X[i, :L] = torch.tensor(x)
        mask[i, :L] = 1.0
        next_idx[i, :L] = torch.tensor(nxt, dtype=torch.long)
        Y[i, :L] = torch.tensor(y)

    return X, mask, next_idx, Y


def _masked_bce_loss(pred_probs, next_idx, y, mask):
    """pred_probs: (batch, max_len, n_chapters). Gathers the predicted
    probability at the chapter actually attempted next, then computes BCE
    only at valid (non-padded) positions."""
    picked = pred_probs.gather(2, next_idx.unsqueeze(-1)).squeeze(-1)  # (batch, max_len)
    eps = 1e-7
    picked = picked.clamp(eps, 1 - eps)
    bce = -(y * torch.log(picked) + (1 - y) * torch.log(1 - picked))
    return (bce * mask).sum() / mask.sum().clamp(min=1.0)


def train_dkt(train_student_records: dict, n_chapters: int, hidden_size: int = 64,
              max_epochs: int = 300, lr: float = 0.005, patience: int = 15,
              val_fraction: float = 0.2, seed: int = 0) -> DKTModel:
    """train_student_records: {student_id: [SyntheticRecord, ...]} sorted by
    global_order - training students only (the real held-out test set the
    caller will evaluate on is never touched here).

    Full-batch training with early stopping: a `val_fraction` slice of
    these training students (seeded, disjoint from the fit slice) is held
    out purely to decide when to stop. Without this, a fixed epoch count
    either underfits (predictions barely beat a coin flip) or overfits
    (training loss keeps falling while held-out AUC degrades, since
    full-batch Adam on a small student pool memorises sequences quickly) -
    both were observed empirically while calibrating this baseline. Returns
    the model state with the lowest validation loss seen; stops once
    validation loss fails to improve for `patience` consecutive epochs."""
    torch.manual_seed(seed)
    ids = sorted(train_student_records.keys())
    random.Random(seed).shuffle(ids)
    n_val = max(1, int(len(ids) * val_fraction))
    val_ids, fit_ids = ids[:n_val], ids[n_val:]

    fit_sequences = [encode_student_sequence(train_student_records[sid], n_chapters)
                      for sid in fit_ids if len(train_student_records[sid]) >= 2]
    val_sequences = [encode_student_sequence(train_student_records[sid], n_chapters)
                      for sid in val_ids if len(train_student_records[sid]) >= 2]

    X, mask, next_idx, Y = build_padded_batch(fit_sequences, n_chapters)
    Xv, maskv, next_idxv, Yv = build_padded_batch(val_sequences, n_chapters)

    model = DKTModel(n_chapters, hidden_size=hidden_size)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    best_val_loss = float("inf")
    best_state = None
    epochs_without_improvement = 0

    for _ in range(max_epochs):
        model.train()
        optimizer.zero_grad()
        loss = _masked_bce_loss(model(X), next_idx, Y, mask)
        loss.backward()
        optimizer.step()

        model.eval()
        with torch.no_grad():
            val_loss = _masked_bce_loss(model(Xv), next_idxv, Yv, maskv).item()

        if val_loss < best_val_loss - 1e-4:
            best_val_loss = val_loss
            best_state = {k: v.clone() for k, v in model.state_dict().items()}
            epochs_without_improvement = 0
        else:
            epochs_without_improvement += 1
            if epochs_without_improvement >= patience:
                break

    if best_state is not None:
        model.load_state_dict(best_state)
    return model


def predict_walk_forward(model: DKTModel, student_records: list, n_chapters: int) -> list:
    """A single forward pass over one held-out student's sequence naturally
    gives a prefix-only prediction at every step (the hidden state at t
    only ever saw attempts [0..t]). Returns [(y_true, y_pred), ...] for
    every predictable step. Empty list if the student has < 2 attempts."""
    if len(student_records) < 2:
        return []
    x, next_idx, y = encode_student_sequence(student_records, n_chapters)
    model.eval()
    with torch.no_grad():
        X = torch.tensor(x).unsqueeze(0)
        pred = model(X).squeeze(0)  # (seq_len, n_chapters)
        idx = torch.tensor(next_idx, dtype=torch.long).unsqueeze(-1)
        picked = pred.gather(1, idx).squeeze(-1)
    return list(zip(y, picked.tolist()))
