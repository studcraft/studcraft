"""A branch that places a drawn image places it, and does nothing else.

`scripts/check_image_change.py` asks about scope rather than consistency, which
is the question no other check here asks. Every failure below leaves a tree that
`insert_images.py --check` calls correct: the index and the ruleset agree in all
of them. What is wrong is what else the branch did on the way.

Every case runs the script as a subprocess against a repository built in
`tmp_path`, per `system/ci-gates.md`: a script finds its own repository through
`REPO_ROOT`, so copying `scripts/` into a temporary tree is what points it there.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from conftest import commit_all, run_git

DOCUMENT = """# StudCraft Construction Components

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
"""

EMBED = "![CMP-018 — clear opening](../assets/images/cmp-018-clear-opening.png)"


def placement_repo(temp_repo: Path) -> Path:
    """A repository whose committed state specifies the image but has not drawn it."""
    docs = temp_repo / "docs"
    docs.mkdir()
    (docs / "05-construction-components.md").write_text(DOCUMENT)

    assets = temp_repo / "assets"
    (assets / "images").mkdir(parents=True)
    (assets / "IMAGES.md").write_text(INDEX)
    (assets / "images" / ".gitkeep").write_text("")

    system = temp_repo / "system"
    system.mkdir()
    (system / "workflow.md").write_text("# Workflow\n")

    commit_all(temp_repo, "The state before the image was drawn")
    run_git(temp_repo, "checkout", "-b", "add-image-to-clear-opening-rule")
    return temp_repo


def draw_and_place(repo: Path) -> None:
    """What `insert_images.py --write` and the illustrator between them produce."""
    (repo / "assets" / "images" / "cmp-018-clear-opening.png").write_bytes(b"PNG")

    document = repo / "docs" / "05-construction-components.md"
    document.write_text(
        document.read_text().replace(
            "> **If it fits, it passes.**\n",
            f"> **If it fits, it passes.**\n\n{EMBED}\n",
        )
    )


def check(repo: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(repo / "scripts" / "check_image_change.py"), *args],
        cwd=repo,
        capture_output=True,
        text=True,
    )


def test_a_bare_placement_passes(temp_repo: Path) -> None:
    repo = placement_repo(temp_repo)
    draw_and_place(repo)

    result = check(repo)

    assert result.returncode == 0, result.stdout + result.stderr
    assert "1 image file(s), 1 embed line(s)" in result.stdout
    assert "05-construction-components.md" in result.stdout


def test_a_branch_touching_no_image_is_not_a_placement(temp_repo: Path) -> None:
    """The index gains an entry for an image nobody has drawn. A different change."""
    repo = placement_repo(temp_repo)
    index = repo / "assets" / "IMAGES.md"
    index.write_text(
        index.read_text()
        + "| CMP-019 | `assets/images/cmp-019-hinges.png` | A hinge. | The arc is spatial. |\n"
    )

    result = check(repo)

    assert result.returncode == 0, result.stdout + result.stderr
    assert "not a placement" in result.stdout


def test_editing_the_entry_alongside_the_image_fails(temp_repo: Path) -> None:
    """The failure this script exists for: the entry narrowed to fit the drawing."""
    repo = placement_repo(temp_repo)
    draw_and_place(repo)

    index = repo / "assets" / "IMAGES.md"
    index.write_text(
        index.read_text().replace("A doorway, twice.", "A doorway with a minifig.")
    )

    result = check(repo)

    assert result.returncode == 1
    assert "assets/IMAGES.md is edited" in result.stdout
    assert "separate change on its own branch" in result.stdout


def test_a_file_outside_the_three_allowed_places_fails(temp_repo: Path) -> None:
    repo = placement_repo(temp_repo)
    draw_and_place(repo)
    (repo / "system" / "workflow.md").write_text("# Workflow\n\nA sentence about images.\n")

    result = check(repo)

    assert result.returncode == 1
    assert "system/workflow.md" in result.stdout


def test_rewording_a_rule_on_the_way_through_fails(temp_repo: Path) -> None:
    """The tree stays consistent; a rule changed without a proposal saying so."""
    repo = placement_repo(temp_repo)
    draw_and_place(repo)

    document = repo / "docs" / "05-construction-components.md"
    document.write_text(
        document.read_text().replace(
            "An opening is measured by what a model can pass through, not by its frame.",
            "An opening is measured by the clear width a model can pass through.",
        )
    )

    result = check(repo)

    assert result.returncode == 1
    assert "not an image embed" in result.stdout


def test_removing_an_image_is_the_same_shape_backwards(temp_repo: Path) -> None:
    repo = placement_repo(temp_repo)
    draw_and_place(repo)
    commit_all(repo, "An image reaches the clear-opening rule")

    base = run_git(repo, "rev-parse", "HEAD")
    (repo / "assets" / "images" / "cmp-018-clear-opening.png").unlink()
    document = repo / "docs" / "05-construction-components.md"
    document.write_text(document.read_text().replace(f"\n{EMBED}\n", ""))

    result = check(repo, base)

    assert result.returncode == 0, result.stdout + result.stderr
    assert "1 image file(s)" in result.stdout


def test_a_base_named_and_missing_is_an_error(temp_repo: Path) -> None:
    """CI names the pull request's base. A base that is not there is a wrong
    answer, not a missing one — skipping would report the placement clean
    without comparing it against anything."""
    repo = placement_repo(temp_repo)
    draw_and_place(repo)

    result = check(repo, "no-such-revision")

    assert result.returncode == 1
    assert "no-such-revision" in result.stderr
    assert "Skipping" not in result.stdout


def test_no_base_to_find_skips(temp_repo: Path, tmp_path: Path) -> None:
    """A fresh clone with neither origin/main nor main legitimately has nothing
    to compare against, and that is not a failure."""
    repo = placement_repo(temp_repo)
    draw_and_place(repo)
    # Leave `main` behind: an orphan branch shares no history with it, so no
    # merge base exists and auto-detection finds nothing.
    run_git(repo, "checkout", "--orphan", "detached-work")

    result = check(repo)

    assert result.returncode == 0
    assert "Skipping" in result.stdout
