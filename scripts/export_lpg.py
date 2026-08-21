#!/usr/bin/env python3
"""Project AI Labs Markdown/YAML into a rebuildable SQLite LPG.

The repository files remain the source of truth. The SQLite database is a
disposable local projection and should not be committed to Git.
"""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

import yaml


WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")


def split_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end < 0:
        return {}, text
    try:
        metadata = yaml.safe_load(text[4:end]) or {}
    except yaml.YAMLError as error:
        raise ValueError(f"invalid frontmatter: {error}") from error
    return (metadata if isinstance(metadata, dict) else {}), text[end + 4 :]


def canonical_id(root: Path, path: Path) -> str:
    relative = path.relative_to(root).with_suffix("")
    return "ailabs:" + "/".join(relative.parts)


def normalize_target(root: Path, source: Path, target: str) -> str:
    target = target.strip().strip('"\'')
    if ":" in target.split("/", 1)[0]:
        return target
    target = target.split("#", 1)[0].removesuffix(".md")
    candidate = ((source.parent / target) if target.startswith(".") else (root / target)).with_suffix(".md").resolve()
    if not candidate.exists() and "/" not in target:
        matches = list(root.rglob(f"{target}.md"))
        if len(matches) == 1:
            candidate = matches[0].resolve()
    if candidate.exists():
        return canonical_id(root, candidate)
    return "ailabs:" + target.replace(" ", "-")


def relation_rows(root: Path, path: Path, metadata: dict, body: str):
    source_id = str(metadata.get("id") or canonical_id(root, path))
    relations = metadata.get("relations") or []
    if isinstance(relations, dict):
        relations = [relations]
    for relation in relations:
        if not isinstance(relation, dict) or not relation.get("target"):
            continue
        yield (
            source_id,
            str(relation.get("type", "related_to")),
            normalize_target(root, path, str(relation["target"])),
            float(relation.get("confidence", 1.0)),
            str(relation.get("evidence", "")),
            str(relation.get("review_status", "manual")),
        )
    for target in WIKILINK_RE.findall(body):
        yield source_id, "related_to", normalize_target(root, path, target), 0.5, "wikilink", "inferred"


def build_database(root: Path, database: Path) -> tuple[int, int]:
    database.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(database)
    try:
        connection.executescript(
            """
            PRAGMA foreign_keys = ON;
            DROP TABLE IF EXISTS relations;
            DROP TABLE IF EXISTS entities;
            CREATE TABLE entities (
                entity_id TEXT PRIMARY KEY,
                entity_type TEXT NOT NULL,
                title TEXT NOT NULL,
                path TEXT NOT NULL,
                metadata_json TEXT NOT NULL,
                indexed_at TEXT NOT NULL
            );
            CREATE TABLE relations (
                relation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                source_id TEXT NOT NULL,
                relation_type TEXT NOT NULL,
                target_id TEXT NOT NULL,
                confidence REAL NOT NULL,
                evidence TEXT,
                review_status TEXT NOT NULL,
                FOREIGN KEY (source_id) REFERENCES entities(entity_id)
            );
            CREATE INDEX idx_rel_source ON relations(source_id);
            CREATE INDEX idx_rel_target ON relations(target_id);
            """
        )
        documents = (
            sorted(root.glob("raw/**/*.md"))
            + sorted(root.glob("wiki/**/*.md"))
            + sorted(root.glob("entities/**/*.md"))
        )
        entities = {}
        edges = []
        indexed_at = datetime.now(timezone.utc).isoformat()
        for path in documents:
            text = path.read_text(encoding="utf-8", errors="replace")
            metadata, body = split_frontmatter(text)
            entity_id = str(metadata.get("id") or canonical_id(root, path))
            entity_type = str(metadata.get("type") or "Document")
            title = str(metadata.get("title") or next(
                (line[2:].strip() for line in body.splitlines() if line.startswith("# ")), path.stem
            ))
            entities[entity_id] = (
                entity_id, entity_type, title, str(path.relative_to(root)),
                json.dumps(metadata, ensure_ascii=False, default=str), indexed_at,
            )
            edges.extend(relation_rows(root, path, metadata, body))
        connection.executemany("INSERT OR REPLACE INTO entities VALUES (?, ?, ?, ?, ?, ?)", entities.values())
        connection.executemany(
            "INSERT INTO relations(source_id, relation_type, target_id, confidence, evidence, review_status) VALUES (?, ?, ?, ?, ?, ?)",
            edges,
        )
        connection.commit()
        return len(entities), len(edges)
    finally:
        connection.close()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--database", type=Path, default=Path(".runtime/ai-labs-lpg.sqlite3"))
    args = parser.parse_args()
    entities, relations = build_database(args.root.resolve(), args.database.resolve())
    print(f"indexed entities={entities} relations={relations} database={args.database}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
