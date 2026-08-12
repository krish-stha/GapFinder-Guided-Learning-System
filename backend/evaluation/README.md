# Evaluation tooling (RQ1/RQ2/RQ3)

Pure Python, no DB, no API - same philosophy as `app/engine/mastery.py`.
Every script here is independently runnable from `backend/`:

```
python -m evaluation.run_ground_truth_recovery     # J.1 -> RQ1 headline result
python -m evaluation.run_predictive_benchmark       # J.2 -> RQ2
python -m evaluation.run_sensitivity_analysis       # J.3 -> RQ3
```

Each prints a summary table to stdout and writes a JSON results file to
`evaluation/results/` (gitignored - regenerate anytime; commit the numbers
you actually cite, not the files).

## Data source - read this before citing any number here

Real activity data barely exists yet (a handful of manually-generated test
attempts from the live API). All three experiments run on the **synthetic
generator** in `synthetic.py`, per the project charter's own Section H.6:
real data has no ground truth to measure a detector against, so a synthetic
strand with *injected, known* weakness is required regardless of real-data
volume. Ground truth (`ground_truth_weak_chapters`) is computed only from
the generator's latent `true_ability_at_t` values - never from the
archetype label, never from sampled correctness - so it cannot be circular
with any model's own output, including the interpretable engine under test.

**Limitation, stated once here rather than in every script:** J.2's
"predictive benchmark" charter text calls for real + public data
(ASSISTments/Junyi). Public-dataset ingestion is a separate data-engineering
task (schema mapping, licence verification) that was out of scope for this
pass; real-DB-data ingestion is blocked on actual student usage volume that
doesn't exist yet within the project timeline. Both are Further Work. This
is the same honest-fallback framing the charter itself uses for a DKT
baseline that might not train in time (Section K.1) - applied here to the
data source instead of the model.

## `synthetic.py` - the generator

`generate_dataset(GeneratorConfig())` produces ~20k attempt records across
120 students × 10 chapters. Each student gets one of six archetypes per
chapter (`chronically_weak`, `declining`, `improving`, `noisy_adequate`,
`sparse`, `healthy`), with at least one weak/declining/improving chapter
guaranteed per student. Response correctness is sampled from
`sigmoid(true_ability − difficulty)`. Every record carries **both** a
per-chapter `order` (what `compute_chapter_evidence` expects) and a
per-student `global_order` (the interleaved cross-chapter sequence DKT
needs). Reproducible via a local `random.Random(seed)` instance - no global
random state is ever touched.

`attempts_per_chapter_range` is deliberately kept mostly above
`MIN_ATTEMPTS_FOR_CONFIDENCE` (10) so the ground-truth-recovery experiment
mainly tests ranking *quality*, not the sparsity-confidence gate - the
dedicated `sparse` archetype (2–4 attempts) is where that gate is meant to
dominate instead. This was a real calibration finding, not an assumption:
an earlier, lower attempt-count range caused the confidence gate to fire on
~50% of chapters regardless of archetype, which dragged the interpretable
model *below* the threshold baseline on recovery - not because the model
was wrong, but because the experiment wasn't giving it enough evidence to
use its own designed sparsity-awareness correctly. Worth a sentence in the
report: it's a concrete illustration of why the confidence field exists.

## J.1 - `run_ground_truth_recovery.py`

Ranks each student's chapters two ways (interpretable model via
`mastery.rank_chapters`, and the naive threshold baseline via
`rank_chapters_threshold`) and measures precision/recall/F1@3 against the
ground-truth weak-chapter set. Evaluated only over students with at least
one truly weak chapter (standard practice - a student with none has no
positive case to recover). Runtime: a few seconds.

Latest run: interpretable model F1 = 0.631 vs. threshold baseline F1 =
0.598 (92/120 students evaluated) - the model recovers injected weaknesses
better than the naive baseline, the headline RQ1 result.

## J.2 - `run_predictive_benchmark.py`

Held-out next-response prediction, AUC + RMSE, for the threshold baseline,
the interpretable model, and DKT. Split **by student** (80/20, seeded) -
splitting by attempt would leak a held-out student's own future responses
into their own evaluation through DKT's recurrent state.

All three models are scored on an **identical event set**: for every
held-out student, every attempt at chapter-local position `order ≥ 1`. The
threshold baseline and interpretable model predict from that chapter's own
prefix only; DKT predicts from the same event but using the student's
*full cross-chapter* history (that asymmetry is real and is the actual
subject of RQ2, not something to hide - DKT is allowed to win by using more
information; the question is how much that's worth).

DKT training uses early stopping against an internal validation slice
carved out of the training students (never the real held-out test set) -
this was necessary, not cosmetic: a fixed low epoch count under-trained the
model (AUC ≈ 0.676, below both baselines), and training much longer
over-fit it (loss kept falling while held-out AUC dropped from ~0.69 to
~0.58 by epoch 600). Early stopping is what makes the reported number
trustworthy rather than an artifact of an arbitrarily-chosen epoch count.

Runtime: ~10-30 seconds on CPU at the default dataset size.

Latest run (96 train / 24 held-out students): threshold AUC 0.690, RMSE
0.490; interpretable AUC 0.691, RMSE 0.491; DKT AUC 0.699, RMSE 0.469. DKT
wins, narrowly, on both metrics - a modest, defensible margin for the
"cost of interpretability" discussion in RQ2, not a dramatic one. That's
itself worth discussing: within-chapter evidence, once there are enough
attempts, already captures most of what's predictable; DKT's edge comes
from the modest amount of additional signal in cross-chapter correlation
(a shared per-student ability term in the generator).

## J.3 - `run_sensitivity_analysis.py`

30 parameter configurations against `app/engine/mastery.MasteryWeights`: 20
one-at-a-time (recency half-life, difficulty-weight scale, volume prior,
trend weight - 5 values each, exceeding the charter's ≥20 minimum on its
own) plus 10 jointly-randomized configs (checks for interaction effects the
OAT sweep alone would miss). Rank stability of each config's per-student
chapter ranking vs. the default-weights ranking is measured via Kendall's
tau (full ranking) and overlap@5 (top-5 set overlap). Runtime: a few
seconds.

Latest run: mean Kendall's tau ranges 0.706–1.000 across the 30 configs
(median 0.919); 4/30 configs show meaningful instability (tau < 0.8), most
of them at the extremes of the volume-prior (`min_attempts_for_confidence`)
sweep - unsurprising, since that parameter directly controls how many
chapters get gated into "Insufficient evidence" and sorted to the bottom
regardless of score. Reported as-is, per the charter's own guidance
(Section I.5): if the ranking is unstable under some parameter choices,
that instability is itself the RQ3 finding, not a result to explain away.

## Tests

`tests/test_synthetic.py`, `tests/test_metrics.py`, `tests/test_baselines.py`
- fast, DB-free, run as part of the normal suite (`pytest tests/ -v`). The
DKT test is structural only (forward-pass shape, no NaNs, loss stays finite
after one training step) - not a full training run, which is slow and
stochastic and belongs in the runner script, not the fast test suite.
