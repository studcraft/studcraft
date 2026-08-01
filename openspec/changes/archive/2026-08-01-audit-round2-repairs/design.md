## Context

Second-pass audit against `full-audit-repairs` (#28). Its own closing note is worth restating here: of the 24 findings, all but one (R-01) were propagation misses — a canonical rule was fixed correctly, but a summary, glossary entry, or mirror rule elsewhere that restated the same fact wasn't updated alongside it. R-01 was the exception: a genuine systemic consequence of a correct fix, not a missed reference.

## Goals / Non-Goals

**Goals:** Fix R-01 without touching anything that didn't need to change (Impact Strength scale, infantry weapon-size ceiling, WPN-018 proportion rule all stay exactly as they are); close every propagation gap the second pass found; adopt the audit's own closing recommendation (when changing a canonical rule, also check its own document's Summary, its `14-glossary.md` entry, and every rule that cites it by ID) as a checklist for this change's own edits, to avoid generating a third-pass audit.

**Non-Goals:** Re-opening any of the five other design decisions from `full-audit-repairs` (A-01, A-04, A-05, A-06, A-07) — none of the second-pass findings challenge them.

## Decisions

### R-01: minifig Resistance is a fixed baseline, not a construction measurement

**Alternative 1 considered — rescale Impact Strength to plate layers (e.g. `Impact Strength = muzzle size × 3`)**: rejected. Muzzle size (`WPN-002`) is a *width* measurement on the Weapon Front (studs across), while Resistance is a *depth* measurement (plate layers through the component) — these are orthogonal LEGO-grid dimensions with no natural conversion factor between them. Multiplying one by 3 to match the other's unit would be an arbitrary retrofit, and it changes every weapon's Impact Strength in the game, not just the infantry case that's actually broken.

**Alternative 2 considered — raise infantry's effective Platform Length, or exempt infantry weapons from WPN-018's proportion rule**: rejected. `WPN-004`'s Platform Length ceiling is the same mechanism that makes "small platforms carry light weapons, large platforms carry heavy weapons" true for *every* unit type, vehicles included — carving out an infantry-specific exception here reintroduces the "infantry gets its own physics" pattern this repo's review process has already eliminated at least twice (Findings 1 and 5 of `ruleset-consistency-fixes`).

**Chosen — a minifig is not "built" the way a shield or hull is, so DMG-003's construction-derived measurement doesn't apply to it.** A minifig torso is a single fixed, pre-molded LEGO piece — there is no player decision analogous to "build this shield from bricks vs. plates" for a minifig's body. `DMG-003` now explicitly scopes its plate-layer measurement to *constructed* components, and states that a fixed piece (a minifig, named as the concrete case that matters) uses a set baseline instead. This preserves `DMG-008`'s "no material-specific mechanics" principle *in spirit* — the distinction being drawn is constructed-vs-fixed, not organic-vs-plastic, and it would apply identically to any other fixed, non-modular piece the ruleset introduced later (e.g. a standard wheel, if its Resistance were ever specified). No other value changes: Impact Strength, the infantry weapon-size ceiling, and every constructed-component example in `DMG-004` are untouched.

### N-01: Resistance added to the Gameplay Geometry taxonomy, with a structural-vs-decorative carve-out

The audit's exploit was real and literal: `GEO-002` listed "decorative armour" as Visual Geometry with no caveat, and Resistance never appeared in `GEO-001`/`GEO-003`'s lists of what Visual Geometry is *not* allowed to affect — so, read literally, bolting decorative plates onto a hull could inflate its Resistance for free. Fixed by adding Resistance to both lists and adding the missing rule to `GEO-002`: a plate is Visual Geometry only if it sits *outside* the structural cross-section an Impact must cross. A plate that's actually in the way structurally is Gameplay Geometry no matter how decorative it looks — the same "function beats appearance" principle `GEO-003`'s own weapon example already uses (a decorative antenna not part of the Weapon Body doesn't change Range; a plate not part of the structural path doesn't change Resistance).

### N-02: Repairs get an equipment requirement and a self-repair limit

Two problems, two independent fixes: `CORE-014` already requires visible equipment for anything a unit "uses," and `DMG-019` let a unit repair *another* unit with nothing in hand — fixed by requiring visible repair equipment for that case specifically. Self-repair ("standing up") doesn't need equipment — a soldier doesn't need a med-kit to stand — but was unlimited, which the audit correctly flagged as making Wounded purely nominal (no cost, no limit, heals every turn for free). Limited to once per activation: Wounded still means something within a single Turn, without inventing a new "medic" role or equipment sub-system nobody asked for.

### N-03/N-04: procedure gaps resolved by extending already-established rules, not new mechanics

Both gaps existed because a newer rule (B-02's "1 AP per weapon system," or DMG-018's rotating-mount exception) was added without checking its interaction with an older one (CBT-001's single-target procedure, MEL-003's per-weapon Attack Dice count). Both are resolved by stating the interaction explicitly rather than inventing anything: split-target attacks verify each sub-target individually and still cost the one AP CBT-001 already defines; dual-wielding costs 2 AP for 2 dice because two independently wielded weapons are already, by WPN-008's own definition, two weapon systems.

### N-05: falling damage declared as an explicit Geometry Check exception

`MOVE-016` was never wrong mechanically (DMG-008 already establishes no material-specific hit thresholds, and a fall genuinely has no attacker or Impact Strength to check) — it just never said so, leaving an undeclared gap between it and DMG-009's canonical sequence. Declared explicitly rather than silently: falling has no Impact Strength, so there's no Geometry Check to run, and Resistance plays no role. Scoped to infantry only, since vehicle falling is already an acknowledged gap from `full-audit-repairs` (B-08) — no reason to solve half of a gap that's already honestly documented as open.

## Risks / Trade-offs

- [Risk] R-01 introduces a "constructed vs. fixed piece" distinction that didn't exist before, which is new conceptual surface area even though it changes no numbers beyond the minifig case. → Mitigation: scoped narrowly (only stated for the minifig, the concrete case the audit found broken), framed explicitly as compatible with DMG-008 rather than an exception to it.
- [Risk] This is the second consecutive round of audit-driven fixes; a third-pass audit could plausibly find more propagation misses from this round's own edits. → Mitigation: applied the audit's own recommended checklist (check the doc's Summary, its glossary entry, and every citing rule) while making each edit this round, specifically to reduce that risk — not a guarantee, but a deliberate change in process from the first round.

## Open Questions

None outstanding.
