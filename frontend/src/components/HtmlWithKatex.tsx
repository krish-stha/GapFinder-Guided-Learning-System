import { useMemo } from "react";
import { renderMathHtml } from "../utils/renderMath";

interface HtmlWithKatexProps {
  html: string;
  className?: string;
  as?: "div" | "span";
}

/**
 * Drop-in replacement for a raw `dangerouslySetInnerHTML` div/span when
 * the HTML may contain the content partner's `<ki data-katex>` math/structure
 * tags - see utils/renderMath.ts for why those need special handling.
 * Memoized since DOM parsing + KaTeX rendering on every keystroke/render
 * would be wasteful; only re-runs when the underlying HTML string changes.
 */
export default function HtmlWithKatex({ html, className, as = "div" }: HtmlWithKatexProps) {
  const processed = useMemo(() => renderMathHtml(html), [html]);
  const Tag = as;
  return <Tag className={className} dangerouslySetInnerHTML={{ __html: processed }} />;
}
