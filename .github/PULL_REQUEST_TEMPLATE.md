<!--
Delete whichever sections do not apply. A one-line typo fix does not need
the whole form — but if you are touching docs/, the OpenSpec section is not
optional, and CI will tell you so.
-->

## What this changes

<!-- One or two sentences. What is different after this merges? -->

## Why

<!--
The reasoning, not the restatement. If this fixes a contradiction between two
rules, name both. If it closes a gap, say where the gap was declared.
-->

---

## If this touches `docs/` (the ruleset)

- [ ] There is a change under `openspec/changes/<name>/` with `proposal.md`, `design.md` and `tasks.md`
- [ ] This branch is dedicated to that one proposal — `openspec/config.yaml` requires one branch per proposal
- [ ] The proposal states plainly whether this is a **mechanical change** (it changes what is legal at the table) or **editorial** (it does not)
- [ ] Every rule this touches was read in full, not just the lines being edited
- [ ] No rule ID was renumbered, reused or deleted — IDs are stable, superseded rules keep their number with a note
- [ ] `python3 scripts/lint_ruleset.py` passes

## Design check

The ruleset has fifteen principles in `CODE_OF_DESIGN.md`. These three catch most problems:

- [ ] **The model is the rules** — could a player read this off the LEGO model instead of a written value?
- [ ] **Reuse before invention** — does this extend an existing system (Impacts, Action Points, Unit Bases, Component States) rather than adding a parallel one?
- [ ] **One source of truth** — is this rule stated once, with everything else pointing at it? Restating a rule in a second document is how they drift apart.

## What you deliberately did *not* do

<!--
Optional, and the most useful section in this template.

If you considered a change and rejected it, record it and why. Reviews on this
repo have repeatedly re-proposed things that had already been considered and
turned down, because nobody wrote down the reason. See MEL-010 and CBT-011 for
how the ruleset itself handles this.
-->

---

## Not touching `docs/`?

Then most of the above does not apply. Say what changed and why, and check:

- [ ] Workflow or script changes explain what breaks if they are wrong
- [ ] Nothing under `docs/` or `openspec/specs/` is modified — those have their own gated paths
