#!/usr/bin/env python3
"""Structural linter for the docs/*.md ruleset.

Checks things a human reviewer shouldn't have to catch by hand:

- Duplicate rule IDs within a document (e.g. two `# WPN-002` headers).
- Rule IDs that aren't strictly increasing within their document.
- Cross-document rule references that point at an ID which doesn't exist
  in the target document, in both of the forms this repo writes:
  the parenthesised "`10-weapons.md` (WPN-002)" and the comma form
  "`08-vehicles.md`, VEH-013", including comma-separated runs of IDs.
- `**Version:**` headers that are missing, malformed, or disagree with
  each other (all docs/*.md are expected to share one project version).
- The document skeleton required by system/documentation-standards.md:
  Purpose, Design Philosophy and Summary sections, and a closing motto.

This is a structural check, not a semantic one: it cannot tell you that
a rule contradicts another rule's intent (see system/workflow.md and
review the diff by hand for that). It only catches mechanical breakage.
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"

RULE_HEADER_RE = re.compile(r"^#{1,2} ([A-Z]{2,6})-(\d{3}) — ", re.MULTILINE)
VERSION_RE = re.compile(r"^\*\*Version:\*\*\s*(\d+\.\d+\.\d+)\s*(.*)$", re.MULTILINE)
CROSS_REF_RE = re.compile(r"`([\w.-]+\.md)`[^\n]{0,80}?\(([A-Z]{2,6}-\d{3})\)")

# The comma form — "`08-vehicles.md`, VEH-013" — is what this repo writes most,
# and until this existed nothing checked it: roughly two thirds of the citations
# in docs/ were never verified by any script. A citation may name several IDs in
# a run ("`02-core-rules.md`, CORE-008, CORE-009"), so capture the whole run and
# split it afterwards. The run stops at the first thing that isn't an ID, which
# is what keeps "`16-damage-system.md`, DMG-019, Repairs)" from swallowing the
# word Repairs.
COMMA_REF_RE = re.compile(r"`([\w.-]+\.md)`,\s+((?:[A-Z]{2,6}-\d{3}(?:,\s+)?)+)")
RULE_ID_RE = re.compile(r"[A-Z]{2,6}-\d{3}")

MOTTOS = ("> **Every Brick Matters.**", "> **The Model Is The Rules.**")

# Required sections, per system/documentation-standards.md. "Rule Definitions"
# is in that list but is not a heading anywhere in docs/ — the rule headers
# themselves are the definitions — so it is not checked as one.
REQUIRED_SECTIONS = ("Purpose", "Design Philosophy", "Summary")

# 02-core-rules.md predates the standard and has neither a Design Philosophy nor
# a Summary section. Adding them changes the ruleset, which needs an OpenSpec
# proposal, so it is recorded here rather than fixed in passing. The point of
# the exemption is that it is a closed list: a *new* document cannot join it
# without someone editing this line.
SECTION_DEBT = {"02-core-rules.md": ("Design Philosophy", "Summary")}


def collect_rule_ids(text: str) -> list[tuple[str, int]]:
    return [(prefix, int(number)) for prefix, number in RULE_HEADER_RE.findall(text)]


def check_structure(
    texts: dict[str, str], ids_by_file: dict[str, set[str]]
) -> list[str]:
    """Verify the skeleton every ruleset document is required to have.

    Sections are only required of documents that define rules, which is the
    same test the **Version:** check already uses. 01-foundations.md and
    14-glossary.md define none: one is the introduction, the other a glossary,
    and neither is a rulebook chapter.

    The closing motto is required of all of them. Every document in docs/ ends
    with one today, so this is a rule the repo already keeps rather than a new
    obligation.
    """
    errors: list[str] = []

    for name, text in sorted(texts.items()):
        if ids_by_file.get(name):
            exempt = SECTION_DEBT.get(name, ())
            for section in REQUIRED_SECTIONS:
                if section in exempt:
                    continue
                if not re.search(rf"^#{{1,2}} {re.escape(section)}\s*$", text, re.MULTILINE):
                    errors.append(f"{name}: missing required '# {section}' section")

        lines = [line for line in text.splitlines() if line.strip()]
        if not lines:
            errors.append(f"{name}: file is empty")
            continue

        closing = lines[-1].strip()
        if closing not in MOTTOS:
            errors.append(
                f"{name}: does not close with a motto. The last line must be "
                f"exactly {MOTTOS[0]!r} for construction and gameplay documents, "
                f"or {MOTTOS[1]!r} for the two about the model-defines-values "
                f"mechanism. Found: {closing!r}"
            )

    return errors


def main() -> int:
    errors: list[str] = []
    docs = sorted(DOCS_DIR.glob("*.md"))
    texts = {doc.name: doc.read_text() for doc in docs}
    ids_by_file: dict[str, set[str]] = {}
    versions: dict[str, str] = {}

    for name, text in texts.items():
        rule_ids = collect_rule_ids(text)
        ids_by_file[name] = {f"{p}-{n:03d}" for p, n in rule_ids}

        seen: dict[str, int] = {}
        last_number: dict[str, int] = {}
        for prefix, number in rule_ids:
            rule_id = f"{prefix}-{number:03d}"
            if rule_id in seen:
                errors.append(f"{name}: duplicate rule ID {rule_id}")
            seen[rule_id] = seen.get(rule_id, 0) + 1

            if prefix in last_number and number <= last_number[prefix]:
                errors.append(
                    f"{name}: {rule_id} is not strictly increasing after "
                    f"{prefix}-{last_number[prefix]:03d}"
                )
            last_number[prefix] = number

        version_match = VERSION_RE.search(text)
        if version_match is None:
            if rule_ids:
                errors.append(f"{name}: missing or malformed **Version:** header")
        else:
            versions[name] = version_match.group(1)

    if len(set(versions.values())) > 1:
        grouped = ", ".join(f"{v}={[n for n, ver in versions.items() if ver == v]}" for v in sorted(set(versions.values())))
        errors.append(f"docs/*.md Version headers disagree: {grouped}")

    for name, text in texts.items():
        for target_file, rule_id in CROSS_REF_RE.findall(text):
            if target_file not in ids_by_file:
                continue
            if rule_id not in ids_by_file[target_file]:
                errors.append(f"{name}: references {target_file} ({rule_id}), which does not exist")

        for target_file, id_run in COMMA_REF_RE.findall(text):
            if target_file not in ids_by_file:
                continue
            for rule_id in RULE_ID_RE.findall(id_run):
                if rule_id not in ids_by_file[target_file]:
                    errors.append(f"{name}: references {target_file}, {rule_id}, which does not exist")

    errors.extend(check_structure(texts, ids_by_file))

    if errors:
        for error in errors:
            print(f"::error::{error}")
        print(f"\n{len(errors)} issue(s) found.")
        return 1

    print(f"Checked {len(docs)} docs, no structural issues found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
