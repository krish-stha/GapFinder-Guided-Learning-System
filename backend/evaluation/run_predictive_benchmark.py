"""
J.2 - Predictive benchmark (RQ2): what predictive accuracy is sacrificed by
the interpretable mastery model relative to a DKT baseline, and how does a
naive percentage-threshold baseline compare? Reports AUC and RMSE for all
three on an identical held-out student split, evaluated on an identical
prediction-event set.

Run from `backend/`:
    python -m evaluation.run_predictive_benchmark

Uses the SAME synthetic dataset as J.1 (documented limitation: real usage
data is far too sparse to train/evaluate a DKT baseline within the project
timeline, and public-dataset ingestion, e.g. ASSISTments/Junyi, is out of
scope for this pass - both are Further Work, consistent with the charter's
own honest-fallback framing in Section K.1).

Split: by STUDENT (80/20, seeded), not by attempt - splitting by attempt
would leak a held-out student's own future responses into their own
evaluation through DKT's recurrent hidden state.

Evaluation events: for every held-out student, every attempt at
chapter-local position `order >= 1` (i.e. every attempt except the first
one in each chapter, which has no prefix to predict from). All three
models are scored on exactly this same event set:
  - threshold baseline : running accuracy of that chapter's prefix
  - interpretable model: compute_chapter_evidence(...).mastery_estimate on that chapter's prefix
  - DKT                 : the recurrent model's prediction at that exact
                           global-sequence position, using the student's
                           FULL cross-chapter history up to that point
DKT genuinely gets more information (cross-chapter history) than the other
two - that asymmetry is the real, honestly-reported subject of RQ2, not an
artefact to hide. Expect DKT to win on AUC; the point is to measure the
margin, not to erase it.
"""
import json
import random
from pathlib import Path

from app.engine import mastery
from evaluation.synthetic import GeneratorConfig, generate_dataset, attempts_by_student_chapter, attempts_by_student
from evaluation.baselines.threshold import predict_next_prefix
from evaluation.baselines.dkt import train_dkt, predict_walk_forward
from evaluation.metrics import auc, rmse

RESULTS_PATH = Path(__file__).parent / "results" / "predictive_benchmark.json"
TEST_FRACTION = 0.2
SPLIT_SEED = 99
DKT_HIDDEN_SIZE = 64
DKT_MAX_EPOCHS = 300
DKT_PATIENCE = 15


def _split_students(student_ids: list, test_fraction: float, seed: int):
    ids = sorted(student_ids)
    random.Random(seed).shuffle(ids)
    n_test = max(1, int(len(ids) * test_fraction))
    return ids[n_test:], ids[:n_test]  # train, test


def _threshold_and_interpretable(test_ids, by_student_chapter, n_chapters):
    events = {"threshold": {"true": [], "pred": []}, "interpretable": {"true": [], "pred": []}}
    for sid in test_ids:
        for chapter_id in range(n_chapters):
            atts = by_student_chapter.get((sid, chapter_id))
            if not atts:
                continue
            for k in range(1, len(atts)):
                true = 1.0 if atts[k]["is_correct"] else 0.0
                events["threshold"]["true"].append(true)
                events["threshold"]["pred"].append(predict_next_prefix(atts, k))
                ev = mastery.compute_chapter_evidence(chapter_id, atts[:k])
                events["interpretable"]["true"].append(true)
                events["interpretable"]["pred"].append(ev.mastery_estimate)
    return events


def _dkt(test_ids, by_student, train_ids, n_chapters, hidden_size, max_epochs, patience):
    train_records = {sid: by_student[sid] for sid in train_ids}
    model = train_dkt(train_records, n_chapters, hidden_size=hidden_size,
                       max_epochs=max_epochs, patience=patience)

    true_list, pred_list = [], []
    for sid in test_ids:
        seq = by_student[sid]
        preds = predict_walk_forward(model, seq, n_chapters)  # aligned to seq[1:]
        for (true, pred), record in zip(preds, seq[1:]):
            if record.order >= 1:  # same eligibility filter as threshold/interpretable
                true_list.append(true)
                pred_list.append(pred)
    return true_list, pred_list


def run(config: GeneratorConfig = GeneratorConfig()) -> dict:
    records = generate_dataset(config)
    by_student_chapter = attempts_by_student_chapter(records)
    by_student = attempts_by_student(records)

    train_ids, test_ids = _split_students(list(by_student.keys()), TEST_FRACTION, SPLIT_SEED)

    events = _threshold_and_interpretable(test_ids, by_student_chapter, config.n_chapters)
    dkt_true, dkt_pred = _dkt(test_ids, by_student, train_ids, config.n_chapters,
                               DKT_HIDDEN_SIZE, DKT_MAX_EPOCHS, DKT_PATIENCE)

    def score(true, pred):
        a = auc(true, pred)
        return {"auc": round(a, 4) if a is not None else None, "rmse": round(rmse(true, pred), 4)}

    result = {
        "n_train_students": len(train_ids), "n_test_students": len(test_ids),
        "n_eval_events": {"threshold_baseline": len(events["threshold"]["true"]),
                           "interpretable_model": len(events["interpretable"]["true"]),
                           "dkt": len(dkt_true)},
        "threshold_baseline": score(events["threshold"]["true"], events["threshold"]["pred"]),
        "interpretable_model": score(events["interpretable"]["true"], events["interpretable"]["pred"]),
        "dkt": score(dkt_true, dkt_pred),
        "config": {"seed": config.seed, "n_students": config.n_students, "n_chapters": config.n_chapters,
                   "test_fraction": TEST_FRACTION, "split_seed": SPLIT_SEED,
                   "dkt_hidden_size": DKT_HIDDEN_SIZE, "dkt_max_epochs": DKT_MAX_EPOCHS,
                   "dkt_patience": DKT_PATIENCE},
    }
    return result


if __name__ == "__main__":
    result = run()

    print(f"J.2 Predictive benchmark - {result['n_train_students']} train / "
          f"{result['n_test_students']} held-out students\n")
    print(f"{'Model':<22}{'AUC':>10}{'RMSE':>10}{'N events':>12}")
    for name, key in (("Threshold baseline", "threshold_baseline"),
                       ("Interpretable model", "interpretable_model"),
                       ("DKT", "dkt")):
        m = result[key]
        auc_str = f"{m['auc']:.3f}" if m["auc"] is not None else "n/a"
        n_events = result["n_eval_events"][key]
        print(f"{name:<22}{auc_str:>10}{m['rmse']:>10.4f}{n_events:>12}")

    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_PATH.write_text(json.dumps(result, indent=2))
    print(f"\nWrote {RESULTS_PATH}")
