import { useMemo, useState } from "react";
import { buildTree, filterTree, type TreeNode } from "../utils/tree";
import type { Chapter } from "../types";

interface PickerNodeProps {
  node: TreeNode;
  selectedChapterId: number | null;
  onSelect: (chapter: Chapter) => void;
  forceExpanded: boolean;
}

function PickerNode({ node, selectedChapterId, onSelect, forceExpanded }: PickerNodeProps) {
  const [expanded, setExpanded] = useState(false);

  if (node.type === "Chapter") {
    const isSelected = node.id === selectedChapterId;
    return (
      <li className="tree-leaf">
        <button
          type="button"
          className={`tree-leaf-name picker-leaf-btn${isSelected ? " picker-leaf-selected" : ""}`}
          onClick={() => onSelect(node)}
        >
          {node.name}
        </button>
      </li>
    );
  }

  const isExpanded = forceExpanded || expanded;
  return (
    <li>
      <button type="button" className="tree-toggle" onClick={() => setExpanded((x) => !x)}>
        {isExpanded ? "▾" : "▸"} {node.name}
      </button>
      {isExpanded && node.children.length > 0 && (
        <ul>
          {node.children.map((child) => (
            <PickerNode
              key={child.id}
              node={child}
              selectedChapterId={selectedChapterId}
              onSelect={onSelect}
              forceExpanded={forceExpanded}
            />
          ))}
        </ul>
      )}
    </li>
  );
}

interface ChapterTreePickerProps {
  sections: Chapter[];
  selectedChapterId: number | null;
  onSelect: (chapter: Chapter) => void;
}

/**
 * Click-to-select Subject->Unit->Chapter tree, shared by Assessment
 * Management and Learning Content Management for picking which chapter a
 * new question/note/resource attaches to. Same buildTree/filterTree utility
 * as ChaptersPage's student-facing tree, different leaf (select, not
 * navigate-to-practice).
 */
export default function ChapterTreePicker({ sections, selectedChapterId, onSelect }: ChapterTreePickerProps) {
  const [query, setQuery] = useState("");
  const tree = useMemo(() => buildTree(sections), [sections]);
  const filtered = useMemo(() => filterTree(tree, query), [tree, query]);

  return (
    <div className="chapter-tree-picker">
      <label className="tree-search">
        <input
          type="search"
          placeholder="Search chapters…"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
      </label>
      {filtered.length === 0 ? (
        <p className="page-loading">No chapters match "{query}".</p>
      ) : (
        <ul className="section-tree">
          {filtered.map((node) => (
            <PickerNode
              key={node.id}
              node={node}
              selectedChapterId={selectedChapterId}
              onSelect={onSelect}
              forceExpanded={query.trim().length > 0}
            />
          ))}
        </ul>
      )}
    </div>
  );
}
