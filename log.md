# 2026-09-02

- Prepared the 2026-09-04 AI Labs meeting note focused on Yuil's service presentation.

# 2026-08-29

- Added the Crack service entity, raw analysis, and reviewed wiki page.
- Linked Crack to the creative-content use case and existing AI Labs services/tools.
- Recorded strategy hypotheses connecting Crack with 모두의 개소리, Dalar, Lampas, connect-ai, and SSOT Viewer.

# AI Labs Log

## 2026-10-02

- Added a captured note and reviewed wiki page for the OpenAI DevDay 2026 shared video.
- Recorded Dots, Space, multi-agent delegation, GPT-6.1 Sol, computer use, Codex, security, and plugin platform topics.
- Linked the page to Connect AI, Graphify, LLM Wiki, and the creative-content production use case.

## 2026-09-21

- Updated the 2026-09-18 meeting note with the Slack discussion: postponed harness presentation, AI trend discussion, video-generation examples, and TTS references.


## 2026-09-04

- Added the Yuil presentation analysis based on the AI Labs Episode 4 recording and the checked-in presentation notes.
- Enriched the 2026-09-04 meeting note with the presentation summary, evidence boundaries, and follow-up actions.
- Added the Mungme service entity and reviewed wiki page, linking its data-product patterns to existing AI Labs knowledge.

## 2026-07-08

- brain-template style structure initialized.
- Existing meeting note moved into `raw/meeting/20260626.md` and promoted concept into `wiki/`.
- Meeting notes now use `raw/meeting/YYYYMMDD.md` while keeping the template structure intact.
- Pre-created draft note for the 2026-07-10 Friday meeting at `raw/meeting/20260710.md`.

## 2026-07-23

- Added `raw/2026-07-23-Open-Knowledge-Format.md` with an analysis of Google's Open Knowledge Format article.
- Linked the note from `wiki/AI-Labs.md` as a discussion agenda item.

## 2026-08-21

- Added `raw/2026-08-21-AI-Labs-vs-AI-Community.md` to document the distinction between AI Labs and AI Community/AI Committee.
- Updated `wiki/AI-Labs.md` with the separation rule so meeting records are not mixed.
- Added `raw/2026-07-23-Claude-Tag.md` with an analysis of Anthropic's Claude Tag article.
- Linked the note from `wiki/AI-Labs.md` as a discussion agenda item.

- Added ontology classes and relation vocabulary under `ontology/`.
- Added stable IDs and typed relations to existing wiki and meeting documents.
- Added `scripts/export_lpg.py` to build a disposable SQLite graph projection.
- Added wiki analyses for the five services listed in `raw/meeting/20260821.md`: Connect AI, Claude Tag, Pi, Grok Bot, and Aside.
- Linked the five service pages from `wiki/README.md` and `index.md`.
- Added wiki analyses for Dalar, Lampas, Graphify, and Hermes Agent found in earlier AI Labs meeting notes.
- Linked the additional service pages from `wiki/README.md` and `index.md`.

## 2026-08-22

- Promoted Pi, Grok Bot, Aside, Graphify, Hermes Agent, and 모두의 개소리 into `entities/`.
- Added missing service relations to the 2026-07-24 and 2026-08-21 meeting notes.
- Normalized reusable wiki/raw metadata and extended the ontology with the `owned_by` inverse relation.
- Ran metadata lint successfully and rebuilt the disposable SQLite LPG projection.
- Added the document lifecycle contract in `ontology/statuses.yaml` and normalized active/source/provisional statuses.
- Added `promotions.yaml` plus `scripts/lint.py` and `scripts/promote.py` to validate raw-to-entity/wiki coverage.
- Linked canonical entities and wiki pages with `describes`/`described_by`, and recorded source provenance on service/tool wiki pages.
- Added generated wiki/entity catalogs through `scripts/build_index.py`; README and index navigation are now reproducible.
- Excluded navigation README files from the LPG projection and added `.DS_Store` to `.gitignore`.
- Added the `obsidian-plugin/ai-labs-relations` presentation layer, which renders YAML relations as navigable links in Reading view without changing the source metadata model.
