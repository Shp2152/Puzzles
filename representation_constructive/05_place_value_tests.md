# Place-Value Tests

Target words for this pass:

- `ones`
- `tens`
- `hundred`
- `hundreds`
- `total`
- `get`
- `find`
- `add`

Rule for promotion:

- the test must run forward from an exact representation-defined object
- then to an exact place-value or extraction phrase
- then to an exact total or final-positive-integer story
- no backsolving from a desired number

## Positive Exact Hits

### 1. Representation object to `tens`

- exact `decimal tens`
  - `H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11 / C12 -> B13 -> A12 -> A11`
  - alternate `tens` ending `B12`
- exact `hexadecimal tens`
  - `I3 -> I4 -> I5 -> I6 -> H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11 / C12 -> B13 -> A12 -> A11`
  - alternate `tens` ending `B12`
- exact `binary tens`
  - `F10 -> E10 -> E11 -> E12 -> E13 -> F13 / F14 -> G13 -> H12 -> I13`
  - alternate `binary` path starts `F10 -> F11`

Assessment:

- exact representation-to-place-value attachment exists for `tens`
- no corresponding exact `decimal ones`, `hexadecimal ones`, `binary ones`, `decimal hundred(s)`, `hexadecimal hundred(s)`, or `binary hundred(s)` was found

### 2. Representation object to `total`

- exact `binary get nine total`
  - `F10 -> E10 -> E11 -> E12 -> E13 -> F13 / F12 -> G13 -> F14 / E14 -> D13 -> C14 -> B13 / C13 -> D12 -> C12 -> B11 -> B10`
  - alternate `binary` path starts `F10 -> F11`

Assessment:

- this is the strongest new exact bridge in the place-value/total direction
- it proves that a representation label can exact-chain directly into the lower total cluster
- it does not tell us what arithmetic or digit-extraction interpretation is intended

### 3. Representation object to `tens` plus imperative word

- exact `binary get nine tens`
  - `F10 -> E10 -> E11 -> E12 -> E13 -> F13 / F12 -> G13 -> F14 / E14 -> D13 -> C14 -> D14 / C13 -> B13 -> A12 -> A11`
  - alternate `binary` path starts `F10 -> F11`
  - alternate `tens` ends `B12`

Assessment:

- this is the cleanest exact representation-plus-place-value phrase in the raw grid
- if read literally, it suggests the candidate number family `90`
- what is still missing is an exact rule telling us whether `binary` labels the object, the extraction method, or the output format

## Secondary Exact Place-Value Phrases

- exact `get ones` at `J3 -> J2 -> K2 / K3 -> L4 -> M5 -> M6`
- exact `ten hundred` at either:
  - `C3 -> C4 -> C5 / B6 -> C6 -> D5 -> D4 -> D3 -> D2 -> C1`
  - `B5 -> C4 -> C5 / B6 -> C6 -> D5 -> D4 -> D3 -> D2 -> C1`
- exact `ten hundreds` on the same paths extended to `B1`
- exact `three ten hundred`
- exact `three ten hundreds`
- exact `ten total` at `A14 -> B13 -> C14 / C13 -> D12 -> C12 -> B11 -> B10`
- exact `tens total` at `A14 -> B13 -> A12 -> B12 / C13 -> D12 -> C12 -> B11 -> B10`

Assessment:

- these phrases show that place-value vocabulary is real
- they do not yet form one exact extraction chain with the lower-right representation object family

## Forward Story Tests

### Test A. `decimal/hexadecimal/binary` object first, then `tens`

Supported exactly:

- yes for `decimal tens`
- yes for `hexadecimal tens`
- yes for `binary tens`

Unsupported exactly:

- no exact continuation from `decimal tens` or `hexadecimal tens` to `total`
- no exact continuation from `decimal tens` or `hexadecimal tens` to `baseten integer`
- no exact continuation from `decimal tens` or `hexadecimal tens` to `integer by six`

Conclusion:

- the place-value direction exists, but only as a label-level extension for `decimal` and `hexadecimal`

### Test B. `binary` object first, then `tens` or `total`

Supported exactly:

- `binary get nine total`
- `binary get nine tens`
- `binary ten integer by six`

Unsupported exactly:

- no exact `binary get nine total integer`
- no exact `binary get nine total baseten integer`
- no exact `binary get nine total integer by six`
- no exact `binary get nine tens integer by six`

Conclusion:

- `binary` is the only representation label that exact-attaches both to the `integer by six` tail and to the `get nine total` / `get nine tens` cluster
- that makes `binary` the best candidate pivot inside Branch B
- even so, the exact chain still stops before a unique final integer emerges

### Test C. Upper-left place values into the lower-right representation component

Supported exactly:

- `three ten hundred`
- `three ten hundreds`
- `get ones`

Unsupported exactly:

- no exact attachment from `three ten hundred(s)` into `binary`, `decimal`, `hexadecimal`, `baseten`, `base ten integer`, or `integer by six`
- no exact attachment from `get ones` into the lower-right representation component

Conclusion:

- the upper-left place-value family remains detached

## Best Partial Forward Story

The strongest forward exact sequence found in this pass is:

1. representation object: `binary ten integer by six`
2. alternate representation-to-total branch: `binary get nine total`
3. alternate representation-to-tens branch: `binary get nine tens`

Why it matters:

- all three phrases share the same lower-right `binary` anchor instance
- this is the first exact forward structure that lets one representation label touch both an object-like tail and a total/tens clue family

Why it still fails as a solve:

- no exact phrase states which branch to apply
- no exact phrase converts the branch result into the `baseten integer` output label
- no exact phrase tells us whether `nine` is a count, a digit, or part of a representation string

## Bottom Line

- An exact place-value extraction story is more plausible now than before.
- It is still not complete.
- The decisive exact gap is not the existence of place-value language; it is the missing exact attachment that says what to extract from which representation object.
