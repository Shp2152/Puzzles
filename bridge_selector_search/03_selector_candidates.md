# Selector Candidates

This file focuses only on exact phrases that might plausibly act as control language, dispatch language, or output-routing language.

## Strongest Exact Selector-Like Family

### S1. `step or`

- exact instances:
  - `N9 -> M9 -> M10 -> L11 / K12 -> K13`
  - `N9 -> N10 -> M10 -> L11 / K12 -> K13`
  - `N9 -> N10 -> M11 -> L11 / K12 -> K13`
  - `I13 -> I14 -> J14 -> J13 / K12 -> K13`

Why it matters:

- this is the clearest exact selector shell found in the raw grid
- it lives in the lower-right cluster where the unresolved branch and output questions live

### S2. `step or integer by six`

- exact instances include:
  - `N9 -> M9 -> M10 -> L11 / K12 -> K13 / J12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
  - `N9 -> N10 -> M10 -> L11 / K12 -> K13 / J12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
  - `I13 -> I14 -> J14 -> J13 / K12 -> K13 / J12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`

Read as a selector candidate:

- the phrase explicitly places `or` between `step` and the `integer by six` tail
- this is stronger control-language evidence than plain adjacency alone

### S3. `step or baseten integer`

- exact instances:
  - `N9 -> M9 -> M10 -> L11 / K12 -> K13 / L12 -> L13 -> K14 -> J14 -> I14 -> H13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
  - `N9 -> N10 -> M10 -> L11 / K12 -> K13 / L12 -> L13 -> K14 -> J14 -> I14 -> H13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`

### S4. `step or base ten integer`

- exact instances:
  - `N9 -> M9 -> M10 -> L11 / K12 -> K13 / L12 -> L13 -> K14 -> J14 / I14 -> H13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
  - `N9 -> N10 -> M10 -> L11 / K12 -> K13 / L12 -> L13 -> K14 -> J14 / I14 -> H13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`

Read as a selector/output candidate:

- these are the strongest exact phrases making `baseten integer` / `base ten integer` look less like isolated labels and more like alternatives inside a control shell

## Secondary Exact Control Candidates

### S5. `binary get nine tens to`

- exact instances:
  - `F10 -> E10 -> E11 -> E12 -> E13 -> F13 / F12 -> G13 -> F14 / E14 -> D13 -> C14 -> D14 / C13 -> B13 -> A12 -> B12 / C12 -> D12`
  - alternate `binary` path starts `F10 -> F11`

Why it matters:

- this is the cleanest exact branch-side phrase ending in an obvious dispatch preposition

Why it does not solve the selector problem:

- no exact continuation from this `to` into `integer by six` or into the output labels was found

### S6. `to integer by six`

- exact instances:
  - `H10 -> I10 / J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
  - `H11 -> I10 / J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`

Why it matters:

- it is explicit direction-language attached to the tail branch

Why it still fails:

- its `to` does not match the `to` in `binary get nine tens to`

### S7. `into integer by six`

- exact instances:
  - `I12 -> H12 -> H11 -> I10 / J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
  - `G11 -> H12 -> H11 -> I10 / J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`

Assessment:

- exact motion-language exists on the tail side
- but it is not connected to the binary branch or to the top ribbon

### S8. `or baseten integer` / `or base ten integer`

- exact phrases:
  - `K12 -> K13 / L12 -> L13 -> K14 -> J14 -> I14 -> H13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
  - `K12 -> K13 / L12 -> L13 -> K14 -> J14 / I14 -> H13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`

Assessment:

- exact disjunctive shell exists around the output label
- but it still lacks an exact preceding branch phrase

### S9. `go ahead`

- exact instances include the top-ribbon `go`:
  - `J3 -> K3 / J4 -> I3 -> I2 -> H2 -> G2`
- other exact `go ahead` instances also exist with a different upper `go`

Assessment:

- this is the strongest new exact control phrase on the top-ribbon side
- it still does not attach to the lower-right backbone

## Questions From The Workflow

### Is there any exact phrase that selects between the `... total / ... tens` branch and the `... integer by six` branch?

- No.
- Closest near-miss:
  - `binary get nine tens to`
  - `to integer by six`
- exact failure:
  - disconnected `to` instance

### Is there any exact phrase that specifies an order of operations?

- Not globally.
- Locally, `step or ...` and `go ahead` are exact control-language shells.
- Neither one states a complete order of operations connecting the unresolved components.

### Is there any exact phrase that turns `baseten integer` into an output label rather than just a nearby object phrase?

- Not decisively.
- Strongest local evidence in that direction:
  - `or baseten integer`
  - `step or baseten integer`
  - `or base ten integer`
  - `step or base ten integer`
- This makes the output label more control-linked than before, but still does not prove final-output status.

## Selector Takeaway

- The strongest exact new selector is the lower-right `step or` family.
- It improves the local control-language picture.
- It does not resolve the main global selector gap, because it still does not connect to the binary total/tens branch or to the top/upper-left detached nodes.
