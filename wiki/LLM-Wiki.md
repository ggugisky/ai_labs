---
id: ailabs:wiki/llm-wiki
type: Concept
tags: [ai, llm, wiki, knowledge-base]
created: 2026-07-08
status: stable
area: ai-labs
relations:
  - type: derived_from
    target: ailabs:raw/meeting/20260626
  - type: related_to
    target: ailabs:wiki/ai-labs
---

# LLM Wiki

> Source: AI Labs meeting note and brain-template style structure

LLM Wiki is a lightweight knowledge system that stores reusable AI and workflow notes in a structured way.

## Structure

- `raw/`: source notes and drafts
- `wiki/`: reviewed and reusable knowledge
- `index.md`: navigation
- `log.md`: change history
- `AGENTS.md`: operating rules
- `ontology/`: allowed classes and relation vocabulary
- `entities/`: reusable people, organizations, services, use cases, and tools
- `scripts/export_lpg.py`: rebuildable SQLite LPG projection

## Operating Model

- Capture first in `raw/`.
- Promote stable knowledge into `wiki/`.
- Link related pages.
- Keep the repository easy to navigate.

## Knowledge Graph Layer

The repository keeps Markdown/YAML in Git as its source of truth. Stable
documents use `id`, `type`, `status`, `area`, and typed `relations` metadata.
The `ontology/` vocabulary constrains those values, while
`scripts/export_lpg.py` creates a disposable SQLite projection for graph
queries and future GraphRAG use.

## Why It Matters

- Reduces repeated explanation.
- Preserves useful meeting outcomes.
- Makes shared knowledge easier to reuse.

## Related Pages

- [[AI-Labs]]
