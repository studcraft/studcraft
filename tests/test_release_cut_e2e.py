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


class TestADocumentAddedBetweenCuts:
    """The cut is the only thing allowed to write a **Version:** header, so it is
    the only thing that can give one to a document created since the last cut.
    Before this, `DOC_VERSION_RE.subn` found nothing and the file was skipped —
    and the ruleset linter, which requires the header, failed forever.
    """

    NEW = """# 17-infantry.md

# INF-001 — Infantry Unit

An infantry model is a minifigure.

---

> **Every Brick Matters.**
"""

    def add(self, repo: Path) -> Path:
        doc = repo / "docs" / "17-infantry.md"
        doc.write_text(self.NEW)
        commit_all(repo, "docs(infantry): add the infantry document")
        return doc

    def test_the_cut_supplies_the_header(self, released_repo):
        doc = self.add(released_repo)
        cut(released_repo)
        assert "**Version:** 0.5.0" in doc.read_text()

    def test_exactly_one_line_is_added(self, released_repo):
        doc = self.add(released_repo)
        cut(released_repo)

        after = doc.read_text().splitlines()
        assert len(after) == len(self.NEW.splitlines()) + 1
        assert after[1] == "**Version:** 0.5.0"

    def test_the_title_still_comes_first(self, released_repo):
        doc = self.add(released_repo)
        cut(released_repo)
        assert doc.read_text().splitlines()[0] == "# 17-infantry.md"

    def test_a_document_defining_no_rules_is_left_alone(self, released_repo):
        glossary = "# 14-glossary.md\n\n## UB\n\nA volume.\n\n> **Every Brick Matters.**\n"
        doc = released_repo / "docs" / "14-glossary.md"
        doc.write_text(glossary)
        commit_all(released_repo, "docs(glossary): add an entry")

        cut(released_repo)

        assert doc.read_text() == glossary


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


class TestTheEntryListsOnlyTheRuleset:
    """A release exists because `docs/` changed, so its entry says what changed
    in `docs/`. v0.2.0's entry listed "Fix Gemfile.lock: bump pinned Bundler"
    and "Apply just-the-docs default layout" in the changelog of a tabletop
    wargame, and by the release after it three commits in four touched no rule.

    CHANGELOG.md is append-only in practice — no pull request may edit it — so
    an entry that lists the wrong thing stays wrong."""

    @pytest.fixture
    def mixed_repo(self, released_repo: Path) -> Path:
        """The docs/ commit from the fixture, with tooling commits either side."""
        (released_repo / "scripts").mkdir(exist_ok=True)
        (released_repo / "scripts" / "tool.py").write_text("# a tool\n")
        commit_all(released_repo, "Add a script nobody reading the rules cares about")

        (released_repo / "README.md").write_text("# Readme\n")
        commit_all(released_repo, "Fix Gemfile.lock: bump pinned Bundler to 2.5.6")
        return released_repo

    def test_a_commit_touching_docs_is_listed(self, mixed_repo):
        cut(mixed_repo)

        changelog = (mixed_repo / "CHANGELOG.md").read_text()
        assert "- docs(vehicles): measure VEH-001 on the grid" in changelog

    def test_a_commit_touching_no_document_is_not(self, mixed_repo):
        cut(mixed_repo)

        changelog = (mixed_repo / "CHANGELOG.md").read_text()
        assert "Add a script nobody reading the rules cares about" not in changelog
        assert "Gemfile.lock" not in changelog

    def test_the_release_still_happens(self, mixed_repo):
        """The tooling commits neither add to the entry nor block the cut."""
        result = cut(mixed_repo)

        assert result.returncode == 0, result.stderr
        assert result.stdout.strip() == "0.5.0"


class TestSeverityStillReadsEveryCommit:
    """A `**Bump:** major` marker is a claim about the release wherever it was
    written. Dropping a declared major because its commit touched no ruleset
    file is worse than listing one line too few: a version is permanent, and
    correcting it would mean rewriting history."""

    @pytest.fixture
    def flagged_elsewhere(self, released_repo: Path) -> Path:
        (released_repo / "scripts").mkdir(exist_ok=True)
        (released_repo / "scripts" / "tool.py").write_text("# a tool\n")
        commit_all(
            released_repo,
            "Change how a rule is read\n\n**Bump:** major\n",
        )
        return released_repo

    def test_the_marker_escalates_the_bump(self, flagged_elsewhere):
        result = cut(flagged_elsewhere)

        assert result.returncode == 0, result.stderr
        assert result.stdout.strip() == "1.0.0"

    def test_and_its_commit_is_still_not_listed(self, flagged_elsewhere):
        cut(flagged_elsewhere)

        changelog = (flagged_elsewhere / "CHANGELOG.md").read_text()
        assert "Change how a rule is read" not in changelog
        assert "- docs(vehicles): measure VEH-001 on the grid" in changelog
