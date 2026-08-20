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

    def test_a_section_written_three_levels_deep_is_still_reported_missing(self):
        # The section this check requires is `^#{1,2} Design Philosophy\s*$`
        # in spirit — a `###` heading of the same name is not that section,
        # the same as it was never matched by the regex this check replaced.
        errors = structure_errors(
            "08-vehicles.md", COMPLETE.replace("# Design Philosophy", "### Design Philosophy")
        )
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
    """Requiring a header of every rule-bearing document made a new ruleset
    document impossible to add: only the Release cut may write that line, and a
    document created between two cuts cannot have one. The check that survives is
    the one that catches a repository being wrong rather than being new.
    """

    HEADERLESS = COMPLETE.replace("**Version:** 0.4.0\n\n", "")

    def test_a_document_without_one_is_not_an_error(self):
        assert lint_ruleset.check_versions({"17-infantry.md": self.HEADERLESS}) == []

    def test_headers_that_disagree_are_reported(self):
        errors = lint_ruleset.check_versions(
            {"08-vehicles.md": COMPLETE, "09-transport.md": COMPLETE.replace("0.4.0", "0.5.0")}
        )
        assert any("disagree" in error for error in errors)

    def test_headers_that_agree_are_not(self):
        assert lint_ruleset.check_versions(
            {"08-vehicles.md": COMPLETE, "09-transport.md": COMPLETE}
        ) == []

    def test_a_document_without_one_does_not_count_as_disagreement(self):
        assert lint_ruleset.check_versions(
            {"08-vehicles.md": COMPLETE, "17-infantry.md": self.HEADERLESS}
        ) == []


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


class TestCitations:
    """The citation scan reads prose (Section.prose_lines()), not the raw
    file, so a citation-shaped line inside a fenced block is never read as a
    real citation. This is the change the whole file exists for.
    """

    def _errors(self, texts: dict[str, str], ids_by_file: dict[str, set[str]]) -> list[str]:
        prefixes_by_file = {
            name: {rid.split("-")[0] for rid in ids} for name, ids in ids_by_file.items()
        }
        return lint_ruleset.check_citations(texts, ids_by_file, prefixes_by_file)

    def test_a_citation_shaped_line_inside_a_fence_is_not_read_as_a_citation(self):
        # `08-vehicles.md` (VEH-999) names an ID that does not exist. Before
        # this change, reading raw text, that would be reported as a broken
        # reference. Inside a fence it is a worked example, not a citation.
        text = (
            "# 08-vehicles.md\n\n"
            "# VEH-001 — Vehicle Footprint\n\n"
            "A vehicle occupies whole studs.\n\n"
            "```\n"
            "`08-vehicles.md` (VEH-999)\n"
            "```\n\n"
            "> **Every Brick Matters.**\n"
        )
        errors = self._errors({"08-vehicles.md": text}, {"08-vehicles.md": {"VEH-001"}})
        assert errors == []

    def test_a_real_citation_outside_a_fence_still_resolves(self):
        text = (
            "# 08-vehicles.md\n\n"
            "# VEH-001 — Vehicle Footprint\n\n"
            "A vehicle occupies whole studs. See `10-weapons.md` (WPN-001) for mounts.\n\n"
            "> **Every Brick Matters.**\n"
        )
        errors = self._errors(
            {"08-vehicles.md": text},
            {"08-vehicles.md": {"VEH-001"}, "10-weapons.md": {"WPN-001"}},
        )
        assert errors == []

    def test_a_real_citation_naming_an_id_that_does_not_exist_is_still_reported(self):
        text = (
            "# 08-vehicles.md\n\n"
            "# VEH-001 — Vehicle Footprint\n\n"
            "A vehicle occupies whole studs. See `10-weapons.md` (WPN-999) for mounts.\n\n"
            "> **Every Brick Matters.**\n"
        )
        errors = self._errors(
            {"08-vehicles.md": text},
            {"08-vehicles.md": {"VEH-001"}, "10-weapons.md": {"WPN-001"}},
        )
        assert any("WPN-999" in error for error in errors)


CHAPTERED = """# 16-damage-system.md

# Purpose

Why this document exists.

# Design Philosophy

What it is built on.

# Component Damage

The structural model.

## DMG-001 — Component Targeting

Every impact is assigned to one component.

---

## DMG-002 — Components Have No Hit Points

A component has a state, not a total.

# DMG-003 — Geometry Defines Resistance

Resistance is read from the model.

# Summary

What the rules above say.

> **Every Brick Matters.**
"""

ONE_RULE_CHAPTER = CHAPTERED.replace(
    "---\n\n## DMG-002 — Components Have No Hit Points\n\n"
    "A component has a state, not a total.\n\n",
    "",
)


class TestChapterDepth:
    def test_a_chapter_of_two_and_a_rule_of_its_own_report_nothing(self):
        assert lint_ruleset.check_chapter_depth({"16-damage-system.md": CHAPTERED}) == []

    def test_a_chapter_holding_one_rule_is_reported(self):
        (error,) = lint_ruleset.check_chapter_depth({"16-damage-system.md": ONE_RULE_CHAPTER})
        assert "Component Damage" in error

    def test_a_section_holding_no_rules_is_prose_and_not_a_chapter(self):
        text = CHAPTERED.replace("# Summary", "# Combat Flow\n\nA diagram.\n\n# Summary")
        assert lint_ruleset.check_chapter_depth({"16-damage-system.md": text}) == []

    def test_a_rule_at_the_top_level_closes_the_chapter_above_it(self):
        # DMG-003 sits at `#`, so the `##` rule below it counts toward nothing.
        # If a `#` rule did not close a chapter, `# Component Damage` would look
        # like a chapter of two and its one-rule defect would go unreported.
        #
        # That arrangement is *also* the nested-rule defect — a `##` rule under
        # a `#` rule — so two errors are correct here, and the two assertions
        # below are what keep this test about the first of them.
        text = ONE_RULE_CHAPTER.replace(
            "# Summary", "## DMG-004 — Reading Resistance\n\nHow.\n\n# Summary"
        )
        errors = lint_ruleset.check_chapter_depth({"16-damage-system.md": text})
        assert len(errors) == 2
        assert any("Component Damage" in error for error in errors)
        assert any("nested under" in error for error in errors)

    def test_a_rule_written_three_levels_deep_is_reported(self):
        text = CHAPTERED.replace(
            "# Summary", "### DMG-004 — Three Deep\n\nHow.\n\n# Summary"
        )
        (error,) = lint_ruleset.check_chapter_depth({"16-damage-system.md": text})
        assert "three" in error

    def test_a_rule_nested_under_another_rule_is_reported(self):
        text = CHAPTERED.replace(
            "# Summary", "## DMG-004 — Nested\n\nHow.\n\n# Summary"
        )
        (error,) = lint_ruleset.check_chapter_depth({"16-damage-system.md": text})
        assert "nested under" in error

    def test_a_heading_inside_a_fenced_block_is_not_a_heading(self):
        # A document about document structure is the one most likely to show a
        # worked example of a heading. Read as real, the fenced `# Fake Chapter`
        # would close `# Component Damage` after one rule and fail a valid file.
        text = CHAPTERED.replace(
            "---\n\n## DMG-002",
            "```\n# Fake Chapter\n\n## DMG-999 — Fake\n```\n\n---\n\n## DMG-002",
        )
        assert lint_ruleset.check_chapter_depth({"16-damage-system.md": text}) == []
