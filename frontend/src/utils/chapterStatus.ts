import type { LearningPathStatus } from "../types";

// A friendlier read of the engine's real priority_band (plus the
// not_started state) - "Insufficient evidence" and "not_started" both
// collapse to "Not Assessed" here, since from a student's perspective
// both mean the same thing: there isn't enough evidence to say anything
// yet, not "this is a weak area." The underlying band/status is untouched -
// this is presentation only.
export type ChapterStatus = "Needs Attention" | "Developing" | "Strong" | "Not Assessed";

export function chapterStatusFor(status: LearningPathStatus): ChapterStatus {
  switch (status) {
    case "High":
      return "Needs Attention";
    case "Medium":
      return "Developing";
    case "Low":
      return "Strong";
    default:
      return "Not Assessed";
  }
}

// Reuses the same band-* color tokens as everywhere else in the app -
// "Not Assessed" gets the neutral insufficient-evidence tone.
export const CHAPTER_STATUS_CLASS: Record<ChapterStatus, string> = {
  "Needs Attention": "band-high",
  Developing: "band-medium",
  Strong: "band-low",
  "Not Assessed": "band-insufficient",
};
