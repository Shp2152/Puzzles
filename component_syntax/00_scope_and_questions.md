# Scope And Questions

## Scope Boundary

- This file is derived only from these context files:
  - `representation_constructive/02_exact_representation_phrases.md`
  - `representation_constructive/03_instance_hypergraph.md`
  - `representation_constructive/04_branch_comparison.md`
  - `bridge_selector_search/02_bridge_candidates.md`
  - `bridge_selector_search/03_selector_candidates.md`
  - `bridge_selector_search/05_resolution_test.md`
- Those files define the lower-right connected component and the syntax questions.
- They are not treated as proof.
- All parse claims after this file must be re-grounded in `can u dig it.csv:1-14`.

## Lower-Right Component Seed Nodes

These are the exact phrase instances that seed the syntax pass.

### Branch-side phrases

- `binary get nine total`
  - context coordinates: `F10 -> E10 -> E11 -> E12 -> E13 -> F13 / F12 -> G13 -> F14 / E14 -> D13 -> C14 -> B13 / C13 -> D12 -> C12 -> B11 -> B10`
  - alternate exact `binary` path starts `F10 -> F11`
- `binary get nine tens`
  - context coordinates: `F10 -> E10 -> E11 -> E12 -> E13 -> F13 / F12 -> G13 -> F14 / E14 -> D13 -> C14 -> D14 / C13 -> B13 -> A12 -> B12`
  - alternate exact `binary` path starts `F10 -> F11`
- `binary ten integer by six`
  - context coordinates: `F10 -> E10 -> E11 -> E12 -> E13 -> F13 / F14 -> G13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
  - alternate exact `binary` path starts `F10 -> F11`

### Representation-object phrases

- `decimal ten ten ten integer`
- `decimal ten ten ten integer by six`
- `hexadecimal ten ten ten integer`
- `hexadecimal ten ten ten integer by six`

Representative exact coordinates from context:

- `decimal`: `H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11`
- `hexadecimal`: `I3 -> I4 -> I5 -> I6 -> H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11`
- shared `ten / ten / ten / integer` tail:
  - `C12 -> B13 -> C14`
  - `C13 -> D14 -> E14`
  - `F14 -> G13 -> H12`
  - `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`

### Tail phrases

- `integer by six`
- `step by six`
- `step into integer by six`

Representative exact coordinates from context:

- `integer by six`
  - strongest instance: `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
- `step by six`
  - one exact instance: `N9 -> M9 -> M10 -> L11 / L12 -> M13 / L14 -> M14 -> N14`
- `step into integer by six`
  - `I13 -> I14 -> J14 -> J13 / I12 -> H12 -> H11 -> I10 / J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`

### Selector-like and output-side phrases

- `step or`
- `step or integer by six`
- `step or baseten integer`
- `step or base ten integer`
- `baseten integer`
- `base ten integer`

Representative context coordinates:

- `step or`
  - `N9 -> M9 -> M10 -> L11 / K12 -> K13`
  - `N9 -> N10 -> M10 -> L11 / K12 -> K13`
  - `I13 -> I14 -> J14 -> J13 / K12 -> K13`
- `or baseten integer`
  - `K12 -> K13 / L12 -> L13 -> K14 -> J14 -> I14 -> H13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- `or base ten integer`
  - `K12 -> K13 / L12 -> L13 -> K14 -> J14 / I14 -> H13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`

## Open Syntax Questions

This pass must answer these questions as strictly as possible.

### Q1. `by six` attachment

- Does `by six` attach to `integer`?
- Does `by six` attach to `step`?
- Does `by six` attach to a larger phrase such as `binary ten integer` or `decimal ten ten ten integer`?

### Q2. `or` scope

- Does `or` join two outputs?
- Does `or` join two actions?
- Does `or` merely mark co-located phrase overlap without licensing a compositional parse?

### Q3. `base ten integer` / `baseten integer` role

- Is `base ten integer` a noun phrase?
- Is it an imperative target?
- Is it a final reporting label?
- Is it a conversion target inside a larger phrase?

### Q4. Representation-label scope

- Is `binary` modifying an object phrase?
- Is `binary` modifying an instruction?
- Is `binary` a result-format label?
- Are `decimal` and `hexadecimal` cleaner as object labels, mode labels, operation modifiers, or output-format labels?

### Q5. `get nine total` / `get nine tens` syntax

- Are these imperative phrases?
- Are they label-like noun phrases?
- Are they partial clauses that require a missing object?

### Q6. Shared-instance contact vs exact syntax

- When two phrases share `binary`, `integer`, `step`, `or`, or `ten`, is that enough to support compositional syntax?
- When is the overlap only local contact, not instruction flow?

### Q7. Executability threshold

- Which local parse families are syntactically coherent enough to execute semantically?
- Which ones are only cohabiting in the same lower-right zone?

## Pass Criterion

- The success condition for this pass is not a number.
- The success condition is a disciplined answer to this narrower question:
  - does the lower-right component actually parse into an executable exact structure, or is it mainly a connected cluster of overlapping exact phrases?
