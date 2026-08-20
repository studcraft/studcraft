"""`scripts/rule.py` has carried no tests until now. This covers `cmd_doc`
alone — the command this change touches. Backfilling `show`, `refs`,
`neighbors`, `touched`, `orphans` and `glossary` is its own change; mixing it
in here would bury the diff that motivated this file.

A small index dict is built by hand rather than reading the real
`.studcraft/index.json`, so these tests do not move when `docs/` does.
"""

from __future__ import annotations

import rule

INDEX = {
    "documents": {
        "test.md": {
            "rules": ["AAA-001", "BBB-002", "BBB-003"],
            "prefixes": ["AAA", "BBB"],
            "outline": [
                {"level": 1, "title": "Purpose", "line": 5, "rule_id": None},
                {"level": 1, "title": "Standalone", "line": 10, "rule_id": "AAA-001"},
                {"level": 1, "title": "A Chapter", "line": 20, "rule_id": None},
                {"level": 2, "title": "In Chapter", "line": 24, "rule_id": "BBB-002"},
                {"level": 2, "title": "Also In Chapter", "line": 30, "rule_id": "BBB-003"},
            ],
        },
    },
    "rules": {
        "AAA-001": {
            "id": "AAA-001", "doc": "test.md", "line": 10, "line_end": 18,
            "title": "Standalone",
            "summary": "A standalone rule that opens with a real sentence.",
            "cites": [], "cited_by": [],
        },
        "BBB-002": {
            "id": "BBB-002", "doc": "test.md", "line": 24, "line_end": 28,
            "title": "In Chapter", "summary": "",
            "cites": [], "cited_by": ["AAA-001"],
        },
        "BBB-003": {
            "id": "BBB-003", "doc": "test.md", "line": 30, "line_end": 34,
            "title": "Also In Chapter",
            "summary": "Cited by nothing, but still printed.",
            "cites": [], "cited_by": [],
        },
    },
    "glossary": [],
}


class TestCmdDoc:
    def test_a_chapter_prints_with_the_number_of_rules_under_it(self, capsys):
        rule.cmd_doc(INDEX, "test.md")
        out = capsys.readouterr().out
        assert "# A Chapter  [2 rules]" in out

    def test_a_hash_section_holding_no_rules_prints_as_prose(self, capsys):
        rule.cmd_doc(INDEX, "test.md")
        out = capsys.readouterr().out
        assert "# Purpose  [prose]" in out

    def test_a_rule_prints_its_summary_and_an_empty_summary_prints_no_blank_line(self, capsys):
        rule.cmd_doc(INDEX, "test.md")
        lines = capsys.readouterr().out.splitlines()

        aaa = next(i for i, line in enumerate(lines) if "AAA-001" in line)
        assert "standalone rule" in lines[aaa + 1]

        # BBB-002's summary is empty, so nothing indented follows its own
        # line — the next line printed is BBB-003's, not a blank line.
        bbb002 = next(i for i, line in enumerate(lines) if "BBB-002" in line)
        assert "BBB-003" in lines[bbb002 + 1]

    def test_a_rule_inside_a_chapter_is_indented_further_than_one_outside(self, capsys):
        rule.cmd_doc(INDEX, "test.md")
        lines = capsys.readouterr().out.splitlines()

        standalone = next(line for line in lines if "AAA-001" in line)
        nested = next(line for line in lines if "BBB-002" in line)

        def indent(text: str) -> int:
            return len(text) - len(text.lstrip(" "))

        assert indent(nested) > indent(standalone)

    def test_the_hash_prefix_states_heading_level_like_parse_ruleset_py(self, capsys):
        """A chapter and a rule outside one are written at `#` in the
        documents, so both print with one hash. A rule inside a chapter is
        written at `##`, so it prints with two — the same notation
        `scripts/parse_ruleset.py` prints for the same headings.
        """
        rule.cmd_doc(INDEX, "test.md")
        lines = capsys.readouterr().out.splitlines()

        chapter = next(line for line in lines if "A Chapter" in line)
        standalone = next(line for line in lines if "AAA-001" in line)
        nested = next(line for line in lines if "BBB-002" in line)

        assert "# A Chapter" in chapter and "## A Chapter" not in chapter
        assert "# AAA-001" in standalone and "## AAA-001" not in standalone
        assert "## BBB-002" in nested
