"""A placement's three artifacts are generated, so the values in them are read.

`scripts/propose_placement.py` exists because the part of a placement nobody had
automated — writing `proposal.md`, `design.md` and `tasks.md` — is the part that
produced the wrong expected value. What is pinned here is that the numbers come
from the index rather than from a template: the embed line, the line it must
follow, and how many entries the index holds.

The one thing it must *not* write is pinned too. The maintainer's reading of the
image against its entry leaves a placeholder, and a run that quietly filled that
in would be worse than no script.

Every case runs the script as a subprocess against a repository built in
`tmp_path`, per `system/ci-gates.md`: a script finds its own repository through
`REPO_ROOT`, so copying `scripts/` into a temporary tree is what points it there.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import propose_placement
from conftest import commit_all, run_git

CHANGE = "add-image-to-clear-opening-rule"

DOCUMENT = """# StudCraft Construction Components

**Purpose**

**Version:** 0.4.0

---

# CMP-018 — Clear Opening

An opening is measured by what a model can pass through, not by its frame.

> **If it fits, it passes.**

---

# CMP-019 — Hinges

A hinged element is part of the opening it hangs across.

---
"""

INDEX = """# Example Images Index

Prose about the format, holding a table that is not an entry.

| Rule | Filename | What it must show | Why text alone is not enough |
|---|---|---|---|

## docs/05-construction-components.md

| Rule | Filename | What it must show | Why text alone is not enough |
|---|---|---|---|
| CMP-018 | `assets/images/cmp-018-clear-opening.png` | A doorway, twice. | The frame is the wrong thing to measure. |
| CMP-019 | `assets/images/cmp-019-hinges.png` | A hinge arc. | The swept area is spatial. |
"""


def placement_repo(temp_repo: Path, branch: str = CHANGE) -> Path:
    """A repository with one image drawn, unplaced, and a branch named for it."""
    docs = temp_repo / "docs"
    docs.mkdir()
    (docs / "05-construction-components.md").write_text(DOCUMENT)

    assets = temp_repo / "assets"
    (assets / "images").mkdir(parents=True)
    (assets / "IMAGES.md").write_text(INDEX)
    (assets / "images" / ".gitkeep").write_text("")

    (temp_repo / "openspec" / "changes").mkdir(parents=True)

    commit_all(temp_repo, "The state before the image was drawn")
    run_git(temp_repo, "checkout", "-b", branch)

    (assets / "images" / "cmp-018-clear-opening.png").write_bytes(b"PNG")
    return temp_repo


def propose(repo: Path, change: str = CHANGE) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(repo / "scripts" / "propose_placement.py"), change],
        cwd=repo,
        capture_output=True,
        text=True,
    )


def artifacts(repo: Path, change: str = CHANGE) -> dict[str, str]:
    directory = repo / "openspec" / "changes" / change
    return {path.name: path.read_text() for path in directory.iterdir()}


class TestWhatItWrites:
    def test_all_three_artifacts_are_written(self, temp_repo: Path) -> None:
        repo = placement_repo(temp_repo)

        result = propose(repo)

        assert result.returncode == 0, result.stdout + result.stderr
        assert set(artifacts(repo)) == {"proposal.md", "design.md", "tasks.md"}

    def test_the_embed_line_is_computed_not_described(self, temp_repo: Path) -> None:
        repo = placement_repo(temp_repo)
        propose(repo)

        embed = "![CMP-018 — clear opening](../assets/images/cmp-018-clear-opening.png)"
        written = artifacts(repo)
        assert embed in written["proposal.md"]
        assert embed in written["tasks.md"]

    def test_the_line_the_embed_follows_is_read_from_the_document(self, temp_repo: Path) -> None:
        """An embed under the *next* rule illustrates the wrong rule and breaks
        nothing, so the task names the line it must land after."""
        repo = placement_repo(temp_repo)
        propose(repo)

        assert "> **If it fits, it passes.**" in artifacts(repo)["tasks.md"]

    def test_the_counts_come_from_the_index(self, temp_repo: Path) -> None:
        repo = placement_repo(temp_repo)
        propose(repo)

        tasks = artifacts(repo)["tasks.md"]
        # Two entries in the index, one of them drawn.
        assert "2 image entr(ies), 1 drawn" in tasks
        # And the proposal says how many stay undrawn, from the same count.
        assert "1 entr(ies) stay specified and" in artifacts(repo)["proposal.md"]

    def test_the_maintainers_reading_is_left_unwritten(self, temp_repo: Path) -> None:
        repo = placement_repo(temp_repo)

        result = propose(repo)

        assert propose_placement.PLACEHOLDER in artifacts(repo)["tasks.md"]
        # And the run says so, rather than leaving it to be discovered.
        assert propose_placement.PLACEHOLDER in result.stdout

    def test_no_task_is_pre_ticked(self, temp_repo: Path) -> None:
        """A generated tasks.md describes work nobody has done yet."""
        repo = placement_repo(temp_repo)
        propose(repo)

        assert "[x]" not in artifacts(repo)["tasks.md"]


class TestWhatItRefuses:
    def test_a_branch_not_named_for_the_change(self, temp_repo: Path) -> None:
        repo = placement_repo(temp_repo, branch="some-other-work")

        result = propose(repo)

        assert result.returncode == 1
        assert "is not add-image-to-clear-opening-rule" in result.stderr

    def test_main(self, temp_repo: Path) -> None:
        repo = placement_repo(temp_repo)
        run_git(repo, "checkout", "main")

        result = propose(repo)

        assert result.returncode == 1
        assert "on main" in result.stderr

    def test_a_change_directory_that_already_holds_a_proposal(self, temp_repo: Path) -> None:
        repo = placement_repo(temp_repo)
        propose(repo)

        result = propose(repo)

        assert result.returncode == 1
        assert "does not rewrite one" in result.stderr

    def test_no_image_drawn_and_unplaced(self, temp_repo: Path) -> None:
        repo = placement_repo(temp_repo)
        (repo / "assets" / "images" / "cmp-018-clear-opening.png").unlink()

        result = propose(repo)

        assert result.returncode == 1
        assert "no image is drawn and unplaced" in result.stderr

    def test_an_image_already_embedded_is_not_pending(self, temp_repo: Path) -> None:
        repo = placement_repo(temp_repo)
        document = repo / "docs" / "05-construction-components.md"
        document.write_text(
            document.read_text().replace(
                "> **If it fits, it passes.**\n",
                "> **If it fits, it passes.**\n\n"
                "![CMP-018 — clear opening](../assets/images/cmp-018-clear-opening.png)\n",
            )
        )

        result = propose(repo)

        assert result.returncode == 1
        assert "no image is drawn and unplaced" in result.stderr

    def test_two_drawn_images_at_once(self, temp_repo: Path) -> None:
        """One placement per proposal. Two is a decision, not a default."""
        repo = placement_repo(temp_repo)
        (repo / "assets" / "images" / "cmp-019-hinges.png").write_bytes(b"PNG")

        result = propose(repo)

        assert result.returncode == 1
        assert "2 images are drawn and unplaced" in result.stderr

    def test_a_refusal_writes_nothing(self, temp_repo: Path) -> None:
        repo = placement_repo(temp_repo, branch="some-other-work")

        propose(repo)

        assert not (repo / "openspec" / "changes" / CHANGE).exists()
