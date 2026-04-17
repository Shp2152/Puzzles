# Puzzles

Workspace for solving the Jane Street-style puzzle "Can U dig it?"

## Current State

- Primary solver: `canudigitv1/canudig_search.py`
- Retired experiment: `canudigitv2/`
- Current leading hypothesis: the grid is pointing at number language or number representation, not chemistry
- Expected final answer: a positive integer
- Current live final-answer candidates: `360`, `297`, `864`

The most credible fragments found so far are things like `baseten`, `decimal`, `integer`, `hexadecimal`, `binary`, `three`, `ten`, `hundred`, `nineteen`, `six`, and the instruction fragment `find the start`.

Latest rerun highlights:

- Fake hex-token seed noise has been removed from the top phrase results.
- `solver v1` now prints content-core summaries that collapse bridge words out of phrase text.
- The strongest current cores are `decimal ten ten ten integer`, `hexadecimal ten ten ten integer`, `step baseten integer`, `baseten integer`, and `three ten hundred`.
- The current best story is no longer "read a sentence"; it is "combine a weak instruction layer with a stronger number-representation layer."

## Puzzle Setup

- Grid file: `can u dig it.csv`
- Movement rule: standard Boggle-style 8-neighbor adjacency
- Constraint: a cell cannot be reused inside a single word path, and chained phrase paths also avoid reusing cells
- Answer form: positive integer

## Repo Layout

- `can u dig it.csv`
  The puzzle grid.
- `HYPOTHESIS_LOG.md`
  Append-only running log of decisions, breakthroughs, and current theories.
- `README.md`
  Repo-level orientation and current attempt summary.
- `canudigitv1/`
  Main active solving area.
- `canudigitv2/`
  Retired exact-search branch kept only for reference.
- `all_found_words.csv`
  Large unrestricted dictionary sweep output copied from the older broad search.
- `all_found_word_instances.csv`
  Per-instance version of the unrestricted sweep.

## Solver V1

Main file: `canudigitv1/canudig_search.py`

What it does:

1. Loads a hand-curated candidate vocabulary from the embedded word list in the script.
2. Auto-adds bridge words like `the`, `to`, `of`, `and`, and `is`.
3. Finds all exact word paths from that vocabulary on the grid.
4. Chains compatible word paths into multiword phrases when the next word starts adjacent to the previous word's end and does not reuse cells.
5. Scores and filters those phrases using rough role tags like `VERB`, `NOUN`, `NUMBER`, `ADJ`, `HEXNUMBER`, and `FUNCTION`.
6. Writes text output summarizing found candidate words, search stats, and top phrase candidates.
7. Also prints content-core summaries so repeated scaffolds like `to`, `as`, `at`, `it`, and `or` can be separated from the content-word backbone of a clue.

Important caveat:

- V1 is useful because it stays close to a curated hypothesis-driven word list.
- V1 has also been biased toward verb-led / instruction-like phrase patterns, which can over-reward English-looking junk and under-reward clue-like noun/number fragments.

## Other Search Paths

### `canudigitv1/all_words.py`

This is a broad CMU-dictionary sweep.

What it is good for:

- spotting possible themes
- seeing what long accidental words the grid permits
- checking special buckets like chemistry terms

What it is bad for:

- deciding whether a theme is real
- ranking clue phrases
- separating genuine signal from combinatorial noise

### `canudigitv2/`

This was a later exact-search experiment. It is now retired. Its outputs can still be useful as secondary corroboration of stable local fragments, but current work should be treated as v1-first.

## Current Evidence Summary

Strong evidence:

- Number / representation language is the dominant theme.
- `baseten`, `decimal`, `decimals`, `integer`, `integers`, `binary`, and `hexadecimal` are more compelling than the chemistry hits.
- `find` + `start` appears to be a real instruction fragment rather than random noise.

Moderate evidence:

- There may be multiple clue regions in the grid.
- One region looks instruction-like: `find`, `the`, `start`, `nine`, `go`.
- Another looks number-expression-like: `baseten`, `decimal`, repeated `ten`, `integer`, `six`.
- A third weaker region includes `three`, `ten`, `hundred`, `nineteen`, and `integers`.

Weak evidence:

- Chemistry remains possible only in the weakest sense that the unrestricted dictionary sweep found some chemistry-adjacent words.
- Full sentence-looking outputs should not be trusted just because they score well.

## Current Hypothesis

Working hypothesis:

- The puzzle likely wants an integer derived from number-language or base / representation clues.
- The most promising clue-bearing fragments are noun/number expressions, not fluent sentences.
- `find` / `start` may provide extraction instructions once the right numeric interpretation is understood.

## Current Solve Model

- The stable clues appear to break into three families.
- Instruction layer: `find`, `start`, `step`, `get`, `add`, maybe `total`.
- Interpretation layer: `binary`, `decimal`, `hexadecimal`, `baseten`, `integer`.
- Payload layer: `three`, `nine`, `ten`, `hundred`, `six`, and related number-word fragments.
- The lower-right region is currently the strongest connected structure. It contains the dense base/representation cluster plus `step`, `six`, and `total`.
- The upper-right region still supports `find the start` and `find the start nine`.
- The upper-left region still supports `three ten hundred` and related number-word fragments.
- Current best-fit endgame: identify a start value or seed, apply a stepping / extraction rule, obtain a numeric result, then report it as a base-10 integer.

## Current Concerns

- The solver now gives stable semantic clusters, but it still does not produce one clean phrase that states the operation explicitly.
- `decimal` and `hexadecimal` are structurally overlapping, so they should not be over-counted as separate evidence.
- The upper-left number island and the lower-right base-conversion cluster still do not have a fully proved bridge between them.
- Sentence-looking outputs remain less trustworthy than repeated content cores.

## Latest Clean Runs

Main refreshed outputs:

- `canudigitv1/top_phrase_candidates.txt`
  Default v1 run with full phrase candidates plus `TOP CONTENT CORES`, `INSTRUCTION CORES`, `NUMERIC CORES`, and `HEX / BASE CORES` sections.
- `canudigitv1/top_phrase_candidates_baseten.txt`
  Focused run with `--must-have baseten`.
- `canudigitv1/top_phrase_candidates_hexadecimal.txt`
  Focused run with `--must-have hexadecimal`.

Planned targeted outputs:

- operation-focused runs anchored on words like `start`, `step`, `total`, `point`, `open`, `into`, `add`, and `get`
- cross-check runs testing the explicit algorithmic reading `start -> nine -> step -> six -> total -> baseten integer`

## Targeted Operation Experiments

Runner:

```bash
python run_targeted_operation_experiments.py
```

Outputs:

- `canudigitv1/operation_experiments/`
- `canudigitv1/operation_experiments/summary.md`

Clause graph / overlap report:

```bash
python build_clause_graph_report.py
```

Generated files:

- `canudigitv1/operation_experiments/clause_graph_report.md`
- `canudigitv1/operation_experiments/clause_graph.dot`

Procedure hypothesis scorecard:

```bash
python build_hypothesis_scorecard.py
```

Generated file:

- `canudigitv1/operation_experiments/hypothesis_scorecard.md`

Attachment experiments:

```bash
python run_attachment_experiments.py
```

Generated files:

- `canudigitv1/attachment_experiments/summary.md`
- `canudigitv1/attachment_experiments/*.txt`

Missing-slot discriminator:

```bash
python build_missing_slot_discriminator.py
```

Generated file:

- `canudigitv1/operation_experiments/missing_slot_discriminator.md`

Current takeaways from that batch:

- Real instruction-like micro-clauses do exist.
- Strongest confirmed ones are `find start nine`, `step integer six`, `nine step six`, `get nine total`, and `step baseten integer`.
- The direct output-label clue is still `baseten integer`.
- The upper-left payload clue is still `three ten hundred`.
- `point integer` and `open integer` do not currently produce phrase results.
- The likely solve story does not exist as one phrase under the current model.
- Full-chain tests like `start + nine + step + six + total` and `start + nine + step + six + total + baseten + integer` failed.
- Cross-island tests like `three + ten + hundred + baseten + integer` also failed.
- Most likely interpretation right now: the puzzle is giving multiple short clauses that need to be composed manually or with a less sentence-centric solver.

## Clause Graph Takeaways

- The clause graph currently treats reliable micro-clues as nodes and connects them by shared words plus spatial overlap / adjacency.
- The strongest current pivots are `nine`, `step`, and `integer`.
- `nine` is the strongest cross-family bridge between the upper-right start family and the lower-right step / total family.
- The lower-right cluster is increasingly consistent with a local story like: step something, get a total, express the result as a base-10 integer.
- `three ten hundred` remains the leading payload candidate, but it is still not proved to plug directly into the lower-right output clauses.
- The graph currently supports a multi-clause solve better than a single hidden sentence.

## Scorecard Takeaways

- The hypothesis scorecard is the current discriminative check against rabbit holes.
- It compares concrete procedure families under one fixed rubric instead of just mapping fragments.
- Under the current minimal-assumption rubric, the best-supported story is:
- `find start nine`
- `nine step six`
- `get nine total`
- `step baseten integer`
- That does not solve the puzzle yet, but it currently outperforms both payload-first and representation-first stories.
- `three ten hundred` remains alive only as a possible fill for the one unresolved payload/process slot, not as a forced part of the procedure.

## Attachment Takeaways

- `hexadecimal` / `decimal` currently fail to attach directly to any tested role in the winning skeleton.
- `three ten hundred` also fails to attach directly to any tested role in the winning skeleton.
- That means the current best procedure layer is stronger than both the representation layer and the payload layer.
- Important nuance: `hexadecimal` still looks intentional because it has its own local family of strong phrases, even though it does not yet integrate with the leading start/step/total/output skeleton.
- Current practical read:
- procedure layer: `find start nine`, `nine step six`, `get nine total`, `step baseten integer`
- detached but likely intentional representation layer: `hexadecimal` / `decimal`
- detached but unresolved payload candidate: `three ten hundred`

## Missing-Slot Takeaways

- The unresolved slot in the current winning skeleton is: what exact object or value is being stepped / totaled?
- The current discriminator ranks the candidate fillers as:
- `Integer Object` first
- `Three-Ten-Hundred Payload` second but far behind
- `Representation-Coded Object` third
- Practical interpretation:
- the leading low-assumption read is currently an integer-stepping / integer-totaling procedure
- `hexadecimal` / `decimal` still look intentional, but not as the direct filler for that missing slot
- `three ten hundred` still looks intentional, but not as the direct filler for that missing slot

## Concrete Procedure Results

Generated files:

- `canudigitv1/operation_experiments/integer_step_procedures.md`
- `canudigitv1/operation_experiments/detached_clue_integration.md`

Current strongest concrete readings:

- minimal-assumption totals:
- `297` = total of first 9 terms of the `9, 15, 21, ...` progression
- `360` = total after 9 steps of size 6 from 9
- strongest forced integration result:
- `864` = total up to `100`
- also `864` = total of `hexadecimal ten` terms, because there are `16` terms up to `100`
- and `864` in hexadecimal is `0x360`

Important negative result:

- direct representation reads such as `hexadecimal ten ten ten = 2730` and `decimal ten ten ten = 101010` do not line up with the current step-6 arithmetic as terms or totals.

Candidate comparison file:

- `canudigitv1/operation_experiments/candidate_number_comparison.md`
- `COLLABORATOR_HANDOFF.md`

Current practical ranking:

- `360` = clean skeleton front-runner
- `297` = pure low-assumption fallback if detached clues are mostly parallel noise
- `864` = interesting forced-integration experiment, but currently weaker than `360` as a lead

Important nuance:

- none of these candidates are currently supported by literal English number words like `three hundred sixty` or `eight hundred sixty four` being spelled in the grid
- they are supported only through the procedure / interpretation layers found so far
- `864` should not be treated as strong merely because `864 = 0x360`; that by itself is too hand-wavy
- `864` only remains alive because it was the cleanest forced integration so far that lets `hundred` and `hexadecimal ten` participate in the same arithmetic-progression construction

## Current Handoff

- Best integrated clause skeleton: `find start nine -> nine step six -> get nine total -> step baseten integer`
- Best concrete front-runner: `360`
- Best pure low-assumption fallback: `297`
- Best forced integration experiment: `864`
- Strong detached but intentional layer: `hexadecimal` / `decimal`
- Strong detached payload-like fragments: `three ten hundred`, `nine three hundred`
- Main unresolved question: do the detached layers refine the clean skeleton result `360`, or are they mostly parallel clue layers?

Current read on those runs:

- `baseten` results are coherent enough to feel real.
- `hexadecimal` results are suggestive but still noisier than the `baseten` and `decimal` clusters.
- The lower-right `decimal` / repeated `ten` / `integer` / `six` area is currently the strongest cluster to analyze next.

## How To Run V1

From `canudigitv1/`:

```bash
python canudig.py
```

Useful options:

```bash
python canudig.py --must-have baseten --output top_phrase_candidates_baseten.txt
python canudig.py --must-have hexadecimal --output top_phrase_candidates_hexadecimal.txt
python canudig.py --must-have-all start,nine --output operation_experiments/op_start_nine.txt
```

## Updating This Repo As The Solve Evolves

- Append new ideas and decisions to `HYPOTHESIS_LOG.md`
- Update this README when the main active solver, current hypothesis, or key output files change
- Prefer concise summaries of what is known versus what is merely speculative
