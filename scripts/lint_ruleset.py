#!/usr/bin/env python3
"""Structural linter for the docs/*.md ruleset.

Checks things a human reviewer shouldn't have to catch by hand:

- Duplicate rule IDs within a document (e.g. two `# WPN-002` headers).
- Rule IDs that aren't strictly increasing within their document.
- Cross-document rule references (e.g. "`10-weapons.md` (WPN-002)")
  that point at an ID which doesn't exist in the target document.
- `**Version:**` headers that are missing, malformed, or disagree with
  each other (all docs/*.md are expected to share one project version).

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


def collect_rule_ids(text: str) -> list[tuple[str, int]]:
    return [(prefix, int(number)) for prefix, number in RULE_HEADER_RE.findall(text)]


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

    if errors:
        for error in errors:
            print(f"::error::{error}")
        print(f"\n{len(errors)} issue(s) found.")
        return 1

    print(f"Checked {len(docs)} docs, no structural issues found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
