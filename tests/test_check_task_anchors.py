"""The two checks this file covers are the ones that used to need a reader.

`.claude/agents/proposal-auditor.md` asks for both — every replacement stated
verbatim, and a coverage table whose rows still point at tasks that exist — and
an expensive model re-deriving either is a minute it did not spend on whether
the change is right. What is tested here is that the mechanical half fires on
the defect and stays quiet on the many shapes that look like it.
"""

from __future__ import annotations

import check_task_anchors
import pytest


@pytest.fixture
def tasks(tmp_path):
    def write(body: str):
        path = tmp_path / "tasks.md"
        path.write_text(body)
        return path
    return write


def errors(findings) -> list[str]:
    return [f.message for f in findings if f.severity == "error"]


PAIR = (
    "- [ ] 1.1 In `docs/02-core-rules.md`, replace this anchor:\n\n"
    "```\nold\n```\n\nwith:\n\n```\nnew\n```\n"
)


class TestATaskMustCarryTheBlockItAnnounces:
    def test_an_announced_anchor_with_no_block_is_an_error(self, tasks):
        found = check_task_anchors.check_edit_tasks_carry_a_block(
            "a-change",
            tasks("- [ ] 1.1 In `docs/02-core-rules.md`, replace this anchor with the "
                  "wording agreed in design.md.\n"),
        )
        assert "carries no fenced" in errors(found)[0]

    def test_an_announced_anchor_with_its_pair_is_clean(self, tasks):
        assert check_task_anchors.check_edit_tasks_carry_a_block("a-change", tasks(PAIR)) == []

    def test_a_task_running_the_anchor_checker_is_not_an_edit_task(self, tasks):
        """`- [ ] 2.5 Run \\`python3 scripts/check_task_anchors.py …\\`` names
        anchors and carries no block, entirely correctly."""
        found = check_task_anchors.check_edit_tasks_carry_a_block(
            "a-change",
            tasks("- [ ] 2.5 Run `python3 scripts/check_task_anchors.py a-change` — "
                  "confirms this file raises no anchor error.\n"),
        )
        assert found == []

    def test_a_verification_task_is_not_an_edit_task(self, tasks):
        found = check_task_anchors.check_edit_tasks_carry_a_block(
            "a-change",
            tasks("- [ ] 3.1 Run `grep -c CORE-001 docs/02-core-rules.md` — after: **2**.\n"),
        )
        assert found == []

    def test_the_repository_s_other_phrasings_are_recognised(self, tasks):
        for line in (
            "- [ ] 5.13 In `TRN-020`, replace this block. Four-backtick fences below.\n",
            "- [ ] 5.1 In `CORE-006`, replace the paragraph added by task 1.1 — this "
            "anchor is what it reads now.\n",
        ):
            found = check_task_anchors.check_edit_tasks_carry_a_block("a-change", tasks(line))
            assert errors(found), f"not recognised as an edit task: {line!r}"


class TestReplacementTextMustBeFenced:
    def test_a_run_of_quoted_lines_inside_a_fence_is_not_a_blockquote_replacement(self, tasks):
        """`TODO.md` is built out of blockquotes, so an anchor quoting three or
        more `> ` lines verbatim inside a fence is the anchor doing its job, not
        the pre-2026-08-10 convention this check exists to catch."""
        found = check_task_anchors.check_replacement_format(
            "a-change",
            tasks(
                "- [ ] 1.1 In `TODO.md`, replace this anchor:\n\n"
                "```\n> - Indirect Fire\n> - Smoke Launchers\n> - Reloading\n```\n\n"
                "with:\n\n```\nnew\n```\n"
            ),
        )
        assert found == []

    def test_the_same_run_unfenced_is_still_a_blockquote_replacement(self, tasks):
        found = check_task_anchors.check_replacement_format(
            "a-change",
            tasks("> - Indirect Fire\n> - Smoke Launchers\n> - Reloading\n\nwith:\n"),
        )
        assert "blockquote" in errors(found)[0]


class TestACoverageTableMustNameTasksThatExist:
    def test_a_row_naming_a_task_that_does_not_exist_is_an_error(self, tasks):
        found = check_task_anchors.check_coverage_table(
            "a-change",
            tasks(PAIR + "\n| `CORE-001` trimmed | 9.9 | `docs/02-core-rules.md` |\n"),
        )
        assert "9.9" in errors(found)[0]

    def test_a_row_naming_a_task_that_exists_is_clean(self, tasks):
        found = check_task_anchors.check_coverage_table(
            "a-change",
            tasks(PAIR + "\n| `CORE-001` trimmed | 1.1 | `docs/02-core-rules.md` |\n"),
        )
        assert found == []

    def test_several_tasks_in_one_cell_are_all_checked(self, tasks):
        found = check_task_anchors.check_coverage_table(
            "a-change",
            tasks(PAIR + "\n| Image candidates retargeted | 1.1, 8.8 | `assets/IMAGES.md` |\n"),
        )
        assert "8.8" in errors(found)[0]

    def test_a_letter_suffixed_task_is_a_reference(self, tasks):
        body = PAIR.replace("1.1", "13c.1")
        found = check_task_anchors.check_coverage_table(
            "a-change", tasks(body + "\n| Audit repair | 13c.1 | `docs/07-movement.md` |\n")
        )
        assert found == []

    def test_prose_that_happens_to_contain_a_number_is_not_a_reference(self, tasks):
        """A cell reading "1 Action Point, 2.5 studs" names no task, and reading
        it as one turns a measurement into an error."""
        found = check_task_anchors.check_coverage_table(
            "a-change",
            tasks(PAIR + "\n| Movement rescaled | costs 2.5 studs per step | `docs/07-movement.md` |\n"),
        )
        assert found == []

    def test_a_file_with_no_tasks_at_all_is_not_checked(self, tasks):
        found = check_task_anchors.check_coverage_table(
            "a-change", tasks("| Item | Task | Path |\n| x | 1.1 | `docs/a.md` |\n")
        )
        assert found == []
