"""`apply_tasks.py` writes the ruleset, so what is tested here is mostly what it
refuses to write.

The one thing an applier must never do is edit a document to make something
pass. A script cannot be tempted, but it can be *wrong* in the same direction:
replacing an anchor that matched twice, applying a task somebody already
applied, or writing half a change and stopping. Each of those has its own test
below.

Nothing here touches the real checkout. `REPO_ROOT` and `CHANGES_DIR` are
pointed at `tmp_path` and `git` is replaced, which is also what lets a test say
"this is `main`" without checking anything out.
"""

from __future__ import annotations

import apply_tasks
import pytest
import tasks_format


@pytest.fixture
def repo(tmp_path, monkeypatch):
    """A repository shaped like this one, on a branch named for `a-change`."""
    root = (tmp_path / "repo").resolve()
    (root / "docs").mkdir(parents=True)
    (root / "openspec" / "changes" / "a-change").mkdir(parents=True)

    monkeypatch.setattr(apply_tasks, "REPO_ROOT", root)
    monkeypatch.setattr(apply_tasks, "CHANGES_DIR", root / "openspec" / "changes")
    monkeypatch.setattr(tasks_format, "REPO_ROOT", root)
    monkeypatch.setattr(apply_tasks, "git", lambda *args: (0, "a-change"))
    return root


def write_tasks(repo, body: str) -> None:
    (repo / "openspec" / "changes" / "a-change" / "tasks.md").write_text(body)


def read_tasks(repo) -> str:
    return (repo / "openspec" / "changes" / "a-change" / "tasks.md").read_text()


def edit_task(number: str, path: str, anchor: str, replacement: str, ticked=False) -> str:
    mark = "x" if ticked else " "
    return (
        f"- [{mark}] {number} In `{path}`, replace this anchor:\n\n"
        f"```\n{anchor}\n```\n\nwith:\n\n```\n{replacement}\n```\n\n"
    )


def run(argv: list[str]) -> int:
    return apply_tasks.main(argv)


class TestItApplies:
    def test_an_edit_lands_and_its_box_is_ticked(self, repo, capsys):
        (repo / "docs" / "02-core-rules.md").write_text("before\nold text\nafter\n")
        write_tasks(repo, edit_task("1.1", "docs/02-core-rules.md", "old text", "new text"))

        assert run(["--write", "a-change"]) == 0
        assert (repo / "docs" / "02-core-rules.md").read_text() == "before\nnew text\nafter\n"
        assert "- [x] 1.1" in read_tasks(repo)

    def test_a_later_anchor_may_be_text_an_earlier_task_wrote(self, repo):
        """Changes here anchor audit sections against post-change text on purpose."""
        (repo / "docs" / "02-core-rules.md").write_text("one\n")
        write_tasks(
            repo,
            edit_task("1.1", "docs/02-core-rules.md", "one", "two")
            + edit_task("2.1", "docs/02-core-rules.md", "two", "three"),
        )

        assert run(["--write", "a-change"]) == 0
        assert (repo / "docs" / "02-core-rules.md").read_text() == "three\n"

    def test_a_deletion_is_an_empty_replacement(self, repo):
        (repo / "docs" / "02-core-rules.md").write_text("keep\ndrop me\nkeep\n")
        write_tasks(
            repo,
            "- [ ] 1.1 In `docs/02-core-rules.md`, replace this anchor:\n\n"
            "```\ndrop me\n\n```\n\nwith:\n\n```\n```\n\n",
        )

        assert run(["--write", "a-change"]) == 0
        assert "drop me" not in (repo / "docs" / "02-core-rules.md").read_text()

    def test_a_letter_suffixed_task_number_is_read(self, repo):
        (repo / "docs" / "02-core-rules.md").write_text("old\n")
        write_tasks(repo, edit_task("13c.1", "docs/02-core-rules.md", "old", "new"))

        assert run(["--write", "a-change"]) == 0
        assert "- [x] 13c.1" in read_tasks(repo)


class TestItRefuses:
    def test_an_anchor_matching_twice_stops_the_run(self, repo, capsys):
        (repo / "docs" / "02-core-rules.md").write_text("same\nsame\n")
        write_tasks(repo, edit_task("1.1", "docs/02-core-rules.md", "same", "changed"))

        assert run(["--write", "a-change"]) == 1
        assert (repo / "docs" / "02-core-rules.md").read_text() == "same\nsame\n"
        assert "occurs 2 times" in capsys.readouterr().out

    def test_a_missing_anchor_on_an_unticked_task_stops_the_run(self, repo, capsys):
        (repo / "docs" / "02-core-rules.md").write_text("nothing like it\n")
        write_tasks(repo, edit_task("1.1", "docs/02-core-rules.md", "absent", "new"))

        assert run(["--write", "a-change"]) == 1
        assert "do not adjust the document to fit" in capsys.readouterr().out

    def test_one_blocked_pair_stops_every_other_pair(self, repo):
        """A run that wrote the good half and stopped would leave the ruleset
        inconsistent, and the tick marks would not say where it got to."""
        (repo / "docs" / "02-core-rules.md").write_text("fine\ntwice\ntwice\n")
        write_tasks(
            repo,
            edit_task("1.1", "docs/02-core-rules.md", "fine", "applied")
            + edit_task("2.1", "docs/02-core-rules.md", "twice", "no"),
        )

        assert run(["--write", "a-change"]) == 1
        assert (repo / "docs" / "02-core-rules.md").read_text() == "fine\ntwice\ntwice\n"
        assert "- [ ] 1.1" in read_tasks(repo)

    def test_a_ticked_task_is_never_re_applied(self, repo):
        (repo / "docs" / "02-core-rules.md").write_text("old\n")
        write_tasks(
            repo, edit_task("1.1", "docs/02-core-rules.md", "old", "new", ticked=True)
        )

        assert run(["--write", "a-change"]) == 0
        assert (repo / "docs" / "02-core-rules.md").read_text() == "old\n"

    def test_an_additive_edit_already_in_place_is_not_applied_again(self, repo):
        """The anchor is repeated inside the replacement as a landmark, so it
        still matches after the edit. The count alone cannot tell."""
        (repo / "docs" / "02-core-rules.md").write_text("kept line\nadded line\n")
        write_tasks(
            repo,
            edit_task(
                "1.1", "docs/02-core-rules.md", "kept line", "kept line\nadded line",
                ticked=True,
            ),
        )

        assert run(["--write", "a-change"]) == 0
        assert (repo / "docs" / "02-core-rules.md").read_text() == "kept line\nadded line\n"

    def test_a_spec_under_openspec_specs_is_refused(self, repo, capsys):
        spec = repo / "openspec" / "specs" / "unit-base"
        spec.mkdir(parents=True)
        (spec / "spec.md").write_text("old\n")
        write_tasks(
            repo, edit_task("1.1", "openspec/specs/unit-base/spec.md", "old", "new")
        )

        assert run(["--write", "a-change"]) == 1
        assert "only the Archive cut writes" in capsys.readouterr().out

    def test_the_changelog_is_refused(self, repo, capsys):
        (repo / "CHANGELOG.md").write_text("old\n")
        write_tasks(repo, edit_task("1.1", "./CHANGELOG.md", "old", "new"))

        assert run(["--write", "a-change"]) == 1
        assert "Release cut" in capsys.readouterr().out

    def test_a_version_header_is_refused(self, repo, capsys):
        (repo / "docs" / "02-core-rules.md").write_text("**Version:** 0.1.0\n")
        write_tasks(
            repo,
            edit_task(
                "1.1", "docs/02-core-rules.md", "**Version:** 0.1.0", "**Version:** 0.2.0"
            ),
        )

        assert run(["--write", "a-change"]) == 1
        assert "Version headers belong to the Release cut" in capsys.readouterr().out

    def test_a_target_outside_the_repository_is_refused(self, repo, capsys):
        outside = repo.parent / "elsewhere.md"
        outside.write_text("old\n")
        write_tasks(repo, edit_task("1.1", "../elsewhere.md", "old", "new"))

        assert run(["--write", "a-change"]) == 1
        assert outside.read_text() == "old\n"

    def test_main_is_refused(self, repo, monkeypatch, capsys):
        monkeypatch.setattr(apply_tasks, "git", lambda *args: (0, "main"))
        (repo / "docs" / "02-core-rules.md").write_text("old\n")
        write_tasks(repo, edit_task("1.1", "docs/02-core-rules.md", "old", "new"))

        assert run(["--write", "a-change"]) == 1
        assert (repo / "docs" / "02-core-rules.md").read_text() == "old\n"
        assert "Git Workflow" in capsys.readouterr().err

    def test_a_branch_not_named_for_a_docs_change_is_refused(self, repo, monkeypatch):
        monkeypatch.setattr(apply_tasks, "git", lambda *args: (0, "some-other-branch"))
        (repo / "docs" / "02-core-rules.md").write_text("old\n")
        write_tasks(repo, edit_task("1.1", "docs/02-core-rules.md", "old", "new"))

        assert run(["--write", "a-change"]) == 1
        assert (repo / "docs" / "02-core-rules.md").read_text() == "old\n"

    def test_a_change_touching_no_docs_may_be_applied_from_any_branch(
        self, repo, monkeypatch
    ):
        """The gate it mirrors only constrains the name when docs/*.md changes."""
        monkeypatch.setattr(apply_tasks, "git", lambda *args: (0, "some-other-branch"))
        (repo / "TODO.md").write_text("old\n")
        write_tasks(repo, edit_task("1.1", "./TODO.md", "old", "new"))

        assert run(["--write", "a-change"]) == 0
        assert (repo / "TODO.md").read_text() == "new\n"


class TestCheckWritesNothing:
    def test_check_reports_what_write_would_do_and_changes_nothing(self, repo, capsys):
        (repo / "docs" / "02-core-rules.md").write_text("old\n")
        write_tasks(repo, edit_task("1.1", "docs/02-core-rules.md", "old", "new"))

        assert run(["--check", "a-change"]) == 0
        assert (repo / "docs" / "02-core-rules.md").read_text() == "old\n"
        assert "- [ ] 1.1" in read_tasks(repo)
        assert "Re-run with --write" in capsys.readouterr().out


class TestTheModeIsRequired:
    def test_no_mode_is_a_usage_error(self, repo):
        write_tasks(repo, "")
        assert run(["a-change"]) == 2

    def test_an_unknown_change_is_reported(self, repo):
        assert run(["--check", "no-such-change"]) == 1
