# Hypothesis Log

Append-only working log for the "Can U dig it?" puzzle.
Add new dated entries at the bottom. Do not delete older entries; supersede them with newer notes.

## 2026-04-16

Summary after reading the repo in its current state:

- Primary working solver is `canudigitv1/canudig_search.py`.
- `canudigitv2/` is an exact-search side path that is now retired and should not drive current conclusions.
- The strongest current theme is numbers / number representation, not chemistry.
- The most meaningful exact hits in the curated v1 search are `baseten`, `decimal`, `decimals`, `integer`, `integers`, `binary`, `hexadecimal`, `three`, `nine`, `ten`, `hundred`, `hundreds`, `nineteen`, `six`, plus instruction words like `find` and `start`.
- Chemistry support exists in the unrestricted dictionary sweep, but it looks weak and noisy compared with the number-system cluster.
- The strongest clue-like fragments so far are `baseten integer`, `three ten hundred`, `decimal ... integer`, and `find the start`.
- The current v1 phrase search is heavily verb-first and grammar-template driven, which likely suppresses noun/number expressions that may contain the real clue.
- Bridge words like `the`, `a`, `to`, `in`, and `of` create many sentence-looking paths that are probably scaffold noise rather than clue text.
- The old fake hex-token experiment (`threee`, `threed`, `onea`, `twoe`, etc.) is suggestive but not trustworthy enough yet to treat as solved signal.
- Current working hypothesis: the puzzle likely resolves to a positive integer via number-language or base / representation clues, with `find/start` potentially giving extraction instructions.

## 2026-04-16

Summary after patching `solver v1`, rerunning, and reviewing the new outputs:

- Decision: `solver v1` now emits content-core summaries in addition to full phrase candidates, so bridge-word scaffolding is easier to separate from clue-bearing fragments.
- Decision: fake hex tokens are no longer allowed to seed phrases. This removed the old `threee ...` / `threed ...` style artifacts from the top results.
- The updated default run strongly reinforces the number/base hypothesis.
- The most stable numeric cores are now `decimal ten ten ten integer`, `hexadecimal ten ten ten integer`, `step baseten integer`, `baseten integer`, `three ten hundred`, and `integer ... six` variants.
- Focused runs confirm that `baseten` and `hexadecimal` are not isolated one-off words; they participate in repeatable phrase cores.
- `top_phrase_candidates_baseten.txt` is coherent enough to matter. Its best cores are `step baseten integer`, `is integer baseten`, and `baseten integer`.
- `top_phrase_candidates_hexadecimal.txt` is more mixed. It does produce stable cores like `hexadecimal ten ten ten integer`, but many wrappers around that core still look combinatorial rather than clue-like.
- The lower-right cluster (`decimal` / repeated `ten` / `integer` / `six` / `baseten`) is now the strongest concrete region in the grid.
- The upper-left / left-center numeric cluster still matters. `three ten hundred` survives the rerun and still looks more meaningful than most sentence-like outputs.
- `find the start` and `find the start nine` still exist, but after the rerun they look secondary compared with the number-system cluster. They may be extraction instructions rather than the main thematic payload.
- Current working hypothesis: the puzzle is very likely about number representation or conversion, but the outputs still do not cleanly specify the final integer. This is progress, not a solve.
- Next likely direction: analyze the geometry of the stable numeric cores directly, especially how `baseten`, `decimal`, `hexadecimal`, repeated `ten`, `integer`, and `six` line up and overlap.

## 2026-04-16

Summary after testing geometric connections between the main clue clusters:

- The stable cores are mostly object language, not action language. We have stronger evidence for what kind of thing the clue is about than for the exact operation needed to finish the puzzle.
- The lower-right cluster is a real connected structure, not just a bag of related words. `decimal`, `hexadecimal`, `binary`, repeated `ten`, `integer`, `step`, `baseten`, `six`, and `total` all live in or immediately around the same region.
- `decimal` is literally embedded in `hexadecimal`, so those should be treated as overlapping structure, not two independent confirmations.
- The upper-right instruction fragment `find the start nine` still looks real, but it does not yet connect cleanly enough to the lower-right numeric cluster to count as a solved instruction chain.
- The upper-left `three` / `ten` / `hundred` / `nine` / `nineteen` cluster is internally coherent, but at the moment it looks more like a second numeric island than part of the same exact path as the lower-right base-conversion cluster.
- The first plausible endgame story is now: find a starting value, step through something, get a total, then report the result as a base-10 integer.
- The strongest current rule-layer fragments are `find the start nine`, `nine step six`, `get nine total`, `step integer six`, and `baseten integer`.
- This story is still not proved. The biggest concern is that there is still no single exact phrase that cleanly states the full operation.
- Current working model:
- one clue family gives the control / traversal instruction
- one clue family gives the numeric payload
- the lower-right cluster tells us the payload is about representation / base
- the final output should be rendered as a base-10 integer
- Next implementation direction: run targeted operation-word experiments around `start`, `step`, `total`, `point`, `open`, `into`, `add`, and `get`, and separately test whether the upper-left `three ten hundred` island can supply the payload for the lower-right rule layer.

## 2026-04-16

Summary after implementing multiword required-word experiments and running the operation-focused batch:

- Decision: `solver v1` now supports `--must-have-all` for multiword hypothesis tests.
- Decision: `canudigitv1/run_targeted_operation_experiments.py` is now the repeatable way to rerun the current instruction-layer experiment set.
- Confirmed micro-clauses:
- `find start nine`
- `start nine`
- `add start nine`
- `step integer six`
- `nine step six`
- `get nine total`
- `step baseten integer`
- `baseten integer`
- `three ten hundred`
- Rejected or unsupported operation candidates:
- `point integer` produced no phrase results
- `open integer` produced no phrase results
- Important structural result: the likely solve story exists as smaller pieces, not as one single phrase.
- The full explicit chain `start + nine + step + six + total` produced no phrase.
- The full explicit chain with output label `start + nine + step + six + total + baseten + integer` also produced no phrase.
- Cross-island tests also failed. `three + ten + hundred + baseten + integer` produced no phrase, and `start + nine + baseten + integer` produced no phrase.
- Important lower-right detail: `step baseten integer` is real, and `step integer six` is real, but adding all four words together (`step + baseten + integer + six`) produced no phrase. That suggests the lower-right region may contain adjacent but distinct subclauses rather than one continuous sentence.
- Current best read:
- upper-right clause: `find/start/nine`
- lower-right clause A: `step/baseten/integer`
- lower-right clause B: `step/integer/six` and `nine/step/six`
- lower-right clause C: `get/nine/total`
- upper-left payload clause: `three/ten/hundred`
- Current concern: the repo now has stronger evidence for a multi-clause solve structure, but we still do not know how those clauses compose into the final integer.
- Updated next direction: analyze the lower-right cluster as a clause graph rather than forcing everything into one phrase, and test whether repeated `nine` is the pivot that links the instruction and payload families.

## 2026-04-16

Summary after generating the first clause graph and spatial overlap report:

- Decision: `canudigitv1/build_clause_graph_report.py` is now the repeatable report builder for the current clause-based interpretation.
- The strongest current clause nodes are `step integer six`, `step baseten integer`, `nine step six`, `get nine total`, `find start nine`, `add start nine`, and `three ten hundred`.
- Important clarification: clause strength is not just phrase frequency. It is now based on whether a clause survives as a top content core, whether it survives a targeted `--must-have-all` experiment, how specific that successful experiment is, how many outputs support it, and its best-score stability.
- `nine` is now the clearest lexical pivot in the graph. It links the upper-right start family to the lower-right step/total family.
- `step` and `integer` are the clearest lower-right pivots.
- The lower-right zone looks increasingly like a cluster of adjacent subclauses, not one sentence. `step integer six`, `step baseten integer`, `baseten integer`, and `get nine total` are all spatially close even when they do not merge into one successful phrase.
- `get nine total` sits immediately adjacent to the lower-right output-format clauses in the spatial report, which strengthens the story that the final result may be a total that must then be rendered as a base-10 integer.
- The upper-right start family remains real, but it still only connects into the lower-right graph lexically through `nine`, not through a successful long phrase.
- `three ten hundred` remains the leading payload candidate, but it is still graph-isolated in the sense that every direct payload-to-output composition test failed.
- Updated working model:
- start value clue: `find/start/nine`
- action / iteration clue: `step/.../six`
- accumulation clue: `get/nine/total`
- output-format clue: `baseten/integer`
- unresolved payload clue: `three/ten/hundred`
- Current concern: this still supports a multi-clause solve, but it does not yet tell us whether `three ten hundred` is the thing being stepped through, the thing being totaled, or a separate alternate clue family.

## 2026-04-16

Summary after building the first procedure hypothesis scorecard:

- Decision: `canudigitv1/build_hypothesis_scorecard.py` is now the discriminative layer on top of the clause graph. It compares concrete endgame stories instead of only listing fragments and bridges.
- The key improvement over the clause graph is methodological: the scorecard ranks whole procedure families under one fixed rubric, rather than hoping a connection will "click" from another descriptive pass.
- Current winner under the minimal-assumption rubric is the non-payload `Procedure Skeleton`:
- `find start nine`
- `nine step six`
- `get nine total`
- `step baseten integer`
- That procedure family currently beats the payload-injected variant because `three ten hundred` still does not attach cleanly to the rest of the chain.
- The payload-slotted story remains alive, but it is no longer the clean front-runner. Its weak point is the unsupported jump from the lower-right output clause to the upper-left payload clause.
- Representation-first stories (`decimal` / `hexadecimal` -> `baseten integer`) score badly under the current rubric because they leave too much Tier 1 start/step/total evidence unexplained.
- Updated current read: the cleanest supported skeleton is now `start 9 -> step 6 style rule -> get total -> output base-10 integer`, with one unresolved slot: what exact thing is being stepped / totaled.

## 2026-04-16

Summary after running direct attachment tests for `hexadecimal` / `decimal` and `three ten hundred` against the current winning skeleton:

- Decision: `canudigitv1/run_attachment_experiments.py` now tests whether unresolved clue families can attach directly to specific roles in the winning skeleton.
- Result: `hexadecimal` and `decimal` currently fail to attach to every tested skeleton role, not just `three ten hundred`.
- Specifically, no direct attachment survived for:
- start role (`start nine + hexadecimal/decimal`)
- action role (`step integer six + hexadecimal/decimal`)
- total role (`get nine total + hexadecimal/decimal`)
- output role (`baseten integer + hexadecimal/decimal`)
- action/output role (`step baseten integer + hexadecimal/decimal`)
- Payload attachments also all failed for the same role slots.
- Important distinction: `hexadecimal` still looks intentional because it has its own strong local family (`hexadecimal ten ten ten integer`, `find hexadecimal ten`, `add hexadecimal ten`) even though it does not currently bind to the winning skeleton.
- Updated read: the winning skeleton is currently a better integrated procedure layer than either the payload or representation layers. `hexadecimal` / `decimal` should currently be treated as a parallel or confirmatory layer, not yet as an integrated clause in the same chain.
- Score margin note: the current leader is ahead, but not by a runaway amount. The `Procedure Skeleton` scores 61 versus 54 for the next two alternatives. That is a lead, not a proof.

## 2026-04-16

Summary after building the missing-slot discriminator for the winning skeleton:

- Decision: `canudigitv1/build_missing_slot_discriminator.py` now compares only three candidate fillers for the one unresolved slot in the current leading procedure skeleton.
- Question being tested: what exact object or value is being stepped / totaled in `find start nine -> nine step six -> get nine total -> step baseten integer`?
- Current ranking:
- `Integer Object` = 24
- `Three-Ten-Hundred Payload` = -1
- `Representation-Coded Object` = -7
- This is the first time the unresolved slot itself has been tested directly rather than indirectly through whole-procedure stories.
- Current winner: the cleanest low-assumption read is that the thing being stepped / totaled is some integer sequence or integer-valued object, not the `hexadecimal` / `decimal` family and not `three ten hundred`.
- Important nuance: this does not mean the representation family or `three ten hundred` are fake. It means they are currently weaker as direct fillers for the missing slot in the leading skeleton.
- Updated current read: the best-supported story is now `start at 9 -> apply a step-6 rule over integers -> get a total -> report as a base-10 integer`, with the exact total rule still unresolved.

## 2026-04-16

Summary after enumerating concrete integer-step procedures and forcing direct integrations of the detached clues:

- Minimal-assumption concrete procedure candidates are now pinned down to two strongest totals:
- total of first 9 terms = `297`
- total after 9 steps = `360`
- Term-only readings (`57`, `63`) remain weaker because they do not satisfy the `get ... total` clue naturally.
- First genuinely new integration result: `864` is now a cross-clue convergence point.
- Using `hundred` as an upper bound in the start-9 step-6 sequence gives 16 terms and total `864`.
- `16` is exactly `hexadecimal ten` in decimal.
- The same total can therefore be described two ways:
- total up to `100` = `864`
- total of `hexadecimal ten` terms = `864`
- In hexadecimal, `864` is `0x360`, which is a compact additional regularity, though not yet a proved clue reading.
- Direct representation values do *not* currently integrate with the step-6 arithmetic:
- `hexadecimal ten ten ten` -> `2730`
- `decimal ten ten ten` -> `101010`
- Neither `2730` nor `101010` appears as a term or arithmetic-progression total in the start-9 step-6 family.
- Updated current read:
- strongest bare skeleton totals: `297`, `360`
- strongest forced integration construction: `864 = 0x360`, obtained either from `hundred` as an upper bound or from `hexadecimal ten` as the term count
- `three ten hundred` still does not slot cleanly into the winning skeleton, but `ten` and `hundred` now participate in nontrivial constructions

## 2026-04-16

Summary after comparing the concrete candidate numbers directly:

- Current live candidates are now `297`, `360`, and `864`.
- `297` remains the best pure minimal-assumption total if `get nine total` means the total of the first 9 terms of the `9,15,21,...` progression.
- `360` remains the cleanest concrete procedure candidate if `nine step six` means 9 steps of size 6 and the result is the accumulated total after those steps.
- `864` remains the best cross-layer integration candidate because:
- terms up to `100` in the start-9 step-6 progression total `864`
- there are `16` such terms, i.e. `hexadecimal ten`
- `864` in hexadecimal is `0x360`
- Important negative result: exact probes found no paths for number words like `zero`, `sixteen`, `sixty`, `eight`, `four`, `threehundredsixty`, or `eighthundredsixtyfour`.
- That means the current candidates are not supported because their English number words are literally spelled in the grid.
- New ranking by style of support:
- `360` = clean skeleton front-runner
- `864` = best integration front-runner
- `297` = best pure low-assumption fallback, but hardest to reconcile with detached clues
- `nine three hundred` keeps a loose `9 / 3 / 100` neighborhood alive and weakly nudges attention toward `360` / `0x360` more than `297`, but this is still speculative.

## 2026-04-16

Summary after tightening the candidate ranking and correcting the interpretation of `864`:

- Important correction: `864` is **not** a strong candidate merely because `864 = 0x360`.
- That hexadecimal coincidence by itself is not meaningful enough to carry the solve.
- The real reason `864` stayed alive was narrower: it was the cleanest forced-integration construction found so far that lets `hundred` and `hexadecimal ten` participate in the same arithmetic-progression story.
- Specifically:
- terms of the `9, 15, 21, ...` progression up to `100` total `864`
- there are `16` such terms, i.e. `hexadecimal ten`
- this makes `864` an interesting integration experiment, but not a lead by itself
- Updated practical ranking:
- `360` = current best concrete front-runner
- `297` = still viable as the cleanest pure low-assumption fallback if `get nine total` means the total of the first 9 terms
- `864` = interesting forced-integration experiment, but weaker than `360` as an actual lead
- Current live final-answer candidates are therefore still three numbers: `297`, `360`, and `864`.
- Current best handoff summary:
- strongest integrated clause skeleton: `find start nine -> nine step six -> get nine total -> step baseten integer`
- strongest detached but intentional representation layer: `hexadecimal` / `decimal`
- strongest detached payload-like fragments: `three ten hundred`, `nine three hundred`
- main unresolved question for the next thread: do the detached layers transform / refine the clean skeleton result `360`, or are they mostly parallel clue layers?
