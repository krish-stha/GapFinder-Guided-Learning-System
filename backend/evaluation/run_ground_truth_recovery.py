"""
J.1 - Ground-truth recovery (synthetic). The headline result for RQ1: does
the interpretable model rank deliberately-injected weak chapters above
healthy ones better than a naive percentage-threshold baseline?

Run from `backend/`:
    python -m evaluation.run_ground_truth_recovery

No DB, no API - pure synthetic data with known ground truth, computed only
from the generator's latent ability trajectories (see evaluation/synthetic.py
for why this is non-circular with the model's own output).

Evaluated only over students who have at least one truly weak chapter
(students with none have no positive case to recover, so precision/recall@k
is undefined/not meaningful for them - standard practice, same as excluding
zero-relevant-result queries in IR evaluation).
"""
import json
import statistics
from pathlib import Path

from app.engine import mastery
from evaluation.synthetic import GeneratorConfig, generate_dataset, ground_truth_weak_chapters, attempts_by_student_chapter
from evaluation.baselines.threshold import rank_chapters_threshold
from evaluation.metrics import precision_recall_f1_at_k

K = 3
RESULTS_PATH = Path(__file__).parent / "results" / "ground_truth_recovery.json"


def _interpretable_ranking(attempts_by_chapter: dict) -> list:
    evidence = [mastery.compute_chapter_evidence(cid, atts) for cid, atts in attempts_by_chapter.items()]
    ranked = mastery.rank_chapters(evidence)
    return [e.chapter_id for e in ranked]


def run(config: GeneratorConfig = GeneratorConfig()) -> dict:
    records = generate_dataset(config)
    ground_truth = ground_truth_weak_chapters(records, config)
    by_student_chapter = attempts_by_student_chapter(records)

    students_by_chapter: dict = {}
    for (student_id, chapter_id), atts in by_student_chapter.items():
        students_by_chapter.setdefault(student_id, {})[chapter_id] = atts

    interpretable_scores, threshold_scores = [], []
    for student_id, gt_weak in ground_truth.items():
        attempts_by_chapter = students_by_chapter[student_id]

        interp_ranking = _interpretable_ranking(attempts_by_chapter)
        thresh_ranking = rank_chapters_threshold(attempts_by_chapter)

        interpretable_scores.append(precision_recall_f1_at_k(interp_ranking, gt_weak, K))
        threshold_scores.append(precision_recall_f1_at_k(thresh_ranking, gt_weak, K))

    def aggregate(scores):
        return {
            metric: round(statistics.mean(s[metric] for s in scores), 4)
            for metric in ("precision", "recall", "f1")
        }

    result = {
        "k": K,
        "n_students_evaluated": len(ground_truth),
        "n_students_total": config.n_students,
        "interpretable_model": aggregate(interpretable_scores),
        "threshold_baseline": aggregate(threshold_scores),
        "config": {"seed": config.seed, "n_students": config.n_students, "n_chapters": config.n_chapters,
                   "weak_ability_threshold": config.weak_ability_threshold},
    }
    return result


if __name__ == "__main__":
    result = run()

    print(f"J.1 Ground-truth recovery (top-{result['k']}, "
          f"{result['n_students_evaluated']}/{result['n_students_total']} students with >=1 true weak chapter)\n")
    print(f"{'Model':<22}{'Precision':>12}{'Recall':>12}{'F1':>12}")
    for name, key in (("Interpretable model", "interpretable_model"), ("Threshold baseline", "threshold_baseline")):
        m = result[key]
        print(f"{name:<22}{m['precision']:>12.3f}{m['recall']:>12.3f}{m['f1']:>12.3f}")

    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_PATH.write_text(json.dumps(result, indent=2))
    print(f"\nWrote {RESULTS_PATH}")
