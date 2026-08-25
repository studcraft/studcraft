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
The document structure itself — where a rule's body starts and ends, sub-headings
included — is **imported from `scripts/ruleset_ast.py`**, for the same reason:
a hand-rolled body-end pattern here would be a second, silently disagreeing
answer to the question `ruleset_ast.py` already answers once.

What each rule entry holds:

  doc, line, line_end   where it is and how far its body reaches, sub-headings
                         included, so it can be opened without a search
  title                  the text after the em dash in its header
  summary                its first sentence, which is the rule in one line
  cites                  every rule ID its body names, minus itself
  cited_by               the inverse, which is the thing no grep gives you cheaply

Run it directly, or let `scripts/preflight.py` run it so the index cannot go
stale without someone noticing.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from repo import DOCS_DIR, REPO_ROOT, RULE_ID_RE  # noqa: E402
from ruleset_ast import Document, parse_text  # noqa: E402

GLOSSARY = "14-glossary.md"
INDEX_PATH = REPO_ROOT / ".studcraft" / "index.json"


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


def _rules_in(document: Document) -> list[dict]:
    """Every rule in an already-parsed document, with its body span resolved
    by the AST.

    A rule's body is its section's span in the tree — `line` through
    `line_end` — which already reaches through the rule's own `##`/`###`
    sub-headings and stops only at the next sibling. The old pattern-based
    scan stopped at *any* heading, sub-headings included; that was the bug.
    """
    rules: list[dict] = []
    for section in document.root.rules():
        body = section.body_text(document.lines)
        # `body` includes fenced content, deliberately: a rule named inside a
        # fenced diagram *is* referenced by that document — a flow diagram
        # naming the rules it sequences is the map of the procedure, not an
        # example of syntax. No fence in docs/ names one today; the inclusion
        # is what keeps the next one counted. This is now
        # different from scripts/lint_ruleset.py's citation scan, which reads
        # prose only. The two answer different questions: this index asks
        # what a rule is connected to, the linter asks whether a written
        # citation resolves. Moving this onto prose would drop legitimate
        # edges from cited_by and grow orphans with rules that are genuinely
        # connected — the divergence is deliberate, not a thing to "fix".
        cited = [
            rid for rid in dict.fromkeys(RULE_ID_RE.findall(body)) if rid != section.rule_id
        ]

        rules.append({
            "id": section.rule_id,
            "doc": document.name,
            "line": section.line,
            "line_end": section.line_end,
            "title": section.rule_title,
            "summary": first_sentence(body.splitlines()),
            "cites": cited,
            "cited_by": [],
        })

    return rules


def parse_document(name: str, text: str) -> list[dict]:
    """Every rule in one document, parsed fresh from `text`.

    A thin wrapper over `_rules_in` for callers — tests, mainly — that hold
    text rather than an already-parsed `Document`. `build()` parses each
    document once and calls `_rules_in` and `build_outline` on that same
    `Document`, so the text is never parsed twice.
    """
    return _rules_in(parse_text(name, text))


def build_outline(document: Document) -> list[dict]:
    """A document's chapters and rules, `#`/`##` only, in document order.

    Walks two levels: `document.root`'s own children (the file's level-1
    sections) and, for any that is not itself a rule, that section's level-2
    children. A level-1 section that *is* a rule is not recursed into — its
    own `##`/`###` sub-headings are its body, not further outline entries.
    A rule presenting several worked scenarios as `##` sub-headings is exactly
    that case: they must not appear as chapters or as rules.

    The document's own title is skipped by position, not by pattern: every
    docs/*.md opens with its own `# Name` line before `# Purpose`, so
    `document.root.children[0]` is always the title, never a rule or chapter.
    """
    outline: list[dict] = []
    for section in document.root.children[1:]:
        outline.append({
            "level": section.level,
            "title": section.rule_title if section.is_rule else section.title,
            "line": section.line,
            "rule_id": section.rule_id,
        })
        if section.is_rule:
            continue
        for child in section.children:
            outline.append({
                "level": child.level,
                "title": child.rule_title if child.is_rule else child.title,
                "line": child.line,
                "rule_id": child.rule_id,
            })

    return outline


def parse_glossary(text: str) -> list[dict]:
    """Every `## Term` entry, with the rule IDs it points at.

    `docs/14-glossary.md` is one `#` section with a `##` child per term — a
    shape the AST already produces, so this walks it for level-2 sections
    rather than matching a pattern of its own.
    """
    document = parse_text(GLOSSARY, text)

    entries: list[dict] = []
    for section in document.root.walk():
        if section.level != 2:
            continue
        body = section.body_text(document.lines)
        entries.append({
            "term": section.title,
            "line": section.line,
            "line_end": section.line_end,
            "cites": list(dict.fromkeys(RULE_ID_RE.findall(body))),
        })

    return entries


def build() -> dict:
    documents: dict[str, dict] = {}
    rules: dict[str, dict] = {}
    order: list[str] = []

    for path in sorted(DOCS_DIR.glob("*.md")):
        document = parse_text(path.name, path.read_text())
        parsed = _rules_in(document)
        documents[path.name] = {
            "rules": [rule["id"] for rule in parsed],
            "prefixes": sorted({rule["id"].split("-")[0] for rule in parsed}),
            "outline": build_outline(document),
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
