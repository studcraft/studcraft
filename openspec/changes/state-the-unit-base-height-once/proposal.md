# State the Unit Base's height once

## Why

`CORE-001` defines the Unit Base as `4 studs wide × 3 studs deep × 12 plate layers
tall`. The literal phrase `12 plate layers` then appears **24 times across seven
ruleset documents**, three further sites build a formula on that height
(`12N + (N − 1)`, in `TRN-020`, `VEH-028` and `assets/IMAGES.md`), three more state a
fraction derived from it (`⅓ UB`, `⅔ UB`, "three quarters of a Unit Base"), and two
more restate it in words (`08-vehicles.md`'s "one Unit Base of height for every two
studs", the glossary's "half a Unit Base").

Those sites divide cleanly, and the division is the whole proposal:

- **Where the unit is introduced or defined**, the figure belongs and stays — five of
  the twenty-four: three in `CORE-001` (the dimension line and both projection rows),
  the glossary's *Unit Base* entry, and `01-foundations.md`'s overview, which states
  it and immediately names `CORE-001` as the authority. `README.md` and
  `CODE_OF_DESIGN.md` (Principle 7) carry the same line outside `docs/` and stay for
  the same reason.
- **One is a derivation** — `VEH-028`'s "4 plate layers for every stud" — which
  computes with the height rather than quoting it, and needs redesigning rather than
  rewording when the height changes (see Out of Scope).
- **Three are measured values that coincide with it** — the drone, motorbike and
  walker rows of `TRN-013`'s cargo table, each 12 plate layers tall. A height read
  from a model is not a restatement of `CORE-001`, even when the two agree, so those
  cells are left exactly as they are.
- **The remaining fifteen are uses**, each a copy of something that already has an
  owner. `system/documentation-standards.md` ("What `system/` Is For") gives the
  standard they fail: one owner per rule, a pointer instead of a copy, always.

The copies are not harmless. Three costs, all present in the shipped text:

- **The arithmetic goes stale invisibly.** `TRN-013`'s table computes `⅓ UB` for a
  4-plate crate and `⅔ UB` for an 8-plate pallet. Those fractions are not read from
  any model — they are `4 / 12` and `8 / 12`, and nothing in the repository connects
  them back to the 12 they were divided by.
- **A formula stands in for a rule.** `TRN-020` says N levels need
  `12N + (N − 1) plate layers`. What the builder actually needs is one Unit Base of
  clear height per level plus a plate for each floor above the lowest — the same fact,
  read off the model instead of computed.
- **The same sentence is written twice in two documents, and they disagree.**
  `CORE-001` derives its height from a minifigure being "about 4 bricks from its feet
  to the top of its head" and cites `CMP-018`; `CMP-018` says "A minifigure **on its
  base** stands about 4 bricks tall, which is where those 12 plate layers come from"
  and cites `CORE-001`. Each defers to the other, and the two differ by exactly the
  plate the model stands on.

There is a second reason, and it is the immediate one. A follow-up change will alter
the Unit Base's height from 12 plate layers to 13, because a minifigure standing on
the base `SCS-002` requires of it measures 4 bricks plus that base's plate — verified
against a render placing the model beside a stack of 4 bricks and 1 plate, flush,
stud for stud. **This change makes no dimensional change of its own.** It retires the
copies first, so that the change which does moves the figure only where the figure is
the definition. `design.md`, "Rejected", records why the reverse order costs twice as
many edits.

## What Changes

Nothing a player measures. Every model legal before this change is legal after it,
every distance and Action Point cost is untouched, no rule is added, removed or
renumbered, and no rule's outcome changes.

- **`CORE-001`** keeps every figure — it is the owner — and stops citing `CMP-018`
  for the minifigure height it states itself.
- **`CMP-018`** stops restating the vertical projection's figures and the derivation
  behind them, and points at `CORE-001` for both.
- **`TRN-001`**, **`TRN-003`**, **`TRN-019`** and the transport Summary express
  clearance as *one Unit Base of clear height* — one phrase, used in every one of
  those places, replacing four different figures and phrasings.
- **`TRN-003`**'s cargo example stops saying three crates "fill" a Unit Base and says
  they *share* one. What a crate occupies is its own height; that three of them come
  to exactly the height of a Unit Base is arithmetic on the figure, not a fact about
  crates.
- **`TRN-013`** states the slice budget as the Unit Base's height and drops the
  `Space` column, whose every value was a fraction of 12 rather than something read
  from a model. The `Footprint` and `Height` columns stay exactly as they are, plate
  counts included.
- **`TRN-019`**'s cargo bullet drops "three quarters of a Unit Base" for *a partial
  Unit Base*, which is `TRN-003`'s existing term for a position that does not hold a
  whole one. Its opening paragraph, which relied on the figure to justify a
  "therefore", is rewritten to say what it actually measures.
- **`TRN-020`** loses its formula. Each level needs one Unit Base of clear height
  above its own floor, and each floor above the lowest costs what it measures. Its
  table loses the `Plate layers` and `Bricks` columns — both are `CORE-001`
  arithmetic, and `CORE-001` already states that twelve plate layers is exactly four
  bricks. Its worked example stops being "a vehicle exactly 8 bricks tall" and
  becomes "an interior exactly two Unit Bases tall": a quiet correction as well as a
  rewording, since the rule has always measured from the lowest interior floor rather
  than from the ground.
- **`VEH-028`**'s closing paragraph in `08-vehicles.md` stops reprinting `TRN-020`'s
  formula and points at it. Its worked answers — one level at 4 studs across, three
  at 8, five at 12 — are unchanged and were re-derived.
- **`WPN-004`**'s note in `10-weapons.md` says the Unit Base's *height* never enters
  Platform Length, without quoting it.
- **`14-glossary.md`**'s *Interior Clearance* and *Slice* entries use the Unit Base
  instead of the figure. The *Unit Base* entry keeps its dimensions: defining the
  term is what a glossary is for.
- **`assets/IMAGES.md`** stops quoting the deleted `TRN-020` formula, and its
  `TRN-019` image brief stops instructing an illustrator to draw "12 clear layers"
  for a rule that will no longer say so. Both rejections and both briefs otherwise
  stand.

## Out of Scope

- **The height itself.** It stays 12 plate layers here. The change to 13 is separate
  and comes next.
- **The three overview surfaces** — `01-foundations.md`, `README.md`,
  `CODE_OF_DESIGN.md` (Principle 7). Each states the dimension line and immediately
  defers to `CORE-001`; each introduces the unit rather than using it. `design.md`,
  Decision 4, records the line drawn here and why removing the figure from one of
  the three, as an earlier draft of this change did, was worse than leaving all three.
- **`VEH-028`'s two derivations** — "A Unit Base is 12 plate layers tall on a
  narrowest side of 3 studs — 4 plate layers for every stud" and "one Unit Base of
  height for every two studs" (`08-vehicles.md`), restated as "half a Unit Base" in
  the glossary's *Maximum Height* entry. These compute a ratio *from* the height
  rather than quoting it for convenience, and the ratio stops dividing evenly when
  the height changes: they need redesign, not rewording, and belong to the change
  that moves the number.
- **Vertical cargo overflow.** What happens when one object's slices exceed a Unit
  Base's height is genuinely undefined in the current ruleset, and an earlier draft
  of this change tried to settle it in one sentence. `design.md`, Decision 3, records
  the question and why answering it needs its own proposal.
- **Distances, ranges and Resistance.** Movement steps, weapon ranges and structural
  thickness stay in studs and plate layers. They measure lengths and material, not
  occupied volume; `design.md`, "Rejected", says why converting them would be worse.
- **`openspec/specs/`.** No requirement changes, so there is no delta — see
  `design.md`, "Why no spec delta". Archiving stays a separate PR
  (`system/workflow.md`, Archiving).
- **`CHANGELOG.md` and every `**Version:**` header.** Release-cut-only
  (`system/documentation-standards.md`, Versioning).
