# Bridge Candidates

All bridge claims below are re-proved directly from `can u dig it.csv:1-14`.

Edge policy used here:

- exact bridge only if there is:
  - identical shared word instance
  - full exact phrase inclusion
  - genuine spatial overlap
  - or an explicitly justified exact local attachment
- lexical siblings such as `tens` vs `total` are not exact bridge edges

## A. Top Ribbon -> Lower-Right Representation Backbone

### Exact bridge

- none found

### Near-miss bridges

#### A1. `find the start nine go` vs `go integer by six`

- exact top-ribbon phrase:
  - `find the start nine go`
  - `E1 -> F1 -> G1 -> H1 / I1 -> J1 -> J2 / K1 -> K2 -> L1 -> M1 -> N1 / M2 -> M3 -> L4 -> K4 / J3 -> K3`
- exact lower-right phrase:
  - `go integer by six`
  - `I9 -> I10 / J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
- what it would have solved if valid:
  - direct attachment from top ribbon into the lower-right tail
- why it fails:
  - disconnected `go` instance
  - top `go` is `J3 -> K3`
  - lower-right `go` is `I9 -> I10`

#### A2. Top `nine` vs lower `nine`

- exact top `nine` in `find the start nine`:
  - `M2 -> M3 -> L4 -> K4`
- exact lower `nine` in `binary get nine total` or `get nine total`:
  - `E14 -> D13 -> C14 -> B13`
  - or `E14 -> D13 -> C14 -> D14`
- what it would have solved if valid:
  - lexical attachment from top ribbon into the binary/total branch
- why it fails:
  - disconnected word instance

### False bridges

- no exact `find the start decimal`
- no exact `find the start hexadecimal`
- no exact `find the start nine go to integer by six`
- no exact `find the start nine go integer by six`

## B. Upper-Left Place-Value Nodes -> Lower-Right Representation Backbone

### Exact bridge

- none found

### Near-miss bridges

#### B1. `three ten hundred` vs `ten integer by six`

- exact upper-left phrase:
  - `three ten hundred`
  - `C3 -> B2 -> C2 -> B3 -> A4 / B5 -> C4 -> C5 / B6 -> C6 -> D5 -> D4 -> D3 -> D2 -> C1`
- exact lower-right phrase:
  - `ten integer by six`
  - `F14 -> G13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
  - alternate lower-right `ten`: `I14 -> H13 -> H12`
- what it would have solved if valid:
  - upper-left payload attachment into the lower-right tail
- why it fails:
  - disconnected `ten` instance
  - upper-left `ten` is `B5 -> C4 -> C5`
  - lower-right `ten` is `F14 -> G13 -> H12` or `I14 -> H13 -> H12`

#### B2. `the get ones` vs `the decimal ten ten ten`

- exact upper/mid phrase:
  - `the get ones`
  - `I1 -> J1 -> I2 / J3 -> J2 -> K2 / K3 -> L4 -> M5 -> M6`
- exact lower-right phrase:
  - `the decimal ten ten ten`
  - `G6 -> H6 -> I7 / H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11 / C12 -> B13 -> C14 / C13 -> D14 -> E14 / F14 -> G13 -> H12`
- what it would have solved if valid:
  - direct glue-bearing bridge from `get ones` into the representation family
- why it fails:
  - disconnected `the` instance

#### B3. `get hundred` vs `get nine total`

- exact upper-left phrase:
  - `get hundred`
  - one instance: `B4 -> A4 -> B5 / B6 -> C6 -> C5 -> D4 -> D3 -> D2 -> C1`
- exact lower phrase:
  - `get nine total`
  - `F12 -> G13 -> F14 / E14 -> D13 -> C14 -> D14 / C13 -> D12 -> C12 -> B11 -> B10`
- what it would have solved if valid:
  - direct `get`-based link from upper-left place values into the lower-right total branch
- why it fails:
  - disconnected `get` instance

### False bridges

- no exact `get ones baseten integer`
- no exact `three ten hundred integer by six`
- no exact `three ten hundred base ten integer`

## C. `binary get nine total` / `binary get nine tens` -> `integer by six`

### Exact bridge

- yes, but only as an exact lower-right chain, not as one exact long phrase

#### C1. `binary get nine total` -> `binary ten integer by six` -> `integer by six`

- exact `binary get nine total`:
  - `F10 -> E10 -> E11 -> E12 -> E13 -> F13 / F12 -> G13 -> F14 / E14 -> D13 -> C14 -> B13 / C13 -> D12 -> C12 -> B11 -> B10`
  - alternate exact `binary` path starts `F10 -> F11`
- exact `binary ten integer by six`:
  - `F10 -> E10 -> E11 -> E12 -> E13 -> F13 / F14 -> G13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
  - alternate exact `binary` path starts `F10 -> F11`
- exact `integer by six`:
  - `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
- bridge justification:
  - identical shared `binary` instance between the first two phrases
  - full exact phrase inclusion of `integer by six` inside the third phrase

#### C2. `binary get nine tens` -> `binary ten integer by six` -> `integer by six`

- exact `binary get nine tens`:
  - `F10 -> E10 -> E11 -> E12 -> E13 -> F13 / F12 -> G13 -> F14 / E14 -> D13 -> C14 -> D14 / C13 -> B13 -> A12 -> B12`
  - alternate exact `binary` path starts `F10 -> F11`
- bridge justification:
  - identical shared `binary` instance into the same `binary ten integer by six` node
  - then full exact phrase inclusion of `integer by six`

### Near-miss bridge

#### C3. `binary get nine tens to` vs `to integer by six`

- exact left phrase:
  - `binary get nine tens to`
  - `F10 -> E10 -> E11 -> E12 -> E13 -> F13 / F12 -> G13 -> F14 / E14 -> D13 -> C14 -> D14 / C13 -> B13 -> A12 -> B12 / C12 -> D12`
- exact right phrase:
  - `to integer by six`
  - `H10 -> I10 / J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
  - alternate `to = H11 -> I10`
- what it would have solved if valid:
  - explicit selector from the binary-tens branch into the tail branch
- why it fails:
  - disconnected `to` instance
  - left `to = C12 -> D12`
  - right `to = H10 -> I10` or `H11 -> I10`

### False bridges

- no exact `binary get nine total integer by six`
- no exact `binary get nine tens integer by six`
- no exact `binary get nine total to integer by six`
- no exact `binary get nine tens to integer by six`

## D. `binary get nine total` / `binary get nine tens` -> `baseten integer` / `base ten integer`

### Exact bridge

- yes, but again only as a lower-right chain, not as an explicit routing phrase

#### D1. Binary branch -> tail -> output label

- exact bridge chain:
  - `binary get nine total` or `binary get nine tens`
  - `-> binary ten integer by six`
  - `-> integer by six`
  - `-> baseten integer` or `base ten integer`
- bridge justification for the last hop:
  - exact `integer by six` shares the identical `integer` instance `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12` with exact `baseten integer`
  - the same lower-right `integer` instance also appears in exact `base ten integer`

### Near-miss bridges

#### D2. Output phrase with exact `or`

- exact output-side phrases:
  - `or baseten integer`
    - `K12 -> K13 / L12 -> L13 -> K14 -> J14 -> I14 -> H13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
  - `or base ten integer`
    - `K12 -> K13 / L12 -> L13 -> K14 -> J14 / I14 -> H13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- what they would have solved if valid:
  - explicit routing from a selected branch into the output label
- why they fail:
  - no exact branch phrase reaches the `or` at `K12 -> K13`
  - no exact combined phrase from the binary-total or binary-tens branch into either output phrase was found

### False bridges

- no exact `binary get nine total baseten integer`
- no exact `binary get nine tens baseten integer`
- no exact `binary get nine total base ten integer`
- no exact `binary get nine tens base ten integer`

## E. `integer by six` -> `baseten integer` / `base ten integer`

### Exact bridge

- yes

#### E1. `integer by six` -> `baseten integer`

- exact `integer by six`:
  - `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
- exact `baseten integer`:
  - `L12 -> L13 -> K14 -> J14 -> I14 -> H13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- bridge justification:
  - identical shared `integer` instance `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`

#### E2. `integer by six` -> `base ten integer`

- exact `base ten integer`:
  - `L12 -> L13 -> K14 -> J14 / I14 -> H13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- bridge justification:
  - the same identical shared `integer` instance

### Near-miss bridges

#### E3. `step integer by six` vs `step baseten integer`

- exact tail-side phrase:
  - `step integer by six`
  - `I13 -> I14 -> J14 -> J13 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
- exact output-side phrase:
  - `step baseten integer`
  - `N9 -> M9 -> M10 -> L11 / L12 -> L13 -> K14 -> J14 -> I14 -> H13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- what it would have solved if valid:
  - same-step routing from the tail branch into the output label
- why it fails:
  - disconnected `step` instance

#### E4. `step or integer by six` vs `step or baseten integer`

- exact tail-side selector-like phrase:
  - `step or integer by six`
- exact output-side selector-like phrase:
  - `step or baseten integer`
- what it would have solved if valid:
  - explicit selector/routing shell inside the lower-right cluster
- why it still fails as a routing proof:
  - both phrases are exact
  - they share exact `step or`
  - but no exact phrase states that one should be chosen after the binary branch, or that `baseten integer` is the final reporting target rather than another alternative object phrase
  - failure type: unsupported semantic jump, not absence of local exactness

### False bridges

- no exact `baseten integer by six`
- no exact `step baseten integer by six`
- no exact `step or baseten integer by six`

## Bridge Takeaway

- A and B remain unbridged.
- C, D, and E do have exact lower-right bridges, but they are internal structural bridges, not decisive selector/routing instructions.
- The central unsolved gap is therefore narrower than before:
  - not whether the lower-right component connects internally
  - but whether any exact phrase selects and routes through it in a puzzle-resolving way.
