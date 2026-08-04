# Delegating to Agents

Applying a well-specified change is mechanical work. Designing it, and
auditing the result, is not. Splitting those two apart along model capability
is cheaper and — measurably, in this repo — no less safe.

This document is about how to write a change so a less capable model executes
it perfectly, and what the reviewer still has to do afterwards.

---

# The Agents, and When to Raise Them

All three roles are defined as repository agents in `.claude/agents/`, so the
constraints below do not have to be retyped from memory each session. They
had been, and they drifted.

| Agent | Model | When |
|---|---|---|
| `ruleset-auditor` | Opus, read-only | **Twice per change** — on the proposal before it is applied, and on the applied text afterwards. Also on `docs/` at any time. |
| `proposal-applier` | Sonnet | Once the proposal has passed its audit. Transcription only. |
| `git-operator` | Haiku | After you have read the result. Branch, commit, push, open the PR. Decides nothing. |

The order matters and is not decoration:

1. Design the change and write `proposal.md`, `design.md`, `tasks.md`.
2. **Raise `ruleset-auditor` on the proposal.** This is where the findings
   are — see the evidence below. Fix what it reports before applying, not
   after.
3. **Raise `proposal-applier`** to apply it. Give it the absolute working
   directory and the branch.
4. **Raise `ruleset-auditor` again on the applied text.**
5. **Read the result yourself.** That step never belongs to an agent, and
   nothing below changes it.
6. Then `git-operator` may issue the commands. It is handed the paths, the
   branch name and the message text — it chooses none of them. Delegating the
   typing is not delegating the judgement, and the judgement is step 5.

`ruleset-auditor` has no `Edit` or `Write` tool by construction, so it cannot
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

Replacement text is shown as a markdown blockquote so it is visually separable
from the instructions around it. That creates two failure modes to pre-empt
explicitly, both of which have happened:

- **The `> ` prefix is not part of the text.** Say so in the preamble.
- **A `#` heading or a `|` table inside a block is real markdown**, not
  quoted text. Say that too.

## Define the vocabulary the tasks use

"Replace the entire body of `RULE-NNN`" is ambiguous until you say that the
body is everything between the rule's `#` heading and the `---` that ends it,
and that the heading itself is never touched.

## Verify every anchor is unique before shipping the tasks

Every quoted anchor must appear exactly once in its target file. Check with
`grep -cF` and state in the tasks that it was checked. An anchor that matches
twice produces a silent wrong edit.

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

## Provide a coverage table

Map every defect or item in `proposal.md` to the task that addresses it, and
recompute the totals mechanically. Counts stated in prose go stale as soon as
anything is added.

---

# What the Reviewer Still Has to Do

Delegation moves the work, it does not remove it.

- **Read the applied text in full**, not the diff. See `system/proposal-review.md`
  — the findings are in how the result reads, and no grep sees that.
- **Check the document's Summary and glossary entry** for every rule touched.
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

# Scope Agents Explicitly

`.claude/agents/proposal-applier.md` already carries the standing boundaries —
never `git add -A`, never touch `assets/studio/`, no amend, no rebase, no
force-push, no push, no PR. What still has to be said per invocation:

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
