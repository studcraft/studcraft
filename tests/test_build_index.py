"""The index is a cache in front of `docs/`, and `rule.py` answers from it.

A wrong index is a wrong answer given confidently, which is worse than no index,
so what is tested here is that it says what the documents say — and that a
reader can never catch it half-written.
"""

from __future__ import annotations

import json
import os

import build_index
import pytest

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

GLOSSARY = """# 14-glossary.md

## Unit Base

The volume one infantry model occupies (`04-construction-standard.md`, SCS-001).

## Impact Strength

Muzzle size times three (WPN-021).
"""


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

    def test_a_body_stops_at_the_next_heading(self):
        rules = build_index.parse_document("08-vehicles.md", DOCUMENT)
        # "Not a rule" sits under `# Summary`, so nothing from it is VEH-002's.
        assert rules[1]["summary"] == "A vehicle faces the long axis of its footprint."

    def test_glossary_entries_carry_the_rules_they_point_at(self):
        entries = build_index.parse_glossary(GLOSSARY)
        assert [entry["term"] for entry in entries] == ["Unit Base", "Impact Strength"]
        assert entries[0]["cites"] == ["SCS-001"]


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
