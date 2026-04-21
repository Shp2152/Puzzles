# Controller Hypotheses

This file tests whether the top ribbon can act as a non-overlap or lightly-overlap controller for the lower-right engine.

Relation labels used here:

- exact overlap/subphrase composition
- meta/control relation
- unsupported leap

## A. Start / Read-Order Controller

### Hypothesis A1

- claim:
  - `find the start` gives a top-level read-order instruction for the puzzle
- exact supporting phrase:
  - `find the start`
  - `E1 -> F1 -> G1 -> H1 / I1 -> J1 -> J2 / K1 -> K2 -> L1 -> M1 -> N1`
- objective referent map used:
  - specific top-ribbon phrase instance
- handoff quality:
  - grounded as local controller/meta language
  - not grounded as a selector of a lower-right engine component
- exact ambiguity remaining:
  - what exactly counts as the “start” beyond the top-ribbon phrase itself

### Hypothesis A verdict

- plausible but weak for global engine control
- better as meta/read-order language than as a selector of a lower-right branch

## B. Start-Value / Start-Index Controller

### Hypothesis B1

- claim:
  - `find the start nine` points to a specific engine parameter or branch because of `nine`
- exact supporting phrase:
  - `find the start nine`
- objective referent map used:
  - top-ribbon `nine` instance only
- handoff quality:
  - unsupported for engine selection
- exact ambiguity remaining:
  - no objective map from top `nine` to lower-right `get nine ...` branches

### Hypothesis B verdict

- unsupported

## C. Direction / Continuation Controller

### Hypothesis C1

- claim:
  - `go ahead` favors a specific continuation or traversal
- exact supporting phrases:
  - `find the start nine go`
  - `find the start nine go ahead`
  - `go ahead`
- objective referent map used:
  - top-ribbon `go` and `ahead` instances only
- handoff quality:
  - grounded as local continuation language
  - unsupported as a lower-right branch selector
- exact ambiguity remaining:
  - no objective target beyond the top-ribbon region

### Hypothesis C verdict

- plausible but weak for global control

## D. Branch Selector For The Lower-Right Engine

### Hypothesis D1

- claim:
  - `find the hexadecimal or get nine tens` selects the `get nine tens` branch
- exact supporting phrase:
  - `find the hexadecimal or get nine tens`
  - `E1 -> F1 -> G1 -> H1 / I1 -> J1 -> I2 / I3 -> I4 -> I5 -> I6 -> H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11 / D12 -> E13 / F12 -> G13 -> F14 / E14 -> D13 -> C14 -> D14 / C13 -> B13 -> A12 -> A11`
  - alternate exact `the` and `tens` variants also exist
- objective referent map used:
  - specific representation label `hexadecimal`
  - specific branch phrase instance `get nine tens`
- handoff quality:
  - grounded
- exact ambiguity remaining:
  - this selects `get nine tens` over `get nine total` because exact `find the hexadecimal or get nine total` was not found
  - but it does not settle competition against exact `find the hexadecimal or ten integer by six` and `find the hexadecimal or tens integer by six`

### Hypothesis D2

- claim:
  - `find the hexadecimal or ten integer by six` / `find the hexadecimal or tens integer by six` select tail-side branches
- exact supporting phrases:
  - `find the hexadecimal or ten integer by six`
  - `find the hexadecimal or tens integer by six`
- objective referent map used:
  - specific `hexadecimal` instance
  - specific tail-side complement instances
- handoff quality:
  - grounded
- exact ambiguity remaining:
  - there are now multiple grounded branch complements under the same `find the hexadecimal or ...` controller shell

### Hypothesis D verdict

- grounded, but not unique

## E. Representation Selector

### Hypothesis E1

- claim:
  - top controller language objectively favors the hexadecimal family
- exact supporting phrases:
  - `find the hexadecimal ten ten ten integer by six`
  - `find the hexadecimal ten ten ten to integer`
  - `find the hexadecimal or get nine tens`
  - `find the hexadecimal or ten integer by six`
  - `find the hexadecimal or tens integer by six`
  - `find the hexadecimal to tens`
- objective referent map used:
  - the specific `hexadecimal` word instance `I3 -> I4 -> I5 -> I6 -> H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11`
  - absence of parallel exact `find the decimal ...` and `find the binary ...` controller phrases in the tested family
- handoff quality:
  - grounded
- exact ambiguity remaining:
  - the controller selects the representation family cleanly, but not one unique branch or output interpretation inside it

### Hypothesis E verdict

- strongest controller hypothesis in this pass

## Controller-Hypothesis Takeaway

- The previous “top ribbon is just meta” view is no longer strong enough.
- The top side still contains detached meta language (`find the start ...`, `go ahead`), but it also contains an attached exact controller family centered on `find the hexadecimal ...`.
- What remains unresolved is not representation selection.
- It is branch and execution selection *inside* the selected hexadecimal controller family.
