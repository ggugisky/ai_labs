#!/usr/bin/env python3
"""Check raw-to-entity/wiki promotion coverage from promotions.yaml."""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    end = text.find("\n---", 4)
    return yaml.safe_load(text[4:end]) or {} if text.startswith("---\n") and end >= 0 else {}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", nargs="?", help="only check promotions containing this source id")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    manifest = yaml.safe_load((root / "promotions.yaml").read_text())
    entries = manifest.get("promotions", [])
    if args.source:
        entries = [entry for entry in entries if args.source in entry.get("sources", [])]
    errors: list[str] = []
    checked = 0
    for entry in entries:
        entity_path = root / entry["entity"]
        wiki_path = root / entry["wiki"] if entry.get("wiki") else None
        if not entity_path.exists():
            errors.append(f"missing entity: {entry['entity']}")
            continue
        entity = frontmatter(entity_path)
        relations = entity.get("relations") or []
        relations = [relations] if isinstance(relations, dict) else relations
        relation_targets = {relation.get("target") for relation in relations if isinstance(relation, dict)}
        for source in entry.get("sources", []):
            if source not in relation_targets:
                errors.append(f"{entry['entity']}: missing source relation {source}")
        if wiki_path:
            if not wiki_path.exists():
                errors.append(f"missing wiki: {entry['wiki']}")
            else:
                wiki = frontmatter(wiki_path)
                wiki_relations = wiki.get("relations") or []
                wiki_relations = [wiki_relations] if isinstance(wiki_relations, dict) else wiki_relations
                if not any(
                    isinstance(relation, dict)
                    and relation.get("type") == "describes"
                    and relation.get("target") == entity.get("id")
                    for relation in wiki_relations
                ):
                    errors.append(f"{entry['wiki']}: missing describes relation to {entity.get('id')}")
        checked += 1
    if errors:
        print(f"promote check failed: {len(errors)} error(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"promote ok: {checked} promotion(s) covered")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
