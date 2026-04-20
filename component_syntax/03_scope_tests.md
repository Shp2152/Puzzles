# Scope Tests

All scope tests below use only exact phrases re-verified from `can u dig it.csv:1-14`.

## A. `by six`

### Test A1. `integer by six`

- Exact support:
  - `integer by six`
  - strongest instance:
    - `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
- Reading supported:
  - `by six` attaches cleanly to `integer` locally
- Unresolved ambiguity:
  - whether that local attachment is the intended semantic core for the whole component
- Needed to promote to solved parse:
  - an exact phrase telling us what kind of relation `by six` expresses

### Test A2. `step by six`

- Exact support:
  - `step by six`
  - one exact instance:
    - `N9 -> M9 -> M10 -> L11 / L12 -> M13 / L14 -> M14 -> N14`
- Reading supported:
  - `by six` also attaches cleanly to `step` locally
- Unresolved ambiguity:
  - the exact `step` here is not the same step instance as in `step integer by six`
- Needed to promote to solved parse:
  - an exact phrase showing whether the puzzle wants the step-reading or the integer-reading

### Test A3. `step into integer by six`

- Exact support:
  - `step into integer by six`
  - `I13 -> I14 -> J14 -> J13 / I12 -> H12 -> H11 -> I10 / J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
- Reading supported:
  - exact local parse `[step] [into integer by six]`
  - exact local parse `[integer by six]`
- Unresolved ambiguity:
  - whether `by six` is scoped inside the `into` phrase, or whether the whole tail is just one frozen local chunk
- Needed to promote to solved parse:
  - another exact phrase reusing the same `into` instance with more explicit complements

### Test A4. Representation objects with `by six`

- Exact support:
  - `binary ten integer by six`
  - `decimal ten ten ten integer by six`
  - `hexadecimal ten ten ten integer by six`
  - plus exact `... to integer` variants for the same representation objects
- Reading supported:
  - `by six` can appear as the immediate tail after `integer`
- Unresolved ambiguity:
  - because the same objects also support `to integer`, the raw syntax does not force `by six` to be the unique intended continuation
- Needed to promote to solved parse:
  - an exact phrase choosing between the `to integer` and `integer by six` tails

### A verdict

- Exact support exists both for `integer by six` and for `step by six`.
- The local syntax does not settle which scope is globally intended.

## B. `or`

### Test B1. Output alternatives?

- Exact support:
  - `or baseten integer`
  - `or base ten integer`
  - `step or baseten integer`
  - `step or base ten integer`
- What this supports:
  - exact local output-like alternatives after `or`
- Unresolved ambiguity:
  - these same word-instance networks also support `... to integer` and reversed orders like `integer baseten`
  - so they are not cleanly unique output labels
- Needed to promote:
  - an exact phrase showing that the complement after `or` is the final reporting form

### Test B2. Action alternatives?

- Exact support:
  - `step or integer by six`
- What this supports:
  - exact local alternative after `step or`
- Unresolved ambiguity:
  - the complement is not clearly an action; it could be a tail phrase or object phrase
- Needed to promote:
  - an exact phrase showing a second explicit action complement

### Test B3. Phrase-fragment adjacency only?

- Exact support:
  - `step or`
  - `or integer by six`
  - `or baseten integer`
  - `or base ten integer`
- What this supports:
  - `or` definitely functions as a real local shell, not just accidental adjacency
- Unresolved ambiguity:
  - what the shell semantically coordinates

### B verdict

- `or` is real exact local syntax.
- It most likely joins complements of the `step or` shell.
- It does not yet tell us whether those complements are outputs, actions, or alternatives of another kind.

## C. Representation-Label Scope

### Test C1. Object labels

- Exact support:
  - `binary ten integer by six`
  - `decimal ten ten ten integer by six`
  - `hexadecimal ten ten ten integer by six`
- What this supports:
  - `binary`, `decimal`, and `hexadecimal` attach cleanly as labels on local object phrases

### Test C2. Mode labels

- Exact support:
  - `binary get nine total`
  - `binary get nine tens`
  - `binary get nine to tens`
- What this supports:
  - `binary` also heads a separate branch-side family
- Unresolved ambiguity:
  - this may be mode-label syntax, or it may be a label-like prefix on a noun phrase family

### Test C3. Operation modifiers

- Exact support:
  - weak
- Reason:
  - there is no exact phrase showing `binary`, `decimal`, or `hexadecimal` directly modifying `step`, `get`, or `or`

### Test C4. Output-format labels

- Exact support:
  - weak
- Reason:
  - no exact phrase routes the branch side into `baseten integer` or `base ten integer`
  - no exact `binary ... baseten integer` style phrase exists

### C verdict

- Best-supported role for `binary`, `decimal`, and `hexadecimal` is object-label scope.
- `binary` is special because it also heads the branch-side `get ...` family.
- None of the representation labels is cleanly licensed as output-format label.

## D. `base ten integer` / `baseten integer`

### Test D1. Noun phrase

- Exact support:
  - `baseten integer`
  - `base ten integer`
- What this supports:
  - noun-like local reads are possible

### Test D2. Imperative target

- Exact support:
  - `baseten to integer`
  - `base ten to integer`
  - `step baseten to integer`
  - `step or baseten to integer`
  - `step or base ten to integer`
- What this supports:
  - target-like or conversion-target local reads are also possible

### Test D3. Final reporting label

- Exact support:
  - only indirect
  - `or baseten integer`
  - `step or baseten integer`
  - `or base ten integer`
  - `step or base ten integer`
- What this supports:
  - local output-like complements inside the `or` shell
- Unresolved ambiguity:
  - reversed exact orders (`integer baseten`, `integer base ten`) and exact `to`-variants weaken any claim that this is a uniquely privileged final label

### D verdict

- `base ten integer` / `baseten integer` is better supported as a flexible local noun/target phrase family than as a fixed final reporting label.

## Scope-Test Takeaway

- The syntax pass strengthens local attachment discipline.
- It weakens several earlier semantic promotions.
- In particular:
  - `by six` is not globally settled
  - `or` is locally real but semantically underdetermined
  - `baseten integer` is not securely a final-output label
