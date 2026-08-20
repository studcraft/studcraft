"""The index is a cache in front of `docs/`, and `rule.py` answers from it.

A wrong index is a wrong answer given confidently, which is worse than no index,
so what is tested here is that it says what the documents say — and that a
reader can never catch it half-written.
"""

from __future__ import annotations

import json
import os
import re

import build_index
import pytest
import ruleset_ast
from repo import DOCS_DIR, RULE_ID_RE

DOCUMENT = """# 08-vehicles.md

**Version:** 0.4.0

# VEH-001 — Vehicle Footprint

A vehicle occupies whole studs. Everything after the first full stop is why.

More body, citing `07-movement.md`, MOVE-004 and VEH-001 itself.

---

# VEH-002 — Vehicle Facing

A vehicle faces the long axis of its footprint.

---

# Summary

Not a rule, and the body of VEH-002 stops here.
"""

DOCUMENT_WITH_A_CHAPTER = """# 08-vehicles.md

**Version:** 0.4.0

# Purpose

Why this document exists.

# VEH-001 — Vehicle Footprint

A vehicle occupies whole studs.

## Scenario One

A worked example, not a rule — VEH-001's own sub-heading.

---

# A Chapter

## VEH-002 — Vehicle Facing

A vehicle faces the long axis of its footprint.

## VEH-003 — Vehicle Length

How a vehicle's length is measured.

---

# Summary

Not a rule.
"""

GLOSSARY = """# 14-glossary.md

## Unit Base

The volume one infantry model occupies (`04-construction-standard.md`, SCS-001).

## Impact Strength

Muzzle size times three (WPN-021).
"""

# The body-end rule `scripts/build_index.py` used before this module started
# reading `scripts/ruleset_ast.py`: any `#` or `##` heading closed a rule's
# body, its own sub-headings included. That pattern is deleted along with the
# code that used it — reimporting it just to keep a comparison test alive
# would keep the defect on life support, so it is reproduced here, once, as a
# literal, for `TestTheMigrationMovesNothingButDEP009` alone.
_OLD_HEADING_RE = re.compile(r"^#{1,2} \S")
_OLD_RULE_HEADER_LINE_RE = re.compile(r"^#{1,2} ([A-Z]{2,6})-(\d{3}) — (.+?)\s*$")


def _pre_migration_parse(text: str) -> dict[str, dict]:
    """What `scripts/build_index.py`'s `parse_document` returned before this
    migration, keyed by rule ID. Kept minimal: only what the comparison test
    needs, `line_end` and `cites`.
    """
    lines = text.splitlines()
    headers: list[tuple[int, str]] = []
    for number, line in enumerate(lines, start=1):
        match = _OLD_RULE_HEADER_LINE_RE.match(line)
        if match:
            prefix, digits, _title = match.groups()
            headers.append((number, f"{prefix}-{digits}"))

    result: dict[str, dict] = {}
    for index, (line_no, rule_id) in enumerate(headers):
        limit = headers[index + 1][0] - 1 if index + 1 < len(headers) else len(lines)
        body: list[str] = []
        for raw in lines[line_no:limit]:
            if _OLD_HEADING_RE.match(raw):
                break
            body.append(raw)
        cited = [
            rid for rid in dict.fromkeys(RULE_ID_RE.findall("\n".join(body))) if rid != rule_id
        ]
        result[rule_id] = {"line_end": line_no + len(body), "cites": cited}
    return result


class TestParsingADocument:
    def test_every_rule_is_found_with_its_line_and_title(self):
        rules = build_index.parse_document("08-vehicles.md", DOCUMENT)
        assert [rule["id"] for rule in rules] == ["VEH-001", "VEH-002"]
        assert rules[0]["title"] == "Vehicle Footprint"
        assert DOCUMENT.splitlines()[rules[0]["line"] - 1].startswith("# VEH-001")

    def test_the_summary_is_the_first_sentence_of_the_body(self):
        rules = build_index.parse_document("08-vehicles.md", DOCUMENT)
        assert rules[0]["summary"] == "A vehicle occupies whole studs."

    def test_a_rule_does_not_cite_itself(self):
        rules = build_index.parse_document("08-vehicles.md", DOCUMENT)
        assert "VEH-001" not in rules[0]["cites"]
        assert "MOVE-004" in rules[0]["cites"]

    def test_a_body_stops_at_the_next_rule_and_at_a_sibling_section(self):
        rules = build_index.parse_document("08-vehicles.md", DOCUMENT)
        # VEH-001's body ends before VEH-002's heading starts.
        assert rules[0]["line_end"] < rules[1]["line"]
        # "Not a rule" sits under `# Summary`, a sibling of VEH-002 rather
        # than a descendant of it, so nothing from it is VEH-002's.
        assert rules[1]["summary"] == "A vehicle faces the long axis of its footprint."

    def test_glossary_entries_carry_the_rules_they_point_at(self):
        entries = build_index.parse_glossary(GLOSSARY)
        assert [entry["term"] for entry in entries] == ["Unit Base", "Impact Strength"]
        assert entries[0]["cites"] == ["SCS-001"]


class TestOutline:
    """`outline` is `#`/`##` sections only, in document order — the title and
    a rule's own sub-headings excluded. `DOCUMENT_WITH_A_CHAPTER` carries one
    of each: a title, a prose section (`Purpose`), a standalone rule with its
    own `##` sub-heading (`VEH-001`, `Scenario One`), a chapter holding two
    `##` rules (`A Chapter`, `VEH-002`, `VEH-003`), and a closing prose
    section (`Summary`).
    """

    def _outline(self) -> list[dict]:
        document = ruleset_ast.parse_text("08-vehicles.md", DOCUMENT_WITH_A_CHAPTER)
        return build_index.build_outline(document)

    def test_the_documents_own_title_is_not_in_the_outline(self):
        titles = [entry["title"] for entry in self._outline()]
        assert "08-vehicles.md" not in titles

    def test_a_rules_own_sub_heading_is_not_a_further_outline_entry(self):
        titles = [entry["title"] for entry in self._outline()]
        assert "Scenario One" not in titles

    def test_the_outline_is_in_document_order(self):
        lines = [entry["line"] for entry in self._outline()]
        assert lines == sorted(lines)

    def test_rule_sections_carry_their_id_and_others_carry_none(self):
        by_title = {entry["title"]: entry["rule_id"] for entry in self._outline()}
        assert by_title == {
            "Purpose": None,
            "Vehicle Footprint": "VEH-001",
            "A Chapter": None,
            "Vehicle Facing": "VEH-002",
            "Vehicle Length": "VEH-003",
            "Summary": None,
        }

    def test_a_rule_inside_a_chapter_is_level_two_and_the_chapter_is_level_one(self):
        by_title = {entry["title"]: entry["level"] for entry in self._outline()}
        assert by_title["A Chapter"] == 1
        assert by_title["Vehicle Facing"] == 2
        assert by_title["Vehicle Length"] == 2

    def test_every_built_document_carries_an_outline(self):
        index = build_index.build()
        for name, document in index["documents"].items():
            assert "outline" in document, name


class TestABodyDoesNotStopAtItsOwnSubHeading:
    """Regression test for the bug this migration exists to fix:
    `scripts/rule.py show DEP-009` printed without its four scenario
    sub-sections, because the old body-end rule stopped at *any* heading,
    including a rule's own `##` scenarios.
    """

    def test_dep_009s_body_reaches_past_massive_battle(self):
        path = DOCS_DIR / "06-deployment.md"
        text = path.read_text()
        lines = text.splitlines()
        massive_battle_line = next(
            number for number, line in enumerate(lines, start=1)
            if line == "## Massive Battle"
        )

        rules = build_index.parse_document(path.name, text)
        (dep009,) = [rule for rule in rules if rule["id"] == "DEP-009"]

        assert dep009["line_end"] > massive_battle_line


class TestLineEnd:
    def test_every_rule_has_a_line_end_no_earlier_than_its_line(self):
        for path in sorted(DOCS_DIR.glob("*.md")):
            for rule in build_index.parse_document(path.name, path.read_text()):
                assert rule["line_end"] >= rule["line"], rule["id"]


class TestTheMigrationMovesNothingButDEP009:
    """The measurements taken for this migration say the citation graph does
    not move — `cites` is identical for all 197 rules, before and after — and
    that exactly one rule's body grows: DEP-009's, whose scenario
    sub-sections name no rule ID at all. This pins both claims against the
    real `docs/`, rather than trusting them.
    """

    def test_197_rules_same_cites_and_only_dep_009s_body_grows(self):
        old: dict[str, dict] = {}
        new: dict[str, dict] = {}
        for path in sorted(DOCS_DIR.glob("*.md")):
            text = path.read_text()
            old.update(_pre_migration_parse(text))
            for rule in build_index.parse_document(path.name, text):
                new[rule["id"]] = {"line_end": rule["line_end"], "cites": rule["cites"]}

        # Not a rule count. Retiring an ID is legal — `system/documentation-standards.md`
        # (Naming Conventions) — and a hardcoded total makes every retirement
        # break a test about body spans. What this pins is that both readings
        # see the same rules, which is what makes the cites comparison below
        # mean anything.
        assert set(old) == set(new)

        old_cites = {rule_id: entry["cites"] for rule_id, entry in old.items()}
        new_cites = {rule_id: entry["cites"] for rule_id, entry in new.items()}
        assert old_cites == new_cites

        grown = [rid for rid in new if new[rid]["line_end"] > old[rid]["line_end"]]
        shrunk = [rid for rid in new if new[rid]["line_end"] < old[rid]["line_end"]]
        assert grown == ["DEP-009"]
        assert shrunk == []


class TestWritingTheIndex:
    """`rule.py` rebuilds this file on demand, so two processes can write while a
    third reads. The write has to be all-or-nothing."""

    def test_the_index_is_valid_json_and_readable(self, tmp_path, monkeypatch):
        monkeypatch.setattr(build_index, "INDEX_PATH", tmp_path / "index.json")
        build_index.write_index({"rules": {}, "documents": {}, "glossary": []})
        assert json.loads((tmp_path / "index.json").read_text())["rules"] == {}

    def test_a_failed_write_leaves_the_previous_index_intact(self, tmp_path, monkeypatch):
        index_path = tmp_path / "index.json"
        index_path.write_text('{"rules": {"VEH-001": {}}}\n')
        monkeypatch.setattr(build_index, "INDEX_PATH", index_path)

        def failing_replace(src, dst):
            raise OSError("disk full")

        monkeypatch.setattr(os, "replace", failing_replace)

        with pytest.raises(OSError):
            build_index.write_index({"rules": {}, "documents": {}, "glossary": []})

        assert json.loads(index_path.read_text())["rules"] == {"VEH-001": {}}

    def test_a_failed_write_leaves_no_temporary_file_behind(self, tmp_path, monkeypatch):
        index_path = tmp_path / "index.json"
        index_path.write_text("{}\n")
        monkeypatch.setattr(build_index, "INDEX_PATH", index_path)
        monkeypatch.setattr(os, "replace", lambda src, dst: (_ for _ in ()).throw(OSError()))

        with pytest.raises(OSError):
            build_index.write_index({"rules": {}, "documents": {}, "glossary": []})

        assert sorted(p.name for p in tmp_path.iterdir()) == ["index.json"]
