import type { Chapter } from "../types";

export interface TreeNode extends Chapter {
  children: TreeNode[];
}

export function buildTree(sections: Chapter[]): TreeNode[] {
  const byId = new Map<number, TreeNode>();
  sections.forEach((s) => byId.set(s.id, { ...s, children: [] }));
  const roots: TreeNode[] = [];
  byId.forEach((node) => {
    if (node.parent_id !== null && byId.has(node.parent_id)) {
      byId.get(node.parent_id)!.children.push(node);
    } else {
      roots.push(node);
    }
  });
  return roots;
}

// Walks each Chapter-type section up its parent chain to the Subject it
// lives under - the tree is Subject -> Unit -> Chapter, there's no direct
// subject_id on a chapter. Shared by every page that needs a subject
// filter or a chapter's course_id (WeakAreasPage, ChapterAnalysisPage).
export function subjectMapFromSections(sections: Chapter[]): Map<number, string> {
  const byId = new Map<number, Chapter>();
  sections.forEach((s) => byId.set(s.id, s));
  const map = new Map<number, string>();
  sections.forEach((s) => {
    if (s.type !== "Chapter") return;
    let node: Chapter | undefined = s;
    while (node && node.type !== "Subject") {
      node = node.parent_id !== null ? byId.get(node.parent_id) : undefined;
    }
    if (node) map.set(s.id, node.name);
  });
  return map;
}

/** Returns a pruned copy of `nodes` containing only branches that lead to
 * a name match, so a search narrows the tree instead of just highlighting
 * within it. Chapter leaves in the result are always shown expanded by
 * the caller. */
export function filterTree(nodes: TreeNode[], query: string): TreeNode[] {
  const q = query.trim().toLowerCase();
  if (!q) return nodes;
  const walk = (list: TreeNode[]): TreeNode[] =>
    list
      .map((node) => {
        const selfMatch = node.name.toLowerCase().includes(q);
        const children = walk(node.children);
        if (selfMatch || children.length > 0) return { ...node, children };
        return null;
      })
      .filter((n): n is TreeNode => n !== null);
  return walk(nodes);
}
