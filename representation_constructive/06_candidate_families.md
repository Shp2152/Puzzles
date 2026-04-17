# Candidate Families

## Bottom Line First

- No final integer is uniquely justified yet.
- This pass improved the exact lower-right backbone.
- It did not produce one decisive extraction rule.

Ranking principle used here:

- exactness first
- disconnected-merge penalties second
- global coverage third

That means some exact local families rank above the older `360` / `297` / `864` placeholders even though they absorb less of the whole puzzle.

## Family A: Exact Place-Value Output From `get nine tens`

### Candidate number

- `90`

### Exact phrase evidence

- exact `get nine tens`
  - `F12 -> G13 -> F14 / E14 -> D13 -> C14 -> D14 / C13 -> B13 -> A12 -> A11`
  - alternate `tens` ends `B12`
- exact `binary get nine tens`
  - `F10 -> E10 -> E11 -> E12 -> E13 -> F13 / F12 -> G13 -> F14 / E14 -> D13 -> C14 -> D14 / C13 -> B13 -> A12 -> A11`
  - alternate `binary` path starts `F10 -> F11`

### Exact operation chain

- read `get nine tens` literally as `9` tens
- output `90`

### Assumptions doing the work

- `get` is an imperative instruction rather than merely phrase glue
- `nine tens` is literal decimal place-value language
- if `binary get nine tens` is used, `binary` is either an object label or a local modifier, but does not change the value `90`

### What remains unsupported

- no exact attachment from this output to `baseten integer`
- no exact rule says why the binary-labeled branch is the intended branch
- no exact attachment from the top `find the start ...` ribbon

### Robustness judgment

- strongest current candidate family under an exact place-value reading
- still not submission-ready

## Family B: Exact Local Representation Read From `binary ten`

### Candidate number

- `2`

### Exact phrase evidence

- exact `binary ten`
  - `F10 -> E10 -> E11 -> E12 -> E13 -> F13 / F14 -> G13 -> H12`
  - alternate `binary` path starts `F10 -> F11`
- exact `binary ten integer`
- exact `binary ten integer by six`

### Exact operation chain

- interpret `ten` as the token `10` in binary
- convert `10_2` to decimal `2`

### Assumptions doing the work

- the phrase is a direct representation object, not just a label fragment
- no additional operation is required before output

### What remains unsupported

- does not absorb `decimal`, `hexadecimal`, `get nine total`, `get nine tens`, or `baseten integer` decisively
- no exact phrase says to output the direct conversion result

### Robustness judgment

- lower-assumption than the old procedure numbers
- too local to promote as an answer

## Family C: Direct Repeated-Ten Representation Objects

### Candidate numbers

- `101010` from `decimal ten ten ten`
- `1052688` from a literal-token read of `hexadecimal ten ten ten` as `0x101010`
- `2730` from a digit-value read of `hexadecimal ten ten ten` as `AAA_hex`

### Exact phrase evidence

- exact `decimal ten ten ten integer`
  - `H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11 / C12 -> B13 -> C14 / C13 -> D14 -> E14 / F14 -> G13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- exact `hexadecimal ten ten ten integer`
  - `I3 -> I4 -> I5 -> I6 -> H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11 / C12 -> B13 -> C14 / C13 -> D14 -> E14 / F14 -> G13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`

### Exact operation chain

- decimal family:
  - concatenate the three exact `ten` tokens after the `decimal` label
  - read the result as `101010`
- hexadecimal family, literal-token model:
  - concatenate the three exact `ten` tokens after the `hexadecimal` label
  - read the result as `0x101010 = 1052688`
- hexadecimal family, digit-value model:
  - interpret each `ten` as digit-value `10`
  - read `10,10,10` as `AAA_hex = 2730`

### Assumptions doing the work

- token concatenation is intended
- or, for `2730`, the word `ten` stands for hex digit-value `A`
- the trailing `integer` is read as an object label rather than an operation target

### What remains unsupported

- no exact phrase says to concatenate the tokens
- no exact phrase chooses between the literal-token and digit-value models
- no exact phrase routes the result through `get nine total`, `get nine tens`, or `baseten integer`

### Robustness judgment

- exact object family, weak extraction family
- better than the old procedure placeholders on local exactness
- worse than Families A and B on interpretive simplicity

## Family D: Single-Token Base Values

### Candidate numbers

- `10` from exact `decimal ten`
- `16` from exact `hexadecimal ten`

### Exact phrase evidence

- exact `decimal ten`
  - `H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11 / C12 -> B13 -> C14`
- exact `hexadecimal ten`
  - `I3 -> I4 -> I5 -> I6 -> H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11 / C12 -> B13 -> C14`

### Exact operation chain

- read the token `10` in the named base

### Assumptions doing the work

- same as Family B, but with even less global coverage

### What remains unsupported

- too local
- no exact output rule
- no exact integration with the rest of the clue network

### Robustness judgment

- exact but too small to carry the puzzle

## Family E: Older Procedure Placeholders

### Candidate numbers

- `360`
- `297`
- `864`

### Exact phrase evidence they still depend on

- `find the start nine`
  - `E1 -> F1 -> G1 -> H1 / I1 -> J1 -> J2 / K1 -> K2 -> L1 -> M1 -> N1 / M2 -> M3 -> L4 -> K4`
- `step by six`
  - lower-right `step / by / six` family
- `get nine total`
  - `F12 -> G13 -> F14 / E14 -> D13 -> C14 -> D14 / C13 -> D12 -> C12 -> B11 -> B10`
- for `864`, detached use of `hundred` from `three ten hundred`

### Exact operation chain

- still not exact
- these numbers require importing a manual arithmetic progression story over disconnected `nine` and `step` instances

### Assumptions doing the work

- top-ribbon `nine` and bottom `nine` play one semantic role
- disconnected `step` instances play one semantic role
- `get nine total` means a specific arithmetic accumulation rule not stated exactly
- `864` also requires detached use of `hundred` as upper bound plus an extra representation interpretation

### What remains unsupported

- the exact global chain itself
- exact representation-first attachment still does not select these numbers

### Robustness judgment

- weaker than the new representation-first candidate families under an exact-instance standard
- still useful as comparison baselines, not as leads

## Ranking By Robustness

1. No answer yet
2. Family A: `90` from exact `get nine tens` / `binary get nine tens`
3. Family B: `2` from exact `binary ten`
4. Family D: `10` / `16` single-token base values
5. Family C: repeated-ten direct representation objects (`101010`, `1052688`, `2730`)
6. Family E: old procedure placeholders (`360`, `297`, `864`)

## Why The Old Numbers Fall Behind Here

- They still need disconnected-instance merges.
- The newer representation-first families at least start from exact local object phrases.
- None of the exact families is globally sufficient yet, but the procedure placeholders are no longer the cleanest provisional stories under this pass's stricter standard.

## What Would Actually Promote A Candidate

One of these exact resolutions is still needed:

- an exact attachment from `find the start ...` into the connected lower-right representation component
- an exact attachment from `get ones` or `three ten hundred(s)` into that same component
- an exact phrase that selects between the binary-total branch and the `integer by six` branch
- an exact phrase that routes a branch result into the `baseten integer` output label
