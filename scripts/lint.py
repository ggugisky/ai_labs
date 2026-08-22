#!/usr/bin/env python3
"""Validate AI Labs Markdown/YAML knowledge contracts."""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml


SKIP_NAMES = {"README.md"}
REQUIRED = ("id", "type", "status", "area")


def documents(root: Path) -> list[Path]:
    paths = sorted(
        list(root.glob("raw/**/*.md"))
        + list(root.glob("wiki/**/*.md"))
        + list(root.glob("entities/**/*.md"))
    )
    return [path for path in paths if path.name not in SKIP_NAMES]


def parse(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing frontmatter")
    end = text.find("\n---", 4)
    if end < 0:
        raise ValueError("unterminated frontmatter")
    metadata = yaml.safe_load(text[4:end]) or {}
    if not isinstance(metadata, dict):
        raise ValueError("frontmatter must be a mapping")
    return metadata, text[end + 4 :]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    classes = yaml.safe_load((root / "ontology/classes.yaml").read_text())["classes"]
    relations = yaml.safe_load((root / "ontology/relations.yaml").read_text())["relations"]
    statuses = yaml.safe_load((root / "ontology/statuses.yaml").read_text())["statuses"]
    errors: list[str] = []
    metadata_by_id: dict[str, tuple[Path, dict]] = {}
    parsed: list[tuple[Path, dict, str]] = []

    for path in documents(root):
        try:
            metadata, body = parse(path)
        except (OSError, ValueError, yaml.YAMLError) as error:
            errors.append(f"{path.relative_to(root)}: {error}")
            continue
        parsed.append((path, metadata, body))
        for field in REQUIRED:
            if not metadata.get(field):
                errors.append(f"{path.relative_to(root)}: missing {field}")
        if metadata.get("type") not in classes:
            errors.append(f"{path.relative_to(root)}: invalid type {metadata.get('type')}")
        if metadata.get("status") not in statuses:
            errors.append(f"{path.relative_to(root)}: invalid status {metadata.get('status')}")
        entity_id = metadata.get("id")
        if entity_id:
            if entity_id in metadata_by_id:
                errors.append(f"duplicate id {entity_id}: {path} and {metadata_by_id[entity_id][0]}")
            metadata_by_id[entity_id] = (path, metadata)
        relations_list = metadata.get("relations") or []
        relations_list = [relations_list] if isinstance(relations_list, dict) else relations_list
        for relation in relations_list:
            if not isinstance(relation, dict):
                errors.append(f"{path.relative_to(root)}: relation must be a mapping")
                continue
            if relation.get("type") not in relations:
                errors.append(f"{path.relative_to(root)}: invalid relation {relation.get('type')}")
            target = str(relation.get("target", ""))
            if not target:
                errors.append(f"{path.relative_to(root)}: relation missing target")
            elif not target.startswith(("http://", "https://")) and target not in metadata_by_id:
                # Validate after all documents are collected below as well.
                pass
        provenance = metadata.get("provenance") or {}
        sources = provenance.get("sources", []) if isinstance(provenance, dict) else []
        if sources and not isinstance(sources, list):
            errors.append(f"{path.relative_to(root)}: provenance.sources must be a list")
        for source in sources if isinstance(sources, list) else []:
            if not isinstance(source, dict) or not (source.get("id") or source.get("url")):
                errors.append(f"{path.relative_to(root)}: every provenance source needs id or url")

    for path, metadata, _body in parsed:
        relations_list = metadata.get("relations") or []
        relations_list = [relations_list] if isinstance(relations_list, dict) else relations_list
        for relation in relations_list:
            if not isinstance(relation, dict):
                continue
            target = str(relation.get("target", ""))
            if target and not target.startswith(("http://", "https://")) and target not in metadata_by_id:
                errors.append(f"{path.relative_to(root)}: missing relation target {target}")
        if path.parts[0] == "wiki" and metadata.get("type") in {"Service", "Tool"}:
            if not any(
                isinstance(relation, dict)
                and relation.get("type") == "describes"
                and str(relation.get("target", "")).startswith("ailabs:")
                for relation in relations_list
            ):
                errors.append(f"{path.relative_to(root)}: wiki service/tool needs a describes relation to an entity")

    if errors:
        print(f"lint failed: {len(errors)} error(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"lint ok: {len(parsed)} documents, {len(metadata_by_id)} unique ids")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
