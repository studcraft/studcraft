"""`open_pr.py` end to end, against a throwaway repository and a bare remote.

This is the script that exists so the BLOCKER rules in
`system/repository-strategy.md` stop being instructions an agent is trusted to
follow — no `git add -A`, no force-push, one commit per run, the staged set
checked against the given set. Those are the properties tested here.

No pull request is opened: every case passes `--existing-pr` with no body file,
which is the one path through the script that reaches neither `gh` nor a
network.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest
from conftest import commit_all, run_git


@pytest.fixture
def work_repo(temp_repo: Path, bare_remote: Path, tmp_path: Path) -> Path:
    (temp_repo / "docs").mkdir()
    (temp_repo / "docs" / "08-vehicles.md").write_text("# VEH-001\n\nFirst.\n")
    (temp_repo / "docs" / "10-weapons.md").write_text("# WPN-001\n\nFirst.\n")
    commit_all(temp_repo, "Initial state")

    run_git(temp_repo, "remote", "add", "origin", str(bare_remote))
    run_git(temp_repo, "push", "-u", "origin", "main")
    run_git(temp_repo, "checkout", "-b", "measure-on-the-grid")

    (tmp_path / "message.txt").write_text(
        "docs(vehicles): measure VEH-001 on the grid\n\nBody.\n"
    )
    return temp_repo


def open_pr(repo: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(repo / "scripts" / "open_pr.py"), *args],
        cwd=repo,
        capture_output=True,
        text=True,
    )


def default_args(tmp_path: Path, *paths: str) -> list[str]:
    return [
        "--branch", "measure-on-the-grid",
        "--message-file", str(tmp_path / "message.txt"),
        "--existing-pr", "1",
        *[arg for path in paths for arg in ("--path", path)],
    ]


def committed_paths(repo: Path) -> list[str]:
    return run_git(repo, "show", "--name-only", "--format=", "HEAD").split()


class TestTheOrdinaryRun:
    def test_only_the_named_path_is_committed(self, work_repo, tmp_path):
        (work_repo / "docs" / "08-vehicles.md").write_text("# VEH-001\n\nSecond.\n")
        (work_repo / "docs" / "10-weapons.md").write_text("# WPN-001\n\nUnrelated edit.\n")

        result = open_pr(work_repo, *default_args(tmp_path, "docs/08-vehicles.md"))

        assert result.returncode == 0, result.stderr
        assert committed_paths(work_repo) == ["docs/08-vehicles.md"]

    def test_the_unnamed_edit_is_left_in_the_working_tree(self, work_repo, tmp_path):
        (work_repo / "docs" / "08-vehicles.md").write_text("# VEH-001\n\nSecond.\n")
        (work_repo / "docs" / "10-weapons.md").write_text("# WPN-001\n\nUnrelated edit.\n")

        open_pr(work_repo, *default_args(tmp_path, "docs/08-vehicles.md"))

        assert "Unrelated edit" in (work_repo / "docs" / "10-weapons.md").read_text()
        assert run_git(work_repo, "status", "--short").split() == ["M", "docs/10-weapons.md"]

    def test_the_branch_reaches_the_remote(self, work_repo, tmp_path, bare_remote):
        (work_repo / "docs" / "08-vehicles.md").write_text("# VEH-001\n\nSecond.\n")

        open_pr(work_repo, *default_args(tmp_path, "docs/08-vehicles.md"))

        assert "measure-on-the-grid" in run_git(bare_remote, "branch", "--list")

    def test_one_run_makes_exactly_one_commit(self, work_repo, tmp_path):
        (work_repo / "docs" / "08-vehicles.md").write_text("# VEH-001\n\nSecond.\n")
        before = run_git(work_repo, "rev-list", "--count", "HEAD")

        open_pr(work_repo, *default_args(tmp_path, "docs/08-vehicles.md"))

        after = run_git(work_repo, "rev-list", "--count", "HEAD")
        assert int(after) == int(before) + 1

    def test_a_deletion_is_staged_without_git_add(self, work_repo, tmp_path):
        (work_repo / "docs" / "10-weapons.md").unlink()

        result = open_pr(work_repo, *default_args(tmp_path, "docs/10-weapons.md"))

        assert result.returncode == 0, result.stderr
        assert run_git(work_repo, "show", "--stat", "HEAD").count("10-weapons.md") == 1
        assert not (work_repo / "docs" / "10-weapons.md").exists()


class TestItStopsInsteadOfImprovising:
    def test_it_refuses_to_commit_to_main(self, work_repo, tmp_path):
        run_git(work_repo, "checkout", "main")
        args = default_args(tmp_path, "docs/08-vehicles.md")
        args[1] = "main"

        result = open_pr(work_repo, *args)

        assert result.returncode == 1
        assert "protected" in result.stderr

    def test_it_refuses_a_path_that_is_neither_on_disk_nor_in_head(self, work_repo, tmp_path):
        result = open_pr(work_repo, *default_args(tmp_path, "docs/99-invented.md"))

        assert result.returncode == 1
        assert "neither on disk nor in HEAD" in result.stderr

    def test_it_refuses_a_directory_path(self, work_repo, tmp_path):
        (work_repo / "docs" / "08-vehicles.md").write_text("# VEH-001\n\nSecond.\n")

        result = open_pr(work_repo, *default_args(tmp_path, "docs"))

        assert result.returncode == 1
        assert "docs is a directory" in result.stderr
        assert "docs/08-vehicles.md" in result.stderr

    def test_a_directory_refusal_leaves_the_index_as_it_was_found(self, work_repo, tmp_path):
        (work_repo / "docs" / "08-vehicles.md").write_text("# VEH-001\n\nSecond.\n")
        before_head = run_git(work_repo, "rev-parse", "HEAD")
        before_staged = run_git(work_repo, "diff", "--cached", "--name-only")

        open_pr(work_repo, *default_args(tmp_path, "docs"))

        assert run_git(work_repo, "rev-parse", "HEAD") == before_head
        assert run_git(work_repo, "diff", "--cached", "--name-only") == before_staged

    def test_it_refuses_when_the_named_paths_hold_no_change(self, work_repo, tmp_path):
        result = open_pr(work_repo, *default_args(tmp_path, "docs/08-vehicles.md"))

        assert result.returncode == 1
        assert "nothing staged" in result.stderr

    def test_it_refuses_when_something_else_is_already_staged(self, work_repo, tmp_path):
        (work_repo / "docs" / "08-vehicles.md").write_text("# VEH-001\n\nSecond.\n")
        (work_repo / "docs" / "10-weapons.md").write_text("# WPN-001\n\nSomebody staged this.\n")
        run_git(work_repo, "add", "docs/10-weapons.md")

        result = open_pr(work_repo, *default_args(tmp_path, "docs/08-vehicles.md"))

        assert result.returncode == 1
        assert "staged already" in result.stderr

    def test_a_refusal_leaves_the_index_as_it_was_found(self, work_repo, tmp_path):
        (work_repo / "docs" / "08-vehicles.md").write_text("# VEH-001\n\nSecond.\n")
        (work_repo / "docs" / "10-weapons.md").write_text("# WPN-001\n\nSomebody staged this.\n")
        run_git(work_repo, "add", "docs/10-weapons.md")
        before = run_git(work_repo, "diff", "--cached", "--name-only")

        open_pr(work_repo, *default_args(tmp_path, "docs/08-vehicles.md"))

        assert run_git(work_repo, "diff", "--cached", "--name-only") == before


class TestTheDryRun:
    def test_it_touches_nothing(self, work_repo, tmp_path):
        (work_repo / "docs" / "08-vehicles.md").write_text("# VEH-001\n\nSecond.\n")
        before = run_git(work_repo, "rev-parse", "HEAD")

        result = open_pr(
            work_repo, *default_args(tmp_path, "docs/08-vehicles.md"), "--dry-run"
        )

        assert result.returncode == 0
        assert run_git(work_repo, "rev-parse", "HEAD") == before
        assert run_git(work_repo, "diff", "--cached", "--name-only") == ""

    def test_it_prints_the_plan(self, work_repo, tmp_path):
        result = open_pr(
            work_repo, *default_args(tmp_path, "docs/08-vehicles.md"), "--dry-run"
        )

        assert "docs/08-vehicles.md" in result.stdout
        assert "measure-on-the-grid" in result.stdout
