import argparse
import csv
import heapq
import string
from collections import defaultdict
from contextlib import redirect_stdout
from dataclasses import dataclass
from pathlib import Path


DIRS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_CSV_PATH = SCRIPT_DIR / "can u dig it.csv"
DEFAULT_OUTPUT_PATH = SCRIPT_DIR / "top_phrase_candidates.txt"

# Edit this block directly if you want to change the candidate vocabulary.
# Format per line:
#   word
#   word,weight
#   word,weight,TAG1|TAG2
#
# Tags matter because the phrase search enforces structure with them.
# If a candidate should count as a verb, noun, adjective, or number-like token,
# tag it explicitly when possible.
#
# Built-in bridge words such as "the", "to", "of", "and", "is", "were", etc.
# are added automatically in code; keep this list focused on clue-relevant content words.
EMBEDDED_CANDIDATE_WORDS = """
find,1,VERB
get,1,VERB
getup,1,VERB
start,1,NOUN|VERB
starting,1,ADJ|VERB
end,1,NOUN|VERB
one,6,NOUN|NUMBER
two,6,NOUN|NUMBER
three,6,NOUN|NUMBER
four,6,NOUN|NUMBER
five,6,NOUN|NUMBER
six,6,NOUN|NUMBER
seven,6,NOUN|NUMBER
eight,6,NOUN|NUMBER
nine,6,NOUN|NUMBER
ten,6,NOUN|NUMBER
eleven,6,NOUN|NUMBER
twelve,6,NOUN|NUMBER
thirteen,6,NOUN|NUMBER
fourteen,6,NOUN|NUMBER
fifteen,6,NOUN|NUMBER
sixteen,6,NOUN|NUMBER
seventeen,6,NOUN|NUMBER
eighteen,6,NOUN|NUMBER
nineteen,6,NOUN|NUMBER
twenty,6,NOUN|NUMBER
hundred,6,NOUN|NUMBER
hundreds,6,NOUN|NUMBER
thousand,6,NOUN|NUMBER
thousands,6,NOUN|NUMBER
onea,8,NOUN|NUMBER|HEXNUMBER
oneb,8,NOUN|NUMBER|HEXNUMBER
onec,8,NOUN|NUMBER|HEXNUMBER
oned,8,NOUN|NUMBER|HEXNUMBER
onee,8,NOUN|NUMBER|HEXNUMBER
onef,8,NOUN|NUMBER|HEXNUMBER
twoa,8,NOUN|NUMBER|HEXNUMBER
twob,8,NOUN|NUMBER|HEXNUMBER
twoc,8,NOUN|NUMBER|HEXNUMBER
twod,8,NOUN|NUMBER|HEXNUMBER
twoe,8,NOUN|NUMBER|HEXNUMBER
twof,8,NOUN|NUMBER|HEXNUMBER
threea,8,NOUN|NUMBER|HEXNUMBER
threeb,8,NOUN|NUMBER|HEXNUMBER
threec,8,NOUN|NUMBER|HEXNUMBER
threed,8,NOUN|NUMBER|HEXNUMBER
threee,8,NOUN|NUMBER|HEXNUMBER
threef,8,NOUN|NUMBER|HEXNUMBER
integer,6,NOUN
integers,6,NOUN
decimal,6,NOUN
decimals,6,NOUN
number,1,NOUN
hexadecimal,1,NOUN
hexagon,3,NOUN
add,3,VERB
subtract,3,VERB
plus,3,VERB
minus,3,VERB
positive,6,ADJ
negative,6,ADJ
digit,6,NOUN
digits,6,NOUN
odd,6,ADJ
even,6,ADJ
binary,8,NOUN|ADJ
baseone,8,NOUN
basetwo,8,NOUN
basethree,8,NOUN
basefour,8,NOUN
basefive,8,NOUN
basesix,8,NOUN
baseseven,8,NOUN
baseeight,8,NOUN
basenine,8,NOUN
baseten,8,NOUN
total,6,NOUN|ADJ
sum,3,NOUN|VERB
step,1,NOUN|VERB
open,1,VERB
point,1,NOUN|VERB
do,1,VERB
is,1,VERB
point,1,NOUN|VERB
""".strip()

DEFAULT_BRIDGE_WORDS = {
    "an", "and", "as", "at", "be", "by", "for", "from", "in", "into",
    "it", "of", "on", "or", "that", "the", "then", "this", "to",
    "were", "with",
}

COMMON_VERBS = {
    "is", "are", "was", "were", "be", "been", "being",
    "do", "does", "did", "have", "has", "had",
    "find", "spray", "get", "start","step", "tune", "open", "point",
    "take", "turn", "read", "use",
}

COMMON_NOUNS = {
    "start", "integer", "path", "spray",
    "point", "twenty", "six", "noun", "verb", "word","sentence", "rule", "paths",

}

CONTENT_BONUS = 6
BRIDGE_PENALTY = 0 #-4
SYNTAX_BONUS = 8
REPEAT_WORD_PENALTY = 5
HEXNUMBER_PAIR_BONUS = 200
MUST_HAVE_WORD = None  # Set to a word like "baseten" to require it in every completed phrase.
ROLE_TAGS = ("VERB", "NOUN", "ADJ", "NUMBER", "HEXNUMBER", "FUNCTION")

# 1) action / instruction phrases
ACTION_PATTERNS = (
    ("VERB", "FUNCTION", "NOUN"),                # find the start
    ("VERB", "FUNCTION", "NOUN", "NUMBER"),      # find the start nine
    ("VERB", "NOUN"),                            # step baseten / step integer
    ("VERB", "NUMBER"),                          # get nine
    ("VERB", "NUMBER", "NOUN"),                  # get nine total / find three ten
    ("VERB", "NUMBER", "FUNCTION", "NUMBER"),    # get nine to ten
    ("VERB", "NOUN", "FUNCTION", "NOUN"),        # step baseten to integer
    ("VERB", "NOUN", "FUNCTION", "NUMBER"),      # step integer by six
    ("VERB", "FUNCTION", "NOUN", "FUNCTION", "NUMBER"),  # step into integer by six
)

# 2) relation / definition phrases
RELATION_PATTERNS = (
    ("VERB", "NOUN"),                            # is integer
    ("VERB", "NOUN", "NOUN"),                    # is integer baseten
    ("VERB", "NUMBER", "NOUN"),                  # is ten integer
    ("VERB", "NUMBER", "NUMBER"),                # is ten ten
    ("VERB", "NUMBER", "NUMBER", "NOUN"),        # is ten ten integer
    ("VERB", "NUMBER", "FUNCTION", "NOUN"),      # is ten to integer
    ("VERB", "NUMBER", "FUNCTION", "NOUN", "FUNCTION", "NUMBER"),  # is ten to integer by six
    ("VERB", "NOUN", "FUNCTION", "NUMBER"),      # is integer as six
)

# 3) expression / label phrases
EXPR_PATTERNS = (
    ("NOUN", "NUMBER"),                          # hexadecimal ten / start nine
    ("ADJ", "NUMBER"),                           # binary ten
    ("NOUN", "NOUN"),                            # baseten integer / nine total
    ("NUMBER", "NOUN"),                          # ten integer / nine total
    ("NUMBER", "NUMBER"),                        # ten ten
    ("NOUN", "NUMBER", "NUMBER"),                # hexadecimal ten ten
    ("NUMBER", "NUMBER", "NOUN"),                # ten ten integer
    ("NOUN", "NOUN", "NOUN"),                    # integer baseten ...
)

PATTERN_GROUPS = {
    "action": ACTION_PATTERNS,
    "relation": RELATION_PATTERNS,
    "expression": EXPR_PATTERNS,
}

ALLOWED_PATTERNS = tuple(
    dict.fromkeys(pattern for patterns in PATTERN_GROUPS.values() for pattern in patterns)
)


@dataclass(frozen=True)
class CandidateWord:
    word: str
    manual_weight: int
    tags: frozenset
    is_bridge: bool

    @property
    def meta_bonus(self):
        if self.is_bridge:
            return self.manual_weight + BRIDGE_PENALTY
        return self.manual_weight + CONTENT_BONUS


@dataclass(frozen=True)
class WordInstance:
    index: int
    word: str
    start: int
    end: int
    mask: int
    path: tuple
    length: int
    tags: frozenset
    is_bridge: bool
    meta_bonus: int


@dataclass(frozen=True)
class SearchResult:
    score: int
    letters_used: int
    content_words: int
    bridge_words: int
    has_noun: bool
    has_verb: bool
    words: tuple
    paths: tuple

    @property
    def text(self):
        return " ".join(self.words)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Candidate-driven exact path search for the Can U Dig It grid."
    )
    parser.add_argument(
        "--csv",
        default=str(DEFAULT_CSV_PATH),
        help="Path to the puzzle grid CSV.",
    )
    parser.add_argument(
        "--candidates",
        default=None,
        help="Optional override path for candidate words. If omitted, uses the editable list inside canudig_search.py.",
    )
    parser.add_argument(
        "--output",
        default=str(DEFAULT_OUTPUT_PATH),
        help="Path to the text file that will receive the solver output.",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=500,
        help="Keep only the top K completed phrase candidates.",
    )
    parser.add_argument(
        "--max-words",
        type=int,
        default=7,
        help="Maximum number of words in a phrase.",
    )
    parser.add_argument(
        "--min-words",
        type=int,
        default=3,
        help="Minimum number of words required for a phrase result.",
    )
    parser.add_argument(
        "--max-paths-per-word",
        type=int,
        default=12,
        help="How many matching paths to print for each found candidate word.",
    )
    parser.add_argument(
        "--show-bridge-matches",
        action="store_true",
        help="Also print bridge-word matches such as 'the' or 'to'.",
    )
    parser.add_argument(
        "--allow-bridge-seeds",
        action="store_true",
        help="Allow phrase search to start from bridge words. This is slower.",
    )
    parser.add_argument(
        "--must-have",
        default=MUST_HAVE_WORD,
        help="Optional word that must appear in every completed phrase. Use None/off/blank to disable.",
    )
    return parser.parse_args()


def normalize_word(raw_word):
    word = raw_word.strip().lower().replace("'", "")
    if not word:
        return ""
    if not word.isalpha():
        raise ValueError(f"Candidate word must be alphabetic: {raw_word!r}")
    return word


def normalize_optional_word(raw_word):
    if raw_word is None:
        return None
    text = str(raw_word).strip()
    if not text or text.lower() in {"none", "off"}:
        return None
    return normalize_word(text)


def guess_tags(word):
    tags = set()
    is_bridge_word = word in DEFAULT_BRIDGE_WORDS
    if word in COMMON_VERBS:
        tags.add("VERB")
    if word in COMMON_NOUNS:
        tags.add("NOUN")
    if is_bridge_word:
        tags.add("FUNCTION")
    if not is_bridge_word and (word.endswith("ing") or word.endswith("ed")):
        tags.add("VERB")
    if not is_bridge_word and (word.endswith("tion") or word.endswith("ment") or word.endswith("ness") or word.endswith("ity")):
        tags.add("NOUN")
    if not is_bridge_word and (word.endswith("er") or word.endswith("or")):
        tags.add("NOUN")
    return tags


def parse_candidate_rows(rows, source_name):
    candidates = {}

    for word in sorted(DEFAULT_BRIDGE_WORDS):
        tags = frozenset(guess_tags(word) | {"FUNCTION"})
        candidates[word] = CandidateWord(word=word, manual_weight=0, tags=tags, is_bridge=True)

    for line_no, raw_line in rows:
        line = raw_line.split("#", 1)[0].strip()
        if not line:
            continue
        row = next(csv.reader([line]))
        if not row:
            continue
        try:
            word = normalize_word(row[0])
        except ValueError as exc:
            raise ValueError(f"{source_name}:{line_no}: {exc}") from exc
        if not word:
            continue

        manual_weight = 0
        if len(row) >= 2 and row[1].strip():
            try:
                manual_weight = int(row[1].strip())
            except ValueError as exc:
                raise ValueError(
                    f"{source_name}:{line_no}: invalid weight {row[1]!r}"
                ) from exc

        raw_tags = ""
        if len(row) >= 3:
            raw_tags = ",".join(row[2:])
        tags = {
            tag.strip().upper()
            for chunk in raw_tags.split("|")
            for tag in chunk.split()
            if tag.strip()
        }

        guessed = guess_tags(word)
        is_bridge = "FUNCTION" in tags or (word in DEFAULT_BRIDGE_WORDS and "CONTENT" not in tags)
        if is_bridge:
            tags.add("FUNCTION")
        else:
            tags.discard("FUNCTION")
        tags |= guessed
        candidates[word] = CandidateWord(
            word=word,
            manual_weight=manual_weight,
            tags=frozenset(tags),
            is_bridge=is_bridge,
        )

    return candidates


def load_candidates(candidate_path):
    if candidate_path:
        candidate_path = Path(candidate_path)
        if not candidate_path.exists():
            raise FileNotFoundError(
                f"Candidate list not found: {candidate_path}. Pass a valid --candidates path or use the embedded list in canudig_search.py."
            )
        with candidate_path.open(encoding="utf-8") as handle:
            rows = list(enumerate(handle, start=1))
        return parse_candidate_rows(rows, str(candidate_path)), str(candidate_path)

    embedded_lines = EMBEDDED_CANDIDATE_WORDS.splitlines()
    rows = list(enumerate(embedded_lines, start=1))
    return parse_candidate_rows(rows, "canudig_search.py:EMBEDDED_CANDIDATE_WORDS"), "canudig_search.py:EMBEDDED_CANDIDATE_WORDS"


def load_grid(csv_path):
    csv_path = Path(csv_path)
    with csv_path.open(newline="", encoding="utf-8") as handle:
        grid = [row for row in csv.reader(handle)]

    rows = len(grid)
    cols = len(grid[0])
    col_labels = string.ascii_uppercase[:cols]

    letters = []
    neighbors = []
    alpha_cell_count = 0
    for r in range(rows):
        for c in range(cols):
            letters.append(grid[r][c].lower())
            if grid[r][c].isalpha():
                alpha_cell_count += 1
            cell_neighbors = []
            for dr, dc in DIRS:
                rr = r + dr
                cc = c + dc
                if 0 <= rr < rows and 0 <= cc < cols:
                    cell_neighbors.append(rr * cols + cc)
            neighbors.append(tuple(cell_neighbors))

    return {
        "grid": grid,
        "rows": rows,
        "cols": cols,
        "col_labels": col_labels,
        "letters": tuple(letters),
        "neighbors": tuple(neighbors),
        "alpha_cell_count": alpha_cell_count,
    }


def build_prefixes(words):
    prefixes = set()
    max_word_len = 0
    for word in words:
        max_word_len = max(max_word_len, len(word))
        for idx in range(1, len(word) + 1):
            prefixes.add(word[:idx])
    return prefixes, max_word_len


def cell_to_coord(cell_id, cols, col_labels):
    row = cell_id // cols
    col = cell_id % cols
    return f"{col_labels[col]}{row + 1}"


def path_to_coords(path, cols, col_labels):
    return [cell_to_coord(cell_id, cols, col_labels) for cell_id in path]


def find_word_instances(grid_info, candidates):
    letters = grid_info["letters"]
    neighbors = grid_info["neighbors"]
    allowed_words = set(candidates)
    prefixes, max_word_len = build_prefixes(allowed_words)

    instances = []
    instances_by_word = defaultdict(list)
    current_path = []

    def dfs(cell_id, current, used_mask):
        ch = letters[cell_id]
        if not ch.isalpha():
            return

        current += ch
        if current not in prefixes:
            return

        used_mask |= 1 << cell_id
        current_path.append(cell_id)

        if current in candidates:
            meta = candidates[current]
            instance = WordInstance(
                index=len(instances),
                word=current,
                start=current_path[0],
                end=current_path[-1],
                mask=used_mask,
                path=tuple(current_path),
                length=len(current_path),
                tags=meta.tags,
                is_bridge=meta.is_bridge,
                meta_bonus=meta.meta_bonus,
            )
            instances_by_word[current].append(len(instances))
            instances.append(instance)

        if len(current) < max_word_len:
            for next_cell in neighbors[cell_id]:
                bit = 1 << next_cell
                if used_mask & bit:
                    continue
                dfs(next_cell, current, used_mask)

        current_path.pop()

    for cell_id, ch in enumerate(letters):
        if ch.isalpha():
            dfs(cell_id, "", 0)

    return instances, instances_by_word


def build_search_graph(instances, neighbors):
    instances_by_start = defaultdict(list)
    for instance in instances:
        instances_by_start[instance.start].append(instance.index)

    next_indices = []
    for instance in instances:
        candidates = []
        for start_cell in neighbors[instance.end]:
            candidates.extend(instances_by_start.get(start_cell, ()))
        candidates.sort(
            key=lambda idx: (
                instances[idx].length + instances[idx].meta_bonus,
                instances[idx].length,
                instances[idx].word,
            ),
            reverse=True,
        )
        next_indices.append(tuple(candidates))
    return tuple(next_indices)


def syntax_bonus(has_noun, has_verb):
    if has_noun and has_verb:
        return SYNTAX_BONUS
    return 0


def instance_roles(instance):
    roles = set()
    for tag in ROLE_TAGS:
        if tag in instance.tags:
            roles.add(tag)
    if instance.is_bridge:
        roles.add("FUNCTION")
    return frozenset(roles)


def matches_pattern_prefix(role_stack):
    depth = len(role_stack)
    for pattern in ALLOWED_PATTERNS:
        if depth > len(pattern):
            continue
        if all(pattern[idx] in role_stack[idx] for idx in range(depth)):
            return True
    return False


def matches_complete_pattern(role_stack):
    depth = len(role_stack)
    for pattern in ALLOWED_PATTERNS:
        if depth != len(pattern):
            continue
        if all(pattern[idx] in role_stack[idx] for idx in range(depth)):
            return True
    return False


def can_extend_pattern(role_stack):
    depth = len(role_stack)
    for pattern in ALLOWED_PATTERNS:
        if depth >= len(pattern):
            continue
        if all(pattern[idx] in role_stack[idx] for idx in range(depth)):
            return True
    return False


def passes_word_constraints(instances, stack, next_instance):
    if "HEXNUMBER" in next_instance.tags:
        if not stack:
            return False
        prev_instance = instances[stack[-1]]
        return prev_instance.word == "hexadecimal"
    return True


def transition_bonus(prev_instance, next_instance):
    if prev_instance.word == "hexadecimal" and "HEXNUMBER" in next_instance.tags:
        return HEXNUMBER_PAIR_BONUS
    return 0


def result_rank(result):
    return (
        result.score,
        result.letters_used,
        result.content_words,
        -result.bridge_words,
        result.text,
    )


def search_phrases(instances, next_indices, alpha_cell_count, top_k, min_words, max_words, allow_bridge_seeds, must_have_word):
    if not instances:
        return [], {"states": 0, "pruned_bound": 0, "pruned_overlap": 0, "pruned_structure": 0, "pruned_mandatory": 0}

    internal_top_k = max(top_k, top_k * 5)
    max_positive_meta_bonus = max(0, max(instance.meta_bonus for instance in instances))
    stats = {"states": 0, "pruned_bound": 0, "pruned_overlap": 0, "pruned_structure": 0, "pruned_mandatory": 0}
    heap = []
    serial = 0
    stack = []
    role_stack = []
    word_counts = defaultdict(int)

    def maybe_record(base_score, letters_used, has_noun, has_verb, content_words, bridge_words, has_mandatory):
        nonlocal serial
        if must_have_word and not has_mandatory:
            stats["pruned_mandatory"] += 1
            return
        final_score = base_score + syntax_bonus(has_noun, has_verb)
        result = SearchResult(
            score=final_score,
            letters_used=letters_used,
            content_words=content_words,
            bridge_words=bridge_words,
            has_noun=has_noun,
            has_verb=has_verb,
            words=tuple(instances[idx].word for idx in stack),
            paths=tuple(instances[idx].path for idx in stack),
        )
        entry = (result_rank(result), serial, result)
        serial += 1
        if len(heap) < internal_top_k:
            heapq.heappush(heap, entry)
            return
        if entry[0] > heap[0][0]:
            heapq.heapreplace(heap, entry)

    def dfs(used_mask, base_score, letters_used, has_noun, has_verb, content_words, bridge_words, has_mandatory):
        stats["states"] += 1
        depth = len(stack)

        if depth >= min_words and matches_complete_pattern(role_stack):
            maybe_record(base_score, letters_used, has_noun, has_verb, content_words, bridge_words, has_mandatory)

        if depth >= max_words:
            return

        if not can_extend_pattern(role_stack):
            return

        if len(heap) >= internal_top_k:
            remaining_slots = max_words - depth
            optimistic_score = base_score + (alpha_cell_count - letters_used)
            optimistic_score += remaining_slots * (max_positive_meta_bonus + HEXNUMBER_PAIR_BONUS)
            if not (has_noun and has_verb):
                optimistic_score += SYNTAX_BONUS
            if optimistic_score < heap[0][0][0]:
                stats["pruned_bound"] += 1
                return

        last_instance = instances[stack[-1]]
        for next_idx in next_indices[last_instance.index]:
            next_instance = instances[next_idx]
            if used_mask & next_instance.mask:
                stats["pruned_overlap"] += 1
                continue
            if not passes_word_constraints(instances, stack, next_instance):
                stats["pruned_structure"] += 1
                continue
            role_stack.append(instance_roles(next_instance))
            if not matches_pattern_prefix(role_stack):
                role_stack.pop()
                stats["pruned_structure"] += 1
                continue
            stack.append(next_idx)
            repeat_penalty = REPEAT_WORD_PENALTY if word_counts[next_instance.word] > 0 else 0
            pair_score = transition_bonus(last_instance, next_instance)
            word_counts[next_instance.word] += 1
            dfs(
                used_mask | next_instance.mask,
                base_score + next_instance.length + next_instance.meta_bonus + pair_score - repeat_penalty,
                letters_used + next_instance.length,
                has_noun or ("NOUN" in next_instance.tags),
                has_verb or ("VERB" in next_instance.tags),
                content_words + (0 if next_instance.is_bridge else 1),
                bridge_words + (1 if next_instance.is_bridge else 0),
                has_mandatory or (next_instance.word == must_have_word),
            )
            word_counts[next_instance.word] -= 1
            stack.pop()
            role_stack.pop()

    seed_indices = [
        instance.index
        for instance in instances
        if allow_bridge_seeds or not instance.is_bridge
    ]
    if not seed_indices:
        seed_indices = [instance.index for instance in instances]

    seed_indices.sort(
        key=lambda idx: (
            instances[idx].length + instances[idx].meta_bonus,
            instances[idx].length,
            instances[idx].word,
        ),
        reverse=True,
    )

    for seed_idx in seed_indices:
        seed = instances[seed_idx]
        seed_roles = instance_roles(seed)
        if not matches_pattern_prefix((seed_roles,)):
            stats["pruned_structure"] += 1
            continue
        stack[:] = [seed_idx]
        role_stack[:] = [seed_roles]
        word_counts.clear()
        word_counts[seed.word] = 1
        dfs(
            used_mask=seed.mask,
            base_score=seed.length + seed.meta_bonus,
            letters_used=seed.length,
            has_noun=("NOUN" in seed.tags),
            has_verb=("VERB" in seed.tags),
            content_words=0 if seed.is_bridge else 1,
            bridge_words=1 if seed.is_bridge else 0,
            has_mandatory=(seed.word == must_have_word),
        )

    ordered_results = [entry[2] for entry in sorted(heap, key=lambda item: item[0], reverse=True)]
    variant_counts = defaultdict(int)
    for result in ordered_results:
        variant_counts[result.text] += 1

    unique_results = []
    seen_texts = set()
    for result in ordered_results:
        if result.text in seen_texts:
            continue
        seen_texts.add(result.text)
        unique_results.append((result, variant_counts[result.text]))
        if len(unique_results) >= top_k:
            break

    return unique_results, stats


def print_candidate_summary(candidate_source, instances, instances_by_word, candidates, cols, col_labels, max_paths_per_word, show_bridge_matches):
    print(f"=== CANDIDATE SOURCE ===\n{candidate_source}")
    print()

    content_words = [word for word, meta in candidates.items() if not meta.is_bridge]
    bridge_words = [word for word, meta in candidates.items() if meta.is_bridge]

    found_content = [word for word in content_words if instances_by_word.get(word)]
    missing_content = [word for word in content_words if not instances_by_word.get(word)]

    print("=== CANDIDATE WORDS FOUND ===")
    if not found_content:
        print("No content words from the candidate list were found in the grid.")
    for word in sorted(found_content, key=lambda item: (-len(item), item)):
        meta = candidates[word]
        hits = instances_by_word[word]
        tag_text = "|".join(sorted(meta.tags)) if meta.tags else "-"
        print(f"\n{word} | instances={len(hits)} | weight={meta.manual_weight} | tags={tag_text}")
        for idx in hits[:max_paths_per_word]:
            coords = " -> ".join(path_to_coords(instances[idx].path, cols, col_labels))
            print(f"  {coords}")
        if len(hits) > max_paths_per_word:
            print(f"  ... {len(hits) - max_paths_per_word} more")

    print("\n=== CANDIDATE WORDS NOT FOUND ===")
    if missing_content:
        print(", ".join(sorted(missing_content)))
    else:
        print("All content candidates were found at least once.")

    if show_bridge_matches:
        found_bridge = [word for word in bridge_words if instances_by_word.get(word)]
        print("\n=== BRIDGE WORDS FOUND ===")
        if not found_bridge:
            print("No bridge words were found.")
        for word in sorted(found_bridge):
            hits = instances_by_word[word]
            print(f"{word} | instances={len(hits)}")


def print_search_results(results, stats, cols, col_labels, must_have_word):
    print("\n=== SEARCH STATS ===")
    print(f"states_visited={stats['states']}")
    print(f"bound_prunes={stats['pruned_bound']}")
    print(f"overlap_prunes={stats['pruned_overlap']}")
    print(f"structure_prunes={stats['pruned_structure']}")
    print(f"mandatory_prunes={stats['pruned_mandatory']}")
    print(f"must_have_word={must_have_word or 'None'}")
    for group_name, patterns in PATTERN_GROUPS.items():
        print(f"{group_name}_patterns={[' '.join(pattern) for pattern in patterns]}")

    print("\n=== TOP PHRASE CANDIDATES ===")
    if not results:
        print("No phrase candidates satisfied the current settings.")
        return

    for result, variant_count in results:
        print(f"\nTEXT: {result.text}")
        print(
            f"SCORE: {result.score} | letters={result.letters_used} | "
            f"content_words={result.content_words} | bridge_words={result.bridge_words} | "
            f"noun={result.has_noun} | verb={result.has_verb} | "
            f"path_variants_in_top_pool={variant_count}"
        )
        for word, path in zip(result.words, result.paths):
            coords = " -> ".join(path_to_coords(path, cols, col_labels))
            print(f"  {word}: {coords}")


def main():
    args = parse_args()
    if args.min_words < 1:
        raise SystemExit("--min-words must be at least 1")
    if args.max_words < args.min_words:
        raise SystemExit("--max-words must be >= --min-words")
    if args.top_k < 1:
        raise SystemExit("--top-k must be at least 1")
    must_have_word = normalize_optional_word(args.must_have)

    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = SCRIPT_DIR / output_path

    with output_path.open("w", encoding="utf-8") as handle:
        with redirect_stdout(handle):
            candidates, candidate_source = load_candidates(args.candidates)
            grid_info = load_grid(args.csv)
            instances, instances_by_word = find_word_instances(grid_info, candidates)
            print_candidate_summary(
                candidate_source=candidate_source,
                instances=instances,
                instances_by_word=instances_by_word,
                candidates=candidates,
                cols=grid_info["cols"],
                col_labels=grid_info["col_labels"],
                max_paths_per_word=args.max_paths_per_word,
                show_bridge_matches=args.show_bridge_matches,
            )

            if must_have_word and must_have_word not in candidates:
                print(f"\nMandatory word '{must_have_word}' is not in the current candidate vocabulary.")
                results = []
                stats = {"states": 0, "pruned_bound": 0, "pruned_overlap": 0, "pruned_structure": 0, "pruned_mandatory": 0}
            elif must_have_word and not instances_by_word.get(must_have_word):
                print(f"\nMandatory word '{must_have_word}' is in the candidate list but was not found in the grid.")
                results = []
                stats = {"states": 0, "pruned_bound": 0, "pruned_overlap": 0, "pruned_structure": 0, "pruned_mandatory": 0}
            else:
                next_indices = build_search_graph(instances, grid_info["neighbors"])
                results, stats = search_phrases(
                    instances=instances,
                    next_indices=next_indices,
                    alpha_cell_count=grid_info["alpha_cell_count"],
                    top_k=args.top_k,
                    min_words=args.min_words,
                    max_words=args.max_words,
                    allow_bridge_seeds=args.allow_bridge_seeds,
                    must_have_word=must_have_word,
                )
            print_search_results(results, stats, grid_info["cols"], grid_info["col_labels"], must_have_word)

    print(f"Saved output to {output_path}")


if __name__ == "__main__":
    main()
