"""
J.3 - Sensitivity analysis (RQ3): how much does the weakness ranking change
under different parameter choices, and what does that imply about the
confidence with which such rankings should be presented to learners?

20 one-at-a-time (OAT) configurations (four parameters swept independently
across five values each) plus 10 jointly-randomized configurations (checks
for interaction effects the OAT sweep alone would miss) = 30 configurations,
exceeding the charter's >=20 minimum (Objective O7).

Run from `backend/`:
    python -m evaluation.run_sensitivity_analysis

Rank stability is measured against the DEFAULT_WEIGHTS ranking via Kendall's
tau (full per-student chapter ordering) and overlap@5 (top-5 set overlap).
Reported honestly regardless of outcome - per the charter (Section I.5): if
the ranking turns out unstable, that instability is itself the RQ3 finding,
not a result to explain away.
"""
import json
import statistics
from pathlib import Path

import numpy as np

from app.engine import mastery
from evaluation.synthetic import GeneratorConfig, generate_dataset, attempts_by_student_chapter
from evaluation.metrics import kendalls_tau, overlap_at_k

RESULTS_PATH = Path(__file__).parent / "results" / "sensitivity_analysis.json"

# each OAT list includes the default value, so one config per parameter is
# a trivial tau=1.0 sanity check that the sweep reproduces the baseline
OAT_RANGES = {
    "recency_half_life": [1, 3, 5, 10, 15],
    "difficulty_weight_scale": [0.0, 0.5, 1.0, 1.5, 2.0],   # scales Medium/Hard weight above Easy=1.0
    "min_attempts_for_confidence": [3, 6, 10, 15, 20],
    "trend_penalty": [0.0, 0.075, 0.15, 0.225, 0.3],
}
DEFAULTS = {"recency_half_life": 5, "difficulty_weight_scale": 1.0,
            "min_attempts_for_confidence": 10, "trend_penalty": 0.15}
N_RANDOM_CONFIGS = 10
RANDOM_SEED = 7


def _weights_from(recency_half_life, difficulty_weight_scale, min_attempts_for_confidence, trend_penalty):
    difficulty_weight = {"Easy": 1.0, "Medium": 1.0 + 0.5 * difficulty_weight_scale,
                          "Hard": 1.0 + 1.0 * difficulty_weight_scale}
    return mastery.MasteryWeights(
        difficulty_weight=difficulty_weight, recency_half_life=recency_half_life,
        min_attempts_for_confidence=min_attempts_for_confidence, trend_penalty=trend_penalty,
    )


def _build_configs() -> list:
    configs = []
    for param, values in OAT_RANGES.items():
        for v in values:
            kwargs = dict(DEFAULTS)
            kwargs[param] = v
            configs.append({"label": f"OAT:{param}={v}", "sweep_param": param, "sweep_value": v,
                             "weights": _weights_from(**kwargs)})

    rng = np.random.default_rng(RANDOM_SEED)
    for i in range(N_RANDOM_CONFIGS):
        kwargs = {
            "recency_half_life": float(rng.uniform(1, 15)),
            "difficulty_weight_scale": float(rng.uniform(0, 2)),
            "min_attempts_for_confidence": float(rng.uniform(3, 20)),
            "trend_penalty": float(rng.uniform(0, 0.3)),
        }
        configs.append({"label": f"RANDOM:{i}", "sweep_param": "joint", "sweep_value": None,
                         "weights": _weights_from(**kwargs)})
    return configs


def _ranking(attempts_by_chapter: dict, weights: mastery.MasteryWeights) -> list:
    evidence = [mastery.compute_chapter_evidence(cid, atts, weights=weights)
                for cid, atts in attempts_by_chapter.items()]
    return [e.chapter_id for e in mastery.rank_chapters(evidence)]


def run(config: GeneratorConfig = GeneratorConfig()) -> dict:
    records = generate_dataset(config)
    by_student_chapter = attempts_by_student_chapter(records)

    students_by_chapter: dict = {}
    for (student_id, chapter_id), atts in by_student_chapter.items():
        students_by_chapter.setdefault(student_id, {})[chapter_id] = atts

    default_ranking_by_student = {
        sid: _ranking(chapters, mastery.DEFAULT_WEIGHTS) for sid, chapters in students_by_chapter.items()
    }

    sweep_configs = _build_configs()
    per_config_results = []
    for cfg in sweep_configs:
        taus, overlaps = [], []
        for sid, chapters in students_by_chapter.items():
            cfg_ranking = _ranking(chapters, cfg["weights"])
            default_ranking = default_ranking_by_student[sid]
            tau = kendalls_tau(cfg_ranking, default_ranking)
            if tau is not None:
                taus.append(tau)
            overlaps.append(overlap_at_k(cfg_ranking, default_ranking, 5))

        per_config_results.append({
            "label": cfg["label"], "sweep_param": cfg["sweep_param"], "sweep_value": cfg["sweep_value"],
            "mean_kendalls_tau": round(statistics.mean(taus), 4) if taus else None,
            "median_kendalls_tau": round(statistics.median(taus), 4) if taus else None,
            "mean_overlap_at_5": round(statistics.mean(overlaps), 4),
        })

    all_taus = [r["mean_kendalls_tau"] for r in per_config_results if r["mean_kendalls_tau"] is not None]
    summary = {
        "n_configs": len(sweep_configs),
        "n_students": len(students_by_chapter),
        "overall_min_mean_tau": round(min(all_taus), 4),
        "overall_median_mean_tau": round(statistics.median(all_taus), 4),
        "overall_max_mean_tau": round(max(all_taus), 4),
        "configs_with_mean_tau_below_0.8": sum(1 for t in all_taus if t < 0.8),
    }

    return {"summary": summary, "configs": per_config_results}


if __name__ == "__main__":
    result = run()
    s = result["summary"]

    print(f"J.3 Sensitivity analysis - {s['n_configs']} configurations, {s['n_students']} students\n")
    print(f"Kendall's tau vs. default weights: min={s['overall_min_mean_tau']}, "
          f"median={s['overall_median_mean_tau']}, max={s['overall_max_mean_tau']}")
    print(f"Configs with mean tau < 0.8 (meaningfully unstable): "
          f"{s['configs_with_mean_tau_below_0.8']}/{s['n_configs']}\n")

    print(f"{'Config':<28}{'Mean tau':>12}{'Overlap@5':>12}")
    for r in result["configs"]:
        tau_str = f"{r['mean_kendalls_tau']:.3f}" if r["mean_kendalls_tau"] is not None else "n/a"
        print(f"{r['label']:<28}{tau_str:>12}{r['mean_overlap_at_5']:>12.3f}")

    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_PATH.write_text(json.dumps(result, indent=2))
    print(f"\nWrote {RESULTS_PATH}")
