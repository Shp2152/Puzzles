# Instance Hypergraph

Nodes below are exact phrase instances from `representation_constructive/02_exact_representation_phrases.md`.

## Active Node Set

### Detached top ribbon

- T1 = `find the start nine`
  - `E1 -> F1 -> G1 -> H1 / I1 -> J1 -> J2 / K1 -> K2 -> L1 -> M1 -> N1 / M2 -> M3 -> L4 -> K4`
- T2 = `find the start nine go`
  - T1 plus `J3 -> K3`

### Lower-right representation and output nodes

- R1 = `hexadecimal ten ten ten integer`
- R2 = `hexadecimal ten ten ten integer by six`
- R3 = `decimal ten ten ten integer`
- R4 = `decimal ten ten ten integer by six`
- R5a = `binary ten integer`
  - `binary = F10 -> E10 -> E11 -> E12 -> E13 -> F13`
- R5b = `binary ten integer`
  - `binary = F10 -> F11 -> E11 -> E12 -> E13 -> F13`
- R6a = `binary ten integer by six`
  - same `binary` as R5a
- R6b = `binary ten integer by six`
  - same `binary` as R5b
- R7 = `baseten integer`
- R8a = `step baseten integer`
  - `step = N9 -> M9 -> M10 -> L11`
- R8b = `step baseten integer`
  - `step = N9 -> N10 -> M10 -> L11`
- R9 = `step by six`
  - promoted step-path family in the same lower-right zone
- R10 = `step into integer by six`
  - `step = I13 -> I14 -> J14 -> J13`
- R11 = `base ten integer`
- R12a = `step base ten integer`
  - same `step` as R8a
- R12b = `step base ten integer`
  - same `step` as R8b
- R13 = `integer by six`
  - promoted lower-right `integer / by / six` tail family

### Lower-right representation-to-total and representation-to-tens bridge nodes

- B1 = `binary get nine total`
  - `binary = F10 -> E10 -> E11 -> E12 -> E13 -> F13`
- B2 = `binary get nine total`
  - `binary = F10 -> F11 -> E11 -> E12 -> E13 -> F13`
- B3 = `binary get nine tens`
  - `binary = F10 -> E10 -> E11 -> E12 -> E13 -> F13`
- B4 = `binary get nine tens`
  - `binary = F10 -> F11 -> E11 -> E12 -> E13 -> F13`
- P1 = `get nine total`
- P2 = `decimal tens`
- P3 = `hexadecimal tens`
- P4 = `binary tens`

### Detached place-value nodes

- U1 = `three ten hundred`
- U2 = `three ten hundreds`
- U3 = `get ones`

## Allowed Edge Types

- direct reuse of the same word instance
- genuine spatial overlap
- strong exact local attachment already justified by the full phrase path

## Core Edges

### Representation objects to the shared `integer by six` tail

- R1 <-> R2
  - direct reuse of the same `hexadecimal`, three `ten` instances, and `integer`
- R3 <-> R4
  - direct reuse of the same `decimal`, three `ten` instances, and `integer`
- R5a <-> R6a
  - direct reuse of the same `binary`, `ten`, and `integer`
- R5b <-> R6b
  - direct reuse of the same `binary`, `ten`, and `integer`
- R2 <-> R13
  - direct reuse of the same `integer`, `by`, and `six`
- R4 <-> R13
  - direct reuse of the same `integer`, `by`, and `six`
- R6a <-> R13
  - direct reuse of the same `ten`, `integer`, `by`, and `six`
- R6b <-> R13
  - direct reuse of the same `ten`, `integer`, `by`, and `six`
- R10 <-> R13
  - direct reuse of the same lower-right `integer`, `by`, and `six`

### Output-label subcluster

- R7 <-> R8a
  - direct reuse of the same `baseten` and `integer`
- R7 <-> R8b
  - direct reuse of the same `baseten` and `integer`
- R7 <-> R11
  - genuine spatial overlap
  - `R11` splits the exact `baseten` path in R7 into `base` plus `ten`
- R8a <-> R12a
  - genuine spatial overlap
  - `R12a` splits the exact `baseten` path in R8a into `base` plus `ten`
- R8b <-> R12b
  - genuine spatial overlap
  - `R12b` splits the exact `baseten` path in R8b into `base` plus `ten`
- R11 <-> R12a
  - direct reuse of `base`, `ten`, and `integer`
- R11 <-> R12b
  - direct reuse of `base`, `ten`, and `integer`
- R8a <-> R9
  - direct reuse of the same lower-right `step` instance family
- R8b <-> R9
  - direct reuse of the same lower-right `step` instance family

### Representation-to-total and representation-to-tens bridge

- R5a <-> B1
  - direct reuse of the same `binary` instance `F10 -> E10 -> E11 -> E12 -> E13 -> F13`
- R5a <-> B3
  - direct reuse of the same `binary` instance `F10 -> E10 -> E11 -> E12 -> E13 -> F13`
- R6a <-> B1
  - direct reuse of the same `binary` instance
- R6a <-> B3
  - direct reuse of the same `binary` instance
- R5b <-> B2
  - direct reuse of the same `binary` instance `F10 -> F11 -> E11 -> E12 -> E13 -> F13`
- R5b <-> B4
  - direct reuse of the same `binary` instance `F10 -> F11 -> E11 -> E12 -> E13 -> F13`
- R6b <-> B2
  - direct reuse of the same `binary` instance
- R6b <-> B4
  - direct reuse of the same `binary` instance
- B1 <-> P1
  - direct reuse of `get`, `nine`, and `total`
- B2 <-> P1
  - direct reuse of `get`, `nine`, and `total`
- B3 <-> P4
  - direct reuse of the same `binary` instance
- B4 <-> P4
  - direct reuse of the same `binary` instance
- B3 <-> P1
  - direct reuse of `get` and one lower `nine` instance family; the last word differs (`tens` vs `total`)
- B4 <-> P1
  - same justification as B3 <-> P1

### Representation objects to place-value labels

- R3 <-> P2
  - direct reuse of the same `decimal` instance `H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11`
- R1 <-> P3
  - direct reuse of the same `hexadecimal` instance `I3 -> I4 -> I5 -> I6 -> H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11`
- R5a <-> P4
  - direct reuse of the same `binary` instance `F10 -> E10 -> E11 -> E12 -> E13 -> F13`
- R5b <-> P4
  - direct reuse of the same `binary` instance `F10 -> F11 -> E11 -> E12 -> E13 -> F13`

## Detached Or Weakly Attached Nodes

- T1 and T2 remain detached from the lower-right component.
  - no exact attachment from `find the start ...` into `binary`, `decimal`, `hexadecimal`, `baseten`, `base ten integer`, or `integer by six`
- U1 and U2 remain detached from the lower-right component.
  - any attempt to make their upper-left `ten` the same semantic `ten` as the lower-right representation tail is a disconnected merge
- U3 remains detached from the lower-right component.
  - `get ones` is exact at `J3 -> J2 -> K2 / K3 -> L4 -> M5 -> M6`, but no exact continuation into the lower-right representation cluster was found

## Forced Same-Word Merges To Penalize

- `nine`
  - top-ribbon `nine`: `M2 -> M3 -> L4 -> K4` in T1/T2
  - lower bridge `nine`: `E14 -> D13 -> C14 -> B13` or `E14 -> D13 -> C14 -> D14` in B1-B4 and P1
  - any one-story reading that treats these as one semantic `nine` is forcing a disconnected merge
- `step`
  - output-label `step`: `N9 -> M9 -> M10 -> L11` or `N9 -> N10 -> M10 -> L11` in R8a/R8b/R9/R12a/R12b
  - tail `step`: `I13 -> I14 -> J14 -> J13` in R10
  - any one-operation reading that treats these as one single exact `step` is forcing a disconnected merge
- `ten`
  - lower-right triple-ten tail in R1-R4
  - lower-right split `base ten` in R11/R12a/R12b
  - lower-left `ten` in U1/U2
  - only the first two are exact local resegmentations of the same lower-right structure; the upper-left `ten` is disconnected
- `integer`
  - lower-right `integer`: `I12/J11/J12 -> ... -> M12` in R1-R13
  - upper-left `integer` instances exist near `D6/C5/B5/...` but do not exact-attach into the lower-right component in this pass

## Graph Reading

- The dominant exact component is now larger than in the prior audit.
- It includes representation objects, the `integer by six` tail, the `baseten` / `base ten` output label, and the binary bridge into `get nine total` and `get nine tens`.
- The most important new fact is that `get nine total` is no longer graph-detached if the binary bridge nodes B1/B2 are admitted.
- The still-detached material is concentrated in:
  - the top `find the start ...` ribbon
  - the upper-left `three ten hundred(s)` family
  - the upper/mid `get ones` fragment

## Consequence For Global Stories

- A representation-first story is now strictly better connected than a procedure-first story under the exact-instance rubric.
- That does not solve the puzzle.
- It means the unresolved global problem has shifted:
  - not "can representation attach to anything?"
  - but rather "what exact bridge selects or extracts the intended value from the now-connected lower-right representation component?"
