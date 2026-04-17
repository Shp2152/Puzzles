# Hypothesis Test

Rubric used for each framework:

- local phrase strength
- spatial coherence
- ability to attach detached clues
- assumption count
- whether any operation has an unresolved object slot
- whether a unique final integer emerges cleanly

Heavy penalties applied for:

- deleting glue words to improve a phrase
- candidate-first backsolving
- unresolved operation objects
- treating disconnected same-word instances as one clue
- preferring a global story over stronger local exact phrases

## Framework A: procedure / step-first story

Core exact evidence available:

- `find the start` at `E1-H1 / I1-J2 / K1-N1`
- `find the start nine go` at `E1-K4 / J3-K3`
- `step by six` at `N9-L11 / L12-M13 / L14-N14`
- `step into integer by six` at `I13-J13 / I12-I10 / J11-M12 / L12-M13 / L14-N14`
- `get nine total` at `F12-F14 / E14-D14 / C13-B10`

Assessment:

- local phrase strength: mixed
  - `find the start` is strong.
  - `step by six` and `step into integer by six` are strong.
  - `find the start nine go` is exact but awkward.
  - `get nine total` is exact but detached.
- spatial coherence: weak-mixed
  - top ribbon, lower-right step cluster, and lower-left total cluster do not exact-attach.
- ability to attach detached clues: weak
  - it does not naturally absorb the representation family.
- assumption count: high
  - needs at least two disconnected `step` instances.
  - often needs at least two disconnected `nine` instances.
- unresolved object slot: yes
  - `go` in `find the start nine go` still lacks a destination or object.
  - `get nine total` leaves open what total means operationally.
- unique final integer emerges cleanly: no

Verdict:

- This framework has real local fragments.
- It fails as the primary global framework because it needs disconnected merges and unresolved operation objects too early.

## Framework B: representation / base-first story

Core exact evidence available:

- `hexadecimal ten ten ten integer`
- `decimal ten ten ten integer`
- `binary ten`
- `baseten integer`
- `decimal tens`
- `hexadecimal tens`
- `binary tens`

All are cited in `02_exact_phrase_inventory.md` as P6 and P10-P15 with exact coordinates.

Assessment:

- local phrase strength: very strong
  - the family contains multiple exact, high-specificity technical labels.
- spatial coherence: strong
  - `hexadecimal` and `decimal` feed the same `ten-ten-ten-integer` tail.
  - `binary` and `baseten` lie in the same lower-right representation neighborhood.
- ability to attach detached clues: moderate
  - it naturally absorbs most of the lower-right component.
  - it still does not absorb the top ribbon or `get nine total` exactly.
- assumption count: moderate
  - fewer disconnected merges than framework A.
  - still requires interpretation of what the repeated `ten` instances mean.
- unresolved object slot: mostly no
  - this family reads more like labels or representations than operations.
  - its weakness is not missing objects, but missing a decisive extraction rule.
- unique final integer emerges cleanly: no

Verdict:

- This is the strongest current framework.
- The evidence is concentrated, exact, and instance-reusing.
- It still does not uniquely determine a final integer by itself.

## Framework C: place-value / number-expression family

Core exact evidence available:

- `three ten hundred` at `C3-A4 / B5-C5 / B6-C1`
- `decimal tens`
- `hexadecimal tens`
- `binary tens`
- singleton `ones` at `K3-L4-M5-M6`
- singleton `hundreds` at `B6-C6-D5-D4-D3-D2-C1-B1`

Assessment:

- local phrase strength: moderate
  - `three ten hundred` is exact.
  - `decimal/hexadecimal/binary tens` are exact.
- spatial coherence: weak-mixed
  - `ones`, `tens`, and `hundreds` do not form one exact chain.
  - upper-left and lower-right place-value hints are detached.
- ability to attach detached clues: weak
  - this framework does not absorb `find the start` or `get nine total`.
- assumption count: high
  - requires converting scattered place-value nouns into one decomposition without an exact attachment.
- unresolved object slot: not mainly an operation issue
  - instead, the weakness is under-specification of what to do with the place values.
- unique final integer emerges cleanly: no

Verdict:

- This is a real secondary family, not nonsense.
- It is weaker than framework B because it is less instance-coherent and more spatially scattered.

## Head-to-Head Ranking

1. Framework B: representation / base-first
2. Framework C: place-value / number-expression
3. Framework A: procedure / step-first

## Why Framework B Wins

- It scores best on exact phrase specificity.
- It has the best instance-level reuse.
- It avoids the worst disconnected same-word merges.
- It does not depend on deleting `the`, `into`, or `by` to sound plausible.

## Why No Final Integer Is Justified Yet

- No framework produces a clean unique extraction rule from exact local evidence alone.
- The top instruction ribbon is still detached from the strongest lower-right representation component.
- `get nine total` and `three ten hundred` are both real, but exact attachment is missing.

## Most Decisive Missing Attachment

The single highest-value missing resolution is:

- an exact attachment from the detached instruction layer or detached payload layer into the lower-right representation component

Most specifically:

- either prove that `find the start ...` exact-chains into the `decimal/hexadecimal/binary/baseten` component,
- or prove that `get nine total` exact-chains into that same component,
- or prove that `three ten hundred` is the intended payload of the shared `ten-ten-ten-integer` tail without forcing disconnected `ten` instances.

Until one of those attachments is real, candidate integers are not uniquely supported.
