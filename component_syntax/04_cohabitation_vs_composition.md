# Cohabitation Vs Composition

This is the key audit for the lower-right component.

For each hop below, the question is not just whether the phrases touch.
The question is whether the touch licenses one instruction-level continuation.

## H1. `binary get nine total` -> `binary ten integer by six`

- Contact type:
  - identical shared `binary` instance
  - e.g. `F10 -> E10 -> E11 -> E12 -> E13 -> F13`
- What is proved:
  - exact local contact only
- What is not proved:
  - one instruction flowing from branch phrase to object phrase
- Classification:
  - exact local contact only

## H2. `binary get nine tens` -> `binary ten integer by six`

- Contact type:
  - identical shared `binary` instance
- What is proved:
  - exact local contact only
- What is not proved:
  - one instruction flowing from branch phrase to object phrase
- Classification:
  - exact local contact only

## H3. `binary ten integer by six` -> `integer by six`

- Contact type:
  - full exact phrase inclusion
- What is proved:
  - exact compositional continuation locally
  - `integer by six` is a real subphrase of `binary ten integer by six`
- Classification:
  - exact compositional continuation

## H4. `integer by six` -> `baseten integer`

- Contact type:
  - identical shared `integer` instance
  - strongest shared instance: `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- What is proved:
  - local contact inside the same component
- What is not proved:
  - that the result of `integer by six` should flow into `baseten integer`
- Why not:
  - the same local network also supports exact alternatives:
  - `integer baseten`
  - `baseten to integer`
  - `integer baseten to`
- Classification:
  - parse-ambiguous

## H5. `integer by six` -> `base ten integer`

- Contact type:
  - identical shared `integer` instance
- What is proved:
  - local contact inside the same component
- What is not proved:
  - unique routing into an output label
- Why not:
  - the same local network also supports:
  - `integer base ten`
  - `base ten to integer`
  - `integer base ten to`
- Classification:
  - parse-ambiguous

## H6. `step or integer by six` -> `step or baseten integer`

- Contact type:
  - identical shared `step or` shell
- What is proved:
  - exact local coordination shell exists
- What is not proved:
  - that the two complements are execution alternatives selected by the puzzle
- Why not:
  - the complements themselves are heterogeneous and locally ambiguous
  - the same shell also supports `step or baseten to integer` and `step or base ten to integer`
- Classification:
  - parse-ambiguous

## H7. `step or baseten integer` -> `step or base ten integer`

- Contact type:
  - genuine spatial overlap
  - `base ten` splits the `baseten` path
- What is proved:
  - exact resegmentation of the same local material
- What is not proved:
  - any new instruction flow
- Classification:
  - exact local contact only

## H8. `step by six` -> `step integer by six`

- Contact type:
  - partial shared `step` role and exact `by six` tail
- What is proved:
  - both are exact local phrases in the same region
- What is not proved:
  - that they are one larger parse
- Why not:
  - the `step` instances differ from the `step` in `step integer by six`
  - one phrase is just `step by six`, the other inserts `integer`
- Classification:
  - not justified as continuation

## H9. `step into integer by six` -> `step integer by six`

- Contact type:
  - exact local overlap on `step` and the tail material
- What is proved:
  - both support the local tail `integer by six`
- What is not proved:
  - that one is the reduced or intended reading of the other
- Classification:
  - parse-ambiguous

## H10. `binary get nine tens` -> `binary get nine tens to`

- Contact type:
  - full exact phrase inclusion
- What is proved:
  - exact compositional continuation locally
- What is not proved:
  - that the trailing `to` dispatches to the tail branch
- Classification:
  - exact compositional continuation locally

## H11. `binary get nine tens` -> `binary get nine to tens`

- Contact type:
  - shared first three words only
- What is proved:
  - local family resemblance
- What is not proved:
  - a single stable parse for the branch phrase
- Classification:
  - exact local contact only

## H12. `baseten integer` -> `baseten to integer`

- Contact type:
  - same local words plus inserted exact `to`
- What is proved:
  - one exact local family supports both a noun-like read and a target-like read
- What is not proved:
  - that either one is the privileged puzzle-level interpretation
- Classification:
  - parse-ambiguous

## Main Correction To Earlier Bridge Reasoning

The most important downgrade is this:

- `binary get nine total` / `binary get nine tens`
  - touching `binary ten integer by six`
  - touching `integer by six`
  - touching `baseten integer`

does **not** by itself yield one executable instruction chain.

Why:

- some hops are only shared-instance contact
- some hops are exact subphrase inclusion
- some hops are exact local shells with unresolved complement scope
- and the output-side family is itself internally order-ambiguous

## Takeaway

- The lower-right component is definitely connected.
- Only some hops are true compositional continuations.
- Several earlier “bridge” moves were really cohabitation, not composition.
