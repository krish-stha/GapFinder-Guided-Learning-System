# GapFinder - frontend

React + TypeScript + Vite single-page app. Student side (browse the curriculum, practice, take mock exams, view weak-area/progress/performance reports) and teacher side (class overview, cohort heatmap, per-student detail), role-gated on both the routes and the backend.

## Setup

```
npm install
npm run dev
```
Runs on http://localhost:5173 by default. Needs the backend running (see `../backend/README.md`) - copy `.env.example` to `.env` if the API isn't on the default `http://127.0.0.1:8000`.

```
npm run build
```
Type-checks (`tsc -b`) and produces a production build in `dist/`.

## Notable bits

- `src/engine`-equivalent logic (mastery bands, chapter status, evidence formatting) lives on the backend - the frontend renders what the API already computed rather than recalculating anything itself, so the numbers a student sees always trace back to the same evidence the backend's tests cover.
- `context/ThemeContext.tsx` drives light/dark/reading themes via a `data-theme` attribute, applied before mount (inline script in `index.html`) to avoid a flash of the wrong theme.
- Charts use Recharts; math notation renders via KaTeX.
