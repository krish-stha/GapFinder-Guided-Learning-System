// Small day-granularity relative-time label for "Continue practicing" cards -
// deliberately coarse (Today/Yesterday/N days ago), not a full i18n library.
export function relativeDayLabel(isoDateTime: string): string {
  const then = new Date(isoDateTime);
  const now = new Date();
  const startOfDay = (d: Date) => new Date(d.getFullYear(), d.getMonth(), d.getDate());
  const diffDays = Math.round((startOfDay(now).getTime() - startOfDay(then).getTime()) / 86_400_000);

  if (diffDays <= 0) return "Today";
  if (diffDays === 1) return "Yesterday";
  return `${diffDays} days ago`;
}
