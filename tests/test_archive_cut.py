"""The batch archives several changes in one run, and one of them can be refused
half way through. What is tested here is what it says when that happens: the
ones already archived are moved on disk, and a run that stops without naming
them leaves whoever picks it up guessing.

`openspec` itself is never invoked — the call is replaced, so these run on a
machine that does not have the CLI installed.
"""

from __future__ import annotations

import subprocess

import archive_cut
import pytest


class FakeOpenSpec:
    """Stands in for `openspec archive`, failing on the names it was told to."""

    def __init__(self, failing: set[str] | None = None):
        self.failing = failing or set()
        self.calls: list[str] = []

    def __call__(self, args, **kwargs):
        assert args[:2] == ["openspec", "archive"]
        name = args[2]
        self.calls.append(name)
        if name in self.failing:
            return subprocess.CompletedProcess(
                args, 1, "", f"Error: {name} delta does not match the living spec"
            )
        return subprocess.CompletedProcess(args, 0, f"Archived {name}", "")


@pytest.fixture
def changes(tmp_path, monkeypatch):
    """A changes/ directory the test fills in, with `archive/` already present."""
    root = tmp_path / "changes"
    (root / "archive").mkdir(parents=True)
    monkeypatch.setattr(archive_cut, "CHANGES_DIR", root)
    monkeypatch.setattr(archive_cut, "unarchived_changes", lambda: sorted(
        path.name for path in root.iterdir() if path.is_dir() and path.name != "archive"
    ))
    return root


def add_change(changes, name: str, tasks: str | None) -> None:
    directory = changes / name
    directory.mkdir()
    if tasks is not None:
        (directory / "tasks.md").write_text(tasks)


DONE = "- [x] 1.1 Apply it\n- [x] 1.2 Verify it\n"
PENDING = "- [x] 1.1 Apply it\n- [ ] 1.2 Verify it\n"


def test_every_fully_applied_change_is_archived(changes, monkeypatch, capsys):
    add_change(changes, "a-change", DONE)
    add_change(changes, "b-change", DONE)
    fake = FakeOpenSpec()
    monkeypatch.setattr(subprocess, "run", fake)

    assert archive_cut.main() == 0
    assert fake.calls == ["a-change", "b-change"]
    assert "Archived: a-change, b-change" in capsys.readouterr().out


def test_a_change_with_unchecked_tasks_is_left_alone(changes, monkeypatch, capsys):
    add_change(changes, "a-change", PENDING)
    add_change(changes, "b-change", DONE)
    monkeypatch.setattr(subprocess, "run", FakeOpenSpec())

    assert archive_cut.main() == 0
    out = capsys.readouterr().out
    assert "Archived: b-change" in out
    assert "still has unchecked items): a-change" in out


def test_a_change_with_no_tasks_file_is_reported_as_such(changes, monkeypatch, capsys):
    add_change(changes, "a-change", None)
    add_change(changes, "b-change", DONE)
    monkeypatch.setattr(subprocess, "run", FakeOpenSpec())

    assert archive_cut.main() == 0
    out = capsys.readouterr().out
    assert "no tasks.md" in out
    assert "a-change" in out.split("no tasks.md")[1]


def test_a_failure_names_what_was_already_archived(changes, monkeypatch, capsys):
    add_change(changes, "a-change", DONE)
    add_change(changes, "b-change", DONE)
    add_change(changes, "c-change", DONE)
    monkeypatch.setattr(subprocess, "run", FakeOpenSpec(failing={"b-change"}))

    assert archive_cut.main() == 1
    captured = capsys.readouterr()
    assert "Archived: a-change" in captured.out
    assert "STOPPED on b-change" in captured.err
    assert "1 change(s) were archived before it" in captured.err


def test_a_failure_stops_the_batch(changes, monkeypatch):
    add_change(changes, "a-change", DONE)
    add_change(changes, "b-change", DONE)
    add_change(changes, "c-change", DONE)
    fake = FakeOpenSpec(failing={"b-change"})
    monkeypatch.setattr(subprocess, "run", fake)

    archive_cut.main()
    assert "c-change" not in fake.calls


def test_nothing_to_archive_is_not_a_success(changes, monkeypatch, capsys):
    add_change(changes, "a-change", PENDING)
    monkeypatch.setattr(subprocess, "run", FakeOpenSpec())

    assert archive_cut.main() == 1
    assert "Nothing to archive" in capsys.readouterr().out
