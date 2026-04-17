# Candidate Integers

## Bottom Line First

No final integer is uniquely justified yet.

The strongest exact raw evidence is still framework-level, not answer-level.

## Candidate: `297`

### Evidence that supports it

- existing procedure enumeration: `integer_step_procedures.md:16-17`, `23-31`
- this reads the procedure as:
  - start at `9`
  - use step size `6`
  - interpret `get nine total` as total of the first `9` terms

Raw clues that can be cited toward this story:

- `find the start nine` at `E1 -> H1 / I1 -> J2 / K1 -> N1 / M2 -> M3 -> L4 -> K4`
- `step by six` at `N9 -> N10 -> M10 -> L11 / L12 -> M13 / L14 -> N14`
- `get nine total` at `F12 -> G13 -> F14 / E14 -> D13 -> C14 -> D14 / C13 -> D12 -> C12 -> B11 -> B10`

### Assumptions doing the work

- top-ribbon `nine` and bottom `nine` are treated as one semantic `nine`
- `get nine total` is interpreted as “total of 9 terms” rather than another 9-related instruction
- `step by six` is promoted into an arithmetic progression with no exact object specified
- the representation family is treated as secondary or ignored

### Audit judgment

- coherent as a minimal arithmetic toy model
- not uniquely justified by exact phrase evidence
- too dependent on disconnected `nine` reuse

## Candidate: `360`

### Evidence that supports it

- existing procedure enumeration: `integer_step_procedures.md:17-18`, `32-40`
- candidate comparison: `candidate_number_comparison.md:16-20`, `35-37`, `80-89`
- this reads the procedure as:
  - start at `9`
  - do `9` steps of size `6`
  - total after those steps

Raw clues that can be cited toward this story:

- `find the start nine` at `E1 -> H1 / I1 -> J2 / K1 -> N1 / M2 -> M3 -> L4 -> K4`
- exact `step by six` at `N9 -> N10 -> M10 -> L11 / L12 -> M13 / L14 -> N14`
- exact `step into integer by six` at `I13 -> I14 -> J14 -> J13 / I12 -> H12 -> H11 -> I10 / J11 -> M12 / L12 -> M13 / L14 -> N14`
- exact `get nine total` at `F12 -> G13 -> F14 / E14 -> D13 -> C14 -> D14 / C13 -> D12 -> C12 -> B11 -> B10`

### Assumptions doing the work

- there is no exact `nine step six`; the candidate depends on a stripped core or on converting `find the start nine` plus `step by six` into “9 steps of 6”
- top `nine` and bottom `nine` are merged semantically
- `get nine total` is read as accumulated sum after those steps rather than something else
- the representation family is still not doing decisive work, despite being the strongest exact family

### Audit judgment

- cleaner than `297` if one insists on a procedure-first arithmetic reading
- still not uniquely justified
- stronger than `297` only if the stripped `nine step six` core is allowed, which the blind pass does not grant

## Candidate: `864`

### Evidence that supports it

- existing detached-integration pass: `detached_clue_integration.md:21-25`, `37-59`, `101-110`
- candidate comparison: `candidate_number_comparison.md:21-29`, `35-37`, `85-97`
- this uses a forced integration:
  - treat `hundred` as upper bound `100`
  - count terms of `9, 15, 21, ...` up to `100`
  - get `16` terms, i.e. `hexadecimal ten`
  - total those terms to obtain `864`

Raw clues that can be cited toward this story:

- `hundred` inside exact `three ten hundred` at `B6 -> C6 -> D5 -> D4 -> D3 -> D2 -> C1`
- exact `hexadecimal ten` begins with `hexadecimal = I3 -> ... -> D11` and `ten = C12 -> B13 -> C14`

### Assumptions doing the work

- upper-left `hundred` is detached from the lower-right step/representation component
- `hexadecimal ten` is interpreted numerically as decimal `16`
- the step-6 arithmetic progression is still imported from the same unsupported procedure skeleton as `297`/`360`
- the nice `864 = 0x360` coincidence is not itself grid-supported

### Audit judgment

- most cross-layer use of leftover clues
- also the most constructed of the three main candidates
- not clean enough to justify as final answer

## Additional Integers Worth Mentioning, But Not Promoting

### `16`

- support: `detached_clue_integration.md:23-25`, `53-59`
- rationale: count terms up to `100`, or interpret `hexadecimal ten` directly
- problem: still depends on the same detached upper-bound story and does not satisfy the `total` clue naturally

### `2730`

- support: `detached_clue_integration.md:30-33`
- rationale: direct reading of `hexadecimal ten ten ten`
- problem: no exact output rule tells us to use that direct value, and it does not integrate with the procedure layer

### `101010`

- support: `detached_clue_integration.md:32-34`
- rationale: direct reading of `decimal ten ten ten`
- problem: same issue as `2730`, plus it clashes with the lower-right `baseten integer` flavor rather than resolving it

## Current Ranking Under This Audit

1. No answer yet
2. `360` as the least-bad procedure-first placeholder
3. `297` as the least-bad pure minimal-assumption fallback
4. `864` as the least-bad forced integration experiment

That ranking is not a recommendation to submit `360`.

It means only this:

- if forced to name the cleanest provisional arithmetic story, `360` is easiest to narrate
- if forced to respect exact local evidence more than narration, none of the three is justified yet

## What Would Actually Decide The Candidate Set

One of these exact resolutions needs to happen:

- prove an exact attachment from `find the start ...` into the lower-right representation component
- prove an exact attachment from `get nine total` into the lower-right representation component
- prove that `three ten hundred` is the intended payload of the shared `ten-ten-ten-integer` tail without merging disconnected `ten` instances

Without one of those, the candidate set remains underdetermined.
