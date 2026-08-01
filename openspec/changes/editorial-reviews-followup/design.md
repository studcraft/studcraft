## Context

Three defects found while reviewing the merged diff of `editorial-reviews-cleanup` (#31). All three are self-inflicted by that change: two are placement consequences of text it inserted, and one is dead weight in a spec delta it authored.

The verification #31 carried could not have caught any of them. Its greps assert counts, anchors and absence of leakage — all of which passed. None of them can detect that a correctly-inserted paragraph landed somewhere that reads badly, or that a correctly-written scenario asserts nothing. Those need a reader.

## Decisions

### Fix by moving, never by rewording

All three fixes are moves or deletions. No sentence is reworded, because none is wrong — #31's text was reviewed and is correct. Rewording now would invite drift from text that has already been agreed and shipped, and would make the diff harder to check than the problem warrants.

This is why `tasks.md` asserts byte-identity after each move, and why its verification counts occurrences rather than matching prose: the only failure mode worth guarding against is a paragraph being copied instead of moved, or subtly retyped.

### DMG-004's paragraph goes back where it was, mid-list, on purpose

The move puts a commentary paragraph between Example 4 and Example 5, interrupting an otherwise continuous list. That looks wrong at a glance and is worth stating plainly, because a reviewer will notice it.

It is nonetheless correct. The paragraph was written as the closing commentary on Examples 3 and 4, when those were the final two examples in the rule. Examples 5 and 6 arrived with `resistance-clarification-review`, and Example 7 with #31 — each inserted ahead of the paragraph, each pushing it one step further from what it discusses. The paragraph did not drift; it was displaced three times.

Restoring its original position is the fix that requires no new text. The alternatives were worse: rewording it to name Examples 3 and 4 explicitly means editing shipped prose that is not wrong, and giving it a heading means inventing a section the document's structure does not otherwise use — `---` inside a rule would also conflict with the convention that `---` separates rules.

The paragraph does partly self-identify, since it cites "(Resistance 3)" and "(Resistance 4)". That is why this is the weakest of the three findings and is presented as such rather than as a correctness issue.

### Correct #31's spec delta rather than defer to archive time

Defect 3 sits in a merged change's delta file. Two options existed.

Leaving it and dropping the scenario during `archive-cut` keeps this change purely `docs/`-scoped, but it makes correctness depend on a future reader spotting a scenario that reads as reasonable — the exact reason it survived review in the first place. If missed, a scenario that no legal build can violate lands permanently in `openspec/specs/weapon-construction/spec.md`.

Correcting the delta now costs one deletion and removes the dependency on future vigilance. The delta has not been archived, so the living spec is untouched either way; the difference is only whether the fix is guaranteed or remembered.

### A separate change, not an amendment

While `editorial-reviews-cleanup` was unmerged, amending it was correct and was drafted as its section 7 — the vacuous scenario in particular had no existence outside that change, so no other change could sensibly claim to modify it.

Merging inverted that. #31's proposal and tasks now document work that shipped and verified; appending an amendment would edit the record of a finished change and leave its verification section describing a state that no longer matches its own tasks. The three fixes stand on their own and get their own change directory, branch and PR. #31 is left exactly as it merged.

## Risks / Trade-offs

- **Moving a paragraph can silently duplicate it.** The likeliest failure is an insert without the corresponding delete. Tasks 4.4 and 4.5 count occurrences and require exactly one each.
- **Editing a merged change's directory is unusual** and will look odd in the diff. The proposal states why in its Impact section so a reviewer does not have to reconstruct the reasoning.
- **Defect 2 is a matter of taste.** Whether a summary should close on its architectural statement or on its plainest sentence is a judgement, not a correctness issue. It is included because #31 introduced the line specifically as a closing statement and then did not place it last.

## Open Questions

None. Not applied — proposal only.
