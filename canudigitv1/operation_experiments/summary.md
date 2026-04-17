# Targeted Operation Experiments

Batch run for the current instruction-layer hypothesis.

## op_find_start_nine

- words: `find, start, nine`
- note: Upper-right instruction candidate.
- output: `op_find_start_nine.txt`
- stats: `states_visited=1818 | mandatory_prunes=771 | must_have_words=find, start, nine`
- has_results: yes
- core: `find start nine`
- best_phrase: `find the start nine`

## op_start_nine

- words: `start, nine`
- note: Minimal start-anchor test.
- output: `op_start_nine.txt`
- stats: `states_visited=1818 | mandatory_prunes=765 | must_have_words=start, nine`
- has_results: yes
- core: `add start nine`
- best_phrase: `add the start nine`
- core: `find start nine`
- best_phrase: `find the start nine`
- core: `start nine`
- best_phrase: `start nine`

## op_step_six

- words: `step, six`
- note: Lower-right stepping anchor.
- output: `op_step_six.txt`
- stats: `states_visited=1818 | mandatory_prunes=746 | must_have_words=step, six`
- has_results: yes
- core: `step integer six`
- best_phrase: `step into integer by six`
- core: `nine step six`
- best_phrase: `nine step or six`
- core: `ten step six`
- best_phrase: `ten step or six`

## op_nine_step_six

- words: `nine, step, six`
- note: Explicit step-size reading.
- output: `op_nine_step_six.txt`
- stats: `states_visited=1818 | mandatory_prunes=772 | must_have_words=nine, step, six`
- has_results: yes
- core: `nine step six`
- best_phrase: `nine step or six`

## op_get_total

- words: `get, total`
- note: Potential accumulation instruction.
- output: `op_get_total.txt`
- stats: `states_visited=1818 | mandatory_prunes=771 | must_have_words=get, total`
- has_results: yes
- core: `get nine total`
- best_phrase: `get nine total`

## op_get_nine_total

- words: `get, nine, total`
- note: Explicit accumulation reading.
- output: `op_get_nine_total.txt`
- stats: `states_visited=1818 | mandatory_prunes=771 | must_have_words=get, nine, total`
- has_results: yes
- core: `get nine total`
- best_phrase: `get nine total`

## op_add_start_nine

- words: `add, start, nine`
- note: Alternate instruction-style branch.
- output: `op_add_start_nine.txt`
- stats: `states_visited=1818 | mandatory_prunes=769 | must_have_words=add, start, nine`
- has_results: yes
- core: `add start nine`
- best_phrase: `add the start nine`

## op_step_integer_six

- words: `step, integer, six`
- note: Operation + output-region test in the lower-right cluster.
- output: `op_step_integer_six.txt`
- stats: `states_visited=1818 | mandatory_prunes=761 | must_have_words=step, integer, six`
- has_results: yes
- core: `step integer six`
- best_phrase: `step into integer by six`

## op_step_baseten_integer

- words: `step, baseten, integer`
- note: Direct lower-right rule + output-label test.
- output: `op_step_baseten_integer.txt`
- stats: `states_visited=1818 | mandatory_prunes=767 | must_have_words=step, baseten, integer`
- has_results: yes
- core: `step baseten integer`
- best_phrase: `step baseten to integer`

## op_step_baseten_integer_six

- words: `step, baseten, integer, six`
- note: Direct lower-right rule + output + step-size test.
- output: `op_step_baseten_integer_six.txt`
- stats: `states_visited=1818 | mandatory_prunes=773 | must_have_words=step, baseten, integer, six`
- has_results: no
- core: none

## op_into_integer_six

- words: `into, integer, six`
- note: Alternate motion phrasing in the lower-right cluster.
- output: `op_into_integer_six.txt`
- stats: `states_visited=1818 | mandatory_prunes=769 | must_have_words=into, integer, six`
- has_results: yes
- core: `step integer six`
- best_phrase: `step into integer by six`
- core: `is integer six`
- best_phrase: `is into integer by six`

## op_point_integer

- words: `point, integer`
- note: Suppressed operation candidate near the lower-right cluster.
- output: `op_point_integer.txt`
- stats: `states_visited=1818 | mandatory_prunes=773 | must_have_words=point, integer`
- has_results: no
- core: none

## op_open_integer

- words: `open, integer`
- note: Another suppressed operation candidate near the lower-right cluster.
- output: `op_open_integer.txt`
- stats: `states_visited=1818 | mandatory_prunes=773 | must_have_words=open, integer`
- has_results: no
- core: none

## op_baseten_integer

- words: `baseten, integer`
- note: Output-normalization clue.
- output: `op_baseten_integer.txt`
- stats: `states_visited=1818 | mandatory_prunes=759 | must_have_words=baseten, integer`
- has_results: yes
- core: `step baseten integer`
- best_phrase: `step baseten to integer`
- core: `is integer baseten`
- best_phrase: `is integer baseten`
- core: `baseten integer`
- best_phrase: `baseten to integer`

## op_get_total_baseten_integer

- words: `get, total, baseten, integer`
- note: Accumulation phrase merged with output-label test.
- output: `op_get_total_baseten_integer.txt`
- stats: `states_visited=1818 | mandatory_prunes=773 | must_have_words=get, total, baseten, integer`
- has_results: no
- core: none

## op_three_ten_hundred

- words: `three, ten, hundred`
- note: Upper-left numeric payload cluster.
- output: `op_three_ten_hundred.txt`
- stats: `states_visited=1818 | mandatory_prunes=770 | must_have_words=three, ten, hundred`
- has_results: yes
- core: `three ten hundred`
- best_phrase: `three ten in hundred`

## op_payload_to_output

- words: `three, ten, hundred, baseten, integer`
- note: Cross-island payload-to-output test.
- output: `op_payload_to_output.txt`
- stats: `states_visited=1818 | mandatory_prunes=773 | must_have_words=three, ten, hundred, baseten, integer`
- has_results: no
- core: none

## op_story_chain

- words: `start, nine, step, six, total`
- note: Explicit algorithmic chain without output label.
- output: `op_story_chain.txt`
- stats: `states_visited=1818 | mandatory_prunes=773 | must_have_words=start, nine, step, six, total`
- has_results: no
- core: none

## op_start_nine_baseten_integer

- words: `start, nine, baseten, integer`
- note: Upper-right start fragment merged with lower-right output-label test.
- output: `op_start_nine_baseten_integer.txt`
- stats: `states_visited=1818 | mandatory_prunes=773 | must_have_words=start, nine, baseten, integer`
- has_results: no
- core: none

## op_story_chain_with_output

- words: `start, nine, step, six, total, baseten, integer`
- note: Full explicit algorithmic chain with output label.
- output: `op_story_chain_with_output.txt`
- stats: `states_visited=1818 | mandatory_prunes=773 | must_have_words=start, nine, step, six, total, baseten, integer`
- has_results: no
- core: none

