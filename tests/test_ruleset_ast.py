"""`scripts/ruleset_ast.py` replaces four disagreeing regexes with one tree,
and every check built on it is only as trustworthy as the parse underneath —
`TestLosslessParse` is the one that has to hold before anything else here
means anything.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

import ruleset_ast
from repo import DOCS_DIR

DOCS = sorted(DOCS_DIR.glob("*.md"))


class TestLosslessParse:
    """Every document reassembles: every line is a heading line, a line inside
    exactly one block, or a blank line between blocks — never two of those,
    never none. `system/documentation-standards.md` names fifteen documents;
    this runs the same assertion over all fifteen.
    """

    @pytest.mark.parametrize("path", DOCS, ids=lambda p: p.name)
    def test_every_line_is_accounted_for_exactly_once(self, path: Path) -> None:
        text = path.read_text()
        lines = text.splitlines()
        document = ruleset_ast.parse_text(path.name, text)

        heading_lines: list[int] = []
        block_lines: list[int] = []

        for section in document.root.walk():
            if section.level:
                heading_lines.append(section.line)
            for block in section.blocks:
                block_lines.extend(range(block.line_start, block.line_end + 1))

        # Nothing is claimed twice — not by two blocks, and not by a block
        # that also thinks it is a heading.
        assert len(heading_lines) == len(set(heading_lines)), path.name
        assert len(block_lines) == len(set(block_lines)), path.name
        assert not (set(heading_lines) & set(block_lines)), path.name

        accounted = set(heading_lines) | set(block_lines)
        for lineno in range(1, len(lines) + 1):
            if lineno in accounted:
                continue
            assert lines[lineno - 1].strip() == "", (
                f"{path.name}:{lineno} is neither a heading line, inside a "
                f"block, nor blank — the parse dropped it: {lines[lineno - 1]!r}"
            )


class TestNesting:
    def test_hash_then_double_then_triple_nests_parent_child_grandchild(self):
        text = "# One\n\ntext\n\n## Two\n\ntext\n\n### Three\n\ntext\n"
        document = ruleset_ast.parse_text("t.md", text)

        (top,) = document.root.children
        (mid,) = top.children
        (leaf,) = mid.children

        assert (top.title, top.level) == ("One", 1)
        assert (mid.title, mid.level) == ("Two", 2)
        assert (leaf.title, leaf.level) == ("Three", 3)

    def test_a_skipped_level_still_nests(self):
        # A `###` following a `#` with no `##` between them is a child of the
        # `#`, not an error and not a sibling.
        text = "# One\n\n### Three\n\ntext\n"
        document = ruleset_ast.parse_text("t.md", text)

        (top,) = document.root.children
        (leaf,) = top.children
        assert leaf.title == "Three"
        assert leaf.level == 3

    def test_four_hashes_is_not_a_heading(self):
        text = "# One\n\n#### Deeper\n\nmore text\n"
        document = ruleset_ast.parse_text("t.md", text)

        (top,) = document.root.children
        assert top.children == []
        assert any(
            "#### Deeper" in line for block in top.blocks for line in block.lines
        )


class TestRuleHeadings:
    def test_a_rule_heading_is_split_into_its_parts(self):
        document = ruleset_ast.parse_text("t.md", "# MOVE-012 — Slopes\n\ntext\n")
        (section,) = document.root.children

        assert section.is_rule
        assert section.rule_id == "MOVE-012"
        assert section.rule_prefix == "MOVE"
        assert section.rule_number == 12
        assert section.rule_title == "Slopes"

    def test_no_em_dash_is_not_a_rule(self):
        document = ruleset_ast.parse_text("t.md", "## DMG-005 States\n\ntext\n")
        (section,) = document.root.children

        assert not section.is_rule
        assert section.rule_id is None


class TestFences:
    def test_a_heading_inside_a_fence_does_not_close_its_section(self):
        text = "# One\n\n```\n# Fake Chapter\n```\n\n## Two\n\ntext\n"
        document = ruleset_ast.parse_text("t.md", text)

        (top,) = document.root.children
        (fence,) = top.blocks
        assert fence.kind == "fence"
        assert "# Fake Chapter" in fence.lines

        (two,) = top.children
        assert two.title == "Two"

    def test_a_dashes_line_inside_a_fence_is_not_a_break(self):
        text = "# One\n\n```\n---\n```\n"
        document = ruleset_ast.parse_text("t.md", text)

        (top,) = document.root.children
        (block,) = top.blocks
        assert block.kind == "fence"
        assert "---" in block.lines


class TestLineEndCoversDescendants:
    """The regression test for the bug that motivated this module: a rule
    printed without its own sub-sections, because the old pattern ended a
    rule's body at *any* heading, including its own.

    Which rules in `docs/` carry sub-sections is a property of the ruleset on
    the day it is read, so the behaviour is pinned against a document written
    here and the invariant is pinned against all fifteen.
    """

    def test_a_rules_span_reaches_past_its_own_sub_sections(self):
        text = (
            "# DEP-001 — With Scenarios\n\nintro\n\n"
            "## Patrol\n\nsmall\n\n"
            "## Massive Battle\n\nthe last line of the rule\n\n"
            "# DEP-002 — After\n\nnext\n"
        )
        document = ruleset_ast.parse_text("t.md", text)
        rule, _after = document.root.children

        assert [child.title for child in rule.children] == ["Patrol", "Massive Battle"]

        last = rule.children[-1]
        assert rule.line_end == last.line_end
        assert rule.line_end > last.line

    @pytest.mark.parametrize("path", DOCS, ids=lambda p: p.name)
    def test_no_section_ends_before_its_last_descendant(self, path: Path) -> None:
        document = ruleset_ast.parse(path)
        for section in document.root.walk():
            if not section.children:
                continue
            assert section.line_end == section.children[-1].line_end, (
                f"{path.name}:{section.line} {section.title!r} ends at "
                f"{section.line_end}, before its last sub-section does"
            )


class TestBodyText:
    def test_strips_trailing_blank_lines_and_one_trailing_break(self):
        text = "# One\n\ncontent line\n\n---\n\n# Two\n\nmore\n"
        document = ruleset_ast.parse_text("t.md", text)
        (top, _two) = document.root.children

        assert top.body_text(document.lines) == "\ncontent line"

    def test_does_not_strip_a_break_followed_by_more_content(self):
        text = "# One\n\nintro\n\n---\n\nreal content after the break\n\n# Two\n\nmore\n"
        document = ruleset_ast.parse_text("t.md", text)
        (top, _two) = document.root.children

        assert top.body_text(document.lines) == (
            "\nintro\n\n---\n\nreal content after the break"
        )


class TestProseLines:
    def test_excludes_fenced_content(self):
        # A citation scanner run over prose_lines() can never see a rule ID
        # that only a fenced example contains. Written here rather than read
        # out of `docs/`: which document holds a fence today is not what this
        # is about.
        text = (
            "# DMG-001 — Fenced Example\n\nReal prose, citing DMG-015.\n\n"
            "```\nFenced prose, citing DMG-999.\n```\n\nMore real prose.\n"
        )
        document = ruleset_ast.parse_text("t.md", text)
        assert any("DMG-999" in line for line in document.lines)

        prose = document.root.prose_lines(document.lines)
        assert not any("DMG-999" in line for line in prose)
        assert any("DMG-015" in line for line in prose)

    @pytest.mark.parametrize("path", DOCS, ids=lambda p: p.name)
    def test_drops_the_fenced_lines_of_a_real_document_and_nothing_else(
        self, path: Path
    ) -> None:
        document = ruleset_ast.parse(path)
        fenced = {
            number
            for section in document.root.walk()
            for block in section.blocks
            if block.kind == "fence"
            for number in range(block.line_start, block.line_end + 1)
        }

        prose = document.root.prose_lines(document.lines)
        assert len(prose) == len(document.lines) - len(fenced), path.name


class TestToDict:
    @pytest.mark.parametrize("path", DOCS, ids=lambda p: p.name)
    def test_survives_json_dumps(self, path: Path) -> None:
        document = ruleset_ast.parse(path)
        json.dumps(document.to_dict())


class TestGlossaryNeedsNoSpecialCase:
    def test_terms_come_out_as_level_two_children_of_one_level_one_section(self):
        document = ruleset_ast.parse(DOCS_DIR / "14-glossary.md")

        assert len(document.root.children) == 1
        glossary = document.root.children[0]
        assert glossary.level == 1
        assert len(glossary.children) > 40
        assert all(child.level == 2 for child in glossary.children)
        assert all(not child.is_rule for child in glossary.children)
