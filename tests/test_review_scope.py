"""`scripts/review_scope.py` computes what a review reads, so a review of one
change reads the same text twice.

What is pinned here is the part a prompt used to decide: that the citers of a
changed rule are included, that a Summary and a glossary entry are listed for
every document and term touched, and that the checklist prints whole. A
checklist that silently loses a line is the defect the script exists to remove.

The index is built by hand rather than read from `.studcraft/index.json`, so
these tests do not move when `docs/` does.
"""

from __future__ import annotations

import review_scope

INDEX = {
    "documents": {},
    "rules": {
        "AAA-001": {
            "id": "AAA-001", "doc": "aaa.md", "line": 10, "line_end": 18,
            "title": "Named By The Change", "summary": "",
            "cites": [], "cited_by": ["BBB-002"],
        },
        "BBB-002": {
            "id": "BBB-002", "doc": "bbb.md", "line": 24, "line_end": 28,
            "title": "Cites The Changed Rule", "summary": "",
            "cites": ["AAA-001"], "cited_by": [],
        },
        "CCC-003": {
            "id": "CCC-003", "doc": "ccc.md", "line": 30, "line_end": 34,
            "title": "Unrelated", "summary": "",
            "cites": [], "cited_by": [],
        },
    },
    "glossary": [
        {"term": "Named Term", "line": 40, "line_end": 44, "cites": ["AAA-001"]},
        {"term": "Unrelated Term", "line": 50, "line_end": 54, "cites": ["CCC-003"]},
    ],
}


def make_change(tmp_path, monkeypatch, body: str, name: str = "a-change"):
    """A change directory holding one artifact, with CHANGES_DIR pointed at it."""
    changes = tmp_path / "changes"
    (changes / name).mkdir(parents=True)
    (changes / name / "proposal.md").write_text(body)
    monkeypatch.setattr(review_scope, "CHANGES_DIR", changes)
    return name


class TestScope:
    def test_a_rule_the_change_names_is_read_in_full(self, tmp_path, monkeypatch, capsys):
        change = make_change(tmp_path, monkeypatch, "This change rewrites AAA-001.")
        assert review_scope.scope(change, INDEX) == 0

        out = capsys.readouterr().out
        assert "Read in full — 1 rule(s)" in out
        assert "AAA-001" in out

    def test_a_rule_that_cites_a_changed_rule_is_read_also(self, tmp_path, monkeypatch, capsys):
        change = make_change(tmp_path, monkeypatch, "This change rewrites AAA-001.")
        review_scope.scope(change, INDEX)

        out = capsys.readouterr().out
        assert "Read also — 1 rule(s)" in out
        # BBB-002 is nowhere in the change's own text. Nothing but the inverse
        # citation graph reveals it, which is the half a hand-written prompt drops.
        assert "BBB-002" in out

    def test_a_citer_the_change_also_names_is_not_listed_twice(self, tmp_path, monkeypatch, capsys):
        change = make_change(tmp_path, monkeypatch, "Rewrites AAA-001 and BBB-002 together.")
        review_scope.scope(change, INDEX)

        out = capsys.readouterr().out
        assert "Read in full — 2 rule(s)" in out
        assert "Read also — 0 rule(s)" in out

    def test_only_the_documents_whose_rules_changed_get_a_summary(self, tmp_path, monkeypatch, capsys):
        change = make_change(tmp_path, monkeypatch, "This change rewrites AAA-001.")
        review_scope.scope(change, INDEX)

        out = capsys.readouterr().out
        assert "aaa.md  # Summary" in out
        # bbb.md holds a citer, not a changed rule: its Summary restates BBB-002,
        # which this change does not touch.
        assert "bbb.md  # Summary" not in out

    def test_a_glossary_entry_pointing_at_a_changed_rule_is_listed(self, tmp_path, monkeypatch, capsys):
        change = make_change(tmp_path, monkeypatch, "This change rewrites AAA-001.")
        review_scope.scope(change, INDEX)

        out = capsys.readouterr().out
        assert "Named Term" in out
        assert "Unrelated Term" not in out

    def test_a_change_naming_no_live_rule_still_prints_the_checklist(self, tmp_path, monkeypatch, capsys):
        change = make_change(tmp_path, monkeypatch, "Prose only, and ZZZ-999 does not exist.")
        assert review_scope.scope(change, INDEX) == 0

        out = capsys.readouterr().out
        assert "Names no rule that exists" in out
        assert "Checklist" in out

    def test_an_unknown_change_names_the_ones_that_exist(self, tmp_path, monkeypatch, capsys):
        make_change(tmp_path, monkeypatch, "Anything.", name="a-change")
        assert review_scope.scope("not-a-change", INDEX) == 1

        assert "a-change" in capsys.readouterr().err


class TestChecklist:
    def test_every_item_prints_numbered_and_unticked(self, tmp_path, monkeypatch, capsys):
        change = make_change(tmp_path, monkeypatch, "This change rewrites AAA-001.")
        review_scope.scope(change, INDEX)

        out = capsys.readouterr().out
        for number, item in enumerate(review_scope.CHECKLIST, start=1):
            assert f"{number:2d}. [ ] {item}" in out

    def test_the_checklist_is_not_empty(self):
        # A checklist that emptied itself would still let every test above pass.
        assert len(review_scope.CHECKLIST) >= 10
