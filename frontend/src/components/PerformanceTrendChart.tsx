import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid } from "recharts";
import type { AccuracyPoint } from "../types";

interface Bucket {
  key: string;
  label: string;
  accuracy: number;
  count: number;
  sortKey: number;
}

// Buckets real attempts into real calendar days/weeks and plots the
// average accuracy actually recorded in each bucket - never an invented
// or interpolated point. Daily buckets read better for a 7-day window;
// wider windows use weekly buckets (dated by each week's Monday) so the
// line stays legible instead of a dense forest of daily points.
function bucketTrend(points: AccuracyPoint[], granularity: "day" | "week"): Bucket[] {
  const buckets = new Map<string, { correct: number; total: number; sortKey: number }>();
  for (const p of points) {
    const d = new Date(p.answered_at);
    let key: string;
    let sortKey: number;
    if (granularity === "day") {
      const day = new Date(d.getFullYear(), d.getMonth(), d.getDate());
      key = day.toISOString();
      sortKey = day.getTime();
    } else {
      const day = d.getDay();
      const diffToMonday = day === 0 ? -6 : 1 - day;
      const monday = new Date(d.getFullYear(), d.getMonth(), d.getDate() + diffToMonday);
      key = monday.toISOString();
      sortKey = monday.getTime();
    }
    const existing = buckets.get(key) ?? { correct: 0, total: 0, sortKey };
    existing.total += 1;
    if (p.is_correct) existing.correct += 1;
    buckets.set(key, existing);
  }
  return [...buckets.entries()]
    .map(([key, b]) => ({
      key,
      label: new Date(b.sortKey).toLocaleDateString(undefined, { month: "short", day: "numeric" }),
      accuracy: Math.round((b.correct / b.total) * 100),
      count: b.total,
      sortKey: b.sortKey,
    }))
    .sort((a, b) => a.sortKey - b.sortKey);
}

export default function PerformanceTrendChart({
  points,
  granularity,
  height = 220,
}: {
  points: AccuracyPoint[];
  granularity: "day" | "week";
  height?: number;
}) {
  const data = bucketTrend(points, granularity);

  return (
    <div className="sparkline-container">
      <ResponsiveContainer width="100%" height={height}>
        <LineChart data={data} margin={{ top: 10, right: 20, left: -10, bottom: 0 }}>
          <CartesianGrid strokeDasharray="3 3" stroke="var(--border)" />
          <XAxis dataKey="label" tick={{ fill: "var(--text-muted)", fontSize: 12 }} />
          <YAxis domain={[0, 100]} tick={{ fill: "var(--text-muted)", fontSize: 12 }} width={40} />
          <Tooltip
            contentStyle={{ background: "var(--surface)", border: "1px solid var(--border)", borderRadius: 6 }}
            formatter={(value, _name, item) => [`${value}% (${item.payload.count} question${item.payload.count === 1 ? "" : "s"})`, "Accuracy"]}
          />
          <Line
            type="monotone"
            dataKey="accuracy"
            stroke="var(--accent)"
            strokeWidth={2}
            dot={{ r: 3, fill: "var(--accent)", strokeWidth: 0 }}
            activeDot={{ r: 5 }}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
