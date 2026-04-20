# Frontier And Gaps

## Scope Boundary

- This file is derived only from these context files:
  - `representation_constructive/03_instance_hypergraph.md`
  - `representation_constructive/04_branch_comparison.md`
  - `representation_constructive/05_place_value_tests.md`
  - `representation_constructive/06_candidate_families.md`
- Those files define the frontier for this pass.
- They are not treated as proof.
- All bridge and selector claims after this file must be re-proved directly from `can u dig it.csv:1-14`.

## Active Frontier Nodes

### Top ribbon frontier

- `find the start`
  - context coordinates: `E1 -> F1 -> G1 -> H1 / I1 -> J1 -> J2 / K1 -> K2 -> L1 -> M1 -> N1`
  - source: `representation_constructive/04_branch_comparison.md:117`
- `find the start nine`
  - context coordinates: `E1 -> F1 -> G1 -> H1 / I1 -> J1 -> J2 / K1 -> K2 -> L1 -> M1 -> N1 / M2 -> M3 -> L4 -> K4`
  - source: `representation_constructive/03_instance_hypergraph.md:9-12`, `06_candidate_families.md:175-176`
- `find the start nine go`
  - context coordinates: the same first four words plus `J3 -> K3`
  - source: `representation_constructive/03_instance_hypergraph.md:11-12`, `04_branch_comparison.md:119`

### Detached place-value frontier

- `get ones`
  - context coordinates: `J3 -> J2 -> K2 / K3 -> L4 -> M5 -> M6`
  - source: `representation_constructive/05_place_value_tests.md:67`
- `three ten hundred`
  - context coordinates: `C3 -> B2 -> C2 -> B3 -> A4 / B5 -> C4 -> C5 / B6 -> C6 -> D5 -> D4 -> D3 -> D2 -> C1`
  - source: `representation_constructive/03_instance_hypergraph.md:62`, `05_place_value_tests.md:72`
- `three ten hundreds`
  - context coordinates: same `three` and `ten`, with `hundreds` extending to `B1`
  - source: `representation_constructive/03_instance_hypergraph.md:63`, `05_place_value_tests.md:73`

### Lower-right branch frontier

- `binary get nine total`
  - context coordinates: `F10 -> E10 -> E11 -> E12 -> E13 -> F13 / F12 -> G13 -> F14 / E14 -> D13 -> C14 -> B13 / C13 -> D12 -> C12 -> B11 -> B10`
  - source: `representation_constructive/03_instance_hypergraph.md:47-50`, `05_place_value_tests.md:42-44`
- `binary get nine tens`
  - context coordinates: `F10 -> E10 -> E11 -> E12 -> E13 -> F13 / F12 -> G13 -> F14 / E14 -> D13 -> C14 -> D14 / C13 -> B13 -> A12 -> A11`
  - source: `representation_constructive/03_instance_hypergraph.md:51-54`, `05_place_value_tests.md:54-57`
- `integer by six`
  - context coordinates: lower-right `integer / by / six` tail family with strongest instance `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
  - source: `representation_constructive/03_instance_hypergraph.md:42`, `05_place_value_tests.md:108-121`
- `baseten integer`
  - source: `representation_constructive/03_instance_hypergraph.md:28`, `04_branch_comparison.md:32`
- `base ten integer`
  - source: `representation_constructive/03_instance_hypergraph.md:37`, `04_branch_comparison.md:33`
- `step baseten integer`
  - source: `representation_constructive/03_instance_hypergraph.md:29-32`, `04_branch_comparison.md:34`
- `step base ten integer`
  - source: `representation_constructive/03_instance_hypergraph.md:38-41`, `04_branch_comparison.md:35`
- supporting lower-right exact tail nodes still relevant to selection/routing:
  - `step by six`
  - `step into integer by six`
  - `binary ten integer by six`
  - `decimal ten ten ten integer by six`
  - `hexadecimal ten ten ten integer by six`

## Explicit Unresolved Gaps Carried Into This Pass

### Gap A. Top ribbon attachment

- Current unresolved question:
  - is there any exact attachment from `find the start ...` into the lower-right representation backbone?
- Context source:
  - `representation_constructive/03_instance_hypergraph.md:163-164`
  - `representation_constructive/06_candidate_families.md:224`

### Gap B. Upper-left / `get ones` attachment

- Current unresolved question:
  - is there any exact attachment from `get ones` or `three ten hundred(s)` into the lower-right representation backbone?
- Context source:
  - `representation_constructive/03_instance_hypergraph.md:165-168`
  - `representation_constructive/05_place_value_tests.md:123-138`
  - `representation_constructive/06_candidate_families.md:225`

### Gap C. Branch selector

- Current unresolved question:
  - is there any exact selector between:
    - `binary get nine total` / `binary get nine tens`
    - and `... integer by six`?
- Context source:
  - `representation_constructive/05_place_value_tests.md:153-157`
  - `representation_constructive/06_candidate_families.md:226`

### Gap D. Output routing

- Current unresolved question:
  - is there any exact phrase that routes a selected branch into `baseten integer` or `base ten integer` as output label?
- Context source:
  - `representation_constructive/05_place_value_tests.md:155-157`
  - `representation_constructive/06_candidate_families.md:45-47,225-227`

## Search Priorities For The Raw-Only Pass

1. boundary expansions touching the first and last word instances of each frontier node
2. exact chains that include one frontier node as full phrase inclusion and continue into another frontier component
3. exact control-language candidates involving:
   - `go`, `into`, `to`, `from`, `as`, `or`, `by`, `start`, `find`, `get`, `add`, `step`
4. exact output-routing candidates involving:
   - `baseten integer`
   - `base ten integer`
   - `step baseten integer`
   - `step base ten integer`

## Working Rule For This Pass

- Near-matches such as `tens` vs `total` are not exact bridges.
- They can only appear in the near-miss section.
