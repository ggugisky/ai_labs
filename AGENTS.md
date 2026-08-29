# AI Labs Repository Rules

This repository follows a brain-template style LLM wiki structure.

## Basic Rules

- Read `index.md` first before adding or updating knowledge.
- Store newly captured notes in `raw/` first.
- Promote stable, reusable knowledge to `wiki/`.
- Keep links between related wiki pages.
- Record structural changes in `log.md`.

## Knowledge Graph Metadata

- Markdown/YAML in this repository is the source of truth.
- Stable reusable documents should declare `id`, `type`, `status`, and `area`.
- Use `relations` for typed links. Keep relation types within `ontology/relations.yaml`.
- Use `ontology/classes.yaml` for the allowed document/entity types.
- Use `ontology/statuses.yaml` for the document lifecycle.
- Generated LPG databases are disposable projections and must not be committed.
- New or LLM-extracted relations should include `confidence`, `evidence`, and
  `review_status` when they are not manually verified.
- Use `provenance.sources` for source IDs/URLs and capture/access dates.
- Wiki Service/Tool pages must link to their canonical entity with `describes`.

## Folder Roles

- `raw/meeting/`: shared meeting notes by date.
- `raw/`: source notes and drafts.
- `wiki/`: reviewed summaries and reusable knowledge.
- `index.md`: navigation and current structure.
- `log.md`: creation, promotion, and maintenance history.
- `ontology/`: allowed classes and relation vocabulary.
- `entities/`: reusable people, organizations, services, use cases, and tools.
- `scripts/`: validation and graph projection tools.
- `promotions.yaml`: reviewed raw-to-entity/wiki promotion manifest.
- `obsidian-plugin/ai-labs-relations/`: Obsidian presentation layer for relation metadata.

## Naming

- Meeting notes should use `raw/meeting/YYYYMMDD.md`.
- Other raw notes should use `raw/YYYY-MM-DD-Topic.md`.
- Wiki pages should use concise, stable topic names.
- Use markdown links for cross-references.

## Repo Scope

This repo is for AI Labs meeting notes and the LLM Wiki structure around them.

## Lint And Promote Workflow

- After completing `lint` and `promote`, run the validation checks, commit the changes, and push them to `origin/main`.
- Standard commands are `python scripts/lint.py`, `python scripts/promote.py`,
  and `python scripts/build_index.py`.
- Install the validation dependency `PyYAML` before running these commands.
- Never report knowledge as saved unless validation, commit, and push all succeed.
- If any required command cannot run or fails, report the operation as incomplete and include the blocking error.
