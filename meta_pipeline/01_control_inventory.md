# Control Inventory

All promoted phrases below were re-verified directly against `can u dig it.csv:1-14` with `meta_pipeline/controller_extraction_probe.py`.

Helper note:

- `meta_pipeline/controller_extraction_probe.py` reuses only the generic exact-search assumptions already established in prior helpers:
  - rectangular CSV grid
  - lowercase cell matching
  - standard 8-neighbor adjacency
  - no cell reuse inside a word path
  - no cell reuse across a chained phrase path
- This inventory was generated only from the constrained controller vocabulary for this pass.

## Promoted Control / Directive / Selector Phrases

### Top ribbon, detached

#### `find the start`

- Exact phrase text: `find the start`
- Coordinates:
  - `find`: `E1 -> F1 -> G1 -> H1`
  - `the`: `I1 -> J1 -> J2`
  - `start`: `K1 -> K2 -> L1 -> M1 -> N1`
- Local region / component: top ribbon
- Attached or detached: detached from lower-right engine under direct overlap criteria
- Likely role: controller/meta

#### `find the start nine`

- Exact phrase text: `find the start nine`
- Coordinates:
  - same first three words as above
  - `nine`: `M2 -> M3 -> L4 -> K4`
  - alternate exact `nine`: `M2 -> M3 -> L4 -> M5`
- Local region / component: top ribbon
- Attached or detached: detached
- Likely role: controller/meta

#### `find the start nine go`

- Exact phrase text: `find the start nine go`
- Coordinates:
  - same first four words as above
  - `go`: `J3 -> K3`
- Local region / component: top ribbon
- Attached or detached: detached
- Likely role: controller/meta

#### `find the start nine go ahead`

- Exact phrase text: `find the start nine go ahead`
- Coordinates:
  - same first five words as above
  - `ahead`: `J4 -> I3 -> I2 -> H2 -> G2`
- Local region / component: top ribbon
- Attached or detached: detached
- Likely role: controller/meta

#### `go ahead`

- Exact phrase text: `go ahead`
- Promoted controller-bearing instance:
  - `go`: `J3 -> K3`
  - `ahead`: `J4 -> I3 -> I2 -> H2 -> G2`
- Other exact `go ahead` instances also exist using a different upper `go`
- Local region / component: top ribbon / upper-right
- Attached or detached: detached
- Likely role: controller/meta

### Lower-right, attached local control shell

#### `step by six`

- Exact phrase text: `step by six`
- Representative coordinates:
  - `N9 -> M9 -> M10 -> L11 / L12 -> M13 / L14 -> M14 -> N14`
- Local region / component: lower-right engine
- Attached or detached: attached
- Likely role: action

#### `step into integer by six`

- Exact phrase text: `step into integer by six`
- Coordinates:
  - `I13 -> I14 -> J14 -> J13 / I12 -> H12 -> H11 -> I10 / J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
- Local region / component: lower-right engine
- Attached or detached: attached
- Likely role: action

#### `step or`

- Exact phrase text: `step or`
- Representative coordinates:
  - `N9 -> M9 -> M10 -> L11 / K12 -> K13`
  - alternate exact step families also exist
- Local region / component: lower-right engine
- Attached or detached: attached
- Likely role: selector

#### `step or integer by six`

- Exact phrase text: `step or integer by six`
- Coordinates:
  - one exact instance:
  - `N9 -> M9 -> M10 -> L11 / K12 -> K13 / J12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
- Local region / component: lower-right engine
- Attached or detached: attached
- Likely role: selector

#### `step or baseten integer`

- Exact phrase text: `step or baseten integer`
- Coordinates:
  - one exact instance:
  - `N9 -> M9 -> M10 -> L11 / K12 -> K13 / L12 -> L13 -> K14 -> J14 -> I14 -> H13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- Local region / component: lower-right engine
- Attached or detached: attached
- Likely role: selector

#### `step or base ten integer`

- Exact phrase text: `step or base ten integer`
- Coordinates:
  - one exact instance:
  - `N9 -> M9 -> M10 -> L11 / K12 -> K13 / L12 -> L13 -> K14 -> J14 / I14 -> H13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- Local region / component: lower-right engine
- Attached or detached: attached
- Likely role: selector

#### `step or baseten to integer`

- Exact phrase text: `step or baseten to integer`
- Coordinates:
  - one exact instance:
  - `N9 -> M9 -> M10 -> L11 / K12 -> K13 / L12 -> L13 -> K14 -> J14 -> I14 -> H13 -> H12 / H11 -> I10 / J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- Local region / component: lower-right engine
- Attached or detached: attached
- Likely role: selector

#### `step or base ten to integer`

- Exact phrase text: `step or base ten to integer`
- Coordinates:
  - one exact instance:
  - `N9 -> M9 -> M10 -> L11 / K12 -> K13 / L12 -> L13 -> K14 -> J14 / I14 -> H13 -> H12 / H11 -> I10 / J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- Local region / component: lower-right engine
- Attached or detached: attached
- Likely role: selector

#### `to integer by six`

- Exact phrase text: `to integer by six`
- Coordinates:
  - `H10 -> I10 / J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
  - alternate exact `to = H11 -> I10`
- Local region / component: lower-right engine
- Attached or detached: attached
- Likely role: action / selector

#### `go integer by six`

- Exact phrase text: `go integer by six`
- Coordinates:
  - `I9 -> I10 / J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
- Local region / component: lower-right engine
- Attached or detached: attached
- Likely role: action

### Cross top-to-engine exact controller phrases

These are the most important new phrases in this pass.

#### `find the hexadecimal ten ten ten integer by six`

- Exact phrase text: `find the hexadecimal ten ten ten integer by six`
- Coordinates:
  - `find`: `E1 -> F1 -> G1 -> H1`
  - `the`: `I1 -> J1 -> I2`
    - alternate exact `the`: `I1 -> J1 -> J2`
  - `hexadecimal`: `I3 -> I4 -> I5 -> I6 -> H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11`
  - `ten`: `C12 -> B13 -> C14`
  - `ten`: `C13 -> D14 -> E14`
  - `ten`: `F14 -> G13 -> H12`
  - `integer`: `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
  - `by`: `L12 -> M13`
  - `six`: `L14 -> M14 -> N14`
- Local region / component: cross top ribbon into lower-right engine
- Attached or detached: attached exact composition
- Likely role: controller/meta selecting a representation-engine family

#### `find the hexadecimal ten ten ten to integer`

- Exact phrase text: `find the hexadecimal ten ten ten to integer`
- Coordinates:
  - same first six words as above
  - `to`: `H11 -> I10`
  - `integer`: `J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- Local region / component: cross top ribbon into lower-right engine
- Attached or detached: attached exact composition
- Likely role: controller/meta selecting a representation-engine family, but with unresolved target semantics

#### `find the hexadecimal or get nine tens`

- Exact phrase text: `find the hexadecimal or get nine tens`
- Coordinates:
  - `find`: `E1 -> F1 -> G1 -> H1`
  - `the`: `I1 -> J1 -> I2`
    - alternate exact `the`: `I1 -> J1 -> J2`
  - `hexadecimal`: `I3 -> I4 -> I5 -> I6 -> H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11`
  - `or`: `D12 -> E13`
  - `get`: `F12 -> G13 -> F14`
  - `nine`: `E14 -> D13 -> C14 -> D14`
  - `tens`: `C13 -> B13 -> A12 -> A11`
    - alternate exact `tens` ends `B12`
- Local region / component: cross top ribbon into lower-right engine
- Attached or detached: attached exact composition
- Likely role: selector

#### `find the hexadecimal or ten integer by six`

- Exact phrase text: `find the hexadecimal or ten integer by six`
- Coordinates:
  - same `find / the / hexadecimal / or`
  - `ten`: `F14 -> G13 -> H12`
  - `integer`: `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
  - `by`: `L12 -> M13`
  - `six`: `L14 -> M14 -> N14`
- Local region / component: cross top ribbon into lower-right engine
- Attached or detached: attached exact composition
- Likely role: selector

#### `find the hexadecimal or tens integer by six`

- Exact phrase text: `find the hexadecimal or tens integer by six`
- Coordinates:
  - same `find / the / hexadecimal / or`
  - `tens`: `F14 -> G13 -> H12 -> I13`
  - `integer`: `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
  - `by`: `L12 -> M13`
  - `six`: `L14 -> M14 -> N14`
  - alternate exact `integer` starts `J12`
- Local region / component: cross top ribbon into lower-right engine
- Attached or detached: attached exact composition
- Likely role: selector

#### `find the hexadecimal to tens`

- Exact phrase text: `find the hexadecimal to tens`
- Coordinates:
  - `find`: `E1 -> F1 -> G1 -> H1`
  - `the`: `I1 -> J1 -> I2`
    - alternate exact `the`: `I1 -> J1 -> J2`
  - `hexadecimal`: `I3 -> I4 -> I5 -> I6 -> H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11`
  - `to`: `C12 -> D12`
  - `tens`: `C13 -> B13 -> A12 -> A11`
    - alternate exact `tens` ends `B12`
- Local region / component: cross top ribbon into lower-right engine
- Attached or detached: attached exact composition
- Likely role: selector / unresolved

## Investigated But Not Promoted

### `add`

Exact but not promoted as controller evidence:

- `add the start nine go`
  - one exact instance:
  - `H2 -> G2 -> H1 / I1 -> J1 -> J2 / K1 -> K2 -> L1 -> M1 -> N1 / M2 -> M3 -> L4 -> K4 / J3 -> K3`
- `start nine get add`
  - one exact instance:
  - `K1 -> K2 -> L1 -> M1 -> N1 / M2 -> M3 -> L4 -> K4 / J3 -> I2 -> I1 / H2 -> H1 -> G2`

Why not promoted:

- exact, but the controller role is too unstable and there is no objective handoff into the lower-right engine.

### `find three ten`

- exact phrase exists in the upper-left region
- not promoted here because it is better treated as part of the detached extraction-like family, not controller language

## Control Inventory Takeaway

- The top ribbon is no longer purely detached meta-language.
- Exact `find the hexadecimal ...` phrases attach directly into the lower-right engine and objectively favor the hexadecimal family.
- Exact `find the hexadecimal or get nine tens` is especially important because the parallel `... get nine total` phrase was not found.
- The lower-right `step or X` shell remains the strongest local selector shell.
