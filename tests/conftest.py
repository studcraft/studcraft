"""Fixtures shared by the tests.

Two rules hold here, and both come from `system/ci-gates.md`:

- **Nothing touches the real working directory.** A repo-mutating script is
  tested against a copy in `tmp_path`, never against this checkout — an early
  test of `release_cut.py` run in place, cleaned up with `git reset --hard`,
  wiped an unrelated uncommitted fix.
- **A script reaches its own repository through `REPO_ROOT`**, computed from
  `__file__`. Copying `scripts/` into the temporary repository is therefore what
  points a script at it; there is no environment variable to set.
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = PROJECT_ROOT / "scripts"


def run_git(cwd: Path, *args: str) -> str:
    proc = subprocess.run(
        ["git", *args], cwd=cwd, capture_output=True, text=True, check=True
    )
    return proc.stdout.strip()


@pytest.fixture
def temp_repo(tmp_path: Path) -> Path:
    """A git repository holding a copy of `scripts/`, and nothing else yet.

    `git init` with an explicit identity and `main` as the initial branch, so a
    test does not depend on the machine's git configuration.
    """
    repo = tmp_path / "repo"
    repo.mkdir()

    run_git(repo, "init", "--initial-branch=main")
    run_git(repo, "config", "user.email", "tests@studcraft.invalid")
    run_git(repo, "config", "user.name", "StudCraft tests")

    shutil.copytree(SCRIPTS_DIR, repo / "scripts")
    return repo


@pytest.fixture
def bare_remote(tmp_path: Path) -> Path:
    """A bare repository to push to, so a push can be tested without a network."""
    remote = tmp_path / "remote.git"
    remote.mkdir()
    run_git(remote, "init", "--bare", "--initial-branch=main")
    return remote


def commit_all(repo: Path, message: str) -> None:
    """Commit whatever is in the tree. Tests only — the repository's own scripts
    are forbidden from staging this way (`system/repository-strategy.md`)."""
    run_git(repo, "add", "-A")
    run_git(repo, "commit", "-m", message)
