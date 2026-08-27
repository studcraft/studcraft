"""`docs/`, `assets/images/` and `assets/IMAGES.md` agree, or the script says how.

One rule is under test throughout: an embed exists exactly when the file exists
and the index lists it for that section. Each direction of failing it gets a
test, because each one is a different accident — an image nobody sees, a broken
image, and an image whose argument for existing was never written.

Every case runs the script as a subprocess against a repository built in
`tmp_path`, per `system/ci-gates.md`: a script finds its own repository through
`REPO_ROOT`, so copying `scripts/` into a temporary tree is what points it there.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import insert_images
from conftest import commit_all, run_git

DOCUMENT = """# StudCraft Vehicle Rules

**Version:** 0.4.0

---

# VEH-001 — Vehicle Footprint

A vehicle occupies whole studs.

---

# VEH-002 — Vehicle Facing

A vehicle faces the long axis of its footprint.

---

# Terrain

An obstacle is read in plate layers.

## VEH-006 — One Brick Obstacles

Crossed freely.

---
"""

INDEX_HEAD = """# Example Images Index

Prose about the format, holding a table that is not an entry.

| Rule | Filename | What it must show | Why text alone is not enough |
|---|---|---|---|

## docs/08-vehicles.md

| Rule | Filename | What it must show | Why text alone is not enough |
|---|---|---|---|
"""

REJECTED = """
---

Rules considered and rejected, with reasons:

- **VEH-002 (Vehicle Facing)** — the long axis is self-evident on any model.
"""


def build(repo: Path, rows: str, drawn: tuple[str, ...], document: str = DOCUMENT) -> None:
    """A repository with one document, one index and whichever images are drawn."""
    (repo / "docs").mkdir(exist_ok=True)
    (repo / "docs" / "08-vehicles.md").write_text(document)

    (repo / "assets" / "images").mkdir(parents=True, exist_ok=True)
    (repo / "assets" / "IMAGES.md").write_text(INDEX_HEAD + rows + REJECTED)

    for name in drawn:
        (repo / "assets" / "images" / name).write_bytes(b"\x89PNG\r\n\x1a\n")

    # A commit, so that `git rev-parse --abbrev-ref HEAD` has a branch to name.
    # On an unborn branch it fails, and the script refuses for the wrong reason.
    commit_all(repo, "the tree under test")


def run(repo: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(repo / "scripts" / "insert_images.py"), *args],
        cwd=repo,
        capture_output=True,
        text=True,
    )


def on_a_change_branch(repo: Path, name: str = "add-an-image") -> None:
    """What `--write` requires: a branch naming an unarchived change."""
    (repo / "openspec" / "changes" / name).mkdir(parents=True, exist_ok=True)
    (repo / "openspec" / "changes" / name / "proposal.md").write_text("# A change\n")
    run_git(repo, "checkout", "-b", name)


def document_of(repo: Path) -> str:
    return (repo / "docs" / "08-vehicles.md").read_text()


ROW = (
    "| VEH-001 | `assets/images/veh-001-footprint-studs.png` | Whole studs. "
    "| Studs are not obvious. |\n"
)


def test_listed_and_drawn_but_not_embedded_is_reported(temp_repo: Path) -> None:
    build(temp_repo, ROW, ("veh-001-footprint-studs.png",))

    result = run(temp_repo, "--check")

    assert result.returncode == 1
    assert "does not embed it" in result.stdout
    assert "![" not in document_of(temp_repo)


def test_write_places_the_image_under_the_rule(temp_repo: Path) -> None:
    build(temp_repo, ROW, ("veh-001-footprint-studs.png",))
    on_a_change_branch(temp_repo)

    assert run(temp_repo, "--write").returncode == 0

    text = document_of(temp_repo)
    embed = "![VEH-001 — footprint studs](../assets/images/veh-001-footprint-studs.png)"
    assert embed in text
    # Under the rule's prose and above the thematic break that closes it, not
    # under the next rule's heading.
    assert text.index(embed) < text.index("# VEH-002")
    assert text.index("A vehicle occupies whole studs.") < text.index(embed)


def test_a_second_write_changes_nothing(temp_repo: Path) -> None:
    build(temp_repo, ROW, ("veh-001-footprint-studs.png",))
    on_a_change_branch(temp_repo)

    run(temp_repo, "--write")
    once = document_of(temp_repo)

    assert run(temp_repo, "--check").returncode == 0
    assert run(temp_repo, "--write").returncode == 0
    assert document_of(temp_repo) == once


def test_several_images_on_one_rule_keep_the_table_order(temp_repo: Path) -> None:
    rows = ROW + (
        "| VEH-001 | `assets/images/veh-001-overhang-excluded.png` | An overhang. "
        "| Overhangs mislead. |\n"
    )
    build(temp_repo, rows, (
        "veh-001-footprint-studs.png",
        "veh-001-overhang-excluded.png",
    ))
    on_a_change_branch(temp_repo)

    run(temp_repo, "--write")
    text = document_of(temp_repo)

    assert text.index("veh-001-footprint-studs.png") < text.index("veh-001-overhang-excluded.png")


def test_an_unnumbered_entry_lands_above_its_first_sub_rule(temp_repo: Path) -> None:
    rows = (
        "| Terrain (VEH-006) | `assets/images/08-terrain-thresholds.png` | Three heights. "
        "| Plate layers need converting. |\n"
    )
    build(temp_repo, rows, ("08-terrain-thresholds.png",))
    on_a_change_branch(temp_repo)

    run(temp_repo, "--write")
    text = document_of(temp_repo)

    assert text.index("08-terrain-thresholds.png") < text.index("## VEH-006")
    assert text.index("An obstacle is read in plate layers.") < text.index("08-terrain-thresholds.png")


def test_an_embed_whose_file_is_gone_is_removed(temp_repo: Path) -> None:
    build(temp_repo, ROW, ("veh-001-footprint-studs.png",))
    on_a_change_branch(temp_repo)
    run(temp_repo, "--write")

    (temp_repo / "assets" / "images" / "veh-001-footprint-studs.png").unlink()

    check = run(temp_repo, "--check")
    assert check.returncode == 1
    assert "is not in assets/images/" in check.stdout

    run(temp_repo, "--write")
    assert "![" not in document_of(temp_repo)
    assert "A vehicle occupies whole studs." in document_of(temp_repo)


def test_an_embed_with_no_entry_is_reported_with_the_row_to_paste(temp_repo: Path) -> None:
    build(temp_repo, ROW, ("veh-001-footprint-studs.png",))
    hand_placed = DOCUMENT.replace(
        "A vehicle faces the long axis of its footprint.",
        "A vehicle faces the long axis of its footprint.\n\n"
        "![by hand](../assets/images/veh-002-facing.png)",
    )
    (temp_repo / "docs" / "08-vehicles.md").write_text(hand_placed)

    result = run(temp_repo, "--check")

    assert result.returncode == 1
    assert "no entry in assets/IMAGES.md lists it" in result.stdout
    assert "| VEH-002 | `assets/images/veh-002-facing.png` |" in result.stdout
    # VEH-002 is in the rejected list, so the remedy says which ritual applies.
    assert "rejected list" in result.stdout


def test_an_unlisted_embed_is_removed_by_write(temp_repo: Path) -> None:
    build(temp_repo, ROW, ("veh-001-footprint-studs.png",))
    hand_placed = DOCUMENT.replace(
        "A vehicle faces the long axis of its footprint.",
        "A vehicle faces the long axis of its footprint.\n\n"
        "![by hand](../assets/images/veh-002-facing.png)",
    )
    (temp_repo / "docs" / "08-vehicles.md").write_text(hand_placed)
    on_a_change_branch(temp_repo)

    run(temp_repo, "--write")

    assert "veh-002-facing.png" not in document_of(temp_repo)
    assert "A vehicle faces the long axis of its footprint." in document_of(temp_repo)


def test_a_drawn_file_no_entry_names_is_reported(temp_repo: Path) -> None:
    build(temp_repo, ROW, (
        "veh-001-footprint-studs.png",
        "veh-009-nobody-asked.png",
    ))
    on_a_change_branch(temp_repo)

    result = run(temp_repo, "--write")

    assert result.returncode == 1
    assert "no entry in assets/IMAGES.md names it" in result.stdout
    # Writing the embed it could place does not make the run clean.
    assert "veh-001-footprint-studs.png" in document_of(temp_repo)


def test_a_file_that_is_not_a_png_is_reported(temp_repo: Path) -> None:
    """The convention admits only `.png`, so anything else is invalid — and the
    scan globbed `*.png`, which made it invisible rather than failing."""
    build(temp_repo, ROW, ("veh-001-footprint-studs.png",))
    (temp_repo / "assets" / "images" / "veh-002-facing.jpg").write_bytes(b"\xff\xd8\xff")

    result = run(temp_repo, "--check")

    assert result.returncode == 1
    assert "is not a .png" in result.stdout


def test_the_gitkeep_holding_the_directory_is_not_reported(temp_repo: Path) -> None:
    build(temp_repo, ROW, ())
    (temp_repo / "assets" / "images" / ".gitkeep").write_text("")

    assert run(temp_repo, "--check").returncode == 0


def test_an_entry_naming_no_section_is_reported(temp_repo: Path) -> None:
    rows = (
        "| VEH-004 | `assets/images/veh-004-nowhere.png` | Something. "
        "| Somewhere. |\n"
    )
    build(temp_repo, rows, ("veh-004-nowhere.png",))

    result = run(temp_repo, "--check")

    assert result.returncode == 1
    assert "has nowhere to go" in result.stdout


def test_write_refuses_on_main(temp_repo: Path) -> None:
    build(temp_repo, ROW, ("veh-001-footprint-studs.png",))

    result = run(temp_repo, "--write")

    assert result.returncode == 1
    assert "on main" in result.stderr
    assert "![" not in document_of(temp_repo)


def test_write_refuses_on_a_branch_that_is_not_a_change(temp_repo: Path) -> None:
    build(temp_repo, ROW, ("veh-001-footprint-studs.png",))
    run_git(temp_repo, "checkout", "-b", "tidy-the-assets")

    result = run(temp_repo, "--write")

    assert result.returncode == 1
    assert "names no unarchived change" in result.stderr
    assert "![" not in document_of(temp_repo)


def test_check_never_writes_and_never_refuses(temp_repo: Path) -> None:
    build(temp_repo, ROW, ("veh-001-footprint-studs.png",))
    before = document_of(temp_repo)

    result = run(temp_repo, "--check")

    assert "Refusing" not in result.stderr
    assert document_of(temp_repo) == before


class TestItWritesNothingItWasNotAskedTo:
    """Every document with an entry goes through the rewrite, drawn or not.

    An early version normalised whitespace on the way through, and would have
    written four documents this change never proposed to touch — a `docs/` edit
    no proposal describes, which is the one thing `system/workflow.md` forbids
    outright. Both shapes it tripped over exist in `docs/` today.
    """

    def test_a_document_that_ends_without_a_newline_keeps_ending_without_one(
        self, temp_repo: Path
    ) -> None:
        build(temp_repo, ROW, (), document=DOCUMENT.rstrip("\n"))

        assert run(temp_repo, "--check").returncode == 0
        assert not document_of(temp_repo).endswith("\n")

    def test_a_double_blank_line_is_left_alone(self, temp_repo: Path) -> None:
        doubled = DOCUMENT.replace(
            "A vehicle occupies whole studs.\n",
            "A vehicle occupies whole studs.\n\n\nStill VEH-001's body.\n",
        )
        build(temp_repo, ROW, ("veh-001-footprint-studs.png",), document=doubled)
        on_a_change_branch(temp_repo)

        run(temp_repo, "--write")

        assert "whole studs.\n\n\nStill VEH-001's body." in document_of(temp_repo)

    def test_a_document_whose_images_are_undrawn_is_not_rewritten(
        self, temp_repo: Path
    ) -> None:
        build(temp_repo, ROW, ())
        before = document_of(temp_repo)
        on_a_change_branch(temp_repo)

        assert run(temp_repo, "--write").returncode == 0
        assert document_of(temp_repo) == before

    def test_a_rewrite_nothing_reported_is_itself_reported(self) -> None:
        """The guard, asked directly: the script's own logic can no longer
        produce a rewrite it does not report, which is exactly why the guard is
        there — the version that could reported nothing."""
        finding = insert_images.silent_rewrite("08-vehicles.md", [])

        assert finding is not None
        assert "not asked to touch" in finding.render()

    def test_a_rewrite_its_own_finding_explains_is_not_reported_twice(self) -> None:
        explained = [insert_images.Finding("docs/08-vehicles.md:12", "does not embed it")]

        assert insert_images.silent_rewrite("08-vehicles.md", explained) is None


def test_an_agreeing_repository_exits_zero(temp_repo: Path) -> None:
    build(temp_repo, ROW, ())

    result = run(temp_repo, "--check")

    assert result.returncode == 0
    assert "agree" in result.stdout
