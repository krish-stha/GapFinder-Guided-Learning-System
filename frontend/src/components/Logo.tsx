import { useId } from "react";

interface LogoProps {
  size?: number;
  className?: string;
  // "gradient" (default) = the --accent/--accent-2 brand gradient, for use
  // on ordinary surfaces (nav bar, etc). "solid" = strokes with
  // currentColor instead, for placing on top of a surface that's already
  // that same gradient (the auth hero panel) - otherwise the mark all but
  // disappears against its own gradient.
  variant?: "gradient" | "solid";
}

/**
 * GapFinder mark: a mastery ring with a deliberate gap in it - literal
 * (the "gap" the product finds) and thematic (an incomplete progress
 * ring). One path, no text baked in (the wordmark sits next to it in
 * markup so it stays real, selectable text). The gradient variant uses
 * the existing --accent/--accent-2 CSS custom properties via an inline
 * SVG gradient, so it stays theme-adaptive (dark mode) for free - a
 * static <img src> file can't read page CSS variables, an inline SVG can.
 */
export default function Logo({ size = 28, className, variant = "gradient" }: LogoProps) {
  const strokeId = `gapfinder-logo-gradient-${useId()}`;
  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 100 100"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      className={className}
      aria-hidden="true"
    >
      {variant === "gradient" && (
        <defs>
          <linearGradient id={strokeId} x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="var(--accent)" />
            <stop offset="100%" stopColor="var(--accent-2)" />
          </linearGradient>
        </defs>
      )}
      <path
        d="M 50 10 A 40 40 0 1 1 15.4 30"
        stroke={variant === "gradient" ? `url(#${strokeId})` : "currentColor"}
        strokeWidth="11"
        strokeLinecap="round"
        fill="none"
      />
    </svg>
  );
}
