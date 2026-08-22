#!/usr/bin/env python3
"""Build the generated navigation blocks in index.md and README.md."""

from __future__ import annotations

import re
from pathlib import Path

import yaml


MARKER = re.compile(
    r"<!-- BEGIN GENERATED: (?P<name>[a-z0-9-]+) -->.*?<!-- END GENERATED: (?P=name) -->",
    re.DOTALL,
)


def metadata(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    return yaml.safe_load(text[4:end]) or {} if end >= 0 else {}


def title(path: Path, data: dict) -> str:
    if data.get("title"):
        return str(data["title"])
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").title()


def wiki_block(root: Path) -> str:
    lines = ["<!-- BEGIN GENERATED: wiki-index -->", ""]
    for path in sorted(root.glob("wiki/*.md")):
        if path.name == "README.md":
            continue
        data = metadata(path)
        lines.append(f"- [[wiki/{path.stem}]] — {title(path, data)}")
    lines.extend(["", "<!-- END GENERATED: wiki-index -->"])
    return "\n".join(lines)


def entity_block(root: Path) -> str:
    lines = ["<!-- BEGIN GENERATED: entity-index -->", ""]
    for path in sorted(root.glob("entities/**/*.md")):
        data = metadata(path)
        relative = path.relative_to(root).with_suffix("")
        entity_type = data.get("type", "Entity")
        lines.append(f"- [[{relative.as_posix()}]] — {entity_type}: {title(path, data)}")
    lines.extend(["", "<!-- END GENERATED: entity-index -->"])
    return "\n".join(lines)


def replace_block(text: str, name: str, block: str) -> str:
    pattern = re.compile(
        rf"<!-- BEGIN GENERATED: {re.escape(name)} -->.*?<!-- END GENERATED: {re.escape(name)} -->",
        re.DOTALL,
    )
    if not pattern.search(text):
        raise ValueError(f"missing generated block: {name}")
    return pattern.sub(block, text, count=1)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    index = root / "index.md"
    readme = root / "README.md"
    index_text = index.read_text(encoding="utf-8")
    readme_text = readme.read_text(encoding="utf-8")
    index_text = replace_block(index_text, "wiki-index", wiki_block(root))
    index_text = replace_block(index_text, "entity-index", entity_block(root))
    readme_text = replace_block(readme_text, "wiki-index", wiki_block(root))
    readme_text = replace_block(readme_text, "entity-index", entity_block(root))
    index.write_text(index_text, encoding="utf-8")
    readme.write_text(readme_text, encoding="utf-8")
    print("index ok: generated wiki and entity catalogs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
