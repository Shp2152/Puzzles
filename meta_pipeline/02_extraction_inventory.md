# Extraction Inventory

All promoted phrases below were re-verified directly against `can u dig it.csv:1-14` with `meta_pipeline/controller_extraction_probe.py`.

## Detached Extraction-Like Phrases

### `get ones`

- Exact phrase text: `get ones`
- Coordinates:
  - `get`: `J3 -> J2 -> K2`
  - `ones`: `K3 -> L4 -> M5 -> M6`
- Local region / component: upper-mid detached family
- Likely role: digit extraction

### `three ten hundred`

- Exact phrase text: `three ten hundred`
- Coordinates:
  - `three`: `C3 -> B2 -> C2 -> B3 -> A4`
  - `ten`: `B5 -> C4 -> C5`
  - `hundred`: `B6 -> C6 -> D5 -> D4 -> D3 -> D2 -> C1`
- Local region / component: upper-left detached family
- Likely role: place-value description

### `three ten hundreds`

- Exact phrase text: `three ten hundreds`
- Coordinates:
  - same `three` and `ten` as above
  - `hundreds`: `B6 -> C6 -> D5 -> D4 -> D3 -> D2 -> C1 -> B1`
- Local region / component: upper-left detached family
- Likely role: place-value description

### `ten hundred`

- Exact phrase text: `ten hundred`
- Promoted exact instances:
  - `C3 -> C4 -> C5 / B6 -> C6 -> D5 -> D4 -> D3 -> D2 -> C1`
  - `B5 -> C4 -> C5 / B6 -> C6 -> D5 -> D4 -> D3 -> D2 -> C1`
- Local region / component: upper-left detached family
- Likely role: place-value description

### `ten hundreds`

- Exact phrase text: `ten hundreds`
- Promoted exact instances:
  - `C3 -> C4 -> C5 / B6 -> C6 -> D5 -> D4 -> D3 -> D2 -> C1 -> B1`
  - `B5 -> C4 -> C5 / B6 -> C6 -> D5 -> D4 -> D3 -> D2 -> C1 -> B1`
- Local region / component: upper-left detached family
- Likely role: place-value description

## Lower-Right Engine Extraction / Aggregation Phrases

### `get nine total`

- Exact phrase text: `get nine total`
- Coordinates:
  - `get`: `F12 -> G13 -> F14`
  - `nine`: `E14 -> D13 -> C14 -> B13`
    - alternate exact `nine`: `E14 -> D13 -> C14 -> D14`
  - `total`: `C13 -> D12 -> C12 -> B11 -> B10`
- Local region / component: lower-right engine
- Likely role: aggregation

### `get nine tens`

- Exact phrase text: `get nine tens`
- Coordinates:
  - `get`: `F12 -> G13 -> F14`
  - `nine`: `E14 -> D13 -> C14 -> D14`
  - `tens`: `C13 -> B13 -> A12 -> A11`
    - alternate exact `tens` ends `B12`
- Local region / component: lower-right engine
- Likely role: place-value description / aggregation

### `get nine to tens`

- Exact phrase text: `get nine to tens`
- Coordinates:
  - `get`: `F12 -> G13 -> F14`
  - `nine`: `E14 -> D13 -> C14 -> D14`
  - `to`: `C13 -> D12`
  - `tens`: `C12 -> B13 -> A12 -> A11`
    - alternate exact `tens` ends `B12`
- Local region / component: lower-right engine
- Likely role: unresolved

### `binary get nine total`

- Exact phrase text: `binary get nine total`
- Representative coordinates:
  - `binary`: `F10 -> E10 -> E11 -> E12 -> E13 -> F13`
    - alternate exact path starts `F10 -> F11`
  - same `get nine total` tail as above
- Local region / component: lower-right engine
- Likely role: aggregation / mode-labeled branch

### `binary get nine tens`

- Exact phrase text: `binary get nine tens`
- Representative coordinates:
  - `binary`: `F10 -> E10 -> E11 -> E12 -> E13 -> F13`
    - alternate exact path starts `F10 -> F11`
  - same `get nine tens` tail as above
- Local region / component: lower-right engine
- Likely role: place-value description / mode-labeled branch

### `binary get nine to tens`

- Exact phrase text: `binary get nine to tens`
- Representative coordinates:
  - `binary`: `F10 -> E10 -> E11 -> E12 -> E13 -> F13`
    - alternate exact path starts `F10 -> F11`
  - same `get nine to tens` tail as above
- Local region / component: lower-right engine
- Likely role: unresolved

## Cross Controller-To-Extraction Phrase

### `find the hexadecimal or get nine tens`

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
- Likely role: extraction-branch selection

## Investigated But Not Promoted

- `binary get nine tens to`
  - exact, but better treated as controller/dispatch-side ambiguity than as stable extraction language
- odd long exact chains such as `nine ten get hundred` were not promoted
  - reason: exact, but parser-hostile and not needed for the extraction hypotheses

## Extraction Inventory Takeaway

- The detached extraction family is still headed by `get ones` and `three ten hundred(s)`.
- Inside the lower-right engine, `get nine total` and `get nine tens` remain the main extraction/aggregation candidates.
- The exact `get nine to tens` variant keeps the tens branch syntactically ambiguous.
- The new exact phrase `find the hexadecimal or get nine tens` is the strongest controller-to-extraction handoff found in this pass.
