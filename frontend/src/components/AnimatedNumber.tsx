import { useEffect, useRef, useState } from "react";

/** Counts up from 0 to `value` once on mount/value-change - a lightweight
 * stand-in for a full animation library, just for the handful of headline
 * stats (score %, correct count) where a reveal earns its keep. */
export default function AnimatedNumber({
  value,
  durationMs = 700,
  suffix = "",
}: {
  value: number;
  durationMs?: number;
  suffix?: string;
}) {
  const [display, setDisplay] = useState(0);
  const startRef = useRef<number | null>(null);

  useEffect(() => {
    if (window.matchMedia?.("(prefers-reduced-motion: reduce)").matches) {
      setDisplay(value);
      return;
    }
    startRef.current = null;
    let frame: number;
    const step = (ts: number) => {
      if (startRef.current === null) startRef.current = ts;
      const elapsed = ts - startRef.current;
      const progress = Math.min(1, elapsed / durationMs);
      const eased = 1 - Math.pow(1 - progress, 3);
      setDisplay(Math.round(value * eased));
      if (progress < 1) frame = requestAnimationFrame(step);
    };
    frame = requestAnimationFrame(step);
    return () => cancelAnimationFrame(frame);
  }, [value, durationMs]);

  return (
    <span>
      {display}
      {suffix}
    </span>
  );
}
