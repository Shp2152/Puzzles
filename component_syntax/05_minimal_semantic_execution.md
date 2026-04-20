# Minimal Semantic Execution

Only parse families that survive the syntax audit well enough to execute are considered here.

## Executable Family E1. `get nine tens`

- Exact parse family used:
  - local branch-side `get` family, centered on exact `get nine tens`
  - strongest exact instance:
    - `F12 -> G13 -> F14 / E14 -> D13 -> C14 -> D14 / C13 -> B13 -> A12 -> A11`
- Semantic assumptions:
  - `get` is imperative
  - `nine tens` is literal place-value language
- Computed result:
  - `90`
- What remains unsupported:
  - exact branch-side ambiguity persists because exact `get nine to tens` also exists
  - no exact selector from this branch into the tail family
  - no exact proof that `baseten integer` is the final reporting label
- Robustness rating:
  - low-moderate

## Executable Family E2. `binary ten`

- Exact parse family used:
  - exact `binary ten`
  - representative exact instance:
    - `F10 -> E10 -> E11 -> E12 -> E13 -> F13 / F14 -> G13 -> H12`
- Semantic assumptions:
  - `binary` labels the numeral token `ten`
  - `ten` is read as binary `10`
- Computed result:
  - `2`
- What remains unsupported:
  - no exact output rule
  - no exact reason to prefer the direct local conversion over the other exact local families
- Robustness rating:
  - low

## Non-Executable Or Too-Ambiguous Families

### N1. Representation objects with `integer by six`

- examples:
  - `binary ten integer by six`
  - `decimal ten ten ten integer by six`
  - `hexadecimal ten ten ten integer by six`
- why not executed:
  - syntax does not settle what `integer by six` means semantically
  - `to integer` exact alternatives weaken any forced execution rule

### N2. `step or X` family

- examples:
  - `step or integer by six`
  - `step or baseten integer`
  - `step or base ten to integer`
- why not executed:
  - exact local shell exists
  - but the shell does not identify whether the complements are alternatives to choose, outputs to report, or mere co-located local phrases

### N3. Output/target family

- examples:
  - `baseten integer`
  - `integer baseten`
  - `baseten to integer`
  - `base ten to integer`
- why not executed:
  - exact family is too internally order-ambiguous to support one stable semantic role

## Minimal-Execution Takeaway

- The syntax pass leaves only two direct local computations alive:
  - `90`
  - `2`
- Neither is globally justified.
- `90` survives as the strongest executable local branch read, but with weaker confidence than before because the branch-side syntax is now visibly more ambiguous.
