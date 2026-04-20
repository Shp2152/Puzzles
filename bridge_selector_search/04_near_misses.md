# Near Misses

These are the strongest almost-solves from the raw-only bridge/selector hunt.

## N1. Top ribbon `go` vs lower-right `go`

- attempted chain:
  - `find the start nine go`
  - `go integer by six`
- exact coordinates:
  - top `go`: `J3 -> K3`
  - lower-right `go`: `I9 -> I10`
- what it would have solved if valid:
  - direct attachment from the top ribbon into the lower-right tail branch
- why it fails exactly:
  - wrong word-instance merge
  - same word type, different instance
- likely diagnosis:
  - wrong word-instance merge

## N2. Branch-side `to` vs tail-side `to`

- attempted chain:
  - `binary get nine tens to`
  - `to integer by six`
- exact coordinates:
  - branch-side `to`: `C12 -> D12`
  - tail-side `to`: `H10 -> I10` or `H11 -> I10`
- what it would have solved if valid:
  - an explicit selector between the binary-tens branch and the tail branch
- why it fails exactly:
  - disconnected word instance
- likely diagnosis:
  - wrong word-instance merge

## N3. Upper-left `ten` vs lower-right `ten`

- attempted chain:
  - `three ten hundred`
  - `ten integer by six`
- exact coordinates:
  - upper-left `ten`: `B5 -> C4 -> C5`
  - lower-right `ten`: `F14 -> G13 -> H12` or `I14 -> H13 -> H12`
- what it would have solved if valid:
  - direct payload attachment from the upper-left family into the lower-right tail
- why it fails exactly:
  - disconnected word instance
- likely diagnosis:
  - wrong word-instance merge

## N4. `get ones` via a shared-looking `the`

- attempted chain:
  - `the get ones`
  - `the decimal ten ten ten`
- exact coordinates:
  - upper `the`: `I1 -> J1 -> I2`
  - lower-right `the`: `G6 -> H6 -> I7`
- what it would have solved if valid:
  - exact attachment from `get ones` into the representation family
- why it fails exactly:
  - disconnected word instance
- likely diagnosis:
  - wrong word-instance merge

## N5. Same-looking `step` route into the output label

- attempted chain:
  - `step integer by six`
  - `step baseten integer`
- exact coordinates:
  - tail-side `step`: `I13 -> I14 -> J14 -> J13`
  - output-side `step`: `N9 -> M9 -> M10 -> L11` or `N9 -> N10 -> M10 -> L11`
- what it would have solved if valid:
  - exact routing from the tail branch into the output label
- why it fails exactly:
  - disconnected word instance
- likely diagnosis:
  - wrong word-instance merge

## N6. The lower-right selector shell that still does not dispatch globally

- attempted chain:
  - `step or integer by six`
  - `step or baseten integer`
- exact coordinates:
  - shared lower-right `or`: `K12 -> K13`
  - one exact tail-side instance:
    - `N9 -> M9 -> M10 -> L11 / K12 -> K13 / J12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
  - one exact output-side instance:
    - `N9 -> M9 -> M10 -> L11 / K12 -> K13 / L12 -> L13 -> K14 -> J14 -> I14 -> H13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- what it would have solved if valid:
  - a local selector/routing instruction inside the lower-right backbone
- why it fails exactly:
  - the local phrases are exact
  - the failure is not path-level but interpretive: no exact phrase says this is the dispatch mechanism for the binary branch, or that the output-side phrase is the final report target
- likely diagnosis:
  - wrong interpretation of the output label

## N7. Exact output-shell without branch attachment

- attempted chain:
  - `binary get nine total`
  - `or baseten integer`
- exact coordinates:
  - branch end at `total = C13 -> D12 -> C12 -> B11 -> B10`
  - output-shell start at `or = K12 -> K13`
- what it would have solved if valid:
  - explicit route from branch result into the output label
- why it fails exactly:
  - invalid adjacency and path break
  - the two phrases live in the same broad lower-right zone but do not exact-chain
- likely diagnosis:
  - wrong interpretation of the output label

## Near-Miss Takeaway

- The strongest failures are not random.
- They cluster around three recurring problems:
  - wrong word-instance merge
  - missing phrase family between already-meaningful local shells
  - unresolved interpretation of `baseten integer` / `base ten integer` as output label
