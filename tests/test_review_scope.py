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

import pytest

import review_scope


@pytest.fixture(autouse=True)
def not_a_placement(monkeypatch):
    """No test here runs on an image-placement branch unless it says it does.

    `scope` asks git which images the branch touches, so without this the
    answer would come from whatever branch the suite happens to run on.
    """
    monkeypatch.setattr(review_scope, "placement_images", lambda: [])

INDEX = {
    "documents": {
        "aaa.md": {"rules": ["AAA-001"], "prefixes": ["AAA"], "outline": []},
        "bbb.md": {"rules": ["BBB-002"], "prefixes": ["BBB"], "outline": []},
        "ccc.md": {"rules": ["CCC-003"], "prefixes": ["CCC"], "outline": []},
    },
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


class TestDeltas:
    def test_a_delta_the_change_ships_is_listed(self, tmp_path, monkeypatch, capsys):
        change = make_change(tmp_path, monkeypatch, "Rewrites AAA-001.")
        spec = tmp_path / "changes" / change / "specs" / "a-capability"
        spec.mkdir(parents=True)
        (spec / "spec.md").write_text("## MODIFIED Requirements\n")

        review_scope.scope(change, INDEX)

        out = capsys.readouterr().out
        assert "Deltas — 1 spec delta(s)" in out
        assert "specs/a-capability/spec.md" in out

    def test_a_superseded_delta_is_listed_too(self, tmp_path, monkeypatch, capsys):
        # A superseded delta is the one nobody opens, because the change that
        # owns the requirement now is somewhere else entirely.
        change = make_change(tmp_path, monkeypatch, "Rewrites AAA-001.")
        spec = tmp_path / "changes" / change / "specs-superseded" / "a-capability"
        spec.mkdir(parents=True)
        (spec / "spec.md").write_text("Superseded.\n")

        review_scope.scope(change, INDEX)

        assert "specs-superseded/a-capability/spec.md" in capsys.readouterr().out

    def test_a_change_shipping_no_delta_says_so(self, tmp_path, monkeypatch, capsys):
        change = make_change(tmp_path, monkeypatch, "Rewrites AAA-001.")
        review_scope.scope(change, INDEX)

        out = capsys.readouterr().out
        assert "Deltas — 0 spec delta(s)" in out

    def test_a_change_naming_no_live_rule_still_lists_its_delta(self, tmp_path, monkeypatch, capsys):
        # The rule half and the delta half are printed by different branches.
        # A change whose rules were all retired has no rules to list and a delta
        # that still has to be read.
        change = make_change(tmp_path, monkeypatch, "Prose only, naming AAA-009.")
        spec = tmp_path / "changes" / change / "specs" / "a-capability"
        spec.mkdir(parents=True)
        (spec / "spec.md").write_text("## MODIFIED Requirements\n")

        review_scope.scope(change, INDEX)

        out = capsys.readouterr().out
        assert "Names no rule that exists" in out
        assert "specs/a-capability/spec.md" in out
        assert 'git grep -n "AAA-009"' in out


class TestDeadIds:
    def test_a_retired_id_under_a_real_prefix_is_listed(self, tmp_path, monkeypatch, capsys):
        change = make_change(tmp_path, monkeypatch, "Retires AAA-009 and rewrites AAA-001.")
        review_scope.scope(change, INDEX)

        out = capsys.readouterr().out
        assert 'git grep -n "AAA-009"' in out

    def test_an_illustration_prefix_is_not_listed(self, tmp_path, monkeypatch, capsys):
        # ZZZ names nothing by construction, so grepping it is noise — and a
        # section of noise is a section an auditor learns to skim.
        change = make_change(tmp_path, monkeypatch, "Illustrated with ZZZ-001, and rewrites AAA-001.")
        review_scope.scope(change, INDEX)

        out = capsys.readouterr().out
        assert "ZZZ-001" not in out

    def test_a_high_number_under_a_real_prefix_survives(self, tmp_path, monkeypatch, capsys):
        # Deliberate: an invented number under a real prefix is a sanctioned
        # illustration, and so is every genuinely retired number. Nothing tells
        # them apart, and dropping a real retirement is the costlier mistake.
        change = make_change(tmp_path, monkeypatch, "Illustrated with AAA-099, and rewrites AAA-001.")
        review_scope.scope(change, INDEX)

        assert 'git grep -n "AAA-099"' in capsys.readouterr().out

    def test_a_live_rule_is_not_listed_as_retired(self, tmp_path, monkeypatch, capsys):
        change = make_change(tmp_path, monkeypatch, "Rewrites AAA-001.")
        review_scope.scope(change, INDEX)

        out = capsys.readouterr().out
        assert "Retired IDs — 0 named here" in out


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


class TestPlacementBanner:
    """An auditor raised on a placement is told so by the script, not by a reader.

    This is the one case the `add-image` skill cannot reach: a session that
    raised an auditor without ever invoking it. Both auditors run this script
    first, so it is the last place the narrow brief can still arrive.
    """

    def placement(self, monkeypatch, images=("assets/images/cmp-018-clear-opening.png",)):
        monkeypatch.setattr(review_scope, "placement_images", lambda: list(images))

    def test_the_banner_leads_the_output(self, tmp_path, monkeypatch, capsys):
        change = make_change(tmp_path, monkeypatch, "This change places CMP-018's image.")
        self.placement(monkeypatch)

        review_scope.scope(change, INDEX)
        out = capsys.readouterr().out

        assert out.index("image placement") < out.index("# Review scope")
        assert "cmp-018-clear-opening.png" in out

    def test_it_names_the_agent_that_must_return(self, tmp_path, monkeypatch, capsys):
        change = make_change(tmp_path, monkeypatch, "This change places CMP-018's image.")
        self.placement(monkeypatch)

        review_scope.scope(change, INDEX)
        out = capsys.readouterr().out

        assert "ruleset-auditor — STOP" in out
        assert "without auditing" in out

    def test_it_carries_the_two_questions_verbatim(self, tmp_path, monkeypatch, capsys):
        change = make_change(tmp_path, monkeypatch, "This change places CMP-018's image.")
        self.placement(monkeypatch)

        review_scope.scope(change, INDEX)
        out = capsys.readouterr().out

        assert "Why text alone is not enough" in out
        assert "the embed line, the image file and this directory" in out
        assert ".claude/skills/add-image" in out

    def test_an_ordinary_change_gets_no_banner(self, tmp_path, monkeypatch, capsys):
        change = make_change(tmp_path, monkeypatch, "This change rewrites AAA-001.")

        review_scope.scope(change, INDEX)
        out = capsys.readouterr().out

        assert "image placement" not in out
        assert "STOP" not in out

    def test_the_checklist_still_prints_under_a_banner(self, tmp_path, monkeypatch, capsys):
        """The banner narrows what an answer says, never which lines are answered."""
        change = make_change(tmp_path, monkeypatch, "This change places CMP-018's image.")
        self.placement(monkeypatch)

        review_scope.scope(change, INDEX)
        out = capsys.readouterr().out

        for number, item in enumerate(review_scope.CHECKLIST, start=1):
            assert f"{number:2d}. [ ] {item}" in out
