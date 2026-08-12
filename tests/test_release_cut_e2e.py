"""The release cut, end to end, against a throwaway repository.

`system/ci-gates.md` ("Test Any Repo-Mutating Script in an Isolated Worktree")
is the reason this never runs in place: an early test of this script against a
real working directory, cleaned up with `git reset --hard`, wiped an unrelated
uncommitted fix. Here the repository is built in `tmp_path` and thrown away.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest
from conftest import commit_all, run_git

CHANGELOG = """# Changelog

All notable changes to the StudCraft ruleset.

# [Unreleased]

---

# [0.4.0] - 2026-08-01

- The previous release.
"""

DOCUMENT = """# 08-vehicles.md

**Version:** 0.4.0

# VEH-001 — Vehicle Footprint

A vehicle occupies whole studs.

---

> **Every Brick Matters.**
"""


@pytest.fixture
def released_repo(temp_repo: Path) -> Path:
    """A repository tagged v0.4.0, with one docs/ change committed after the tag."""
    (temp_repo / "docs").mkdir()
    (temp_repo / "docs" / "08-vehicles.md").write_text(DOCUMENT)
    (temp_repo / "CHANGELOG.md").write_text(CHANGELOG)
    commit_all(temp_repo, "The 0.4.0 state")
    run_git(temp_repo, "tag", "v0.4.0")

    (temp_repo / "docs" / "08-vehicles.md").write_text(
        DOCUMENT.replace("whole studs", "whole studs, measured on the grid")
    )
    commit_all(temp_repo, "docs(vehicles): measure VEH-001 on the grid")
    return temp_repo


def cut(repo: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(repo / "scripts" / "release_cut.py")],
        cwd=repo,
        capture_output=True,
        text=True,
    )


def test_a_docs_change_since_the_tag_cuts_a_minor_release(released_repo):
    result = cut(released_repo)

    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == "0.5.0"


def test_the_changelog_entry_is_built_from_the_commit_subjects(released_repo):
    cut(released_repo)

    changelog = (released_repo / "CHANGELOG.md").read_text()
    assert "# [0.5.0] - " in changelog
    assert "- docs(vehicles): measure VEH-001 on the grid" in changelog
    assert "# [0.4.0] - 2026-08-01" in changelog, "the previous entry must survive"


def test_every_version_header_is_rewritten(released_repo):
    cut(released_repo)

    assert "**Version:** 0.5.0" in (released_repo / "docs" / "08-vehicles.md").read_text()


def test_a_fresh_unreleased_section_is_opened_above_the_entry(released_repo):
    cut(released_repo)

    changelog = (released_repo / "CHANGELOG.md").read_text()
    assert changelog.index("# [Unreleased]") < changelog.index("# [0.5.0]")


def test_nothing_to_release_when_no_document_changed(temp_repo):
    (temp_repo / "docs").mkdir()
    (temp_repo / "docs" / "08-vehicles.md").write_text(DOCUMENT)
    (temp_repo / "CHANGELOG.md").write_text(CHANGELOG)
    commit_all(temp_repo, "The 0.4.0 state")
    run_git(temp_repo, "tag", "v0.4.0")

    result = cut(temp_repo)

    assert result.returncode != 0
    assert "Nothing to release" in result.stderr


class TestAHandWrittenUnreleasedSection:
    """`Docs must not edit CHANGELOG.md directly` only fires on a pull request
    that also touches docs/*.md, so text can reach this section. The cut used to
    replace it without a word."""

    @pytest.fixture
    def repo(self, released_repo: Path) -> Path:
        changelog = (released_repo / "CHANGELOG.md").read_text()
        (released_repo / "CHANGELOG.md").write_text(
            changelog.replace(
                "# [Unreleased]\n", "# [Unreleased]\n\n- a note somebody typed here\n"
            )
        )
        commit_all(released_repo, "chore: a hand-written changelog note")
        return released_repo

    def test_the_cut_stops(self, repo):
        result = cut(repo)
        assert result.returncode != 0
        assert "not empty" in result.stderr

    def test_the_note_is_still_there(self, repo):
        cut(repo)
        assert "a note somebody typed here" in (repo / "CHANGELOG.md").read_text()

    def test_no_version_header_was_touched(self, repo):
        cut(repo)
        assert "**Version:** 0.4.0" in (repo / "docs" / "08-vehicles.md").read_text()
