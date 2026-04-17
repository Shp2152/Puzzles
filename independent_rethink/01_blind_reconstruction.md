# Blind Reconstruction

## Method Boundary

- Blind-phase evidence source: `can u dig it.csv:1-14` only.
- No prior solver output was used as evidence in this phase.
- No existing parsing/helper code was reused in this phase.
- The audit helper `independent_rethink/raw_grid_probe.py:23-116` assumes only a rectangular CSV grid, 8-neighbor adjacency, and no cell reuse inside a word or chained phrase.

## Raw-Only Evidence Map

### 1. Cleanest exact instruction ribbon

The cleanest exact English instruction fragment is `find the start`.

- `find`: `E1 -> F1 -> G1 -> H1`
- `the`: `I1 -> J1 -> J2`
- `start`: `K1 -> K2 -> L1 -> M1 -> N1`
- Exact chained phrase: `find the start`
- Source: `can u dig it.csv:1-2`

That ribbon extends exactly to `find the start nine` and then `find the start nine go`.

- `nine`: `M2 -> M3 -> L4 -> K4`
- `go`: `J3 -> K3`
- Exact chained phrase: `find the start nine go`
- Source cells span `E1` through `K4`; letters come from `can u dig it.csv:1-5`

Blind-pass reading:

- `find the start` is locally strong.
- `find the start nine` is plausible but already starts to need interpretation.
- `find the start nine go` is exact, but syntactically rough and still leaves the object of `go` unresolved.

### 2. Strong lower-right procedure fragments exist, but they do not unify cleanly

There are exact lower-right procedure-like phrases.

- `step by six`
  - `step`: `N9 -> N10 -> M10 -> L11`
  - `by`: `L12 -> M13`
  - `six`: `L14 -> M14 -> N14`
  - Source: `can u dig it.csv:9-14`
- `step into integer by six`
  - `step`: `I13 -> I14 -> J14 -> J13`
  - `into`: `I12 -> H12 -> H11 -> I10`
  - `integer`: `J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
  - `by`: `L12 -> M13`
  - `six`: `L14 -> M14 -> N14`
  - Source: `can u dig it.csv:10-14`
- `step baseten integer`
  - `step`: `N9 -> N10 -> M10 -> L11`
  - `baseten`: `L12 -> L13 -> K14 -> J14 -> I14 -> H13 -> H12`
  - `integer`: `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
  - Source: `can u dig it.csv:9-14`

Blind-pass reading:

- These are real exact fragments.
- But they do not come from a single clean action chain.
- `step baseten integer` and `step by six` use one `step` instance in the `L11` corner.
- `step into integer by six` uses a different `step` instance in the `I13-J14` corner.
- A global procedure story therefore already needs at least two disconnected `step` instances to play one semantic role.

### 3. Representation / base family is the strongest local family

The strongest raw family is a representation-label family built on exact phrases that share specific downstream instances.

- `hexadecimal ten ten ten integer`
  - `hexadecimal`: `I3 -> I4 -> I5 -> I6 -> H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11`
  - `ten`: `C12 -> B13 -> C14`
  - `ten`: `C13 -> D14 -> E14`
  - `ten`: `F14 -> G13 -> H12`
  - `integer`: `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
  - Source: `can u dig it.csv:3-14`
- `decimal ten ten ten integer`
  - `decimal`: `H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11`
  - the same three `ten` instances above
  - the same `integer` instance above
  - Source: `can u dig it.csv:7-14`
- `binary ten`
  - `binary`: `F10 -> E10 -> E11 -> E12 -> E13 -> F13`
  - `ten`: `F14 -> G13 -> H12`
  - Source: `can u dig it.csv:10-14`
- `baseten integer`
  - `baseten`: `L12 -> L13 -> K14 -> J14 -> I14 -> H13 -> H12`
  - `integer`: `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
  - Source: `can u dig it.csv:12-14`

Blind-pass reading:

- This family is not just topical. It is instance-coherent.
- `hexadecimal` and `decimal` attach to the same exact `ten-ten-ten-integer` tail.
- `binary` and `baseten` live in the same lower-right neighborhood as that tail.
- This is stronger than a procedure-first story because it needs fewer cross-island jumps.

### 4. There is also a smaller exact numeric-expression cluster

There is an exact `three ten hundred` chain in the upper-left / left-central region.

- `three`: `C3 -> B2 -> C2 -> B3 -> A4`
- `ten`: `B5 -> C4 -> C5`
- `hundred`: `B6 -> C6 -> D5 -> D4 -> D3 -> D2 -> C1`
- Exact chained phrase: `three ten hundred`
- Source: `can u dig it.csv:1-6`

Nearby raw evidence in the same broad region includes:

- `nineteen`: `C5 -> D6 -> D5 -> C4 -> C3 -> B3 -> A2 -> A3`
- `integer`: `D6 -> C5 -> B5 -> A4 -> B4 -> B3 -> C2`
- `integers`: `D6 -> C5 -> B5 -> A4 -> B4 -> B3 -> C2 -> B1`

Blind-pass reading:

- The left side clearly contains number-language.
- But `three ten hundred` does not exact-chain into the lower-right representation family.
- It looks like a detached clue family, not a confirmed payload for the lower-right system.

### 5. `get nine total` is exact, but it is another detached island

- `get`: `F12 -> G13 -> F14`
- `nine`: `E14 -> D13 -> C14 -> D14`
- `total`: `C13 -> D12 -> C12 -> B11 -> B10`
- Exact chained phrase: `get nine total`
- Source: `can u dig it.csv:10-14`

Blind-pass reading:

- This is locally real.
- But it does not exact-chain into `baseten integer` or `step into integer by six`.
- Any theory that promotes it to the core procedure needs an attachment that is not exact yet.

### 6. Place-value evidence exists, but it is incomplete

Exact phrases found:

- `decimal tens`
  - `decimal`: `H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11`
  - `tens`: `C12 -> B13 -> A12 -> A11`
- `hexadecimal tens`
  - `hexadecimal`: `I3 -> I4 -> I5 -> I6 -> H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11`
  - `tens`: `C12 -> B13 -> A12 -> A11`
- `binary tens`
  - `binary`: `F10 -> E10 -> E11 -> E12 -> E13 -> F13`
  - `tens`: `F14 -> G13 -> H12 -> I13`

Nearby singleton evidence:

- `ones`: `K3 -> L4 -> M5 -> M6`
- `hundreds`: `B6 -> C6 -> D5 -> D4 -> D3 -> D2 -> C1 -> B1`

Blind-pass reading:

- This hints at a place-value family.
- But there is no exact `decimal ones`, `binary ones`, `hexadecimal ones`, `decimal hundreds`, or `ones tens hundreds` chain.
- So this family is suggestive but incomplete.

## Blind-Pass Conclusion

Strongest current framework from raw evidence alone:

- representation / base-first

Why:

- It has the highest density of exact phrases.
- It has the best instance-level reuse: the same exact `ten` and `integer` instances support multiple labels.
- It leaves fewer unresolved operation objects than the procedure story.

What is not justified yet:

- A single clean global sentence.
- A single unique final integer.
- Any story that merges top `nine`, bottom `nine`, and left-side `three ten hundred` into one procedure without new exact attachments.
