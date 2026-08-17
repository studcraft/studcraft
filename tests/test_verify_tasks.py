"""`verify_tasks.py` runs commands out of a file anyone can propose by pull
request. Its docstring promises that only read-only ones are executed, and this
is where that promise is checked.

The dangerous commands here are not exotic. Each one is a verb that was on the
allowlist, carrying a flag that makes it write or execute.
"""

from __future__ import annotations

import verify_tasks


def refused(command: str) -> str:
    runnable, why = verify_tasks.is_runnable(command)
    assert not runnable, f"{command!r} was accepted; it must not be"
    return why


def accepted(command: str) -> None:
    runnable, why = verify_tasks.is_runnable(command)
    assert runnable, f"{command!r} was refused: {why}"


class TestReadOnlyCommandsRun:
    def test_a_grep_count_runs(self):
        accepted('grep -c "per Unit Base" docs/09-transport.md')

    def test_a_recursive_grep_runs(self):
        accepted("grep -rn CORE-010 docs/")

    def test_a_read_only_git_subcommand_runs(self):
        accepted("git diff --name-only")

    def test_a_checker_script_runs(self):
        accepted("python3 scripts/check_delta_coverage.py")

    def test_the_index_query_runs_with_several_arguments(self):
        accepted("python3 scripts/rule.py show CORE-002 FLOW-003 WPN-019")


class TestShellConstructsAreRefused:
    def test_a_pipe_is_refused(self):
        assert "'|'" in refused("grep -c x docs/ | wc -l")

    def test_a_chain_is_refused(self):
        assert "'&&'" in refused("grep -c x docs/ && rm -rf docs")

    def test_a_substitution_is_refused(self):
        refused("grep -c $(cat /etc/passwd) docs/")

    def test_a_redirection_is_refused(self):
        refused("grep -c x docs/ > /tmp/out")


class TestExecutionThroughAnAllowedVerb:
    """A verb on the allowlist can still run another program or delete files."""

    def test_find_exec_is_refused(self):
        refused("find docs -name '*.md' -exec sh -c 'echo owned' ;")

    def test_find_execdir_is_refused(self):
        refused("find docs -execdir touch pwned ;")

    def test_find_exec_terminated_with_a_plus_is_refused(self):
        # No `;`, so the shell-construct check above never sees this one.
        refused("find docs -name '*.md' -exec cat {} +")

    def test_find_delete_is_refused(self):
        refused("find docs -name '*.md' -delete")

    def test_ripgrep_preprocessor_is_refused(self):
        refused("rg --pre sh CORE-010 docs/")

    def test_sort_writing_a_file_is_refused(self):
        refused("sort -o docs/02-core-rules.md docs/02-core-rules.md")

    def test_a_bare_interpreter_is_refused(self):
        refused("python3 -c 'import os; os.system(\"id\")'")


class TestRepositoryScriptsThatWrite:
    """`python3 scripts/…` was accepted by prefix. Three of those scripts commit,
    push, or rewrite every version header in the ruleset."""

    def test_the_release_cut_is_refused(self):
        refused("python3 scripts/release_cut.py")

    def test_the_archive_cut_is_refused(self):
        refused("python3 scripts/archive_cut.py")

    def test_opening_a_pull_request_is_refused(self):
        refused("python3 scripts/open_pr.py --branch main --message-file x")

    def test_a_script_that_does_not_exist_is_refused(self):
        refused("python3 scripts/not_a_real_script.py")


class TestACommandThatCannotRunIsAFailure:
    """Exit 1 is an answer — `grep -c` prints 0 and exits 1, and a task may
    expect exactly that. Exit 2 is the command itself failing."""

    @staticmethod
    def change(tmp_path, monkeypatch, codes: dict[str, int]):
        directory = tmp_path / "a-change"
        directory.mkdir()
        (directory / "tasks.md").write_text(
            "".join(
                f"- [x] {number} Run `{command}` — expect **0**.\n"
                for number, command in enumerate_commands(codes)
            )
        )
        monkeypatch.setattr(verify_tasks, "CHANGES_DIR", tmp_path)
        monkeypatch.setattr(
            verify_tasks, "run", lambda command: (f"(exit {codes[command]})", codes[command])
        )

    def test_an_exit_of_two_fails_the_run(self, tmp_path, monkeypatch, capsys):
        self.change(tmp_path, monkeypatch, {"grep -c x docs/": 2})
        assert verify_tasks.verify("a-change") == 1
        assert "cannot run" in capsys.readouterr().out

    def test_an_exit_of_one_does_not(self, tmp_path, monkeypatch):
        self.change(tmp_path, monkeypatch, {"grep -c x docs/a.md": 1})
        assert verify_tasks.verify("a-change") == 0

    def test_a_command_not_on_path_fails_the_run(self, tmp_path, monkeypatch):
        self.change(tmp_path, monkeypatch, {"openspec validate a-change": 127})
        assert verify_tasks.verify("a-change") == 1


def enumerate_commands(codes: dict[str, int]):
    return [(f"1.{index}", command) for index, command in enumerate(codes, start=1)]


class TestTaskParsing:
    def test_a_command_and_its_expectation_are_read_off_one_line(self):
        tasks = '- [x] 2.1 Run `grep -c "x" docs/07-movement.md` — before: **2**, after: **0**.\n'
        (number, ticked, command, expectation), = verify_tasks.tasks_with_commands(tasks)
        assert number == "2.1"
        assert ticked is True
        assert command == 'grep -c "x" docs/07-movement.md'
        assert expectation == "before: **2**, after: **0**."

    def test_a_continuation_line_is_folded_into_the_expectation(self):
        tasks = (
            "- [ ] 3.2 Run `grep -c TRN-005 docs/09-transport.md`\n"
            "      before: **2** (TRN-005's own sentence),\n"
            "      after: **0**.\n"
        )
        (_, ticked, _, expectation), = verify_tasks.tasks_with_commands(tasks)
        assert ticked is False
        assert "after: **0**." in expectation

    def test_a_refused_command_is_still_recognised_as_one(self):
        # Otherwise it is mistaken for prose and skipped without a word, instead
        # of being reported as NOT RUN.
        tasks = "- [ ] 4.1 Run `find docs -name '*.md' -delete` — expect **0**.\n"
        (_, _, command, _), = verify_tasks.tasks_with_commands(tasks)
        assert command.startswith("find ")

    def test_an_inline_span_that_is_not_a_command_is_ignored(self):
        tasks = "- [ ] 1.1 Replace the body of `WPN-021` with the block below.\n"
        assert verify_tasks.tasks_with_commands(tasks) == []
