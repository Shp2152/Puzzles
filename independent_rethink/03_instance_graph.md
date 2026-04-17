# Instance Graph

Nodes below are the specific phrase instances from `02_exact_phrase_inventory.md`.

## Node Set

- P1 `find the start`
- P2 `find the start nine`
- P3 `find the start nine go`
- P4 `step by six`
- P5 `step baseten integer`
- P6 `step into integer by six`
- P7 `into integer by six`
- P8 `get nine total`
- P10 `hexadecimal ten ten ten integer`
- P11 `decimal ten ten ten integer`
- P12 `binary ten`
- P13 `decimal tens`
- P14 `hexadecimal tens`
- P15 `binary tens`
- P16 `three ten hundred`

## Allowed Edge Types Used Here

- direct reuse of the same word instance
- genuine spatial overlap
- strong local attachment justified by endpoint adjacency in the exact chained phrase

## Edges

### Top instruction ribbon

- P1 <-> P2
  - Edge type: direct reuse of the same `find`, `the`, and `start` instances
  - Shared coords: `E1 -> H1`, `I1 -> J2`, `K1 -> N1`
- P2 <-> P3
  - Edge type: direct reuse of the same `find`, `the`, `start`, and `nine` instances
  - Shared `nine`: `M2 -> M3 -> L4 -> K4`

### Lower-right procedure / representation cluster

- P4 <-> P5
  - Edge type: direct reuse of the same `step` instance
  - Shared `step`: `N9 -> N10 -> M10 -> L11`
- P6 <-> P7
  - Edge type: direct reuse of the same `into`, `integer`, `by`, and `six` instances
  - Shared coords: `I12 -> H12 -> H11 -> I10`, `J11 -> M12`, `L12 -> M13`, `L14 -> N14`
- P5 <-> P10
  - Edge type: direct reuse of the same `integer` instance
  - Shared `integer`: `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- P5 <-> P11
  - Edge type: direct reuse of the same `integer` instance
  - Shared `integer`: `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- P5 <-> P6
  - Edge type: genuine spatial overlap
  - Overlap cells: `I14`, `H13`, `H12`, `I12`, `I11`, `J10`, `K10`, `L10`, `M11`, `M12`, `L12`, `M13`, `L14`
  - Important nuance: despite heavy overlap, the `step` instance is different.
- P10 <-> P11
  - Edge type: direct reuse of the same three `ten` instances and the same `integer` instance
  - Shared tens: `C12 -> B13 -> C14`, `C13 -> D14 -> E14`, `F14 -> G13 -> H12`
  - Shared `integer`: `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- P10 <-> P12
  - Edge type: genuine spatial overlap plus direct reuse of the last `ten` instance
  - Shared `ten`: `F14 -> G13 -> H12`
  - Additional overlap cell: `E10`
- P11 <-> P12
  - Edge type: genuine spatial overlap plus direct reuse of the last `ten` instance
  - Shared `ten`: `F14 -> G13 -> H12`
  - Additional overlap cells: `F9` is not shared; `E10` is shared only between `decimal` and `binary`
- P11 <-> P13
  - Edge type: direct reuse of the same `decimal` instance
  - Shared `decimal`: `H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11`
- P10 <-> P14
  - Edge type: direct reuse of the same `hexadecimal` instance
  - Shared `hexadecimal`: `I3 -> I4 -> I5 -> I6 -> H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11`
- P12 <-> P15
  - Edge type: direct reuse of the same `binary` instance
  - Shared `binary`: `F10 -> E10 -> E11 -> E12 -> E13 -> F13`

### Detached clusters

- P8 has no exact attachment edge to P4, P5, P6, P10, or P11.
  - Audit significance: `get nine total` is locally real but graph-detached.
- P16 has no exact attachment edge to P10 or P11.
  - Audit significance: `three ten hundred` is locally real but graph-detached from the lower-right representation tail.
- P3 has no exact attachment edge to P4, P8, P10, or P16.
  - Audit significance: the top instruction ribbon is also detached.

## Forced Same-Word Merges To Flag

These are exactly the places where a theory would need multiple disconnected instances of the same word to play one semantic role.

- `nine`
  - Top ribbon `nine`: `M2 -> M3 -> L4 -> K4` in P2/P3
  - Bottom `nine`: `E14 -> D13 -> C14 -> D14` in P8
  - Left/central `nine` also exists inside `nineteen`-rich territory near `C5/D6/D5/C4`
  - Any single-procedure story that treats these as one semantic `nine` is forcing a disconnected merge.
- `step`
  - P4/P5 use `N9 -> N10 -> M10 -> L11`
  - P6 uses `I13 -> I14 -> J14 -> J13`
  - Any story with one unified `step` operation is forcing a disconnected merge.
- `ten`
  - P10/P11 use the lower `ten-ten-ten` tail
  - P16 uses a different upper-left `ten` at `B5 -> C4 -> C5`
  - Any theory that turns `three ten hundred` into the payload of the lower `decimal/hexadecimal ... integer` chain is forcing a disconnected merge.
- place-value nouns
  - `ones`: `K3 -> L4 -> M5 -> M6`
  - `tens`: lower region near `C12/B13/A12/A11` and `F14/G13/H12/I13`
  - `hundreds`: upper-left `B6 -> C6 -> D5 -> D4 -> D3 -> D2 -> C1 -> B1`
  - A unified `ones/tens/hundreds` decomposition is not exact yet; it is a disconnected merge.

## Graph Reading

The graph has one dominant coherent component:

- P4, P5, P6, P7, P10, P11, P12, P13, P14, P15

That component is anchored by shared exact instances of `integer`, `ten`, `decimal`, `hexadecimal`, `binary`, `baseten`, `by`, and `six`.

The graph also has three detached satellites:

- top instruction ribbon: P1, P2, P3
- lower-left total fragment: P8
- upper-left number-expression fragment: P16

That structure is the main blind-pass reason to prefer a representation-first story over a single global procedure.
