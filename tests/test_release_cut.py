"""The release cut is the only thing that writes `CHANGELOG.md` and the
`**Version:**` headers, and it runs unattended from a workflow. Nobody reads its
output unless it fails, so what it does when the input is odd matters as much as
what it does when the input is ordinary.
"""

from __future__ import annotations

import release_cut


class TestBumping:
    def test_a_minor_bump_resets_the_patch(self):
        assert release_cut.bump_version("0.4.3", "minor") == "0.5.0"

    def test_a_major_bump_resets_both(self):
        assert release_cut.bump_version("1.4.3", "major") == "2.0.0"

    def test_a_patch_bump_moves_the_last_number(self):
        assert release_cut.bump_version("1.4.3", "patch") == "1.4.4"


class TestSeverity:
    def test_the_default_is_minor(self, monkeypatch):
        monkeypatch.delenv("RELEASE_SEVERITY", raising=False)
        commits = [("sha", "docs(vehicles): reword VEH-004", "")]
        assert release_cut.resolve_severity(commits) == "minor"

    def test_a_commit_body_can_flag_itself_as_breaking(self, monkeypatch):
        monkeypatch.delenv("RELEASE_SEVERITY", raising=False)
        commits = [("sha", "subject", "Body text\n\n**Bump:** major\n")]
        assert release_cut.resolve_severity(commits) == "major"

    def test_an_explicit_override_wins_over_the_marker(self, monkeypatch):
        monkeypatch.setenv("RELEASE_SEVERITY", "patch")
        commits = [("sha", "subject", "**Bump:** major\n")]
        assert release_cut.resolve_severity(commits) == "patch"

    def test_auto_is_not_an_override(self, monkeypatch):
        monkeypatch.setenv("RELEASE_SEVERITY", "auto")
        assert release_cut.resolve_severity([("sha", "subject", "")]) == "minor"


class TestSplittingTheChangelog:
    CHANGELOG = (
        "# Changelog\n\nPreamble.\n\n"
        "# [Unreleased]\n\n"
        "# [0.4.0] - 2026-08-01\n\n- something\n"
    )

    def test_the_three_parts_reassemble_into_the_original(self):
        before, unreleased, tail = release_cut.split_unreleased(self.CHANGELOG)
        assert before + release_cut.UNRELEASED_HEADER + unreleased + tail == self.CHANGELOG

    def test_an_empty_unreleased_section_has_no_content(self):
        _, unreleased, _ = release_cut.split_unreleased(self.CHANGELOG)
        assert unreleased.strip() == ""

    def test_the_separator_a_cut_leaves_behind_is_not_content(self):
        # Every cut writes `---` under the header. That is furniture, not a note.
        assert release_cut.unreleased_content("\n\n---\n\n") == ""

    def test_a_typed_line_is_content(self):
        assert release_cut.unreleased_content("\n- a note\n\n---\n") == "- a note"

    def test_a_hand_written_note_lands_in_the_middle_part(self):
        changelog = self.CHANGELOG.replace(
            "# [Unreleased]\n\n", "# [Unreleased]\n\n- a hand-written note\n\n"
        )
        _, unreleased, _ = release_cut.split_unreleased(changelog)
        assert "hand-written note" in unreleased
