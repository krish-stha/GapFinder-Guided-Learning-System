# GapFinder - backend

## Why this exists

Most practice platforms tell a student "you're at 62% in Physics" and stop there. That number treats every question as equally hard, treats an answer from three weeks ago the same as one from this morning, and says nothing about whether 62% is based on 3 attempts or 300.

GapFinder is built around a different idea: figure out which *chapters* a student is actually weak in, and be able to explain why, using evidence rather than a single flat percentage. The scoring model blends difficulty (harder questions count for more), recency (a recent answer says more about where you are now than an old one), and how much data actually backs the number (a chapter with 2 attempts is flagged as "not enough evidence yet," not confidently ranked as strong or weak). It's benchmarked against a plain percentage-threshold baseline and against a small deep-learning model (DKT), so the dissertation can actually show what the interpretable approach costs or gains, not just assert it's better.

The curriculum tree and question bank come from a partner test-prep content provider, under a written data-sharing agreement for this project. All student activity - every practice session, answer, and score - is generated inside this app itself, so the evidence behind every mastery estimate is real and traceable, not simulated.

## Getting it running

```
pip install -r requirements.txt
```

**Import the curriculum and question bank:**
```
python -m app.services.import_content ../../Data/pipeline_out ../../Data/courses.xlsx
```
This builds `guided_learning.db` (SQLite by default - used whenever `.env`'s `DATABASE_URL` is unset). Safe to re-run; it upserts rather than duplicating.

Don't run the server against a `.db` file that lives inside a OneDrive/Dropbox-synced folder for long stretches - the sync client and SQLite's file locking don't get along. Fine for a quick script, not for active development.

To use Postgres instead, set `DATABASE_URL=postgresql://user:pass@host:port/dbname` in `.env` (template in `.env.example`). If you've already got a populated SQLite dev database, `python -m scripts.migrate_sqlite_to_postgres` copies everything across, including sequence resets so new rows don't collide with migrated ids.

**Run the server:**
```
uvicorn app.main:app --reload
```
API docs at http://127.0.0.1:8000/docs.

**Run the tests:**
```
pytest tests/ -v
```
All pure-Python, no database needed - the mastery engine (sparsity, trend detection, difficulty weighting, ranking, explanation output), the achievements engine, the synthetic data generator, the shared metrics, and the baselines (a threshold model plus a structural DKT check).

**Run the evaluation scripts** (these produce the dissertation's RQ1/RQ2/RQ3 results):
```
python -m evaluation.run_ground_truth_recovery     # RQ1
python -m evaluation.run_predictive_benchmark       # RQ2 - trains the DKT baseline
python -m evaluation.run_sensitivity_analysis       # RQ3
```
See `evaluation/README.md` for what each one measures and how long it takes to run.

## How it's put together

- **`app/models.py`** splits cleanly into two halves: content tables (`Course`, `Section`, `Question`, `QuestionChapter`) come from the partner content import, and activity tables (`Student`, `PracticeSession`, `Attempt`) are generated entirely by students using the app.
- **`app/engine/mastery.py`** is the analytics core - plain functions with no database or HTTP dependency, so it's trivial to unit test. Given a student's answer history for a chapter, it computes accuracy, a difficulty-weighted score, a recency-weighted score (exponential decay), a trend, and a confidence figure, then combines those into a mastery estimate and a priority ranking. Every weight is a tunable parameter (`MasteryWeights`) rather than a hardcoded constant, which is what makes the RQ3 sensitivity analysis possible without duplicating the model.
- **`app/engine/achievements.py`** follows the same pure-function style for the streak/badge/milestone logic - nothing here is stored; it's recomputed live from real attempt history every time.
- **`app/routers/auth.py`** handles registration, login (JWT, 7-day expiry), email verification, and password reset. Teacher registration requires an invite code so it isn't wide open to anyone who signs up.
- **`app/routers/practice.py`** is the test-taking flow: single-chapter practice (untimed, instant feedback) and mixed mock exams (timed, deferred feedback until submission). A mock test's deadline is computed fresh on every request rather than trusted from the client, so a session gets scored and closed out the moment anything touches it past its time limit - the frontend countdown is just a display, not the actual enforcement.
- **`app/routers/teacher.py`** is the cohort-facing side: per-chapter heatmaps, which chapters are failing across a cohort, which students need attention, all confidence-gated the same way the student-facing views are.
- **`evaluation/`** holds the standalone scripts behind the dissertation's empirical results - a synthetic dataset with known ground truth, the threshold and DKT baselines, and the three experiment runners above.
- **`../frontend/`** is the React + TypeScript + Vite app: student side (browse curriculum → practice or take a mock test → see ranked, explained weak areas → drill into a chapter's history) and teacher side (class overview, cohort heatmap, per-student detail).

## What's built

**Core loop.** Register, browse the curriculum tree, practice a chapter or take a full mixed mock exam, see results with a per-chapter mastery breakdown and a plain-language explanation of why each chapter is ranked where it is, then track progress over time. Mock exams have a real navigator (jump between questions, mark for review, resume if you refresh mid-test), server-enforced timing, and deferred feedback until you submit.

**Explaining the numbers, not just showing them.** Every page that shows a mastery figure also has a short "how is this calculated?" explainer, and a chapter with too little data is labeled "not enough evidence yet" rather than being confidently called weak or strong. Accuracy and mastery are shown as two different things on purpose - mastery adjusts for difficulty and recency, accuracy doesn't, and the app is explicit about that difference.

**Auth and account basics.** Email verification and password reset via a shared, single-use, expiring token table. Teacher accounts are gated by an invite code; a class/enrollment model lets teachers group students instead of seeing every registered student system-wide.

**Engagement features.** A daily streak indicator, tiered achievement badges (streak length, questions answered, chapters mastered, mock tests completed), a "continue practicing" shortcut back into your most recent chapters, and a fast 5-question Quick Practice mode for when a full session is too much friction. No leaderboard - a public ranking cuts against an app whose whole premise is "evidence-weighted, not a percentage race," and risks discouraging exactly the students it's meant to help.

**Content.** The curriculum spans six courses (NEB Grade 11/12 Science, NEB Grade 11/12 Management, +2 Foundation, and Grade Improvement). Science content comes from the partner question bank; Management-stream and a handful of compulsory subjects (English, Nepali, Social Studies, Computer Science) were authored in-house to close gaps in the source coverage, tagged `source="synthetic"` in the database and documented as such.

**Data layer.** Runs on Postgres in this environment (SQLite still works as the zero-config default for anyone who hasn't set `DATABASE_URL`), with a one-shot migration script that handles the awkward parts - foreign key cycles between tables, and resetting Postgres's auto-increment sequences after copying rows with pre-existing ids.

