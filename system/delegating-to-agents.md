# Delegating to Agents

Applying a well-specified change is mechanical. Designing it, and auditing the
result, is not. This document is how to write a change a less capable model
executes perfectly, and what the reviewer still has to do.

The four roles and when to raise them are in `AGENTS.md`. They are defined in
`.claude/agents/` so they are not retyped from memory each session — they had
been, and they drifted.

---

# The Order

1. Design the change: `proposal.md`, `design.md`, `tasks.md`.
2. **Raise `proposal-auditor`.** Fix what it reports before applying.
3. **Raise `proposal-applier`.** Give it the absolute working directory and the
   branch.
4. **Raise `ruleset-auditor` on the applied text.**
5. **Read the result yourself.** That step never belongs to an agent.
6. **Then `git-operator`** issues the commands, handed the paths, the branch
   name and the message text. It chooses none of them.

Across every delegated change so far, **every defect found afterwards was in
the proposal, not in the execution.** That is the whole argument for the split:
judgement goes into writing and auditing, transcription goes to the applier.

Neither auditor has `Edit` or `Write`, by construction, so neither can repair
what it is measuring. Keep it that way.

Two appliers hit a verification whose stated expectation was wrong and
**reported it instead of editing the ruleset to satisfy a bad check**. That is
the standard.

---

# Writing Tasks a Weaker Model Executes Perfectly

## Give the replacement text verbatim

Never describe an edit — write out exactly what the file should say. If
applying a task requires composing prose, the task is underspecified.

Replacement text goes in a **triple-backtick fence**. State in the preamble
that the fence is not part of the text, and that a `#` heading or `|` table
inside it is real markdown. `scripts/check_task_anchors.py` rejects the old
blockquote form and any mix of the two.

## Define the vocabulary the tasks use

"Replace the body of `RULE-NNN`" is ambiguous until you say the body is
everything between its heading and the `---` that ends it, heading untouched.

## Verify every anchor is unique before shipping the tasks

An anchor matching twice produces a silent wrong edit.
`python3 scripts/check_task_anchors.py <change-name>` counts every anchor
against its target, and distinguishes a zero-match anchor on an unticked task
(a defect) from one on a ticked task (an applied change).

## State what must NOT change

Mark verify-only tasks as verify-only, and name the rules that stay untouched.
A capable executor will otherwise "improve" text the proposal left alone.

## Fix every value in a table, never let it be derived

Tabulate every before/after value. One change renamed weapons without stating
their muzzle sizes, and two rules used "Heavy Cannon" for different weapons —
an executor deriving values backwards would have hit a collision it could not
know existed.

## Test the verification commands against the pre-change state

A verification that has never been run encodes a guess. Three shipped wrong: a
`grep -c "1 Action Point"` against a rule reading "1 **additional** Action
Point", a `grep "^> "` expecting zero hits in documents that all end with an
epigraph, and a count of "the four files" in a directory of five.

`python3 scripts/verify_tasks.py <change-name>` runs each command and prints
what the task expected beside what the command printed. It judges neither. It
runs read-only commands only — a `tasks.md` is a file anyone can open a PR
against.

## Provide a coverage table

Map every item in `proposal.md` to the task that addresses it, and recompute
totals mechanically. Counts stated in prose go stale.

---

# What the Reviewer Still Has to Do

- **Read the applied text in full**, not the diff (`system/proposal-review.md`).
  `python3 scripts/rule.py touched <change-name>` names the rules changed and,
  under `read also`, the rules that cite them.
- **Check the document's Summary and glossary entry** for every rule touched —
  `system/proposal-review.md` ("The Summary Is Part of the Rule").
- **Ask what the executor had to interpret.** Every interpretation reported is
  a place the proposal was unclear.

---

# Isolate Parallel Work in Worktrees

Two changes can be applied concurrently with `git worktree add <path> <branch>`,
one agent per worktree. Before splitting, check two things: whether they edit
the same document (they will conflict at merge time regardless, and a squash
merge makes that conflict much larger than the disagreement — see
`system/repository-strategy.md`), and whether one's text cites wording the other
introduces (then merge order is not optional).

Remove worktrees when done: `git worktree remove <path> --force`.

---

# Commands That Do Not Interrupt

An agent that stops to ask for permission cannot be left running. What decides
is not danger — it is whether the command is **static enough to match a
permission pattern**. A command carrying a shell expansion can never be
allowlisted, whatever is added to `.claude/settings.json`.

- **One bare command per call.** No `&&`, no `;`, no pipe, no redirection.
- **No `$VAR`, no `$(…)`, no loops.** To run over seven rule IDs, pass seven
  arguments — `scripts/rule.py`'s subcommands are variadic for this reason, and
  that is the shape for any new script an agent will call.
- **No backticks inside a `grep` pattern.** A backtick is command substitution,
  so an otherwise read-only `grep` stops being auto-allowed.

---

# Scope Agents Explicitly

`.claude/agents/*.md` carry the standing boundaries. Per invocation, state: the
working directory as an absolute path, the branch and that it must not be left,
the change name, and anything specific the agent could not infer. Ask for a
short report — what was applied, what verification failed and how, what was
ambiguous.

## The commit message

Whoever read the result writes it; `git-operator` is handed the text. The
subject is a conventional `type(scope): …` under 72 characters — `docs(...)`
for `docs/`, `chore(...)` for repository plumbing. The body is prose
paragraphs. Read `git log origin/main..HEAD` for the style, **not** plain
`git log`: `main` carries squashed PR titles ending in `(#NN)`, which is
GitHub's format for a merge, not the format for a commit. End with:

```
Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
```

**Deciding the result is fit to push stays with the reviewer, who has read it.**
`git-operator` then calls `scripts/open_pr.py`, which stages one path at a time
and verifies the staged set against the given set, so the BLOCKER rules in
`system/repository-strategy.md` become things it cannot do rather than things
it is trusted to avoid. The agent stays in front of the script because a script
cannot notice that something is off in a way nobody anticipated.
