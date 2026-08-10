# Delegating to Agents

Applying a well-specified change is mechanical work. Designing it, and
auditing the result, is not. Splitting those two apart along model capability
is cheaper and — measurably, in this repo — no less safe.

This document is about how to write a change so a less capable model executes
it perfectly, and what the reviewer still has to do afterwards.

---

# The Agents, and When to Raise Them

All four roles are defined as repository agents in `.claude/agents/`, so the
constraints below do not have to be retyped from memory each session. They
had been, and they drifted.

| Agent | Model | When |
|---|---|---|
| `proposal-auditor` | Opus, read-only | On the proposal, before it is applied. This is where the findings are. |
| `proposal-applier` | Sonnet | Once the proposal has passed its audit. Transcription only. |
| `ruleset-auditor` | Opus, read-only | On the applied text afterwards. Also on `docs/` at any time. |
| `git-operator` | Haiku | After you have read the result. Branch, commit, push, open the PR. Decides nothing. |

The order matters and is not decoration:

1. Design the change and write `proposal.md`, `design.md`, `tasks.md`.
2. **Raise `proposal-auditor`.** This is where the findings are — see the
   evidence below. Fix what it reports before applying, not after.
3. **Raise `proposal-applier`** to apply it. Give it the absolute working
   directory and the branch.
4. **Raise `ruleset-auditor` on the applied text.**
5. **Read the result yourself.** That step never belongs to an agent, and
   nothing below changes it.
6. Then `git-operator` may issue the commands. It is handed the paths, the
   branch name and the message text — it chooses none of them. Delegating the
   typing is not delegating the judgement, and the judgement is step 5.

The two audits were one agent until the checks below became scripts. Auditing a
proposal and auditing applied text read different inputs against different
checklists, and one prompt holding both made each of them vaguer.

Neither auditor has an `Edit` or `Write` tool, by construction, so neither can
quietly repair what it is measuring. Keep it that way.

---

# The Split, and the Evidence For It

Across every delegated change so far, the executing agents applied the tasks
faithfully: no invented text, no missed anchors, no renumbered rule IDs, every
verification run. **Every defect found afterwards was in the proposal, not in
the execution.**

That is the whole argument. Writing the proposal and auditing the applied text
are where judgement is needed and where the findings actually are. Applying it
is transcription.

Two of the executing agents also did something better than obedience, which is
worth naming as the standard: each hit a verification whose stated expectation
was wrong, and **did not edit the ruleset to satisfy a badly-written check**.
They reported the discrepancy instead. An agent that quietly "fixes" documents
to make a grep pass has done real damage.

---

# Writing Tasks a Weaker Model Executes Perfectly

## Give the replacement text verbatim

Never describe an edit. Write out exactly what the file should say. If
applying a task requires composing prose, the task is underspecified and the
result will drift.

Replacement text goes inside a **triple-backtick fence**, so it is visually
separable from the instructions around it. Two failure modes to pre-empt
explicitly in the preamble, both of which have happened:

- **The fence is not part of the text.** Say so.
- **A `#` heading or a `|` table inside a fence is real markdown**, not quoted
  text. Say that too.

Changes up to 2026-08-07 used a `> ` blockquote instead, and the switch was an
improvement rather than drift: a blockquote forces a `> ` onto every line of the
replacement — including its blank lines and its table rows — and every one of
those prefixes is a character the applier has to strip correctly. A fence has no
per-line prefix to get wrong.

The convention moved on 2026-08-10 and `.claude/agents/proposal-applier.md`
went on describing the old one for several changes afterwards. Nothing broke,
because each `tasks.md` states its own convention in its preamble and the file
wins — but an applier reading one format in its instructions and meeting another
in the file is the situation a weaker model is least able to recover from.
`scripts/check_task_anchors.py` now rejects a `tasks.md` that uses the old form
or mixes the two, so the two cannot drift apart again silently.

## Define the vocabulary the tasks use

"Replace the entire body of `RULE-NNN`" is ambiguous until you say that the
body is everything between the rule's `#` heading and the `---` that ends it,
and that the heading itself is never touched.

## Verify every anchor is unique before shipping the tasks

Every quoted anchor must appear exactly once in its target file. An anchor that
matches twice produces a silent wrong edit.

`python3 scripts/check_task_anchors.py <change-name>` counts every anchor
against its target, and `scripts/preflight.py` runs it over every unarchived
change. It also distinguishes the two readings of a zero-match anchor: on an
unticked task that is a defect, and on a ticked one it is the expected state of
an applied change. State in the tasks that anchors were checked; the script is
how you can honestly say it.

## State what must NOT change

Mark verify-only tasks as verify-only. Name the rules that stay untouched and
why. A capable executor will otherwise "improve" adjacent text that the
proposal deliberately left alone.

## Fix every value in a table, never let it be derived

When a change rescales numbers, tabulate every before/after value. Do not rely
on the executor computing them.

This matters more than it sounds. One change renamed weapons in its examples
without ever stating their muzzle sizes — the sizes existed only implicitly,
inside the old values being replaced. Worse, two different rules used the name
"Heavy Cannon" for weapons of different sizes. An executor deriving the new
values backwards would have had to resolve a collision it had no way to know
existed.

## Test the verification commands against the pre-change state

A verification that has never been run encodes a guess. Three shipped wrong:

- `grep -c "1 Action Point"` expecting a rule that actually reads "1
  **additional** Action Point", which the pattern cannot match.
- `grep "^> "` expecting zero hits, when every document legitimately ends with
  a `> **Every Brick Matters.**` epigraph.
- A count of "the four files" in a directory holding five.

Run each check before shipping the tasks and write down the number it actually
returns, along with the count expected afterwards.

`python3 scripts/verify_tasks.py <change-name>` runs every verification command
a `tasks.md` contains and prints, side by side, what the task said to expect and
what the command actually printed. It judges neither — which half of a
"before/after" applies depends on whether the change has been applied, and the
file cannot say. It only puts both on one screen, which is enough: a fourth
check shipped as `grep -c "..." docs/` with no `-r`, exiting 2 on a directory,
and one run would have shown it.

It executes read-only commands only. A `tasks.md` is a file anyone can open a
pull request against, and running arbitrary commands out of one is how a
checked-in file becomes a way to execute code.

## Provide a coverage table

Map every defect or item in `proposal.md` to the task that addresses it, and
recompute the totals mechanically. Counts stated in prose go stale as soon as
anything is added.

---

# What the Reviewer Still Has to Do

Delegation moves the work, it does not remove it.

- **Read the applied text in full**, not the diff. See `system/proposal-review.md`
  — the findings are in how the result reads, and no grep sees that.
  `python3 scripts/rule.py touched <change-name>` says which rules those are,
  and — under `read also` — which rules cite them. A change to a rule five
  others lean on has five more places to read, and nothing in the change itself
  reveals them.
- **Check the document's Summary and glossary entry** for every rule touched.
  Neither is mechanically checkable: these Summaries are prose that mostly names
  no rule IDs, so only reading catches drift.
- **Ask what the executor had to interpret.** Requiring that in the agent's
  report is how the underspecified parts of a proposal surface. Every
  interpretation an executor reports is a place the proposal was unclear.

---

# Isolate Parallel Work in Worktrees

Two changes can be applied concurrently with `git worktree add <path> <branch>`,
one agent per worktree. They commit to their own branches and cannot collide.

Two cautions, both hit in practice:

- **Check for shared files first.** Two branches editing the same document
  will conflict at merge time regardless of worktree isolation, and after a
  squash merge that conflict is much larger than the real disagreement (see
  `system/repository-strategy.md`).
- **Check for semantic dependencies.** If one change's text cites wording the
  other introduces, parallel application is fine but merge order is not
  optional.

Remove worktrees when done: `git worktree remove <path> --force`.

---

# Commands That Do Not Interrupt

An agent that stops to ask for permission cannot be left running. The rule that
decides whether it asks is not about danger — it is about whether the command is
**static enough to be matched by a permission pattern**.

**A command carrying a shell expansion can never be allowlisted.** `$id`, `$(…)`,
a `for` loop, a chain of `;` or `&&`, a pipe, a redirection — each makes the
command dynamic, and no rule can match what is not fixed until the shell runs it.
Adding entries to `.claude/settings.json` does nothing for these. The only fix is
not to write them.

So, in an agent definition and in anything handed to an agent:

- **One bare command per call.** Never `a && b`, never `a; b`, never a pipe.
- **No `$VAR` and no `$(…)`** in arguments.
- **No loops.** If a command needs running over seven rule IDs, pass seven
  arguments — `scripts/rule.py`'s `show`, `refs`, `neighbors`, `touched` and `doc`
  are variadic for exactly this reason, and that is the shape to reach for when
  writing any new script an agent will call.
- **No backticks inside a `grep` pattern.** A backtick is command substitution to
  the shell, so an otherwise read-only `grep` stops being auto-allowed.

The allowlist in `.claude/settings.json` covers the repository's own scripts, the
read-only `git` subcommands and `grep`. `grep` is on it deliberately: it is
auto-allowed only for arguments the harness can prove safe, and removing the
explicit entry once made every pattern containing a backtick interrupt.

---

# Scope Agents Explicitly

`.claude/agents/proposal-applier.md` already carries the standing boundaries —
never `git add -A`, no amend, no rebase, no force-push, no push, no PR.
What still has to be said per invocation:

- The working directory, as an absolute path.
- The branch, and that it must not be left.
- The change name.
- Anything specific to this change that the agent could not infer.

Ask for a short report — what was applied, what verification failed and how,
and what was ambiguous.

**Deciding that the result is fit to push stays with the reviewer, who has
read it.** `git-operator` runs the commands afterwards and is given the paths,
the branch name and the message text; it never selects them. `system/ci-gates.md`
records why that step is local at all — the org blocks GitHub Actions from
creating pull requests, so both cut workflows push a branch and stop.

Most of that sequence is now `scripts/open_pr.py`, which `git-operator` calls.
The BLOCKER rules in `system/repository-strategy.md` stop being instructions an
agent is trusted to follow and become things it has no way to do: the script
issues `git add` once per path it is given and nothing else, and it verifies the
staged set against the given set before committing. The agent is kept in front
of it deliberately — a script cannot notice that something is off in a way
nobody anticipated, and that noticing is the whole reason a reader is there.
