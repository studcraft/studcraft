"""`target_for` only — the one path in `tasks_format.py` #126 could not resolve.

It could not see a repository-root file (`./TODO.md` was the workaround), and
this pins the fix: a bare filename is a target, but the `design.md`,
`proposal.md` and `tasks.md` every change's own prose mentions are not,
compared by their full matched path so a real `tasks.md` inside a change
directory still resolves. `blocks`, `edits` and the rest of the module are not
covered here.
"""

from __future__ import annotations

import pytest
import tasks_format


class TestUncheckedTasksIgnoresWhatIsQuoted:
    def test_an_unticked_task_is_found(self):
        lines = ["- [ ] 1.1 Do it"]
        assert tasks_format.unchecked_tasks(lines) == [(1, "- [ ] 1.1 Do it")]

    def test_a_ticked_task_is_not(self):
        assert tasks_format.unchecked_tasks(["- [x] 1.1 Done"]) == []

    def test_an_indented_task_is_found(self):
        # The hand-written grep this replaced anchored at column 0.
        lines = ["      - [ ] 1.1 Do it"]
        assert len(tasks_format.unchecked_tasks(lines)) == 1

    def test_a_checkbox_inside_a_fence_is_not_a_task(self):
        # A tasks.md quotes the edits it makes, so an anchor or a replacement
        # can be a checkbox. Counting one kept a fully-applied change out of
        # the archive.
        lines = [
            "- [x] 1.1 In `scripts/tasks_format.py`, replace this anchor:",
            "",
            "```",
            "    - [ ] 2.1 In `AAA-001`, replace this anchor:",
            "```",
        ]
        assert tasks_format.unchecked_tasks(lines) == []

    def test_a_task_after_a_closed_fence_is_found_again(self):
        lines = [
            "```",
            "- [ ] 9.9 Quoted, not real",
            "```",
            "- [ ] 1.1 Real",
        ]
        assert tasks_format.unchecked_tasks(lines) == [(4, "- [ ] 1.1 Real")]


class TestTargetForResolvesPathsWithAndWithoutADirectory:
    def test_a_task_naming_a_docs_path_resolves_to_it(self):
        lines = ["- [ ] 1.1 In `docs/07-movement.md`, replace this anchor:"]
        assert tasks_format.target_for(lines, 1) == "docs/07-movement.md"

    def test_a_task_naming_todo_md_resolves_to_it(self):
        lines = ["- [ ] 1.1 In `TODO.md`, replace this anchor:"]
        assert tasks_format.target_for(lines, 1) == "TODO.md"

    def test_a_task_naming_code_of_design_resolves_to_it(self):
        lines = ["- [ ] 1.1 In `CODE_OF_DESIGN.md`, replace this anchor:"]
        assert tasks_format.target_for(lines, 1) == "CODE_OF_DESIGN.md"


class TestTargetForExcludesAChangesOwnArtifacts:
    @pytest.mark.parametrize("name", ["design.md", "proposal.md", "tasks.md"])
    def test_a_bare_self_reference_is_not_a_target(self, name):
        lines = [f"- [ ] 1.1 As agreed in `{name}`, do this."]
        assert tasks_format.target_for(lines, 1) is None

    def test_a_tasks_md_inside_a_change_directory_is_a_target(self):
        lines = ["- [ ] 1.1 See `openspec/changes/foo/tasks.md` for context."]
        assert tasks_format.target_for(lines, 1) == "openspec/changes/foo/tasks.md"

    def test_design_md_named_first_falls_through_to_the_real_target(self):
        lines = ["- [ ] 1.1 As agreed in `design.md`, edit `docs/02-core-rules.md`:"]
        assert tasks_format.target_for(lines, 1) == "docs/02-core-rules.md"


class TestTargetForReadsHeadingsAndTaskLines:
    def test_a_block_under_a_heading_takes_the_headings_path(self):
        lines = [
            "## 2. `docs/09-transport.md` — Embarking",
            "",
            "Some preamble prose that names no path.",
        ]
        assert tasks_format.target_for(lines, 3) == "docs/09-transport.md"

    def test_a_line_naming_no_path_returns_none(self):
        lines = ["- [ ] 1.1 Just prose, no backticked path here."]
        assert tasks_format.target_for(lines, 1) is None

    def test_a_heading_naming_a_bare_filename_falls_through(self):
        """A heading may mention a file in passing rather than editing it —
        "### Two `skip` lines from `apply_tasks.py` that are correct" talks
        about the script, and a bare filename there must not resolve as if
        the heading were an edit target for it."""
        lines = [
            "## 2. `docs/09-transport.md` — Embarking",
            "",
            "### Two `skip` lines from `apply_tasks.py` that are correct",
            "",
            "Some preamble prose that names no path.",
        ]
        assert tasks_format.target_for(lines, 5) == "docs/09-transport.md"
