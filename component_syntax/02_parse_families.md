# Parse Families

This file uses only exact phrase instances re-verified from `can u dig it.csv:1-14`.

A parse family here is not just a connected set of phrases.
It must specify actual attachment structure and state whether the result is:

- exact compositional syntax
- weak/shared-instance contact only
- unresolved

## PF1. Representation-Object Plus Tail Family

### Exact phrases used

- `the decimal ten ten ten integer by six`
- `the decimal ten ten ten to integer`
- `the hexadecimal ten ten ten integer by six`
- `hexadecimal ten ten ten to integer`
- `binary ten integer by six`
- `binary ten to integer by six`
- `integer by six`
- `to integer by six`

### Proposed attachment structure

- representation label modifies a numeral-like object:
  - `binary ten`
  - `decimal ten ten ten`
  - `hexadecimal ten ten ten`
- tail candidate A:
  - `[integer by six]`
- tail candidate B:
  - `[to integer]`
  - or `[to integer by six]`

### Why each attachment is licensed

- `integer by six` is an exact subphrase in:
  - `binary ten integer by six`
  - `decimal ten ten ten integer by six`
  - `hexadecimal ten ten ten integer by six`
- `to integer` is exact in:
  - `binary ten to integer by six`
  - `decimal ten ten ten to integer`
  - `hexadecimal ten ten ten to integer`
- these are local exact attachments, not inferred semantic rewrites

### Parse judgment

- exact compositional syntax for the local subphrases `[integer by six]` and `[to integer]`
- unresolved for the full-family semantics

### Why unresolved

- the same representation object supports both `... integer by six` and `... to integer` continuations
- the raw syntax does not yet privilege one continuation as the intended executable parse

## PF2. Branch-Side `get` Family

### Exact phrases used

- `get nine total`
- `binary get nine total`
- `get nine tens`
- `get nine to tens`
- `binary get nine tens`
- `binary get nine tens to`
- `binary get nine to`
- `binary get nine to tens`

### Proposed attachment structure

- candidate A:
  - imperative-like `[get] [nine total]`
  - imperative-like `[get] [nine tens]`
- candidate B:
  - target-like `[get] [nine] [to tens]`
  - target-like `[binary] [get] [nine] [to tens]`
- candidate C:
  - label-like `[binary get nine total]`

### Why each attachment is licensed

- all listed phrases are exact and locally chained
- `to` has two different exact scopes:
  - postposed after `tens` in `binary get nine tens to`
  - inserted before `tens` in `binary get nine to tens`

### Parse judgment

- unresolved

### Why unresolved

- the family contains competing exact word orders over the same local branch material
- that means the branch is not one stable imperative string but a small exact phrase family with unresolved scope

## PF3. Tail-Only Action Family

### Exact phrases used

- `step by six`
- `step integer by six`
- `step into integer by six`
- `to integer by six`
- `go integer by six`
- `integer by six`

### Proposed attachment structure

- `[integer by six]` is the strongest stable core
- it can be preceded by:
  - `step`
  - `step into`
  - `to`
  - `go`

### Why each attachment is licensed

- all of those exact phrases reuse the same lower-right `integer / by / six` tail material or exact local variants of it

### Parse judgment

- exact compositional syntax for `[integer by six]`
- unresolved for the larger action shells

### Why unresolved

- `step by six` and `step into integer by six` use different exact local step structures
- `go integer by six` and `to integer by six` exist, but they do not identify one privileged instruction flow

## PF4. `step or X` Disjunctive Shell Family

### Exact phrases used

- `step or`
- `step or integer by six`
- `step or baseten integer`
- `step or baseten to integer`
- `step or base ten integer`
- `step or base ten to integer`

### Proposed attachment structure

- shell:
  - `[step or X]`
- with exact complements X:
  - `integer by six`
  - `baseten integer`
  - `baseten to integer`
  - `base ten integer`
  - `base ten to integer`

### Why each attachment is licensed

- each complement exact-chains directly after the same `step or` shell
- the same `or = K12 -> K13` instance is used throughout
- the same lower-right step family appears in the output-side and tail-side instantiations

### Parse judgment

- exact compositional syntax locally

### Why only locally

- the shell itself is exact and repeated across multiple complements
- but it does not tell us whether the complements are alternatives, sequence stages, or merely co-located options

## PF5. Output/Target Family

### Exact phrases used

- `baseten integer`
- `integer baseten`
- `baseten to integer`
- `integer baseten to`
- `base ten integer`
- `integer base ten`
- `base ten to integer`
- `integer base ten to`
- `or baseten integer`
- `or baseten to integer`
- `or base ten integer`
- `or integer base ten to`

### Proposed attachment structure

- candidate A:
  - noun phrase output label
    - `baseten integer`
    - `base ten integer`
- candidate B:
  - target phrase
    - `baseten to integer`
    - `base ten to integer`
- candidate C:
  - reversed noun phrase / target phrase
    - `integer baseten`
    - `integer base ten`
    - `integer baseten to`
    - `integer base ten to`

### Why each attachment is licensed

- every listed phrase is exact on the same small word-instance network

### Parse judgment

- unresolved

### Why unresolved

- the family supports multiple exact local orderings
- that makes `baseten integer` / `base ten integer` much less secure as a unique output label

## PF6. Contact-Only Binary Bridge Family

### Exact phrases used

- `binary get nine total`
- `binary get nine tens`
- `binary ten integer by six`

### Proposed attachment structure

- one could be tempted to parse:
  - `[binary get nine total] -> [binary ten integer by six]`

### Why the contact is licensed

- same exact `binary` instance in each branch-side and object-side phrase

### Parse judgment

- weak/shared-instance contact only

### Why not compositional syntax

- no exact phrase contains both structures in one ordered clause
- no exact phrase identifies `binary` as one single head governing both families
- the shared-instance bridge proves local contact, not instruction flow

## Parse-Family Takeaway

- The strongest exact local syntax family is PF4: the `step or X` shell.
- The most important caution is PF6.
- Earlier bridge reasoning was strongest where it proved contact, weakest where it quietly promoted contact into composition.
