"""`scripts/repo.py` holds what several scripts would otherwise each spell out.
A wrong answer here is wrong in five places at once.
"""

from __future__ import annotations

import repo


class TestRulePatterns:
    def test_a_rule_header_yields_its_prefix_and_number(self):
        assert repo.RULE_HEADER_RE.findall("# VEH-013 — Vehicle Weapons\n") == [("VEH", "013")]

    def test_a_second_level_header_counts_too(self):
        assert repo.RULE_HEADER_RE.findall("## DMG-004 — Damage Roll\n") == [("DMG", "004")]

    def test_a_hyphen_is_not_an_em_dash(self):
        assert repo.RULE_HEADER_RE.findall("# VEH-013 - Vehicle Weapons\n") == []

    def test_a_heading_that_is_not_a_rule_is_not_matched(self):
        assert repo.RULE_HEADER_RE.findall("# Summary\n") == []

    def test_ids_are_found_wherever_they_appear(self):
        text = "See `08-vehicles.md`, VEH-013 and WPN-021 for the chain."
        assert repo.RULE_ID_RE.findall(text) == ["VEH-013", "WPN-021"]

    def test_a_body_ends_at_the_next_heading(self):
        assert repo.HEADING_RE.match("## Summary")
        assert not repo.HEADING_RE.match("### Scenario: something")
        assert not repo.HEADING_RE.match("Ordinary prose.")


class TestUnarchivedChanges:
    def test_the_archive_is_not_a_change(self, tmp_path, monkeypatch):
        monkeypatch.setattr(repo, "CHANGES_DIR", tmp_path)
        (tmp_path / "archive").mkdir()
        (tmp_path / "measure-on-the-grid").mkdir()

        assert repo.unarchived_changes() == ["measure-on-the-grid"]

    def test_a_loose_file_is_not_a_change(self, tmp_path, monkeypatch):
        monkeypatch.setattr(repo, "CHANGES_DIR", tmp_path)
        (tmp_path / "README.md").write_text("not a change\n")
        (tmp_path / "a-change").mkdir()

        assert repo.unarchived_changes() == ["a-change"]

    def test_the_order_is_stable(self, tmp_path, monkeypatch):
        monkeypatch.setattr(repo, "CHANGES_DIR", tmp_path)
        for name in ("c-change", "a-change", "b-change"):
            (tmp_path / name).mkdir()

        assert repo.unarchived_changes() == ["a-change", "b-change", "c-change"]

    def test_a_missing_directory_is_not_an_error(self, tmp_path, monkeypatch):
        monkeypatch.setattr(repo, "CHANGES_DIR", tmp_path / "nothing-here")
        assert repo.unarchived_changes() == []


class TestGit:
    def test_it_returns_the_exit_code_and_trimmed_output(self):
        code, out = repo.git("rev-parse", "--show-toplevel")
        assert code == 0
        assert out == str(repo.REPO_ROOT)

    def test_a_failing_command_reports_a_non_zero_code(self):
        code, _ = repo.git("rev-parse", "not-a-real-revision")
        assert code != 0

    def test_output_on_failure_is_not_a_result(self):
        # `git rev-parse` echoes its argument to stdout while failing, so the
        # exit code is the only thing a caller may read. Every caller here does.
        code, out = repo.git("rev-parse", "not-a-real-revision")
        assert code != 0 and out == "not-a-real-revision"
