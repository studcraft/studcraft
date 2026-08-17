#!/usr/bin/env python3
"""Structural linter for the docs/*.md ruleset.

Checks things a human reviewer shouldn't have to catch by hand:

- Duplicate rule IDs within a document (e.g. two `# WPN-002` headers).
- Rule IDs that aren't strictly increasing within their document.
- Cross-document rule references that point at an ID which doesn't exist
  in the target document, in both of the forms this repo writes:
  the parenthesised "`10-weapons.md` (WPN-002)" and the comma form
  "`08-vehicles.md`, VEH-013", including comma-separated runs of IDs.
  A parenthesised ID carrying the citing document's own prefix is
  checked against that document instead of against the filename that
  happens to precede it — each document owns its namespace, so
  "`09-transport.md`, TRN-001), ... its own Unit Base (DEP-004)" in
  06-deployment.md is a reference to DEP-004 and not a broken one into
  09-transport.md.
- `**Version:**` headers that are missing, malformed, or disagree with
  each other (all docs/*.md are expected to share one project version).
- The document skeleton required by system/documentation-standards.md:
  Purpose, Design Philosophy and Summary sections, and a closing motto.
- The image filenames in assets/IMAGES.md: that each follows the naming
  convention that file defines, that it names a document which exists,
  and that the rule it illustrates exists in that document.

This is a structural check, not a semantic one: it cannot tell you that
a rule contradicts another rule's intent (see system/workflow.md and
review the diff by hand for that). It only catches mechanical breakage.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from repo import DOCS_DIR, REPO_ROOT, RULE_HEADER_RE, RULE_ID_RE  # noqa: E402

IMAGES_INDEX = REPO_ROOT / "assets" / "IMAGES.md"

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

# assets/IMAGES.md groups its entries under one "## docs/<file>.md" heading per
# document, each holding a single table whose first two columns are the rule and
# the image filename. Only tables under such a heading are entries; the file's
# other tables (the entry-format template, the weapon-grid symbol legend) are
# prose about the format and are skipped by anchoring on the heading.
IMAGE_SECTION_RE = re.compile(r"^## docs/([\w.-]+\.md)\s*$")
IMAGE_PATH_RE = re.compile(r"`(assets/images/[^`]+)`")

# The convention, defined in assets/IMAGES.md: a lowercase hyphen-separated slug
# under assets/images/, prefixed by the lowercased rule ID for a numbered rule
# (wpn-020-muzzle-placement.png) or by the document number for an unnumbered
# section (07-terrain-thresholds.png).
IMAGE_NAME_RE = re.compile(r"^assets/images/[a-z0-9]+(?:-[a-z0-9]+)+\.png$")
DOC_NUMBER_RE = re.compile(r"^(\d{2})-")


def parse_image_entries(text: str) -> list[tuple[int, str, str, str]]:
    """Pull (line number, document, rule cell, filename) out of assets/IMAGES.md.

    Returns raw cells rather than validated ones so the checker below can report
    each kind of breakage separately; a row that names no filename at all is
    still returned, with an empty filename, so it is reported and not skipped.
    """
    entries: list[tuple[int, str, str, str]] = []
    current_doc: str | None = None

    for lineno, line in enumerate(text.splitlines(), start=1):
        heading = IMAGE_SECTION_RE.match(line)
        if heading:
            current_doc = heading.group(1)
            continue
        if line.startswith("#"):
            current_doc = None
            continue
        if current_doc is None or not line.startswith("|"):
            continue

        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 2 or cells[0] in ("Rule", "---") or set(cells[0]) <= {"-", ":"}:
            continue

        path_match = IMAGE_PATH_RE.search(cells[1])
        entries.append((lineno, current_doc, cells[0], path_match.group(1) if path_match else ""))

    return entries


def check_image_index(ids_by_file: dict[str, set[str]]) -> list[str]:
    """Check assets/IMAGES.md against its own naming convention and against docs/.

    This is the one place a filename and a rule ID have to agree across two
    directories, and nothing else verifies it: an image specified for a rule that
    was renumbered or removed would otherwise sit in the index until someone came
    to draw it. Absent index, nothing to check — the file is not required to exist.
    """
    if not IMAGES_INDEX.exists():
        return []

    errors: list[str] = []
    seen_paths: dict[str, int] = {}

    for lineno, doc, rule_cell, path in parse_image_entries(IMAGES_INDEX.read_text()):
        where = f"assets/IMAGES.md:{lineno}"

        if doc not in ids_by_file:
            errors.append(f"{where}: section names docs/{doc}, which does not exist")
            continue

        if not path:
            errors.append(f"{where}: entry for {rule_cell!r} names no assets/images/ file")
            continue

        if not IMAGE_NAME_RE.match(path):
            errors.append(
                f"{where}: {path} does not follow the naming convention in "
                f"assets/IMAGES.md (assets/images/<prefix>-<lowercase-slug>.png)"
            )
        if path in seen_paths:
            errors.append(f"{where}: {path} is already used at line {seen_paths[path]}")
        seen_paths[path] = lineno

        stem = path[len("assets/images/"):-len(".png")]
        cited = RULE_ID_RE.findall(rule_cell)

        for rule_id in cited:
            if rule_id not in ids_by_file[doc]:
                errors.append(f"{where}: {rule_id} does not exist in docs/{doc}")

        # A row whose Rule cell is exactly one ID is the numbered case and takes
        # that ID as its prefix. Anything else — a heading, or a range such as
        # "Terrain Movement (MOVE-009 – MOVE-011)" — is the unnumbered case and
        # takes the document number instead.
        if len(cited) == 1 and rule_cell == cited[0]:
            expected = cited[0].lower()
        else:
            doc_number = DOC_NUMBER_RE.match(doc)
            expected = doc_number.group(1) if doc_number else None

        if expected and not stem.startswith(f"{expected}-"):
            errors.append(
                f"{where}: {path} should start with '{expected}-' for an entry "
                f"under {rule_cell!r} in docs/{doc}"
            )

    return errors


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
    prefixes_by_file: dict[str, set[str]] = {}
    versions: dict[str, str] = {}

    for name, text in texts.items():
        rule_ids = collect_rule_ids(text)
        ids_by_file[name] = {f"{p}-{n:03d}" for p, n in rule_ids}
        prefixes_by_file[name] = {p for p, _ in rule_ids}

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
            # The parenthesised form leaves up to 80 characters between the
            # filename and the ID, which is what lets "see `10-weapons.md`
            # (WPN-002)" and a continuation form, where a second bare ID follows
            # the cited one after a few words of prose, both match. That window also
            # lets the pattern reach past one citation and pick up a bare
            # same-document ID that was never a reference into the cited file.
            # The prefix settles it: each document owns its own namespace
            # (system/documentation-standards.md, Naming Conventions), so an ID
            # carrying this document's own prefix belongs to this document
            # whatever filename precedes it, and it is checked against this
            # document rather than dropped. That only reaches a same-document ID
            # close enough to a filename citation to be caught by this pattern at
            # all; a bare "(VEH-099)" standing on its own is still unchecked, the
            # same as before.
            owner = name if rule_id.split("-")[0] in prefixes_by_file[name] else target_file
            if rule_id not in ids_by_file[owner]:
                errors.append(f"{name}: references {owner} ({rule_id}), which does not exist")

        for target_file, id_run in COMMA_REF_RE.findall(text):
            if target_file not in ids_by_file:
                continue
            for rule_id in RULE_ID_RE.findall(id_run):
                if rule_id not in ids_by_file[target_file]:
                    errors.append(f"{name}: references {target_file}, {rule_id}, which does not exist")

    errors.extend(check_structure(texts, ids_by_file))
    errors.extend(check_image_index(ids_by_file))

    if errors:
        for error in errors:
            print(f"::error::{error}")
        print(f"\n{len(errors)} issue(s) found.")
        return 1

    print(f"Checked {len(docs)} docs, no structural issues found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
