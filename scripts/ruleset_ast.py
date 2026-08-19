#!/usr/bin/env python3
"""One parser for docs/*.md, read by every script that needs its structure.

Before this, "what a rule's body is" had four different answers scattered
across scripts/repo.py and scripts/lint_ruleset.py: a header pattern that
required the em dash, an ID pattern that did not, a body-end pattern that
stopped at *any* heading, and a third, independent copy of the body-end
pattern inside the linter. They disagreed with each other, silently — a rule
written at `###` was invisible to one and not another, and a rule's own
`##`/`###` sub-headings were read as the start of the next rule by every
consumer of `repo.HEADING_RE`, `scripts/rule.py show DEP-009` included.

This module fixes that by building one tree per document and letting every
caller read the same tree. It is not a CommonMark parser and does not try to
be one — it parses the narrow subset of markdown this repository actually
writes, and every place that subset diverges from CommonMark is called out
in a comment where the divergence is made. `scripts/tasks_format.py` makes
the same argument one level down, for `tasks.md` rather than for `docs/`: a
second copy of a parser drifts from the first, and the drift is silent until
something it should have caught does not get caught.

Import it the way `scripts/repo.py` is already imported elsewhere:

    sys.path.insert(0, str(Path(__file__).resolve().parent))

    from ruleset_ast import parse_text, parse_docs  # noqa: E402
"""

from __future__ import annotations

import re
import sys
from collections.abc import Iterator
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from repo import DOCS_DIR, REPO_ROOT  # noqa: E402

# An ATX heading, one to three hashes. Four or more is deliberately excluded:
# `####+` does not occur anywhere in docs/, and matching it would invite a
# fourth level of nesting nothing downstream is built to handle. A line with
# four or more hashes simply falls through and is read as ordinary text —
# the same as a stray `#` with no following space.
ATX_HEADING_RE = re.compile(r"^(#{1,3}) (\S.*?)\s*$")

# The one definition of a rule heading, matched against a heading's *title*
# (the text after the hashes and the one space), never against the raw line.
# The em dash is required — this is repo.RULE_HEADER_RE's stricter reading,
# not repo.RULE_ID_RE's looser one, so a heading like "## DMG-005 States"
# (no em dash) is unambiguously not a rule, everywhere this module is used.
RULE_HEADING_RE = re.compile(r"^([A-Z]{2,6})-(\d{3}) — (.+)$")

# A list item marker: "- ", "* ", or an ordinal like "1. ". Checked against
# the raw line, matching how a heading is detected — this repository does not
# indent list markers.
LIST_ITEM_RE = re.compile(r"^(?:[-*] |\d+\. )")


@dataclass
class Block:
    """A run of lines that is not a heading."""

    kind: str  # "paragraph" | "list" | "table" | "fence" | "quote" | "break"
    line_start: int  # 1-indexed, inclusive
    line_end: int  # 1-indexed, inclusive
    lines: list[str]  # verbatim, fence markers included

    def to_dict(self) -> dict:
        return {
            "kind": self.kind,
            "line_start": self.line_start,
            "line_end": self.line_end,
            "lines": list(self.lines),
        }


@dataclass
class Section:
    """A heading and everything under it, children included."""

    level: int  # 0 for the synthetic root, else 1, 2 or 3
    title: str  # heading text after the hashes and one space
    line: int  # the heading's own line, 1-indexed; 0 for the root
    line_end: int  # last line belonging to this section, descendants included
    rule_id: str | None  # "MOVE-012" when this heading is a rule header
    rule_prefix: str | None  # "MOVE"
    rule_number: int | None  # 12
    rule_title: str | None  # "Slopes"
    blocks: list[Block] = field(default_factory=list)  # this section's own, pre-first-child
    children: list[Section] = field(default_factory=list)

    @property
    def is_rule(self) -> bool:
        return self.rule_id is not None

    def walk(self) -> Iterator[Section]:
        """This section and every descendant, depth first, in document order."""
        yield self
        for child in self.children:
            yield from child.walk()

    def rules(self) -> list[Section]:
        """Every section in this subtree whose heading is a rule header, in order."""
        return [section for section in self.walk() if section.is_rule]

    def body_text(self, lines: list[str]) -> str:
        """This section's text, from just after its heading through `line_end`.

        `lines` is `Document.lines` — Section carries no reference to the raw
        file, so the caller supplies it, the same way `rule.py show` already
        works from a line list rather than storing one per rule. Trailing
        blank lines are dropped, and then a single trailing `---` (with any
        blank lines that separated it from the real content) is dropped too:
        that line is the thematic break this repository writes before the
        next rule, not part of the rule it follows. A `---` that is *not*
        the last thing in the section — one with real content after it — is
        left alone.
        """
        start = self.line  # 0-indexed into `lines`, i.e. one past the heading
        body = list(lines[start:self.line_end])

        while body and not body[-1].strip():
            body.pop()
        if body and body[-1].strip() == "---":
            body.pop()
            while body and not body[-1].strip():
                body.pop()

        return "\n".join(body)

    def prose_lines(self, lines: list[str]) -> list[str]:
        """Every line in this section's span except fenced content and markers.

        This is what citation scanning is meant to run over: a fenced example
        of a heading or a citation must never be able to produce one, and a
        check built on raw text (as `scripts/lint_ruleset.py`'s cross-reference
        scan still is) has no way to tell the two apart.
        """
        fenced: set[int] = set()
        for section in self.walk():
            for block in section.blocks:
                if block.kind == "fence":
                    fenced.update(range(block.line_start, block.line_end + 1))

        start = max(self.line, 1)  # the root has no heading line of its own
        return [lines[n - 1] for n in range(start, self.line_end + 1) if n not in fenced]

    def to_dict(self) -> dict:
        return {
            "level": self.level,
            "title": self.title,
            "line": self.line,
            "line_end": self.line_end,
            "rule_id": self.rule_id,
            "rule_prefix": self.rule_prefix,
            "rule_number": self.rule_number,
            "rule_title": self.rule_title,
            "blocks": [block.to_dict() for block in self.blocks],
            "children": [child.to_dict() for child in self.children],
        }


@dataclass
class Document:
    """One parsed docs/*.md file."""

    name: str  # "07-movement.md"
    path: Path
    lines: list[str]  # the file, split, no trailing newlines
    root: Section  # synthetic, level 0, spans the whole file

    def to_dict(self) -> dict:
        try:
            path = self.path.relative_to(REPO_ROOT).as_posix()
        except ValueError:
            path = str(self.path)
        # `lines` is not included: it is the file's own text, already present
        # (structured, and split into the blocks that hold it) inside `root`.
        # Repeating it flat here would be the file's content twice in one
        # object for no reader that needs it that way.
        return {"name": self.name, "path": path, "root": self.root.to_dict()}


def _classify(line: str) -> str:
    """Which block kind a line starts, decided by how it begins.

    Fences are handled by the scanner before this is ever called — a line
    that opens or closes one never reaches here.
    """
    if line.startswith("|"):
        return "table"
    if line.startswith(">"):
        return "quote"
    if LIST_ITEM_RE.match(line):
        return "list"
    if line.strip() == "---":
        return "break"
    return "paragraph"


def _make_section(level: int, title: str, lineno: int) -> Section:
    match = RULE_HEADING_RE.match(title)
    if match:
        prefix, number, rule_title = match.groups()
        return Section(
            level=level,
            title=title,
            line=lineno,
            line_end=lineno,
            rule_id=f"{prefix}-{number}",
            rule_prefix=prefix,
            rule_number=int(number),
            rule_title=rule_title,
        )
    return Section(
        level=level, title=title, line=lineno, line_end=lineno,
        rule_id=None, rule_prefix=None, rule_number=None, rule_title=None,
    )


def parse_text(name: str, text: str) -> Document:
    """Parse a document already held as a string.

    This is what the tests and `scripts/lint_ruleset.py` use — the linter
    already reads every docs/*.md into a dict of strings before checking
    anything, so handing it a path to re-read would be a second read of a
    file it already has open.

    One pass, line by line. State is a fence flag, the block currently being
    accumulated, and a stack of open sections (root always at the bottom).

    **Fences first, always.** This is the first branch below because a fenced
    markdown example is the bug that motivated this module: a `# Fake
    Chapter` written as an example of a heading was, before this, read as a
    real one. Inside a fence nothing is a heading, a break, a table row or a
    list — every line accumulates into the fence's own block, verbatim,
    including both marker lines.

    Divergences from CommonMark, each deliberate:
      - `---` alone is always a thematic break, never a setext heading
        underline — in this repo `---` always follows a blank line, and
        reading it as an underline would turn the last line of the
        paragraph above it into a heading no one meant to write.
      - Only ATX headings (`#`, `##`, `###`) are recognised; there is no
        setext heading at all.
      - Only backtick fences; `~~~` is not one.
      - `####` and deeper is not a heading (see `ATX_HEADING_RE`).
      - No inline parsing. Emphasis, links and code spans are just text
        inside whatever block holds them.
    """
    lines = text.splitlines()
    root = Section(
        level=0, title="", line=0, line_end=len(lines),
        rule_id=None, rule_prefix=None, rule_number=None, rule_title=None,
    )
    stack: list[Section] = [root]

    in_fence = False
    current: dict | None = None  # {"kind", "start", "end", "lines"}

    def flush() -> None:
        nonlocal current
        if current is not None:
            stack[-1].blocks.append(Block(
                kind=current["kind"],
                line_start=current["start"],
                line_end=current["end"],
                lines=current["lines"],
            ))
            current = None

    for lineno, raw in enumerate(lines, start=1):
        if in_fence:
            current["lines"].append(raw)
            current["end"] = lineno
            if raw.strip().startswith("```"):
                in_fence = False
                flush()
            continue

        if raw.strip().startswith("```"):
            flush()
            current = {"kind": "fence", "start": lineno, "end": lineno, "lines": [raw]}
            in_fence = True
            continue

        if not raw.strip():
            flush()
            continue

        heading = ATX_HEADING_RE.match(raw)
        if heading:
            flush()
            hashes, title = heading.groups()
            level = len(hashes)
            section = _make_section(level, title, lineno)
            while stack[-1].level >= level:
                stack[-1].line_end = lineno - 1
                stack.pop()
            stack[-1].children.append(section)
            stack.append(section)
            continue

        kind = _classify(raw)
        if current is not None and current["kind"] == kind:
            current["lines"].append(raw)
            current["end"] = lineno
        else:
            flush()
            current = {"kind": kind, "start": lineno, "end": lineno, "lines": [raw]}
        if kind == "break":
            # A thematic break is always exactly one line — flush immediately
            # rather than waiting for the next line to differ, so two "---"
            # lines with no blank line between them are two break blocks
            # rather than one two-line block of kind "break".
            flush()

    flush()
    while stack:
        stack[-1].line_end = len(lines)
        stack.pop()

    return Document(name=name, path=Path(name), lines=lines, root=root)


def parse(path: Path) -> Document:
    """Parse a document from disk."""
    document = parse_text(path.name, path.read_text())
    document.path = path
    return document


def parse_docs() -> dict[str, Document]:
    """Every docs/*.md, parsed and keyed by filename, sorted."""
    return {path.name: parse(path) for path in sorted(DOCS_DIR.glob("*.md"))}
