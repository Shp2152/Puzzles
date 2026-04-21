# Extraction Hypotheses

This file tests whether detached extraction language acts on locked lower-right engine outputs.

## A. `get ones` As Second-Stage Digit Extraction

### Hypothesis A1: apply `get ones` to local `90`

- engine output candidate:
  - `90` from exact `get nine tens`
- detached extraction phrase:
  - `get ones`
  - `J3 -> J2 -> K2 / K3 -> L4 -> M5 -> M6`
- handoff status:
  - unsupported
- why:
  - no exact controller or extraction phrase maps `get ones` to the selected lower-right output
- arithmetic result if forced:
  - `0`
- classification:
  - unsupported leap

### Hypothesis A2: apply `get ones` to local `2`

- engine output candidate:
  - `2` from exact `binary ten`
- handoff status:
  - unsupported
- arithmetic result if forced:
  - `2`
- classification:
  - unsupported leap

## B. `three ten hundred` / `three ten hundreds` As Place-Value Decomposition

### Hypothesis B1: apply to local `90`

- detached extraction phrases:
  - `three ten hundred`
  - `three ten hundreds`
- handoff status:
  - unsupported
- why:
  - no exact phrase says that the detached place-value family should act on the lower-right branch result

### Hypothesis B2: apply to a representation-derived hexadecimal result

- engine candidate family:
  - the controller-selected hexadecimal family
- handoff status:
  - unsupported
- why:
  - even before extraction, the hexadecimal engine family does not yield one uniquely executable number

## C. `total` / `tens` As Post-Processing

### Hypothesis C1: `tens` is internal, not detached post-processing

- exact support:
  - `get nine tens`
  - `binary get nine tens`
  - `find the hexadecimal or get nine tens`
- assessment:
  - `tens` is already part of the selected engine branch itself
  - this is not an additional detached extraction layer

### Hypothesis C2: `total` as alternative post-processing branch

- exact support:
  - `get nine total`
  - `binary get nine total`
- assessment:
  - exact lower-right branch exists
  - but controller support is weaker than for `get nine tens` because exact `find the hexadecimal or get nine total` was not found

## D. Detached Extraction Acting On Additional Engine Results

### Hypothesis D1: controller-selected hexadecimal representation result -> detached extraction

- controller evidence:
  - exact `find the hexadecimal ...` family
- engine output status:
  - still not uniquely executable because of competing exact branch/tail continuations
- extraction handoff:
  - unsupported

## Extraction-Hypothesis Takeaway

- No detached extraction hypothesis is grounded enough to act on a lower-right output.
- `get ones` still looks like a secondary extraction layer in principle, but not a licensed one in the current global structure.
- The strongest extraction-like material is actually internal to the lower-right engine: `get nine tens`.
