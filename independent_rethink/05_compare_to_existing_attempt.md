# Compare To Existing Attempt

## Overall Judgment

The current repo logic is mixed.

- Strong when it recognizes the lower-right representation cluster and records failed attachment tests.
- Weak when the clause-graph / content-core layer promotes stripped cores that are not exact phrases on the grid.

## Where The Existing Logic Is Strong

### 1. It correctly identified the representation family as real and spatially important

Strong repo observations:

- `HYPOTHESIS_LOG.md:27-35` already notes that `decimal ten ten ten integer`, `hexadecimal ten ten ten integer`, and `baseten integer` are stable cores.
- `HYPOTHESIS_LOG.md:40-46` correctly says the lower-right cluster is a real connected structure and that `decimal` is embedded in `hexadecimal`.
- `clause_graph_report.md:42-43` records `decimal ten ten ten integer` and `hexadecimal ten ten ten integer` as high-score representation clauses.

Raw-only confirmation:

- exact `hexadecimal ten ten ten integer` uses `I3 -> I4 -> I5 -> I6 -> H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11`, then `C12 -> B13 -> C14`, `C13 -> D14 -> E14`, `F14 -> G13 -> H12`, then `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- exact `decimal ten ten ten integer` reuses the same three `ten` instances and the same `integer` instance
- exact `baseten integer` uses `L12 -> L13 -> K14 -> J14 -> I14 -> H13 -> H12` and `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`

This is the strongest part of the current repo logic.

### 2. It correctly noticed that detached families do not attach cleanly

Strong repo observations:

- `HYPOTHESIS_LOG.md:129-142` explicitly records that direct attachment tests for `hexadecimal` and `decimal` all failed against the current skeleton roles.
- `HYPOTHESIS_LOG.md:146-157` also admits that neither the representation family nor `three ten hundred` cleanly fills the missing slot.

Raw-only confirmation:

- The top ribbon `find the start` / `find the start nine go` has no exact attachment into the lower-right representation component.
- `get nine total` at `F12 -> G13 -> F14 / E14 -> D13 -> C14 -> D14 / C13 -> D12 -> C12 -> B11 -> B10` also has no exact attachment into `baseten integer` or the `decimal/hexadecimal ... integer` tail.
- `three ten hundred` at `C3 -> A4 / B5 -> C5 / B6 -> C1` is likewise detached from the lower-right component.

This negative work is valuable and should be kept.

### 3. It became more cautious about `864`

Strong repo observations:

- `HYPOTHESIS_LOG.md:204-216` explicitly downgrades the naive `864 = 0x360` excitement and reframes `864` as a forced integration experiment.
- `candidate_number_comparison.md:23-29` and `33-37` describe `864` as constructed rather than cleanly attached.

That correction is methodologically healthy.

## Where The Existing Logic Jumps Or Creates False Coherence

### 1. The clause graph treats stripped content cores as if they were exact clauses

Examples from the repo:

- `clause_graph_report.md:27-29` elevates `step integer six` and `nine step six`.
- But its own representative phrases are `step into integer by six` and `nine step or six`; see `clause_graph_report.md:50` and `68`.
- `clause_graph_report.md:164-170` even names a clause `step six` while the representative phrase is `step or six`.

Raw-only contradiction:

- exact `step into integer by six` exists at `I13 -> I14 -> J14 -> J13 / I12 -> H12 -> H11 -> I10 / J11 -> M12 / L12 -> M13 / L14 -> N14`
- exact `step by six` exists at `N9 -> N10 -> M10 -> L11 / L12 -> M13 / L14 -> N14`
- exact `nine step six` has zero matches under the same movement rule

This is the single biggest logic hole.

### 2. The current skeleton merges disconnected `nine` instances into one semantic pivot

Examples from the repo:

- `HYPOTHESIS_LOG.md:97-101` says `nine` is the clearest lexical pivot in the graph.
- `hypothesis_scorecard.md:42-45` awards bridge points because start -> action and action -> total share `nine`.

Raw-only contradiction:

- top-ribbon `nine`: `M2 -> M3 -> L4 -> K4` in `find the start nine go`
- bottom `nine`: `E14 -> D13 -> C14 -> D14` in `get nine total`
- left/central `nine` also exists in the `nineteen` region near `C5 / D6 / D5 / C4`

Those are different instances. Treating them as one pivot is exactly the kind of disconnected same-word merge this audit was supposed to penalize.

### 3. The current skeleton merges disconnected `step` instances too

Examples from the repo:

- `hypothesis_scorecard.md:37-41` uses `nine step six` plus `step baseten integer` in the same winning skeleton.
- `HYPOTHESIS_LOG.md:117-126` similarly promotes a single skeleton built from `find start nine`, `nine step six`, `get nine total`, and `step baseten integer`.

Raw-only contradiction:

- `step baseten integer` uses `step = N9 -> N10 -> M10 -> L11`
- `step into integer by six` uses `step = I13 -> I14 -> J14 -> J13`

A unified `step` operation is not exact. It is stitched together from separate step instances.

### 4. The scoring rubric is biased toward operation experiments because the experiments themselves are operation-shaped

Evidence in the repo:

- `HYPOTHESIS_LOG.md:55` and `59-63` describe targeted operation-word experiments.
- `clause_graph_report.md:12-16` and `53-63` reward clauses that survive those targeted runs.
- `hypothesis_scorecard.md:23-28` then ranks whole frameworks using those clause strengths.

Why this matters:

- Procedure fragments like `find start nine` and `nine step six` get repeated support because the experiment set asked for action words.
- Representation phrases like `decimal ten ten ten integer` and `hexadecimal ten ten ten integer` are exact and high-specificity, but they score as `req=0, op_sup=0` in `clause_graph_report.md:42-43` because the operation experiment layer was not designed around them.

The result is not neutral comparison. It is a rubric that partially bakes in a procedure-first preference.

### 5. The missing-slot framing narrows the search too early

Evidence in the repo:

- `missing_slot_discriminator.md:3-12` assumes the winning skeleton is already fixed.
- The only question left is what fills the missing slot inside that skeleton.

Why this matters:

- That framing demotes the representation family and `three ten hundred` from possible primary frameworks to mere plug-ins.
- The blind pass reached the opposite conclusion: the representation family is the primary exact-evidence component, while the procedure skeleton is the more assumption-heavy component.

## Clause Graph / Content-Core Approach: Helping, Hurting, Or Mixed?

Judgment: mixed, but hurting once used compositionally.

Helping:

- `README.md:17-20` says content-core summaries helped expose number/base fragments instead of fluent junk.
- `HYPOTHESIS_LOG.md:23-35` shows that this did help surface the representation family and demote sentence-looking noise.

Hurting:

- `README.md:18-20` and `57-58` explicitly describe collapsing bridge scaffolds out of phrase text.
- In practice this produced promoted cores like `find start nine`, `step integer six`, and `nine step six` even where the exact grid evidence is `find the start nine`, `step into integer by six`, `step by six`, or `nine step or six`; see `clause_graph_report.md:27-34`, `47-72`, and `164-170`.
- Once those stripped cores are treated as graph nodes, the graph manufactures cleaner bridges than the exact phrases support.

Bottom line:

- content-core reduction is useful as a discovery aid
- content-core reduction is unsafe as a proof object

## Net Comparison To The Blind Pass

Agreement:

- lower-right representation cluster is real
- detached attachment failures are real
- `864` is forced, not clean

Disagreement:

- the repo promotes a procedure-first skeleton to center stage
- the blind pass ranks representation/base-first above procedure-first
- the repo treats shared word types like `nine` and `step` as pivots too aggressively
- the blind pass requires specific instance reuse, not shared labels

## Practical Takeaway

The strongest parts of the current repo should be kept:

- exact local representation evidence
- explicit failed-attachment records
- caution about forced candidates

The main thing to stop doing is this:

- do not let stripped content cores like `nine step six` outrank the exact glue-bearing phrases the grid actually supports
