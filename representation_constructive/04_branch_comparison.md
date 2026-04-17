# Branch Comparison

All branch scores below use the same rubric:

- exact phrase strength
- spatial coherence
- instance coherence
- number of assumptions
- attachment of detached clues
- whether any operation has an unresolved object slot
- whether a unique final integer emerges cleanly
- whether the story is globally cleaner than the old procedure-first story

Heavy penalties:

- disconnected same-word merges
- deleting glue words to improve a phrase
- promoting a candidate integer before an exact operation chain exists
- unresolved object slots

## Branch A: Pure Representation / Conversion Story

### Best exact evidence

- `hexadecimal ten ten ten integer` at `I3 -> I4 -> I5 -> I6 -> H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11 / C12 -> B13 -> C14 / C13 -> D14 -> E14 / F14 -> G13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- `decimal ten ten ten integer` at `H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11 / C12 -> B13 -> C14 / C13 -> D14 -> E14 / F14 -> G13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- `binary ten integer by six` at either:
  - `F10 -> E10 -> E11 -> E12 -> E13 -> F13 / F14 -> G13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
  - `F10 -> F11 -> E11 -> E12 -> E13 -> F13 / F14 -> G13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
- `hexadecimal ten ten ten integer by six`
- `decimal ten ten ten integer by six`
- `baseten integer`
- `base ten integer`
- `step baseten integer`
- `step base ten integer`

### Assessment

- exact phrase strength: very strong
  - the family is dominated by technical labels and repeatable exact tails
- spatial coherence: very strong
  - almost everything important lives in one lower-right component
- instance coherence: very strong
  - many nodes reuse the same `integer`, `ten`, `base/baseten`, `by`, and `six` instances
- number of assumptions: moderate
  - some interpretation is still needed for what `ten ten ten` means numerically
- attachment of detached clues: moderate
  - the branch now absorbs more than before because the same lower-right component also includes a binary bridge to the total cluster
  - it still does not absorb `find the start ...` or `three ten hundred(s)` exactly
- unresolved object slot: low-moderate
  - weaker than the old procedure story because the phrases mostly name objects and tails rather than under-specified actions
- unique final integer emerges cleanly: no
- globally cleaner than the old procedure-first story: yes

### Verdict

- This is still the cleanest branch overall.
- The crucial improvement over the prior audit is that the representation family exact-attaches not only to `integer by six`, but indirectly to the total cluster through binary bridge nodes in the same component.

## Branch B: Representation Plus Place-Value Extraction

### Best exact evidence

- `decimal tens`
- `hexadecimal tens`
- `binary tens`
- `get nine total`
- `get nine tens`
- `binary get nine total`
- `binary get nine tens`
- `get ones`
- `three ten hundred`
- `three ten hundreds`

Representative coordinates:

- `binary get nine total`
  - `F10 -> E10 -> E11 -> E12 -> E13 -> F13 / F12 -> G13 -> F14 / E14 -> D13 -> C14 -> B13 / C13 -> D12 -> C12 -> B11 -> B10`
- `binary get nine tens`
  - `F10 -> E10 -> E11 -> E12 -> E13 -> F13 / F12 -> G13 -> F14 / E14 -> D13 -> C14 -> D14 / C13 -> B13 -> A12 -> A11`
- `get ones`
  - `J3 -> J2 -> K2 / K3 -> L4 -> M5 -> M6`
- `three ten hundred`
  - `C3 -> B2 -> C2 -> B3 -> A4 / B5 -> C4 -> C5 / B6 -> C6 -> D5 -> D4 -> D3 -> D2 -> C1`

### Assessment

- exact phrase strength: strong
  - especially in the lower-right binary bridge subfamily
- spatial coherence: mixed
  - the lower-right `binary get nine total` and `binary get nine tens` phrases are coherent
  - `get ones` and `three ten hundred(s)` are still detached
- instance coherence: mixed-strong
  - the lower-right binary place-value material is coherent
  - a full `ones/tens/hundreds` decomposition still requires disconnected merges
- number of assumptions: moderate-high
  - the branch wants a digit or place-value extraction rule that is not yet stated exactly
- attachment of detached clues: better than before, but incomplete
  - the branch now does absorb the old `get nine total` fragment via binary
  - it still does not absorb the top ribbon or upper-left hundreds family cleanly
- unresolved object slot: moderate
  - better than the old procedure story, worse than pure representation
  - the missing piece is what exactly is being extracted or totaled from the representation object
- unique final integer emerges cleanly: no
- globally cleaner than the old procedure-first story: yes

### Verdict

- This branch absorbs more clue surface area than the prior audit gave it credit for.
- It is not yet cleaner than Branch A because the place-value part is still under-specified and spatially split.
- The best version of Branch B is really a binary-centered refinement of Branch A, not a fully separate global solve.

## Branch C: Salvaged Procedure Story Only Where It Attaches Exactly

### Best exact evidence

- `find the start` at `E1 -> F1 -> G1 -> H1 / I1 -> J1 -> J2 / K1 -> K2 -> L1 -> M1 -> N1`
- `find the start nine` at the same first three word instances plus `M2 -> M3 -> L4 -> K4` or `M2 -> M3 -> L4 -> M5`
- `find the start nine go` at the same first four word instances plus `J3 -> K3`
- `step by six`
- `step into integer by six`
- `get nine total`

### Assessment

- exact phrase strength: mixed
  - several local phrases are real
  - the exact action chain is still fragmented
- spatial coherence: weak-mixed
  - the top ribbon remains detached from the lower-right component
- instance coherence: weak
  - the branch still wants disconnected `nine` and `step` instances to play one semantic role
- number of assumptions: high
  - too much manual stitching is still required
- attachment of detached clues: weak
  - the representation family now has better exact internal structure than the procedure layer itself
- unresolved object slot: high
  - `go` still lacks an exact destination or object
  - `get nine total` still lacks an exact process specification
- unique final integer emerges cleanly: no
- globally cleaner than the old procedure-first story: no

### Verdict

- Still the weakest branch under an exact-instance rubric.
- Even after this pass, the procedure story improves only if it borrows structure from the representation component rather than standing on its own.

## Head-To-Head Ranking

1. Branch A: pure representation / conversion
2. Branch B: representation plus place-value extraction
3. Branch C: salvaged exact-only procedure story

## Main Difference From The Prior Audit

- Branch A is stronger now because the lower-right component exact-attaches farther than previously recognized.
- Branch B is stronger now because `binary get nine total` and `binary get nine tens` are real exact bridges.
- Branch C is not stronger in the same way, because its key missing attachments are still missing.

## Bottom Line

- A representation-first framework is now clearly cleaner than the older procedure-first framework.
- That does not mean the puzzle is solved.
- It means the exact search has succeeded in finding a better global backbone, but not the decisive extraction rule.
