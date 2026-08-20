"""A rule ID may be retired. It may never be renumbered or handed to a new rule.

`scripts/check_id_stability.py` compares `docs/` on disk against a base
revision, which is the only vantage point from which a number that changed
document — or came back on a different rule — is visible at all. These tests pin
the three outcomes: a deletion passes, a move fails, a reissue fails.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from conftest import commit_all, run_git

CORE = """# StudCraft Core Rules

# CORE-001 — Unit Base (UB)

One Unit Base measures 4 studs wide, 3 studs deep and 13 plate layers tall.

# CORE-002 — Facing

Every unit has a facing.

# CORE-003 — Infantry

Infantry are represented by LEGO minifigures.
"""

# CORE-002 is deliberately absent here — a gap that lets a fenced-in "# CORE-002"
# land on a number below the document's ceiling (CORE-003), the exact shape of
# the false positive a fenced rule heading used to cause.
CORE_WITH_A_GAP = """# StudCraft Core Rules

# CORE-001 — Unit Base (UB)

One Unit Base measures 4 studs wide, 3 studs deep and 13 plate layers tall.

# CORE-003 — Infantry

Infantry are represented by LEGO minifigures.
"""

VEHICLES = """# StudCraft Vehicle Rules

# VEH-001 — Vehicle Footprint

A powered vehicle occupies two or more Unit Bases.
"""


def based_repo(temp_repo: Path) -> Path:
    """A repository whose committed `docs/` holds CORE-001 – CORE-003 and VEH-001."""
    docs = temp_repo / "docs"
    docs.mkdir()
    (docs / "02-core-rules.md").write_text(CORE)
    (docs / "08-vehicles.md").write_text(VEHICLES)
    commit_all(temp_repo, "The base state")
    return temp_repo


def check(repo: Path, base: str = "HEAD") -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(repo / "scripts" / "check_id_stability.py"), base],
        cwd=repo,
        capture_output=True,
        text=True,
    )


class TestRetiringARule:
    def test_an_unchanged_ruleset_passes(self, temp_repo):
        result = check(based_repo(temp_repo))

        assert result.returncode == 0, result.stdout
        assert "none renumbered or reused" in result.stdout

    def test_a_deleted_rule_passes_and_is_reported_as_retired(self, temp_repo):
        repo = based_repo(temp_repo)
        (repo / "docs" / "02-core-rules.md").write_text(
            CORE.replace(
                "# CORE-003 — Infantry\n\nInfantry are represented by LEGO minifigures.\n",
                "",
            )
        )

        result = check(repo)

        assert result.returncode == 0, result.stdout
        assert "1 retired" in result.stdout

    def test_deleting_every_rule_in_a_document_still_passes(self, temp_repo):
        repo = based_repo(temp_repo)
        (repo / "docs" / "08-vehicles.md").unlink()

        result = check(repo)

        assert result.returncode == 0, result.stdout
        assert "1 retired" in result.stdout


class TestWhatStaysForbidden:
    def test_a_rule_moved_to_another_document_fails(self, temp_repo):
        repo = based_repo(temp_repo)
        (repo / "docs" / "02-core-rules.md").write_text(
            CORE.replace(
                "# CORE-003 — Infantry\n\nInfantry are represented by LEGO minifigures.\n",
                "",
            )
        )
        (repo / "docs" / "08-vehicles.md").write_text(
            VEHICLES + "\n# CORE-003 — Infantry\n\nMoved here wholesale.\n"
        )

        result = check(repo)

        assert result.returncode == 1
        assert "CORE-003 moved" in result.stdout

    def test_a_retired_number_reappearing_on_a_new_rule_fails(self, temp_repo):
        repo = based_repo(temp_repo)
        (repo / "docs" / "02-core-rules.md").write_text(
            CORE.replace(
                "# CORE-002 — Facing\n\nEvery unit has a facing.\n",
                "# CORE-002 — Something Else Entirely\n\nA different rule, same number.\n",
            )
        )
        run_git(repo, "add", "docs/02-core-rules.md")
        commit_all(repo, "Retire CORE-002")

        # Delete it, commit, then bring the number back on a new rule.
        (repo / "docs" / "02-core-rules.md").write_text(
            CORE.replace(
                "# CORE-002 — Facing\n\nEvery unit has a facing.\n\n",
                "",
            )
        )
        commit_all(repo, "Retire CORE-002 for real")
        base = run_git(repo, "rev-parse", "HEAD")

        (repo / "docs" / "02-core-rules.md").write_text(
            CORE.replace(
                "# CORE-002 — Facing\n\nEvery unit has a facing.\n",
                "# CORE-002 — Reissued\n\nA new rule wearing a retired number.\n",
            )
        )

        result = check(repo, base)

        assert result.returncode == 1
        assert "CORE-002 is new" in result.stdout


class TestFencedHeadingsAreNotRules:
    def test_a_rule_heading_inside_a_fenced_block_is_not_counted(self, temp_repo):
        docs = temp_repo / "docs"
        docs.mkdir()
        (docs / "02-core-rules.md").write_text(CORE_WITH_A_GAP)
        commit_all(temp_repo, "The base state, with a gap at CORE-002")

        # Uncommitted: a worked example of a heading, fenced, using the gap's
        # number. A regex reading straight through the fence would invent
        # CORE-002 here and flag it as reused, below CORE-003's ceiling for
        # this document.
        (docs / "02-core-rules.md").write_text(
            CORE_WITH_A_GAP
            + "\n```markdown\n# CORE-002 — Example Heading\n\n"
            "An example in prose, not a real rule.\n```\n"
        )

        result = check(temp_repo)

        assert result.returncode == 0, result.stdout
        assert "none renumbered or reused" in result.stdout
