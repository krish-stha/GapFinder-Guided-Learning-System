/** Lightweight shimmering placeholders (see `.skeleton` in index.css) used
 * while data is loading, instead of plain "Loading…" text. */

export function EvidenceCardSkeleton() {
  return (
    <div className="evidence-card skeleton-card">
      <header className="evidence-header">
        <div className="skeleton" style={{ height: 20, width: "55%" }} />
        <div className="skeleton" style={{ height: 20, width: 80, borderRadius: 999 }} />
      </header>
      <div className="skeleton" style={{ height: 14, width: "90%", marginTop: 10 }} />
      <div className="skeleton" style={{ height: 14, width: "70%", marginTop: 6 }} />
    </div>
  );
}

export function EvidenceListSkeleton({ count = 3 }: { count?: number }) {
  return (
    <div className="evidence-list">
      {Array.from({ length: count }).map((_, i) => (
        <EvidenceCardSkeleton key={i} />
      ))}
    </div>
  );
}

export function TreeSkeleton() {
  return (
    <ul className="section-tree">
      {Array.from({ length: 5 }).map((_, i) => (
        <li key={i} style={{ marginBottom: 8 }}>
          <div className="skeleton" style={{ height: 34, width: `${70 - i * 6}%` }} />
        </li>
      ))}
    </ul>
  );
}

export function TableSkeleton({ rows = 5, cols = 4 }: { rows?: number; cols?: number }) {
  return (
    <table className="teacher-table">
      <tbody>
        {Array.from({ length: rows }).map((_, r) => (
          <tr key={r}>
            {Array.from({ length: cols }).map((__, c) => (
              <td key={c}>
                <div className="skeleton" style={{ height: 14, width: c === 0 ? "80%" : "50%" }} />
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
}
