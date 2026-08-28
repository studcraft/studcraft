---
paths:
  - "scripts/*.py"
  - "tests/*.py"
  - ".github/workflows/*.yml"
  - ".claude/**/*.md"
  - ".claude/*.json"
---

# Scripts, CI gates, hooks and agent definitions

- `system/ci-gates.md` — required-check design pitfalls: a required check must
  trigger on every pull request unconditionally, a branch-name exemption must
  additionally be constrained by content, and shared state needs a concurrency
  guard. Read it before adding or editing a workflow.
- `system/delegating-to-agents.md` — what belongs in a `.claude/agents/`
  definition, and what the reviewer still has to do afterwards.
- `system/documentation-standards.md` — Repository Structure, how a rule is
  written, and Naming Conventions: **a script never names a rule that exists**,
  in code, comment, docstring or `--help`. A new script states its own job in
  its docstring; the structure table names directories, not files.

`.claude/settings.json` also carries the `permissions` block. Its `deny` list is
the git commands `system/repository-strategy.md` forbids and
`.claude/agents/git-operator.md` lists verbatim — it adds no policy of its own,
and anything added to it that those two documents do not already forbid is a
policy change wearing a configuration disguise. `.claude/settings.local.json` is
per-machine and gitignored; nothing another checkout must have belongs there.

**`allow` holds a broad `Bash(git *)`, and the `deny` list is what makes that
safe.** Permission patterns match by prefix, so `Bash(git status*)` does not
cover `git -C /path status` — and there is no end to the variants worth chasing
one at a time. Denying the destructive commands and allowing the rest closes the
whole class instead, and `deny` wins over `allow` where they overlap. The
consequence to remember: **a new destructive git command is only forbidden if it
is on the `deny` list.** Adding one there is now the control, not omitting it
from `allow`.

`gh` is deliberately *not* broad. Its read-only subcommands are listed one by
one, because `gh api` can POST and PATCH — `scripts/open_pr.py` reaches it as a
subprocess, which needs no permission entry of its own.

A local hook and a CI gate are not alternatives. The gate is authoritative and
runs for everyone; the hook only moves the same refusal earlier, before a push.
When you change one, check whether the other now disagrees with it.

**A `PreToolUse` hook sees `Write` and `Edit`, not a script writing through
`Bash`.** `scripts/apply_tasks.py` is the one script that edits `docs/` on
purpose, so it restates for itself what `guard_repo_edits.py` would have
refused: `main` and `develop`, a branch not named for a change that edits
`docs/*.md`, `openspec/specs/`, `CHANGELOG.md`, a `**Version:**` header, and any
path outside the repository. A new script that writes repository files inherits
that obligation — the hook will not cover it.

`scripts/preflight.py` is the same bargain in script form: it mirrors four of
the workflows plus all three checker scripts so a push is not the first thing to
report a red gate. **Editing a workflow means checking the mirror against it.**

**`tests/` covers `scripts/`, and a change to a script belongs in the same
commit as the test that pins it.** pytest is a development dependency and
`scripts/` stays stdlib-only — every script runs as `python3 scripts/<name>.py`
on a machine with nothing set up:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-dev.txt
.venv/bin/pytest
```

A test imports the script it covers by module name (`import verify_tasks`),
which works because `pytest.ini` sets `pythonpath = scripts`. **That is a
runtime setting and an editor does not read it**, so `pyrightconfig.json`
repeats the path for the language server — the two have to agree, and a test
that resolves in one and not the other is the symptom. Nothing else states it:
no editor's own settings are committed here.

`preflight.py` runs the suite when it can find pytest and reports it skipped
when it cannot. A test that mutates a repository builds one in `tmp_path` and
copies `scripts/` into it — never the real working directory
(`system/ci-gates.md`, "Test Any Repo-Mutating Script in an Isolated
Worktree").

`.claude/hooks/lint_after_edit.py` watches `Bash` as well as `Write` and `Edit`,
because a shell command that writes carries no `file_path` for a hook to read.
It decides by modification time rather than by reading the command — deciding
intent from a shell string is a losing game, and the attempt matched a commit
message quoting a path. Anything that adds a generated file under `.studcraft/`
should keep that split in mind: the directory is a cache, gitignored, and never
a source of truth.
