---
name: add-image
description: The order in which a drawn example image reaches the rule that specified it — where the file goes, reading it against its entry in assets/IMAGES.md, asking the maintainer, and the proposal that places it and nothing else. Use whenever a file appears in or disappears from assets/images/, and whenever asked to add, place, replace or remove a ruleset example image.
---

# Placing a drawn example image

`assets/IMAGES.md` names the images the ruleset needs and specifies each one:
which rule, which filename, what it must show, and why the prose cannot carry
the fact alone. This is what happens once one of them is drawn — or once one is
taken away.

**Nothing routes you here on its own.** The flow begins with a file appearing in
`git status`, which is not an edit and not a prompt, so a session can be well
into the work before anyone notices which procedure it is in. That is why the
order below is written down rather than assembled each time.

## What this produces, and all it produces

One embed line per image, in the one document that specifies it. The image file.
The change directory. **Nothing else** — no rule text, no citation, and **not
`assets/IMAGES.md`**. `scripts/check_image_change.py` refuses the rest and
`scripts/preflight.py` runs it.

## Do not improve this order

Steps 1, 4 and 6 each exist because they were got wrong, twice, in consecutive
placements: a proposal written before the image had been read, a file nearly
committed inside the change directory, an entry nearly rewritten after the
maintainer had already accepted the drawing, and two audits paid for one
proposal. Every fact needed to avoid all four was already written down. What was
missing was the order.

---

## 1. The file goes to `assets/images/`

Under the name its entry already gave it. `assets/IMAGES.md` decided the path
when the entry was written, and it is the only path an embed can point at.

**Not the change directory. Not `docs/`.** A removal is this step backwards: the
file leaves `assets/images/`.

If no entry names the file, **stop — this is not that procedure.** The entry is
where the argument for an image is written, and writing one is an editorial
change on its own branch, decided before anything is drawn. Placement comes
after.

## 2. `python3 scripts/insert_images.py --check`

It says what changed and in which direction: a file nobody listed, an entry
whose image is drawn but not placed, an embed whose file or entry is gone.

Mechanical. It settles nothing else — it checks that a file exists, never what
is in it.

## 3. Read the image against its entry

Does it show what the entry's *What it must show* column asked for? Name the
differences plainly; no script can answer this.

## 4. Ask the maintainer. The answer is final

The question has exactly two answers: **the image is accepted, or it is
redrawn.**

**An accepted image does not change its entry.** The *What it must show* column
was the instruction given to whoever drew it, and it stays as the record of what
was asked for. Do not narrow it to fit the drawing, and do not offer to. If the
maintainer wants the entry itself changed, that is a separate change on its own
branch, after this one.

Ask before writing anything. Asking first costs one question; asking last costs
the proposal.

## 5. Branch, and propose only the placement

Branch from current `main` (`system/repository-strategy.md`, "Creating a new
branch"), named for the change directory — the branch and the directory must
match, or `insert_images.py --write` refuses.

The proposal states no rule, retires no ID, moves no citation and does not touch
`assets/IMAGES.md`. `design.md` names the image file as the non-`docs/` path the
branch carries and says why, which `system/repository-strategy.md` ("Branch
Naming") requires. `tasks.md` has no anchor pairs: the embed is written by a
command, not transcribed.

## 6. Audit — once

Raise `proposal-auditor` (AGENTS.md, "Delegating Work") on this brief:

> The change places one image the maintainer has already accepted. Two
> questions: does the entry for this rule still argue for the image on its own
> terms — the *Why text alone is not enough* column — and is the diff exactly
> the embed line, the image file and the change directory? The drawn image, the
> entry's wording and the rule's wording are out of scope; the maintainer
> settled them before the proposal was written.

**A second audit of the same proposal asks the same two questions twice.** If a
finding changes the proposal, re-audit that finding, not the change.

## 7. Apply

Raise `proposal-applier`. There is nothing to transcribe: it runs
`python3 scripts/insert_images.py --write` on the branch and verifies what the
command wrote against what `tasks.md` said to expect.

## 8. Verify

```bash
python3 scripts/preflight.py
```

Every check, including `check_image_change.py`. Then
`python3 scripts/insert_images.py --write` a second time: it must print no
`Wrote` line at all. A second write that changes something is a defect.

## 9. Audit the applied text

Raise `ruleset-auditor`. AGENTS.md makes all four roles mandatory and does not
exempt a small change, so it is raised here even though an embed line states no
rule, moves no ID and adds no citation. Point it at the one document the
placement touched and at the rule the image now sits under.

## 10. Read the result yourself

Never an agent's step (AGENTS.md). The embed sits under the rule's own prose,
before the `---` that closes it — not under the next rule.

## 11. Hand the commands to `git-operator`

Give it the branch name, the message text and the paths by name: the image, the
document, the change directory. **The image is committed with the embed**, or
`docs/` points at a file that is not in the repository.

---

`assets/IMAGES.md` owns everything this procedure does not: which rules need an
image, the entry format, the filename convention, the size and format limits,
and the record of candidates considered and turned down.
