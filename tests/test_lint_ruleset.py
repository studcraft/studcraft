"""The ruleset linter is a required status check, so what it accepts is what
lands. These cover the parts that decide a pass: the document skeleton, and the
image index — the one place a filename and a rule ID have to agree across two
directories.
"""

from __future__ import annotations

import lint_ruleset

COMPLETE = """# 08-vehicles.md

**Version:** 0.4.0

# Purpose

Why this document exists.

# Design Philosophy

What it is built on.

# VEH-001 — Vehicle Footprint

A vehicle occupies whole studs.

# Summary

What the rules above say.

> **Every Brick Matters.**
"""


def structure_errors(name: str, text: str, has_rules: bool = True) -> list[str]:
    ids = {name: {"VEH-001"} if has_rules else set()}
    return lint_ruleset.check_structure({name: text}, ids)


class TestTheDocumentSkeleton:
    def test_a_complete_document_reports_nothing(self):
        assert structure_errors("08-vehicles.md", COMPLETE) == []

    def test_a_missing_section_is_reported(self):
        errors = structure_errors("08-vehicles.md", COMPLETE.replace("# Design Philosophy", "# Notes"))
        assert any("Design Philosophy" in error for error in errors)

    def test_a_document_defining_no_rules_needs_no_sections(self):
        text = "# 14-glossary.md\n\n## Unit Base\n\nA volume.\n\n> **Every Brick Matters.**\n"
        assert structure_errors("14-glossary.md", text, has_rules=False) == []

    def test_the_recorded_exemption_is_not_reported_again(self):
        assert "02-core-rules.md" in lint_ruleset.SECTION_DEBT
        text = COMPLETE.replace("# Design Philosophy", "# Notes").replace("# Summary", "# Notes")
        assert structure_errors("02-core-rules.md", text) == []

    def test_the_closing_motto_is_required(self):
        errors = structure_errors("08-vehicles.md", COMPLETE.replace("> **Every Brick Matters.**", "Done."))
        assert any("motto" in error for error in errors)

    def test_the_other_motto_is_accepted(self):
        text = COMPLETE.replace("> **Every Brick Matters.**", "> **The Model Is The Rules.**")
        assert structure_errors("16-damage-system.md", text) == []

    def test_trailing_blank_lines_do_not_hide_the_motto(self):
        assert structure_errors("08-vehicles.md", COMPLETE + "\n\n\n") == []


class TestTheVersionHeader:
    """Requiring the header of every rule-bearing document made a new ruleset
    document impossible to add: only the Release cut may write that line, and the
    cut did not insert one that was absent. VERSION_DEBT is the narrow exemption,
    and what matters about it is that it clears itself.
    """

    HEADERLESS = COMPLETE.replace("**Version:** 0.4.0\n\n", "")

    def versions(self, name: str, text: str, has_rules: bool = True) -> list[str]:
        ids = {name: {"VEH-001"} if has_rules else set()}
        return lint_ruleset.check_versions({name: text}, ids)

    def test_a_rule_bearing_document_needs_one(self):
        errors = self.versions("08-vehicles.md", self.HEADERLESS)
        assert any("missing or malformed" in error for error in errors)

    def test_a_document_defining_no_rules_does_not(self):
        assert self.versions("14-glossary.md", self.HEADERLESS, has_rules=False) == []

    def test_a_document_awaiting_its_first_cut_is_exempt(self, monkeypatch):
        monkeypatch.setattr(lint_ruleset, "VERSION_DEBT", frozenset({"17-infantry.md"}))
        assert self.versions("17-infantry.md", self.HEADERLESS) == []

    def test_the_exemption_clears_itself_once_the_cut_supplies_one(self, monkeypatch):
        monkeypatch.setattr(lint_ruleset, "VERSION_DEBT", frozenset({"17-infantry.md"}))
        errors = self.versions("17-infantry.md", COMPLETE)
        assert any("VERSION_DEBT" in error for error in errors)

    def test_headers_that_disagree_are_reported(self):
        errors = lint_ruleset.check_versions(
            {"08-vehicles.md": COMPLETE, "09-transport.md": COMPLETE.replace("0.4.0", "0.5.0")},
            {"08-vehicles.md": {"VEH-001"}, "09-transport.md": {"TRN-001"}},
        )
        assert any("disagree" in error for error in errors)

    def test_an_exempt_document_does_not_drag_the_others_out_of_agreement(self, monkeypatch):
        monkeypatch.setattr(lint_ruleset, "VERSION_DEBT", frozenset({"17-infantry.md"}))
        errors = lint_ruleset.check_versions(
            {"08-vehicles.md": COMPLETE, "17-infantry.md": self.HEADERLESS},
            {"08-vehicles.md": {"VEH-001"}, "17-infantry.md": {"INF-001"}},
        )
        assert errors == []


class TestRuleIds:
    def test_ids_are_read_with_their_numbers(self):
        text = "# VEH-001 — One\n\n# VEH-002 — Two\n"
        assert lint_ruleset.collect_rule_ids(text) == [("VEH", 1), ("VEH", 2)]


IMAGES = """# Image index

| Column | Meaning |
|---|---|
| Rule | the rule illustrated |

## docs/10-weapons.md

| Rule | File |
|---|---|
| WPN-020 | `assets/images/wpn-020-muzzle-placement.png` |
| Terrain (WPN-018 – WPN-019) | `assets/images/10-weapon-grid.png` |

## Not a document heading

| Rule | File |
|---|---|
| WPN-001 | `assets/images/wpn-001-ignored.png` |
"""


class TestTheImageIndex:
    def test_only_rows_under_a_document_heading_are_entries(self):
        entries = lint_ruleset.parse_image_entries(IMAGES)
        assert [entry[3] for entry in entries] == [
            "assets/images/wpn-020-muzzle-placement.png",
            "assets/images/10-weapon-grid.png",
        ]

    def test_each_entry_carries_the_document_it_sits_under(self):
        assert {entry[1] for entry in lint_ruleset.parse_image_entries(IMAGES)} == {
            "10-weapons.md"
        }

    def test_a_row_naming_no_file_is_still_returned(self):
        text = "## docs/10-weapons.md\n\n| Rule | File |\n|---|---|\n| WPN-020 | to be drawn |\n"
        (entry,) = lint_ruleset.parse_image_entries(text)
        assert entry[3] == ""
