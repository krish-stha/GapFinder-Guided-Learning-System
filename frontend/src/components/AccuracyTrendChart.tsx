import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid } from "recharts";

interface DotProps {
  cx?: number;
  cy?: number;
  payload?: { correct: boolean };
}

function CustomDot({ cx, cy, payload }: DotProps) {
  if (cx === undefined || cy === undefined || !payload) return null;
  const color = payload.correct ? "var(--band-low-border)" : "var(--band-high-border)";
  return <circle cx={cx} cy={cy} r={4} fill={color} stroke="var(--surface)" strokeWidth={1} />;
}

interface ScoredPoint {
  is_correct: boolean;
}

interface AccuracyTrendChartProps {
  points: ScoredPoint[];
  height?: number;
}

// A student with hundreds/thousands of attempts (e.g. a demo "topper"
// account) was rendering one React dot component per attempt - 1000+ SVG
// circles on a single line, which is what made the page feel slow, not the
// data fetch. Capping the plotted points and taking an even stride through
// the full history keeps the page fast regardless of attempt count while
// still reflecting every attempt's real, computed running accuracy (no
// point is invented or averaged - a plotted point's "correct" color is that
// exact attempt's real result, just not every attempt gets its own point).
const MAX_PLOTTED_POINTS = 80;

/**
 * Running-accuracy-over-attempts sparkline, lifted out of ChapterDetailPage
 * (originally single-chapter score history) so My Performance and Progress
 * & Improvement can reuse it for a student's whole accuracy trend, not just
 * one chapter's. Single series, status colors (green=correct/red=incorrect)
 * on the dots per the dataviz skill's "status colors are reserved" rule -
 * no categorical palette needed here.
 */
export default function AccuracyTrendChart({ points, height = 200 }: AccuracyTrendChartProps) {
  let runningCorrect = 0;
  const fullData = points.map((p, i) => {
    if (p.is_correct) runningCorrect++;
    return {
      attempt: i + 1,
      runningAccuracy: Math.round((runningCorrect / (i + 1)) * 100),
      correct: p.is_correct,
    };
  });

  const stride = Math.ceil(fullData.length / MAX_PLOTTED_POINTS) || 1;
  const chartData =
    stride <= 1
      ? fullData
      : fullData.filter((_, i) => i % stride === 0 || i === fullData.length - 1);

  return (
    <div>
      <div className="sparkline-container">
        <ResponsiveContainer width="100%" height={height}>
          <LineChart data={chartData} margin={{ top: 10, right: 20, left: -10, bottom: 0 }}>
            <CartesianGrid strokeDasharray="3 3" stroke="var(--border)" />
            <XAxis
              dataKey="attempt"
              tick={{ fill: "var(--text-muted)", fontSize: 12 }}
              label={{ value: "Attempt #", position: "insideBottom", offset: -2, fill: "var(--text-muted)", fontSize: 12 }}
            />
            <YAxis domain={[0, 100]} tick={{ fill: "var(--text-muted)", fontSize: 12 }} width={40} />
            <Tooltip
              contentStyle={{ background: "var(--surface)", border: "1px solid var(--border)", borderRadius: 6 }}
              formatter={(value) => [`${value}%`, "Running accuracy"]}
              labelFormatter={(label) => `Attempt ${label}`}
            />
            <Line type="monotone" dataKey="runningAccuracy" stroke="var(--accent)" strokeWidth={2} dot={<CustomDot />} />
          </LineChart>
        </ResponsiveContainer>
      </div>
      <p className="sparkline-legend">
        <span className="legend-dot legend-correct" /> Correct
        <span className="legend-dot legend-incorrect" /> Incorrect
      </p>
      {stride > 1 && (
        <p className="sparkline-sampling-note">
          Showing every {stride === 2 ? "2nd" : `${stride}th`} attempt of {fullData.length} for readability -
          running accuracy is still computed from your full history.
        </p>
      )}
    </div>
  );
}
