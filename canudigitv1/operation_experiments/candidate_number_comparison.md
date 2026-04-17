# Candidate Number Comparison

Current live candidates after the integer-step enumeration and detached-clue integration passes:

- `297`
- `360`
- `864`

## Why These Three Are Live

### `297`

- Comes from the cleanest pure skeleton reading if `get nine total` means the total of the first 9 terms of the progression starting at 9 with step 6.
- Source: `integer_step_procedures.md`

### `360`

- Comes from the other clean pure skeleton reading if `nine step six` means 9 steps of size 6 and `get ... total` means sum after those 9 steps.
- Source: `integer_step_procedures.md`

### `864`

- Comes from the strongest forced integration result:
- use `hundred` as the upper bound `100`
- count terms in the `9, 15, 21, ...` sequence up to `100`
- there are `16` terms, i.e. `hexadecimal ten`
- the total is `864`
- and `864` in hexadecimal is `360`
- Source: `detached_clue_integration.md`

## Comparison

| Candidate | Main source | Main strength | Main weakness |
| --- | --- | --- | --- |
| `297` | pure skeleton | lowest-assumption total of 9 terms | does not naturally explain the detached `three` / `hundred` / `hexadecimal` clues |
| `360` | pure skeleton | clean step-total reading; also a `3xx` value | still does not naturally use `hundred`; detached clues remain mostly unused |
| `864` | forced integration | first candidate that meaningfully combines `hundred` with `hexadecimal ten` and yields `0x360` | more constructed than the pure skeleton totals; still no literal attachment of the detached clauses |

## Number-Word Probe

Direct exact-word probes for these candidate-number families found no paths for:

- `zero`
- `sixteen`
- `sixty`
- `eight`
- `four`
- `eighty`
- `sixtyfour`
- `threehundredsixty`
- `eighthundredsixtyfour`

Practical takeaway:

- the current candidates are not supported because their English number words are literally present in the grid
- they are supported only through the procedure / interpretation layers

## Remaining Detached Clues

### `hexadecimal` / `decimal`

- still look intentional because they have strong local families
- but direct attachment tests to the winning skeleton all failed
- direct representation readings such as `AAA_hex = 2730` and `101010_dec` do not appear as step-6 terms or totals

### `three ten hundred`

- still looks intentional as a local numeric clause
- but direct attachment tests to the winning skeleton all failed
- still ambiguous whether it is payload, bound family, or separate parallel clue

### `nine three hundred`

- this surviving core keeps the `9 / 3 / 100` neighborhood alive
- it weakly suggests that a `300`-ish quantity may matter
- this nudges `360` and `0x360` more than `297`, but not strongly enough to be decisive

## Current Read

Current ranking by style of support:

1. `360`
Pure skeleton front-runner if we want the cleanest concrete total that still feels compatible with a `3xx` neighborhood.

2. `864`
Best integrated front-runner if we insist on making `hundred` and `hexadecimal ten` do real work.

3. `297`
Best pure low-assumption total if we ignore the detached clue families, but currently the hardest to reconcile with the leftover evidence.

## Bottom Line

- `297` is best for pure minimal-assumption arithmetic
- `360` is best for a concrete clean procedure candidate
- `864` is best for cross-layer integration

The next discrimination step should focus on whether the detached clue layers are trying to push the solve from the clean skeleton result `360` toward the integrated result `864`.
