# Boundary Expansions

All promoted phrases below were re-verified directly against `can u dig it.csv:1-14` with `bridge_selector_search/boundary_bridge_probe.py`.

Helper note:

- The helper uses the raw grid as evidence source.
- It uses `/usr/share/dict/words` plus a small custom frontier-word list only to generate candidate word hypotheses.
- Every promoted phrase below is cited by raw coordinates.
- The helper imports only these generic assumptions:
  - rectangular CSV grid
  - lowercase cell matching
  - standard 8-neighbor adjacency
  - no cell reuse inside a word path
  - no cell reuse across a chained phrase path

Search note:

- A raw 1-word boundary search around each frontier phrase was broad and produced many exact but useless dictionary artifacts.
- Promoted expansions below are the exact results that looked bridge-relevant or selector-relevant.
- 2- to 4-word follow-up searches were run only on those promoted exact expansions.

## Top Ribbon Frontier

### Base node: `find the start`

Promoted exact after-expansion:

- `find the start nine`
  - `E1 -> F1 -> G1 -> H1 / I1 -> J1 -> J2 / K1 -> K2 -> L1 -> M1 -> N1 / M2 -> M3 -> L4 -> K4`
  - alternate `nine` ends `M5`

No promoted exact before-expansion was found.

High-quality near-miss boundary results:

- `there find the start`
- `integers find the start`

Reason not promoted:

- exact but semantically weak, with no bridge value and no attachment into the lower-right frontier.

Junk examples from the exhaustive 1-word search:

- `teeters find the start`
- `eerie find the start`
- `mullahs find the start`

### Base node: `find the start nine`

Promoted exact after-expansions:

- `find the start nine go`
  - `E1 -> F1 -> G1 -> H1 / I1 -> J1 -> J2 / K1 -> K2 -> L1 -> M1 -> N1 / M2 -> M3 -> L4 -> K4 / J3 -> K3`
- `find the start nine go ahead`
  - `E1 -> F1 -> G1 -> H1 / I1 -> J1 -> J2 / K1 -> K2 -> L1 -> M1 -> N1 / M2 -> M3 -> L4 -> K4 / J3 -> K3 / J4 -> I3 -> I2 -> H2 -> G2`

Promoted exact after-follow-up from `find the start nine go ahead`:

- none with bridge or selector value

No promoted exact before-expansion was found.

High-quality near-miss boundary result:

- `find the start nine go` and lower-right exact `go integer by six` both exist
- near-miss reason:
  - the top `go` is `J3 -> K3`
  - the lower-right `go` is `I9 -> I10`
  - disconnected word instance, so no exact bridge

Junk examples:

- `find the start nine naiad`
- `find the start nine wrest`
- `find the start nine stain`

### Base node: `find the start nine go`

Promoted exact after-expansion:

- `find the start nine go ahead`
  - same coordinates as above

No promoted exact before-expansion was found.

Follow-up result:

- no promoted exact continuation from `go ahead` into `to`, `into`, `integer`, `binary`, `decimal`, `hexadecimal`, `baseten`, or `base ten integer`

## Detached Place-Value Frontier

### Base node: `get ones`

Promoted exact before-expansion:

- `the get ones`
  - `I1 -> J1 -> I2 / J3 -> J2 -> K2 / K3 -> L4 -> M5 -> M6`

No promoted exact after-expansion was found.

High-quality near-miss boundary results:

- `get ones the`
- `get ones them`

Reason not promoted:

- exact but not bridge-bearing; no clean continuation into the lower-right component was found.

Junk examples:

- `axe get ones`
- `isolate get ones`
- `get ones theme`

### Base node: `three ten hundred`

Promoted exact expansions:

- none

High-quality near-miss family adjacent to the same upper-left region:

- `find three ten`
  - one exact instance: `E7 -> D6 -> C5 -> D4 / C3 -> B2 -> C2 -> B3 -> A4 / B5 -> C4 -> D5`
  - three other exact variants in the same region also exist

Reason not promoted as a bridge:

- it does not include the full frontier node `three ten hundred`
- it does not reach the lower-right backbone

Junk example:

- `three ten hundred isolate`

### Base node: `three ten hundreds`

Promoted exact expansions:

- none

## Lower-Right Branch Frontier

### Base node: `binary get nine total`

Promoted exact expansions:

- none

High-quality near-miss boundary results:

- no promoted bridge-bearing after-expansion
- exact junky after-expansions do exist, e.g. `binary get nine total aim`
  - one instance: `F10 -> E10 -> E11 -> E12 -> E13 -> F13 / F12 -> G13 -> F14 / E14 -> D13 -> C14 -> B13 / C13 -> D12 -> C12 -> B11 -> B10 / C10 -> B9 -> C8`
  - not promoted because it does not connect to any frontier gap and looks purely combinatorial

### Base node: `binary get nine tens`

Promoted exact after-expansion:

- `binary get nine tens to`
  - `F10 -> E10 -> E11 -> E12 -> E13 -> F13 / F12 -> G13 -> F14 / E14 -> D13 -> C14 -> D14 / C13 -> B13 -> A12 -> B12 / C12 -> D12`
  - alternate `binary` path starts `F10 -> F11`

Promoted follow-up result:

- no promoted exact continuation from `binary get nine tens to` into `integer by six` or the output labels

High-quality near-miss follow-up:

- `to integer by six` is exact, but uses a disconnected `to` instance
  - `binary get nine tens to`: `to = C12 -> D12`
  - `to integer by six`: `to = H10 -> I10` or `H11 -> I10`

Junk examples:

- `binary get nine tens alit`
- `binary get nine tens tail`

### Base node: `integer by six`

Promoted exact before-expansions:

- `into integer by six`
  - one exact instance: `I12 -> H12 -> H11 -> I10 / J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
  - alternate exact `into` instance starts `G11 -> H12 -> H11 -> I10`
- `to integer by six`
  - exact instances:
  - `H10 -> I10 / J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
  - `H11 -> I10 / J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
- `go integer by six`
  - `I9 -> I10 / J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
- `step integer by six`
  - `I13 -> I14 -> J14 -> J13 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
  - alternate exact `integer` starts `J12`
- `step or integer by six`
  - exact instances include:
  - `N9 -> M9 -> M10 -> L11 / K12 -> K13 / J12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
  - `N9 -> N10 -> M10 -> L11 / K12 -> K13 / J12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
  - `I13 -> I14 -> J14 -> J13 / K12 -> K13 / J12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
- `ten integer by six`
  - exact lower-right `ten` instances:
  - `F14 -> G13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
  - `I14 -> H13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
- `tens integer by six`
  - exact lower-right `tens` instances continue the same tail

No promoted exact after-expansion was found.

Junk examples:

- `poi integer by six`
- `yens integer by six`

### Base node: `baseten integer`

Promoted exact before-expansions:

- `or baseten integer`
  - `K12 -> K13 / L12 -> L13 -> K14 -> J14 -> I14 -> H13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- `step baseten integer`
  - exact lower-right step family
- `step or baseten integer`
  - exact instances include:
  - `N9 -> M9 -> M10 -> L11 / K12 -> K13 / L12 -> L13 -> K14 -> J14 -> I14 -> H13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
  - `N9 -> N10 -> M10 -> L11 / K12 -> K13 / L12 -> L13 -> K14 -> J14 -> I14 -> H13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`

No promoted exact after-expansion was found.

Junk examples:

- `air baseten integer`
- `pro baseten integer`

### Base node: `base ten integer`

Promoted exact before-expansions:

- `or base ten integer`
  - `K12 -> K13 / L12 -> L13 -> K14 -> J14 / I14 -> H13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- `step base ten integer`
  - exact lower-right step family
- `step or base ten integer`
  - exact instances include:
  - `N9 -> M9 -> M10 -> L11 / K12 -> K13 / L12 -> L13 -> K14 -> J14 / I14 -> H13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
  - `N9 -> N10 -> M10 -> L11 / K12 -> K13 / L12 -> L13 -> K14 -> J14 / I14 -> H13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`

No promoted exact after-expansion was found.

### Base nodes: `step baseten integer` and `step base ten integer`

Promoted exact expansions:

- none beyond the `step or ...` family already listed above

Junk example:

- `hgt step baseten integer`

## Boundary Expansion Takeaway

- The top ribbon has exact local growth, but it stalls inside its own upper-right region.
- `get ones` and `three ten hundred(s)` do not grow into the lower-right backbone.
- The lower-right boundary produced the strongest new exact functional shells:
  - `binary get nine tens to`
  - `step or integer by six`
  - `step or baseten integer`
  - `step or base ten integer`
- Those shells matter for selector analysis, but none yet gives a complete exact bridge across the unresolved gaps.
