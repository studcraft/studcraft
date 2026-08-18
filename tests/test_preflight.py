"""`preflight.py` mirrors four CI gates so a push is not the first thing to
report a red one. A mirror that disagrees with the gate it mirrors is worse than
no mirror: it says the pull request will pass.

Each check is fed a branch name and a list of changed paths, which is what the
workflow gets from the base/head pair.
"""

from __future__ import annotations

import preflight
import pytest

DOC = "docs/08-vehicles.md"
CHANGE = "openspec/changes/measure-on-the-grid/tasks.md"


def status(result) -> str:
    return result.status


class TestBranchName:
    def test_a_working_branch_is_lowercase_kebab_case(self):
        assert status(preflight.check_branch_name("measure-on-the-grid", [])) == preflight.PASS

    def test_uppercase_is_refused(self):
        assert status(preflight.check_branch_name("Measure-On-The-Grid", [])) == preflight.FAIL

    def test_an_underscore_is_refused(self):
        assert status(preflight.check_branch_name("measure_on_the_grid", [])) == preflight.FAIL

    def test_a_full_release_name_is_accepted(self):
        assert status(preflight.check_branch_name("release/v1.2.3", [])) == preflight.PASS

    def test_a_partial_release_name_is_refused(self):
        # `release/v9` is the shape that once bought a free pass through three
        # gates on the name alone.
        assert status(preflight.check_branch_name("release/v9", [])) == preflight.FAIL

    def test_an_archive_batch_name_is_accepted(self):
        result = preflight.check_branch_name("archive/batch-2026-08-12-123", [])
        assert status(result) == preflight.PASS

    def test_a_ruleset_branch_must_carry_its_change_name(self):
        result = preflight.check_branch_name("something-else", [DOC, CHANGE])
        assert status(result) == preflight.FAIL
        assert "measure-on-the-grid" in result.detail[0]

    def test_a_ruleset_branch_named_for_its_change_passes(self):
        result = preflight.check_branch_name("measure-on-the-grid", [DOC, CHANGE])
        assert status(result) == preflight.PASS

    def test_on_main_the_convention_does_not_apply(self):
        assert status(preflight.check_branch_name("main", [])) == preflight.SKIP


class TestChangelogIsHandsOff:
    def test_a_ruleset_branch_may_not_touch_the_changelog(self):
        result = preflight.check_changelog("measure-on-the-grid", [DOC, "CHANGELOG.md"])
        assert status(result) == preflight.FAIL

    def test_a_ruleset_branch_that_leaves_it_alone_passes(self):
        assert status(preflight.check_changelog("measure-on-the-grid", [DOC])) == preflight.PASS

    def test_a_release_branch_is_checked_in_ci_only(self):
        result = preflight.check_changelog("release/v1.2.3", [DOC, "CHANGELOG.md"])
        assert status(result) == preflight.SKIP


class TestArchiveIsSeparateFromApply:
    def test_specs_outside_an_archive_branch_are_refused(self):
        result = preflight.check_archive_separate(
            "measure-on-the-grid", ["openspec/specs/damage-resolution/spec.md"]
        )
        assert status(result) == preflight.FAIL

    def test_an_archive_branch_may_not_touch_the_ruleset(self):
        result = preflight.check_archive_separate(
            "archive/batch-2026-08-12-1", ["openspec/specs/x/spec.md", DOC]
        )
        assert status(result) == preflight.FAIL

    def test_an_archive_branch_may_not_touch_anything_outside_openspec(self):
        result = preflight.check_archive_separate(
            "archive/batch-2026-08-12-1", ["openspec/specs/x/spec.md", "README.md"]
        )
        assert status(result) == preflight.FAIL

    def test_an_archive_branch_that_archives_nothing_is_refused(self):
        result = preflight.check_archive_separate(
            "archive/batch-2026-08-12-1", ["openspec/changes/still-live/tasks.md"]
        )
        assert status(result) == preflight.FAIL

    def test_moving_a_delta_free_change_is_archiving(self):
        """A change that carried no capability delta writes no spec when it is
        archived; its directory still moves. Requiring a spec write made such a
        change impossible to archive alone, and let it through only when a
        sibling in the same batch happened to carry a delta.
        """
        result = preflight.check_archive_separate(
            "archive/batch-2026-08-12-1", ["openspec/changes/archive/x/tasks.md"]
        )
        assert status(result) == preflight.PASS

    def test_an_archive_only_branch_passes(self):
        result = preflight.check_archive_separate(
            "archive/batch-2026-08-12-1",
            ["openspec/specs/x/spec.md", "openspec/changes/archive/x/tasks.md"],
        )
        assert status(result) == preflight.PASS

    def test_a_branch_touching_no_specs_passes(self):
        assert status(preflight.check_archive_separate("a-branch", [DOC])) == preflight.PASS


class TestDocsRequireAProposal:
    @pytest.fixture
    def proposal(self, tmp_path, monkeypatch):
        """A complete change directory, and a hook to make one incomplete."""
        monkeypatch.setattr(preflight, "REPO_ROOT", tmp_path)
        directory = tmp_path / "openspec" / "changes" / "measure-on-the-grid"
        directory.mkdir(parents=True)
        for artifact in preflight.PROPOSAL_ARTIFACTS:
            (directory / artifact).write_text("...\n")
        return directory

    def test_a_ruleset_change_with_no_proposal_is_refused(self, proposal):
        result = preflight.check_proposal("a-branch", [DOC])
        assert status(result) == preflight.FAIL

    def test_two_proposals_in_one_branch_are_refused(self, proposal):
        result = preflight.check_proposal(
            "a-branch", [DOC, CHANGE, "openspec/changes/another/tasks.md"]
        )
        assert status(result) == preflight.FAIL
        assert "another" in result.detail[0]

    def test_a_complete_proposal_passes(self, proposal):
        assert status(preflight.check_proposal("a-branch", [DOC, CHANGE])) == preflight.PASS

    def test_a_missing_artifact_is_refused(self, proposal):
        (proposal / "design.md").unlink()
        result = preflight.check_proposal("a-branch", [DOC, CHANGE])
        assert status(result) == preflight.FAIL
        assert "design.md" in result.detail[0]

    def test_an_archive_directory_is_not_a_proposal(self, proposal):
        result = preflight.check_proposal("a-branch", ["openspec/changes/archive/old/tasks.md"])
        assert status(result) == preflight.PASS
