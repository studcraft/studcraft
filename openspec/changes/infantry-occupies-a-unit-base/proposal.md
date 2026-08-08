# Infantry occupies a Unit Base rather than being mounted on one

## Why

`CORE-003` says infantry are "LEGO minifigures **mounted on** a standard Unit Base",
and `CORE-001` says of the volume it has just defined, "This is the **standard base**
for infantry."

`unit-base-is-a-volume` (#73) made a Unit Base a volume. A model is not mounted on a
volume and a volume is not a base — both sentences were true of the 4 × 3 plate they
were written against, and neither survived the change of unit.

The reading they invite is the one an external review of `02-core-rules.md` arrived
at: that a Unit Base *is* a mandatory physical baseplate, so the term names a LEGO
part rather than a measurement. The ruleset already contradicts that, but never in
one place:

- A Unit Base is a volume and a measurement (`CORE-001`), not a part. A vehicle
  covering 2 UB contains no 4 × 3 plates at all — its footprint "is defined by the
  LEGO model itself" (`CORE-004`).
- Infantry, nonetheless, **is** required to be built on a physical base
  (`SCS-002`), and that base is load-bearing: `CORE-002` reads facing off its 4-stud
  edge, and `MOVE-003` measures movement "from the edge of the base".

So the requirement is real, the term is a measurement, and the confusion comes from
three documents stating the requirement in three voices while the two sentences that
define the unit use words that no longer fit it.

**The requirement is not being removed.** Removing it is what the review asks for,
and it would strip the physical referent from facing and from movement measurement —
two rules that currently read a value off the model, which is what Principle 1 asks
of them. `design.md`, "Rejected", records that with the evidence.

One pointer is wrong for a related reason. `SCS-001` says "see `02-core-rules.md`
(CORE-001) for its definition (4 × 3 studs)" — it promises the definition and then
gives figures that stopped being it. #73's `design.md` states the test that decides
such a pointer: it changes "because it presents the definition rather than pointing
at a use of it." `SCS-001`'s subject is the unit itself, so the test applies to it.
It does not apply to the pointers in `DEP-001` and `VEH-001`, which read a
deployment area and a footprint — uses, in #73's terms — and those stay as they are.

## What Changes

- **`CORE-001`** stops calling the volume the standard base for infantry. It says
  what the volume is to an infantry model — **read horizontally**, the size of the
  base it is built on — and points at `SCS-002` for the requirement. The qualifier
  matters: the base is 4 × 3 studs, not 4 × 3 × 12.
- **`CORE-003`** loses the words "mounted on a standard Unit Base" and keeps
  occupancy, which is its own job and what other rules cite it for. It gains nothing:
  the base is mentioned two rules earlier, in `CORE-001`.
- **`SCS-002`** keeps the requirement and says what is required: a physical base
  measuring one Unit Base read horizontally. It stops naming the front edge, which
  `CORE-002` owns.
- **`MOVE-002`** cites `SCS-002` and `CORE-002` instead of restating both, states no
  size of its own, and keeps its own sentence — that the base's orientation defines
  movement and line of advance.
- **`MOVE-004`** asks a player to measure by "laying spare **Unit Bases** end to
  end". One word changes, to *infantry bases*: a volume cannot be laid down, and the
  plate a player actually lays is `SCS-002`'s. #73 left this sentence standing on
  `CORE-001`'s old identification of plate with base, which this change removes.
- **`SCS-001`** calls the Unit Base a *measuring* unit rather than "the fundamental
  **building** unit", and defers to `CORE-001` without quoting figures, in the form
  #73 gave `01-foundations.md`. Its next sentence names the horizontal projection, so
  "corresponds to the footprint of a LEGO minifigure" stays true against a volume.
  `measuring` is `CORE-001`'s own word; `consolidate-core-measurements` chose
  `building` on purpose, to keep a "construction-standard-specific framing", and that
  framing rested on the unit being a 4 × 3 plate — which #73 ended. Principle 7's
  unmodified "the fundamental unit of the game" would also have worked; `measuring`
  wins because `SCS-001`'s own next clause points at `CORE-001`, so the noun and the
  pointer agree.

The requirement itself is stated in full in exactly one place, `SCS-002`. `CORE-001`
and `MOVE-002` each mention that a base exists and cite it; `CORE-003` no longer
mentions it at all.

No dimension changes. No Action Point cost changes. No rule is added, removed or
renumbered.

## Impact

- Affected documents: `docs/02-core-rules.md`, `docs/04-construction-standard.md`,
  `docs/07-movement.md`. Ten anchors: eight verbs or pointers — one of which,
  `SCS-001`'s first sentence, also renames the unit's kind — plus one subject
  (`SCS-001`'s second sentence) and one pronoun (`MOVE-002`'s third).
- Affected capabilities: none. No requirement in `openspec/specs/unit-base/spec.md`
  changes — its scenario already reads "**WHEN** an infantry model is placed on its
  standard base / **THEN** it occupies exactly one Unit Base". See `design.md`,
  "Why no spec delta".
- Rule IDs: none added, removed or renumbered. The header count is 225 before and
  after.
- **What this costs an already-built model: nothing.** Every model legal before is
  legal after. `SCS-002` requires exactly what it required; the change is that it
  now says what the base measures.
- **This narrows two of #73's decisions and reverses neither.** Both are named in
  `design.md`, Decisions 3 and 4, so a later reader can see what changed and why.

## Out of Scope

- **Decoupling the Unit Base from the infantry base**, which the external review
  recommends. Rejected with evidence in `design.md`.
- **`DEP-001`'s and `VEH-001`'s `(4 × 3 studs)` pointers.** #73 exempted them as
  uses rather than definitions, and that holds: a deployment area and a footprint
  are horizontal readings. Qualifying them would restate `CORE-001`'s projection
  table in two more documents.
- **`CMP-018`'s "Every model on the table stands on Unit Bases".** Loose as written
  — a vehicle stands on no 4 × 3 plate — but it is reading the measurement, not the
  component, and the width it derives is correct. Separate change.
- **`CORE-001`'s height datum**, phrased as "the top face of the plate an infantry
  model stands on" while defining a universal unit. `TRN-019` generalises it for
  interiors and `VEH-029` supplies a vehicle's datum. Real, and separate: it changes
  the requirement text in `openspec/specs/unit-base/spec.md`, which this change does
  not touch.
- **`SCS-003`'s "size ceiling (none — the agreed Deployment Area naturally limits
  model size)".** Loose since #75: `VEH-028` bounds a vehicle's height off the same
  footprint `SCS-003` points at. Read as *footprint* size the sentence is still true,
  so this is imprecision rather than a contradiction, and it is #75's to repair —
  recorded here because `SCS-003` sits one rule below an edited rule and would
  otherwise be re-found.
- **A glossary entry for the infantry base.** After this change the term appears in
  rule body text exactly once, in `MOVE-004` ("laying spare infantry bases end to
  end"), plus the two `Infantry Base` headings. `SCS-002` defines it, and `MOVE-002`
  cites `SCS-002` twenty-four lines above `MOVE-004`, so a reader who meets the term
  can reach its owner. That is the whole argument for leaving the glossary alone, and
  it is a judgement rather than a certainty — an entry citing `SCS-002` would be
  consistent with `Slice`, `Projection` and `Base Plane`, and adding one later breaks
  nothing. It is out of scope here because it would make a fourth document part of a
  change whose applied text has already been audited.
- **`openspec/specs/unit-base/spec.md`'s "placed on its **standard base**".** After
  this change that phrase survives nowhere in `docs/` and only there, in the scenario
  this proposal cites as the reason no delta is needed. The reasoning still holds — a
  standard base does exist and does occupy one Unit Base — but the wording is the
  part-reading a reader of `docs/` will no longer meet. It cannot be repaired from
  this branch: `openspec/specs/` is Archive-cut-only state and the `PreToolUse` hook
  refuses the write. For the archive cut, or a later delta.
- **`VEH-029` and the glossary's `Base Plane` entry saying a vehicle's Unit Bases
  "rest on" a surface.** Volumes do not rest. The same looseness as `CMP-018`'s
  "stands on Unit Bases", pre-existing and untouched, and sharper now that
  `CORE-001` reserves the physical base to infantry. Recorded so all three siblings
  are on the same list.
