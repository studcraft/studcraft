#!/usr/bin/env python3
"""A CLI over `scripts/ruleset_ast.py`, for eyeballing a document's shape.

    python3 scripts/parse_ruleset.py                     # a readable outline of every doc
    python3 scripts/parse_ruleset.py 07-movement.md       # one doc
    python3 scripts/parse_ruleset.py --json               # the whole tree as JSON, to stdout
    python3 scripts/parse_ruleset.py --json 07-movement.md

The outline is one line per section: indentation by heading level, the rule
ID when the heading carries one, and the line span it covers (descendants
included, which is the fix this module exists for — see `ruleset_ast.py`'s
own docstring).

**JSON always goes to stdout and is never written to a file in this
repository.** A committed copy would be a second source of truth for what
docs/ says, and it would drift the moment docs/ changed without anyone
regenerating it. `.studcraft/` is where a future caller may cache one — it is
gitignored for exactly this reason — and doing that is not this script's job.
"""

from __future__ import annotations

import json
import sys
from collections.abc import Iterator
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from repo import DOCS_DIR  # noqa: E402
from ruleset_ast import Document, Section, parse, parse_docs  # noqa: E402


def outline_lines(root: Section) -> Iterator[str]:
    """One line per section under `root`, root itself excluded (it is synthetic)."""
    for section in root.walk():
        if section.level == 0:
            continue
        indent = "  " * (section.level - 1)
        tag = f" [{section.rule_id}]" if section.rule_id else ""
        yield f"{indent}{'#' * section.level} {section.title}{tag} (lines {section.line}-{section.line_end})"


def load(name: str | None) -> dict[str, Document] | None:
    """The document named, or every document when `name` is None. None on a bad name."""
    if name is None:
        return parse_docs()

    path = DOCS_DIR / name
    if not path.is_file():
        print(f"No document {name} in docs/.", file=sys.stderr)
        return None
    return {name: parse(path)}


def main(argv: list[str]) -> int:
    json_mode = "--json" in argv
    positional = [arg for arg in argv if arg != "--json"]

    if len(positional) > 1:
        print(
            f"parse_ruleset.py takes at most one document name, got {len(positional)}.",
            file=sys.stderr,
        )
        return 1

    documents = load(positional[0] if positional else None)
    if documents is None:
        return 1

    if json_mode:
        print(json.dumps(
            {name: document.to_dict() for name, document in sorted(documents.items())},
            indent=2,
        ))
        return 0

    for name, document in sorted(documents.items()):
        print(name)
        for line in outline_lines(document.root):
            print(f"  {line}")
        print()

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
