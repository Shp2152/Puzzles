# Referent Mapping

This file lists objective referent mappings for the key detached controller/extraction terms.

Rules applied:

- no merging of disconnected instances
- each mapping must point to a concrete referent class
- failed mappings are included explicitly

## `start`

### Plausible objective referents

- the exact top-ribbon `start` word instance
  - `K1 -> K2 -> L1 -> M1 -> N1`
  - strength: strong, but local only
- the top-ribbon directive phrase `find the start`
  - referent class: specific phrase instance
  - strength: strong

### Failed or weak mappings

- lower-right engine entry point
  - strength: weak
  - failure: no exact phrase maps `start` to a specific lower-right word instance or component entry

## `start nine`

### Plausible objective referents

- top-ribbon phrase instance `find the start nine`
  - strongest `nine`: `M2 -> M3 -> L4 -> K4`
  - alternate exact `nine`: `M2 -> M3 -> L4 -> M5`
  - strength: strong, local only
- literal value `9`
  - referent class: exact count/value named in the phrase
  - strength: plausible but weak because no unique downstream target is specified

### Failed or weak mappings

- lower-right `get nine total` / `get nine tens` branches
  - failure: disconnected `nine` instances
- specific branch index inside the lower-right engine
  - failure: no objective indexing scheme is given

## `go`

### Plausible objective referents

- top-ribbon `go` in `find the start nine go`
  - `J3 -> K3`
  - strength: strong, local only
- lower-right `go` in `go integer by six`
  - `I9 -> I10`
  - strength: strong, but separate component role

### Failed or weak mappings

- top `go` controlling lower-right `go integer by six`
  - failure: disconnected word instance

## `ahead`

### Plausible objective referents

- top-ribbon `ahead` in `go ahead`
  - `J4 -> I3 -> I2 -> H2 -> G2`
  - strength: strong, local continuation cue

### Failed or weak mappings

- any lower-right continuation or branch
  - failure: no exact phrase maps `ahead` into the lower-right engine

## `ones`

### Plausible objective referents

- exact detached phrase `get ones`
  - `J3 -> J2 -> K2 / K3 -> L4 -> M5 -> M6`
  - referent class: digit-extraction instruction family
  - strength: strong, local only

### Failed or weak mappings

- ones digit of local engine output `90`
  - plausible arithmetic, but unsupported handoff
- ones digit of local engine output `2`
  - plausible arithmetic, but unsupported handoff

## `three ten hundred`

### Plausible objective referents

- exact detached phrase instance
  - `C3 -> B2 -> C2 -> B3 -> A4 / B5 -> C4 -> C5 / B6 -> C6 -> D5 -> D4 -> D3 -> D2 -> C1`
  - referent class: specific upper-left place-value phrase
  - strength: strong, local only
- a place-value schema involving `3`, `10`, and `100`
  - referent class: extraction schema
  - strength: plausible but weak because the semantic operation is not stated

### Failed or weak mappings

- any specific lower-right engine output
  - failure: no exact handoff or target naming phrase

## `three ten hundreds`

### Plausible objective referents

- exact detached phrase instance
  - same `three` and `ten`, with `hundreds` extending to `B1`
  - referent class: specific upper-left place-value phrase
  - strength: strong, local only

### Failed or weak mappings

- any specific lower-right engine output
  - failure: no exact handoff or target naming phrase

## `nine`

### Plausible objective referents

- top-ribbon `nine` in `find the start nine`
  - `M2 -> M3 -> L4 -> K4`
  - alternate `M5`
  - strength: strong, local only
- lower-right `nine` in `get nine total`
  - `E14 -> D13 -> C14 -> B13`
  - alternate exact `D14`
  - strength: strong, local only
- lower-right `nine` in `get nine tens`
  - `E14 -> D13 -> C14 -> D14`
  - strength: strong, local only

### Failed or weak mappings

- one unified global `nine`
  - failure: disconnected instances

## `total`

### Plausible objective referents

- exact lower-right `total` word instance
  - `C13 -> D12 -> C12 -> B11 -> B10`
  - strength: strong
- exact lower-right aggregation phrase `get nine total`
  - strength: strong

### Failed or weak mappings

- detached upper-left aggregation layer
  - failure: no detached exact `total` phrase outside the lower-right family was found

## `tens`

### Plausible objective referents

- lower-right `get nine tens`
  - one exact `tens`: `C13 -> B13 -> A12 -> A11`
  - alternate exact `tens`: `C13 -> B13 -> A12 -> B12`
  - strength: strong
- lower-right `get nine to tens`
  - exact `tens` at `C12 -> B13 -> A12 -> A11`
  - alternate exact `B12`
  - strength: strong, but branch-internal scope ambiguous
- upper-left place-value family via `three ten hundred(s)` and `ten hundred(s)`
  - strength: plausible family-level referent, but not the same word instance

### Failed or weak mappings

- one unified global `tens`
  - failure: multiple disconnected instance families

## Referent-Mapping Takeaway

- The strongest new objective mapping is not `start`, `go`, or `ones`.
- It is the exact controller phrase family centered on `find the hexadecimal ...`, because it names a specific representation label and exact downstream engine material in one phrase.
- The detached top `start/start nine/go/ahead` phrases still map strongly only to themselves.
