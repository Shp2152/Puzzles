# Maximal Exact Phrases

All promoted phrases below were re-verified directly against `can u dig it.csv:1-14` with `component_syntax/local_component_probe.py`.

Helper note:

- `component_syntax/local_component_probe.py` reuses only the generic assumptions already used by the earlier exact-search helpers:
  - rectangular CSV grid
  - lowercase cell matching
  - standard 8-neighbor adjacency
  - no cell reuse inside a word path
  - no cell reuse across a chained phrase path
- The promoted inventory below was selected from a larger raw-only local enumeration over this controlled syntax vocabulary:
  - `binary decimal hexadecimal integer by six step into or base baseten ten tens total get nine to the go`

## Core Syntax Inventory

### C1. `the decimal ten ten ten integer by six`

- Exact phrase text: `the decimal ten ten ten integer by six`
- Exact coordinates:
  - `the`: `G6 -> H6 -> I7`
  - `decimal`: `H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11`
  - `ten`: `C12 -> B13 -> C14`
  - `ten`: `C13 -> D14 -> E14`
  - `ten`: `F14 -> G13 -> H12`
  - `integer`: `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
  - `by`: `L12 -> M13`
  - `six`: `L14 -> M14 -> N14`
- Maximal or nested: maximal among promoted syntax phrases
- Overlaps:
  - contains `the decimal ten ten ten integer`
  - contains `decimal ten ten ten integer by six`
  - contains `integer by six`
- Syntax shape: unclear, but strongly noun-like / label-like rather than imperative
- Local confidence: high

### C2. `the decimal ten ten ten to integer`

- Exact phrase text: `the decimal ten ten ten to integer`
- Exact coordinates:
  - same `the`, `decimal`, and three `ten` instances as C1
  - `to`: `H11 -> I10`
  - `integer`: `J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- Maximal or nested: maximal among promoted syntax phrases
- Overlaps:
  - contains `the decimal ten ten ten`
  - overlaps C1 on the first five words, but diverges at the tail
- Syntax shape: unclear, but target-like because of exact `to integer`
- Local confidence: medium-high

### C3. `the hexadecimal ten ten ten integer by six`

- Exact phrase text: `the hexadecimal ten ten ten integer by six`
- Exact coordinates:
  - one exact `the` instance: `I1 -> J1 -> I2`
  - alternate exact `the` instances: `I1 -> J1 -> J2`, `K2 -> J1 -> I2`, `K2 -> J1 -> J2`
  - `hexadecimal`: `I3 -> I4 -> I5 -> I6 -> H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11`
  - same three `ten` instances and the same `integer / by / six` tail as C1
- Maximal or nested: maximal among promoted syntax phrases
- Overlaps:
  - contains `the hexadecimal ten ten ten integer`
  - contains `hexadecimal ten ten ten integer by six`
  - contains `integer by six`
- Syntax shape: unclear, but strongly noun-like / label-like rather than imperative
- Local confidence: high

### C4. `hexadecimal ten ten ten to integer`

- Exact phrase text: `hexadecimal ten ten ten to integer`
- Exact coordinates:
  - `hexadecimal`: `I3 -> I4 -> I5 -> I6 -> H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11`
  - same three `ten` instances as C3
  - `to`: `H11 -> I10`
  - `integer`: `J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- Maximal or nested: maximal among promoted syntax phrases
- Overlaps:
  - overlaps C3 on the first four content words, then diverges at the tail
- Syntax shape: unclear, target-like because of exact `to integer`
- Local confidence: medium-high

### C5. `binary ten integer by six`

- Exact phrase text: `binary ten integer by six`
- Exact coordinates:
  - `binary`: `F10 -> E10 -> E11 -> E12 -> E13 -> F13`
    - alternate exact path: `F10 -> F11 -> E11 -> E12 -> E13 -> F13`
  - `ten`: `F14 -> G13 -> H12`
  - `integer`: `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
  - `by`: `L12 -> M13`
  - `six`: `L14 -> M14 -> N14`
- Maximal or nested: maximal among promoted syntax phrases
- Overlaps:
  - contains `binary ten integer`
  - contains `integer by six`
- Syntax shape: noun-like / label-like
- Local confidence: high

### C6. `binary ten to integer by six`

- Exact phrase text: `binary ten to integer by six`
- Exact coordinates:
  - one exact instance:
  - `binary`: `F10 -> E10 -> E11 -> E12 -> E13 -> F13`
  - `ten`: `F14 -> G13 -> H12`
  - `to`: `H11 -> I10`
  - `integer`: `J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
  - `by`: `L12 -> M13`
  - `six`: `L14 -> M14 -> N14`
  - alternate exact `binary` path starts `F10 -> F11`
- Maximal or nested: maximal among promoted syntax phrases
- Overlaps:
  - contains `to integer by six`
  - overlaps C5 on `binary ten`, then diverges by inserting `to`
- Syntax shape: target-like / conversion-like
- Local confidence: high

### C7. `binary get nine total`

- Exact phrase text: `binary get nine total`
- Exact coordinates:
  - `binary`: `F10 -> E10 -> E11 -> E12 -> E13 -> F13`
    - alternate exact path: `F10 -> F11 -> E11 -> E12 -> E13 -> F13`
  - `get`: `F12 -> G13 -> F14`
  - `nine`: `E14 -> D13 -> C14 -> B13`
    - alternate exact lower `nine`: `E14 -> D13 -> C14 -> D14`
  - `total`: `C13 -> D12 -> C12 -> B11 -> B10`
- Maximal or nested: maximal among promoted syntax phrases
- Overlaps:
  - contains `get nine total`
  - overlaps the same `binary` instance as C5/C6
- Syntax shape: verb-like or label-like, unresolved
- Local confidence: high

### C8. `binary get nine tens to`

- Exact phrase text: `binary get nine tens to`
- Exact coordinates:
  - `binary`: `F10 -> E10 -> E11 -> E12 -> E13 -> F13`
    - alternate exact path: `F10 -> F11 -> E11 -> E12 -> E13 -> F13`
  - `get`: `F12 -> G13 -> F14`
  - `nine`: `E14 -> D13 -> C14 -> D14`
  - `tens`: `C13 -> B13 -> A12 -> B12`
  - `to`: `C12 -> D12`
- Maximal or nested: maximal among promoted syntax phrases
- Overlaps:
  - contains `binary get nine tens`
  - overlaps C9 on the first three words, but differs in `tens to` vs `to tens`
- Syntax shape: verb-like or dispatch-like, unresolved
- Local confidence: high

### C9. `binary get nine to tens`

- Exact phrase text: `binary get nine to tens`
- Exact coordinates:
  - `binary`: `F10 -> E10 -> E11 -> E12 -> E13 -> F13`
    - alternate exact path: `F10 -> F11 -> E11 -> E12 -> E13 -> F13`
  - `get`: `F12 -> G13 -> F14`
  - `nine`: `E14 -> D13 -> C14 -> D14`
  - `to`: `C13 -> D12`
  - `tens`: `C12 -> B13 -> A12 -> A11`
    - alternate exact `tens` ends `B12`
- Maximal or nested: maximal among promoted syntax phrases
- Overlaps:
  - contains `binary get nine to`
  - overlaps C8 on `binary get nine`, then diverges in the scope of `to`
- Syntax shape: verb-like or dispatch-like, unresolved
- Local confidence: high

### C10. `step into integer by six`

- Exact phrase text: `step into integer by six`
- Exact coordinates:
  - `step`: `I13 -> I14 -> J14 -> J13`
  - `into`: `I12 -> H12 -> H11 -> I10`
  - `integer`: `J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
  - `by`: `L12 -> M13`
  - `six`: `L14 -> M14 -> N14`
- Maximal or nested: maximal among promoted syntax phrases
- Overlaps:
  - contains `into integer by six`
  - overlaps C11 on `step` and the lower tail, but differs by explicit `into`
- Syntax shape: verb-like
- Local confidence: high

### C11. `step integer by six`

- Exact phrase text: `step integer by six`
- Exact coordinates:
  - `step`: `I13 -> I14 -> J14 -> J13`
  - `integer`: `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
    - alternate exact `integer` starts `J12`
  - `by`: `L12 -> M13`
  - `six`: `L14 -> M14 -> N14`
- Maximal or nested: maximal among promoted syntax phrases
- Overlaps:
  - contains `integer by six`
  - overlaps C10 but drops `into`
- Syntax shape: verb-like, but telegraphic
- Local confidence: medium-high

### C12. `step by six`

- Exact phrase text: `step by six`
- Exact coordinates:
  - one exact instance: `N9 -> M9 -> M10 -> L11 / L12 -> M13 / L14 -> M14 -> N14`
  - alternate exact `step` instances: `N9 -> N10 -> M10 -> L11` and `N9 -> N10 -> M11 -> L11`
- Maximal or nested: maximal among promoted syntax phrases
- Overlaps:
  - shares the `by / six` tail with C10/C11/C13
- Syntax shape: verb-like
- Local confidence: high

### C13. `to integer by six`

- Exact phrase text: `to integer by six`
- Exact coordinates:
  - `to`: `H10 -> I10`
    - alternate exact `to`: `H11 -> I10`
  - `integer`: `J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
  - `by`: `L12 -> M13`
  - `six`: `L14 -> M14 -> N14`
- Maximal or nested: maximal among promoted syntax phrases
- Overlaps:
  - contains `integer by six`
  - contained in C6
- Syntax shape: target-like / prepositional
- Local confidence: medium-high

### C14. `go integer by six`

- Exact phrase text: `go integer by six`
- Exact coordinates:
  - `go`: `I9 -> I10`
  - `integer`: `J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
  - `by`: `L12 -> M13`
  - `six`: `L14 -> M14 -> N14`
- Maximal or nested: maximal among promoted syntax phrases
- Overlaps:
  - contains `integer by six`
- Syntax shape: verb-like, but isolated
- Local confidence: medium

### C15. `step or integer by six`

- Exact phrase text: `step or integer by six`
- Exact coordinates:
  - exact instance 1:
  - `step`: `N9 -> M9 -> M10 -> L11`
  - `or`: `K12 -> K13`
  - `integer`: `J12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
  - `by`: `L12 -> M13`
  - `six`: `L14 -> M14 -> N14`
  - exact instance 2 starts `N9 -> N10 -> M10 -> L11`
  - exact instance 3 uses lower-right `step = I13 -> I14 -> J14 -> J13`
- Maximal or nested: maximal among promoted syntax phrases
- Overlaps:
  - contains `step or`
  - contains `or integer by six`
- Syntax shape: disjunctive / verb-like shell
- Local confidence: high

### C16. `step or baseten integer`

- Exact phrase text: `step or baseten integer`
- Exact coordinates:
  - one exact instance:
  - `step`: `N9 -> M9 -> M10 -> L11`
  - `or`: `K12 -> K13`
  - `baseten`: `L12 -> L13 -> K14 -> J14 -> I14 -> H13 -> H12`
  - `integer`: `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
  - alternate exact `step` starts `N9 -> N10 -> M10 -> L11`
- Maximal or nested: maximal among full exact phrase inclusions; overlaps a longer competing shell in C17
- Overlaps:
  - contains `step or`
  - contains `or baseten integer`
  - overlaps the same `step / or / baseten` shell as C17
- Syntax shape: disjunctive / noun-like shell
- Local confidence: high

### C17. `step or baseten to integer`

- Exact phrase text: `step or baseten to integer`
- Exact coordinates:
  - one exact instance:
  - `step`: `N9 -> M9 -> M10 -> L11`
  - `or`: `K12 -> K13`
  - `baseten`: `L12 -> L13 -> K14 -> J14 -> I14 -> H13 -> H12`
  - `to`: `H11 -> I10`
  - `integer`: `J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
  - alternate exact `step` starts `N9 -> N10 -> M10 -> L11`
- Maximal or nested: maximal among promoted syntax phrases
- Overlaps:
  - overlaps C16 but inserts `to` before `integer`
  - overlaps C19 on the same `step / or` shell
- Syntax shape: disjunctive / target-like shell
- Local confidence: high

### C18. `step or base ten integer`

- Exact phrase text: `step or base ten integer`
- Exact coordinates:
  - one exact instance:
  - `step`: `N9 -> M9 -> M10 -> L11`
  - `or`: `K12 -> K13`
  - `base`: `L12 -> L13 -> K14 -> J14`
  - `ten`: `I14 -> H13 -> H12`
  - `integer`: `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
  - alternate exact `step` starts `N9 -> N10 -> M10 -> L11`
- Maximal or nested: maximal among full exact phrase inclusions; overlaps a longer competing shell in C19
- Overlaps:
  - contains `step or`
  - contains `or base ten integer`
- Syntax shape: disjunctive / noun-like shell
- Local confidence: high

### C19. `step or base ten to integer`

- Exact phrase text: `step or base ten to integer`
- Exact coordinates:
  - one exact instance:
  - `step`: `N9 -> M9 -> M10 -> L11`
  - `or`: `K12 -> K13`
  - `base`: `L12 -> L13 -> K14 -> J14`
  - `ten`: `I14 -> H13 -> H12`
  - `to`: `H11 -> I10`
  - `integer`: `J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
  - alternate exact `step` starts `N9 -> N10 -> M10 -> L11`
- Maximal or nested: maximal among promoted syntax phrases
- Overlaps:
  - overlaps C18 but inserts `to`
  - overlaps C21 on the same `base ten / to integer` material
- Syntax shape: disjunctive / target-like shell
- Local confidence: high

### C20. `baseten integer`

- Exact phrase text: `baseten integer`
- Exact coordinates:
  - `baseten`: `L12 -> L13 -> K14 -> J14 -> I14 -> H13 -> H12`
  - `integer`: `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- Maximal or nested: nested in C16 and in `step baseten integer`
- Overlaps:
  - same word-instance material reorders into C22 and extends into C23
- Syntax shape: noun-like
- Local confidence: high

### C21. `base ten integer`

- Exact phrase text: `base ten integer`
- Exact coordinates:
  - `base`: `L12 -> L13 -> K14 -> J14`
  - `ten`: `I14 -> H13 -> H12`
  - `integer`: `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- Maximal or nested: nested in C18 and `step base ten integer`
- Overlaps:
  - same word-instance material reorders into C24 and extends into C25
- Syntax shape: noun-like
- Local confidence: high

### C22. `integer baseten to`

- Exact phrase text: `integer baseten to`
- Exact coordinates:
  - one exact instance:
  - `integer`: `J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
  - `baseten`: `L12 -> L13 -> K14 -> J14 -> I14 -> H13 -> H12`
  - `to`: `H11 -> I10`
  - alternate exact `integer` starts `I12` or `J12`
- Maximal or nested: nested in exact `step or integer baseten to`
- Overlaps:
  - same word-instance material as C20 and C23, but reversed
- Syntax shape: unclear, but strongly order-ambiguous
- Local confidence: medium-high

### C23. `baseten to integer`

- Exact phrase text: `baseten to integer`
- Exact coordinates:
  - `baseten`: `L12 -> L13 -> K14 -> J14 -> I14 -> H13 -> H12`
  - `to`: `H11 -> I10`
  - `integer`: `J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- Maximal or nested: nested in C17 and in exact `step baseten to integer`
- Overlaps:
  - same word-instance material as C20 and C22, but different order
- Syntax shape: target-like
- Local confidence: high

### C24. `integer base ten to`

- Exact phrase text: `integer base ten to`
- Exact coordinates:
  - one exact instance:
  - `integer`: `J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
  - `base`: `L12 -> L13 -> K14 -> J14`
  - `ten`: `I14 -> H13 -> H12`
  - `to`: `H11 -> I10`
  - alternate exact `integer` starts `I12` or `J12`
- Maximal or nested: nested in exact `step or integer base ten to`
- Overlaps:
  - same word-instance material as C21 and C25, but reversed
- Syntax shape: unclear, but strongly order-ambiguous
- Local confidence: medium-high

### C25. `base ten to integer`

- Exact phrase text: `base ten to integer`
- Exact coordinates:
  - `base`: `L12 -> L13 -> K14 -> J14`
  - `ten`: `I14 -> H13 -> H12`
  - `to`: `H11 -> I10`
  - `integer`: `J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- Maximal or nested: nested in C19 and in exact `step base ten to integer`
- Overlaps:
  - same word-instance material as C21 and C24, but different order
- Syntax shape: target-like
- Local confidence: high

## Promoted Near-Miss Section

These are exact phrases from the local enumeration but not promoted into the core syntax inventory because they look like dictionary spillover rather than stable parse options.

- `go the hexadecimal ten ten ten integer`
- `the get step or baseten into`
- `step get nine step or by six`
- `the hexadecimal or ten step integer by six`

Reason for non-promotion:

- exact, but syntactically unstable and only weakly interpretable as compositional local parses.

## Inventory Takeaway

- The lower-right component contains more genuine exact local orderings than the bridge pass captured.
- The most important new fact is not just longer phrases.
- It is the existence of competing exact orderings over the same local word-instance network, especially around:
  - `get / nine / to / tens`
  - `baseten / to / integer`
  - `integer / baseten / to`
  - `base ten / to / integer`
  - `step or ...`
- That means connectedness inside this component is not enough to prove one privileged parse.
