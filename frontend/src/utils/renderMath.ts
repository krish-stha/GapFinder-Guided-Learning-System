import katex from "katex";
import DOMPurify from "dompurify";

/**
 * The content partner's scraped question/answer HTML encodes math and chemical
 * structures as a custom `<ki data-katex="true" src="...LaTeX...">` tag
 * their own platform knew how to render - this app never did, so these
 * either render blank (LaTeX only in `src`, empty text content) or as
 * raw garbled LaTeX (LaTeX duplicated as literal text content too).
 *
 * Two-pass approach: sanitize the raw third-party HTML first (it's never
 * been sanitized anywhere in this pipeline), keeping the `<ki>` tag and
 * its two attributes through the allowlist since the KaTeX pass below
 * needs them; then replace each `<ki>` with either real KaTeX-rendered
 * markup (when its text content is empty or just a duplicate of the LaTeX
 * source) or plain sanitized text (when the text content is genuine prose
 * that happened to get wrapped in a `<ki>` tag by the source data).
 */

const SANITIZE_CONFIG = {
  ADD_TAGS: ["ki"],
  ADD_ATTR: ["data-katex", "src"],
};

function isPlaceholderText(text: string, src: string): boolean {
  const normalize = (s: string) => s.replace(/^\$+|\$+$/g, "").replace(/\s+/g, "").trim();
  const normalizedText = normalize(text);
  if (normalizedText === "") return true;
  return normalizedText === normalize(src);
}

export function renderMathHtml(rawHtml: string): string {
  if (!rawHtml) return rawHtml;
  const sanitized = DOMPurify.sanitize(rawHtml, SANITIZE_CONFIG);

  const container = document.createElement("div");
  container.innerHTML = sanitized;

  const kiElements = container.querySelectorAll('ki[data-katex="true"]');
  kiElements.forEach((el) => {
    const src = el.getAttribute("src") ?? "";
    const text = el.textContent ?? "";
    const replacement = document.createElement("span");

    if (src.trim() !== "" && isPlaceholderText(text, src)) {
      try {
        replacement.className = "katex-rendered";
        replacement.innerHTML = katex.renderToString(src, { throwOnError: false, output: "html" });
      } catch {
        replacement.textContent = src;
      }
    } else {
      replacement.textContent = text;
    }

    el.replaceWith(replacement);
  });

  // second pass: katex's own output is trusted (we generated it above),
  // but run the final tree through DOMPurify once more anyway since the
  // "genuine prose" branch just moved sanitized-but-still-third-party text
  // into a new element - cheap, and keeps this function safe regardless
  // of future changes to the replacement logic above.
  return DOMPurify.sanitize(container.innerHTML, { ADD_TAGS: ["svg", "path", "g", "line", "annotation", "semantics", "mrow", "mi", "mo", "mn", "msup", "msub", "mfrac", "msqrt"] });
}
