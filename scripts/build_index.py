#!/usr/bin/env python3
"""Build a machine-readable index of the ruleset, so nothing has to re-read it.

`docs/` is fifteen documents, ~4800 lines and 225 rules. `ruleset-auditor` is
told to read all of it, twice per change, and most of what it re-derives on the
way is mechanical: where a rule lives, what it cites, who cites it, what sits
next to it. That is an index, and an index can be built once.

The output is `.studcraft/index.json` — regenerable, gitignored, never edited by
hand and never a source of truth. `docs/` is the source of truth; this is a
cache in front of it. `scripts/rule.py` is the query side.

The rule-ID pattern is **imported from `scripts/repo.py`**, not copied. A second
copy of a convention would drift from the first, and the drift would be silent.

What each rule entry holds:

  doc, line     where it is, so it can be opened without a search
  title         the text after the em dash in its header
  summary       its first sentence, which is the rule in one line
  cites         every rule ID its body names, minus itself
  cited_by      the inverse, which is the thing no grep gives you cheaply

Run it directly, or let `scripts/preflight.py` run it so the index cannot go
stale without someone noticing.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from repo import DOCS_DIR, HEADING_RE, REPO_ROOT, RULE_ID_RE  # noqa: E402

GLOSSARY = "14-glossary.md"
INDEX_PATH = REPO_ROOT / ".studcraft" / "index.json"

# The same header shape repo.RULE_HEADER_RE matches, kept line-anchored here
# because this needs the line number and the title text, which that pattern's
# findall of prefix/number pairs does not return.
RULE_HEADER_LINE_RE = re.compile(r"^#{1,2} ([A-Z]{2,6})-(\d{3}) — (.+?)\s*$")
GLOSSARY_TERM_RE = re.compile(r"^## (.+?)\s*$")


def first_sentence(body: list[str]) -> str:
    """The rule in one line: its first real line, trimmed at the first full stop.

    Rules here open with a statement and then justify it, so the first sentence
    is the rule and everything after it is why. Good enough to decide whether a
    rule is worth opening, which is all the index is for.
    """
    for line in body:
        text = line.strip()
        if not text or text == "---" or text.startswith(("|", ">", "#", "-", "*")):
            continue
        stop = text.find(". ")
        return text[: stop + 1] if stop != -1 else text
    return ""


def parse_document(name: str, text: str) -> list[dict]:
    """Every rule in one document, with its body span resolved."""
    lines = text.splitlines()
    headers: list[tuple[int, str, str, str]] = []

    for number, line in enumerate(lines, start=1):
        match = RULE_HEADER_LINE_RE.match(line)
        if match:
            prefix, digits, title = match.groups()
            headers.append((number, f"{prefix}-{digits}", title, prefix))

    rules: list[dict] = []
    for index, (line_no, rule_id, title, _prefix) in enumerate(headers):
        # The body runs to the next rule header, or to the next section heading
        # if the document moves on to one (a Summary, usually) first.
        limit = headers[index + 1][0] - 1 if index + 1 < len(headers) else len(lines)
        body: list[str] = []
        for raw in lines[line_no:limit]:
            if HEADING_RE.match(raw):
                break
            body.append(raw)

        cited = [rid for rid in dict.fromkeys(RULE_ID_RE.findall("\n".join(body))) if rid != rule_id]

        rules.append({
            "id": rule_id,
            "doc": name,
            "line": line_no,
            "title": title,
            "summary": first_sentence(body),
            "cites": cited,
            "cited_by": [],
        })

    return rules


def parse_glossary(text: str) -> list[dict]:
    """Every `## Term` entry, with the rule IDs it points at."""
    lines = text.splitlines()
    entries: list[dict] = []
    starts = [
        (number, match.group(1))
        for number, line in enumerate(lines, start=1)
        if (match := GLOSSARY_TERM_RE.match(line))
    ]

    for index, (line_no, term) in enumerate(starts):
        limit = starts[index + 1][0] - 1 if index + 1 < len(starts) else len(lines)
        body = "\n".join(lines[line_no:limit])
        entries.append({
            "term": term,
            "line": line_no,
            "cites": list(dict.fromkeys(RULE_ID_RE.findall(body))),
        })

    return entries


def build() -> dict:
    documents: dict[str, dict] = {}
    rules: dict[str, dict] = {}
    order: list[str] = []

    for path in sorted(DOCS_DIR.glob("*.md")):
        text = path.read_text()
        parsed = parse_document(path.name, text)
        documents[path.name] = {
            "rules": [rule["id"] for rule in parsed],
            "prefixes": sorted({rule["id"].split("-")[0] for rule in parsed}),
        }
        for rule in parsed:
            rules[rule["id"]] = rule
            order.append(rule["id"])

    for rule_id in order:
        for target in rules[rule_id]["cites"]:
            if target in rules:
                rules[target]["cited_by"].append(rule_id)

    glossary_path = DOCS_DIR / GLOSSARY
    glossary = parse_glossary(glossary_path.read_text()) if glossary_path.exists() else []

    return {
        "note": "Generated by scripts/build_index.py. Never edit; docs/ is the source of truth.",
        "documents": documents,
        "rules": rules,
        "glossary": glossary,
    }


def write_index(index: dict) -> None:
    """Write the index in one step, so a reader never sees half of it.

    `scripts/rule.py` rebuilds this file whenever a document is newer than it,
    which means two processes can be writing while a third reads — `preflight.py`
    running the build while an agent runs a query. A plain `write_text` truncates
    first and fills in afterwards, so the reader gets a `JSONDecodeError` on a
    file that is merely mid-write. Writing beside it and renaming is atomic:
    the reader sees either the old index or the new one.

    The temporary file carries the writing process's pid, so two concurrent
    builds do not write to the same one.
    """
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(index, indent=2, ensure_ascii=False) + "\n"
    tmp = INDEX_PATH.parent / f"{INDEX_PATH.name}.{os.getpid()}.tmp"
    tmp.write_text(payload)
    try:
        os.replace(tmp, INDEX_PATH)
    except BaseException:
        tmp.unlink(missing_ok=True)
        raise


def main() -> int:
    index = build()
    write_index(index)

    orphans = [rid for rid, rule in index["rules"].items() if not rule["cited_by"]]
    print(
        f"Indexed {len(index['rules'])} rules across {len(index['documents'])} documents, "
        f"{len(index['glossary'])} glossary entries. {len(orphans)} rule(s) uncited."
    )
    print(f"Wrote {INDEX_PATH.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
