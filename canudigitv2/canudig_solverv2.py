
from __future__ import annotations

import csv
import heapq
import itertools
import os
import re
import sys
import time
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

# =========================
# Configuration
# =========================

DEFAULT_GRID_CSV = "can u dig it.csv"
DEFAULT_WORDS_FILE = "candidate_words.txt"
OUTPUT_DIR = "canudig_output"

MAX_WORDS_IN_PHRASE = 6
MIN_WORDS_IN_PHRASE = 2
TOP_K_PHRASES = 300

WRITE_EXACT_BIGRAMS = True
WRITE_EXACT_TRIGRAMS = True

# Set these to an int if you want to cap output size while experimenting.
# Keep them as None for exact, untruncated output.
MAX_BIGRAM_ROWS = None
MAX_TRIGRAM_ROWS = None

# Exact search by default. If you want a safety stop while experimenting,
# set this to an int number of DFS states. Leave as None for exact top-K.
MAX_TOPK_DFS_STATES = None

PRINT_PROGRESS_EVERY = 100000

# =========================
# Editable candidate fallback
# =========================

DEFAULT_CANDIDATES = [
    "a", "an", "and", "answer", "at", "blank", "by", "column", "columns",
    "count", "decimal", "decimals", "digit", "digits", "dig", "down", "end",
    "find", "from", "get", "go", "grid", "hundred", "hundreds", "in",
    "integer", "integers", "is", "it", "left", "line", "move", "next",
    "nineteen", "of", "on", "or", "path", "positive", "read", "right",
    "row", "rows", "six", "start", "sum", "take", "the", "then", "to",
    "turn", "twenty", "up", "use", "word", "words", "zero", "one", "two",
    "three", "four", "five", "seven", "eight", "nine", "ten", "eleven",
    "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
    "eighteen", "ninety", "thirty", "forty", "fifty", "sixty", "seventy",
    "eighty", "thousand"
]

# =========================
# Scoring sets (edit freely)
# =========================

DETS = {"a", "an", "the", "this", "that", "these", "those"}
PREPS = {"in", "on", "at", "by", "to", "from", "under", "over", "into", "onto", "across", "through", "between"}
SEQ_WORDS = {"then", "next", "after", "before"}
DIRECTIONS = {"up", "down", "left", "right", "north", "south", "east", "west"}
IMPERATIVES = {"find", "count", "read", "take", "use", "move", "turn", "start", "get", "go", "dig", "add", "sum"}

CLUE_NOUNS = {
    "start", "end", "answer", "row", "rows", "column", "columns",
    "letter", "letters", "word", "words", "path", "line", "blank", "grid"
}

MATH_WORDS = {
    "integer", "integers", "digit", "digits", "decimal", "decimals",
    "hundred", "hundreds", "thousand", "positive", "negative", "sum", "total"
}

NUMBER_WORDS = {
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
    "seventeen", "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty",
    "sixty", "seventy", "eighty", "ninety"
}

FUNCTION_WORDS = DETS | PREPS | {"and", "or", "if", "is", "it", "of", "as", "for", "with"} | SEQ_WORDS | DIRECTIONS
VERBISH = IMPERATIVES | {"is", "are", "be", "was", "were", "has", "have", "had", "do", "does", "did"}
NOUNISH = CLUE_NOUNS | MATH_WORDS | NUMBER_WORDS

# =========================
# Data structures
# =========================

END = "_end_"

@dataclass(frozen=True)
class WordInstance:
    idx: int
    word: str
    path: Tuple[int, ...]
    mask: int
    start: int
    end: int
    word_score: int

# =========================
# Helpers
# =========================

def normalize_token(s: str) -> str:
    return re.sub(r"[^a-z]", "", s.lower())

def popcount(x: int) -> int:
    try:
        return x.bit_count()
    except AttributeError:
        return bin(x).count("1")

def excel_col(col_idx: int) -> str:
    col_idx += 1
    out = []
    while col_idx > 0:
        col_idx, rem = divmod(col_idx - 1, 26)
        out.append(chr(ord("A") + rem))
    return "".join(reversed(out))

def load_grid(csv_path: Path) -> Tuple[List[List[str]], int, int]:
    with csv_path.open(newline="", encoding="utf-8") as f:
        grid = [[cell.strip() for cell in row] for row in csv.reader(f)]
    if not grid:
        raise ValueError("Grid CSV is empty.")
    widths = {len(row) for row in grid}
    if len(widths) != 1:
        raise ValueError(f"Grid CSV is not rectangular. Row widths found: {sorted(widths)}")
    return grid, len(grid), len(grid[0])

def flatten_grid(grid: List[List[str]]) -> List[str]:
    return [cell.lower() for row in grid for cell in row]

def cell_id(r: int, c: int, cols: int) -> int:
    return r * cols + c

def rc(cell: int, cols: int) -> Tuple[int, int]:
    return divmod(cell, cols)

def coord(cell: int, cols: int) -> str:
    r, c = rc(cell, cols)
    return f"{excel_col(c)}{r + 1}"

def path_to_coord_string(path: Iterable[int], cols: int) -> str:
    return " -> ".join(coord(cell, cols) for cell in path)

def path_to_mask(path: Iterable[int]) -> int:
    m = 0
    for cell in path:
        m |= 1 << cell
    return m

def build_neighbors(rows: int, cols: int) -> List[List[int]]:
    n = rows * cols
    neighbors: List[List[int]] = [[] for _ in range(n)]
    for r in range(rows):
        for c in range(cols):
            here = cell_id(r, c, cols)
            for rr in range(max(0, r - 1), min(rows, r + 2)):
                for cc in range(max(0, c - 1), min(cols, c + 2)):
                    if rr == r and cc == c:
                        continue
                    neighbors[here].append(cell_id(rr, cc, cols))
    return neighbors

def load_candidate_words(words_path: Path) -> List[str]:
    words: List[str] = []
    if words_path.exists():
        with words_path.open(encoding="utf-8") as f:
            for raw_line in f:
                line = raw_line.split("#", 1)[0].strip()
                if not line:
                    continue
                token = normalize_token(line)
                if token:
                    words.append(token)
    else:
        words = [normalize_token(w) for w in DEFAULT_CANDIDATES]
    words = sorted(set(w for w in words if w), key=lambda w: (len(w), w))
    return words

def build_trie(words: Iterable[str]) -> Dict[str, dict]:
    root: Dict[str, dict] = {}
    for word in words:
        node = root
        for ch in word:
            node = node.setdefault(ch, {})
        node.setdefault(END, []).append(word)
    return root

# =========================
# Scoring
# =========================

def word_prior(word: str) -> int:
    score = 0
    if word in CLUE_NOUNS:
        score += 6
    if word in MATH_WORDS:
        score += 6
    if word in NUMBER_WORDS:
        score += 6
    if word in IMPERATIVES:
        score += 5
    if word in DIRECTIONS:
        score += 4
    if word in FUNCTION_WORDS or word in SEQ_WORDS:
        score += 1
    return score

def link_bonus(a: str, b: str) -> int:
    score = 0
    if a in IMPERATIVES and (b in DETS or b in DIRECTIONS):
        score += 4              # find the, get up, move left
    if a in DETS and (b in CLUE_NOUNS or b in MATH_WORDS or b in NUMBER_WORDS):
        score += 3              # the start, the answer
    if a in NUMBER_WORDS and (b in NUMBER_WORDS or b in MATH_WORDS or b in {"hundred", "hundreds"}):
        score += 4              # nineteen hundred, twenty six, three digits
    if a in SEQ_WORDS and b in IMPERATIVES:
        score += 3              # then get, next move
    if a in PREPS and (b in DETS or b in CLUE_NOUNS or b in NUMBER_WORDS):
        score += 2              # under the, in rows
    return score

def initial_phrase_score(first_word: str) -> int:
    score = word_prior(first_word)
    if first_word in IMPERATIVES:
        score += 4
    return score

def extension_gain(prev_word: str, next_word: str) -> int:
    return word_prior(next_word) + link_bonus(prev_word, next_word) + 1  # slight reward for longer phrases

def has_verbish(words: Iterable[str]) -> bool:
    for w in words:
        if w in VERBISH or w.endswith("ing") or w.endswith("ed"):
            return True
    return False

def has_nounish(words: Iterable[str]) -> bool:
    for w in words:
        if w in NOUNISH:
            return True
    return False

# =========================
# Exact word-instance search
# =========================

def find_word_instances(
    letters: List[str],
    neighbors: List[List[int]],
    trie: Dict[str, dict]
) -> Tuple[List[WordInstance], Dict[str, List[int]]]:
    instances: List[WordInstance] = []
    by_word: Dict[str, List[int]] = defaultdict(list)

    if not trie:
        return instances, by_word

    valid_start_letters = set(trie.keys())

    sys.setrecursionlimit(10000)

    def dfs(cell: int, node: Dict[str, dict], used_mask: int, path: List[int]) -> None:
        ch = letters[cell]
        nxt = node.get(ch)
        if nxt is None:
            return

        path.append(cell)
        used_mask |= 1 << cell

        for word in nxt.get(END, ()):
            idx = len(instances)
            path_tuple = tuple(path)
            inst = WordInstance(
                idx=idx,
                word=word,
                path=path_tuple,
                mask=used_mask,
                start=path_tuple[0],
                end=path_tuple[-1],
                word_score=word_prior(word),
            )
            instances.append(inst)
            by_word[word].append(idx)

        for nb in neighbors[cell]:
            if not ((used_mask >> nb) & 1):
                dfs(nb, nxt, used_mask, path)

        path.pop()

    for start in range(len(letters)):
        if letters[start] in valid_start_letters:
            dfs(start, trie, 0, [])

    return instances, by_word

# =========================
# Exact transition graph
# =========================

def build_transition_graph(
    instances: List[WordInstance],
    neighbors: List[List[int]]
) -> Tuple[List[List[Tuple[int, int]]], int]:
    starts_at: Dict[int, List[int]] = defaultdict(list)
    for inst in instances:
        starts_at[inst.start].append(inst.idx)

    out_edges: List[List[Tuple[int, int]]] = [[] for _ in instances]
    edge_count = 0

    for inst in instances:
        candidates: List[Tuple[int, int]] = []
        for start_cell in neighbors[inst.end]:
            for nxt_id in starts_at.get(start_cell, []):
                nxt = instances[nxt_id]
                if inst.mask & nxt.mask:
                    continue
                gain = extension_gain(inst.word, nxt.word)
                candidates.append((nxt_id, gain))
        # Sort likely-good extensions first, to tighten top-K cutoff earlier
        candidates.sort(key=lambda pair: (pair[1], instances[pair[0]].word_score, len(instances[pair[0]].word)), reverse=True)
        out_edges[inst.idx] = candidates
        edge_count += len(candidates)

    return out_edges, edge_count

def compute_additional_score_upper_bounds(
    instances: List[WordInstance],
    out_edges: List[List[Tuple[int, int]]],
    max_extra_words: int
) -> List[List[int]]:
    """
    ub[i][s] = optimistic max ADDITIONAL score obtainable by extending instance i
               with up to s more words, ignoring future mask conflicts.
    This makes pruning exact: it can only overestimate, never underestimate.
    """
    n = len(instances)
    ub = [[0] * (max_extra_words + 1) for _ in range(n)]

    for steps in range(1, max_extra_words + 1):
        for i in range(n):
            best = 0
            for nxt_id, gain in out_edges[i]:
                candidate = gain + ub[nxt_id][steps - 1]
                if candidate > best:
                    best = candidate
            ub[i][steps] = best

    return ub

# =========================
# Reports
# =========================

def ensure_output_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)

def write_found_word_reports(
    output_dir: Path,
    instances: List[WordInstance],
    by_word: Dict[str, List[int]],
    cols: int
) -> None:
    csv_path = output_dir / "found_word_instances.csv"
    txt_path = output_dir / "found_words_grouped.txt"

    # CSV: one row per instance
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "length", "instance_id", "start", "end", "path"])
        for inst in sorted(instances, key=lambda x: (-len(x.word), x.word, x.idx)):
            writer.writerow([
                inst.word,
                len(inst.word),
                inst.idx,
                coord(inst.start, cols),
                coord(inst.end, cols),
                path_to_coord_string(inst.path, cols),
            ])

    # TXT: grouped by word
    with txt_path.open("w", encoding="utf-8") as f:
        sorted_words = sorted(by_word.keys(), key=lambda w: (-len(w), w))
        f.write(f"Unique words found: {len(sorted_words)}\n")
        f.write(f"Total word instances: {len(instances)}\n\n")
        for word in sorted_words:
            ids = by_word[word]
            f.write(f"{word} | length={len(word)} | total_instances={len(ids)}\n")
            for inst_id in ids:
                inst = instances[inst_id]
                f.write(f"  [{inst.idx}] {path_to_coord_string(inst.path, cols)}\n")
            f.write("\n")

def phrase_to_row(
    instances: List[WordInstance],
    phrase_ids: Tuple[int, ...],
    score: int,
    cols: int,
    max_slots: int
) -> Dict[str, str]:
    words = [instances[i].word for i in phrase_ids]
    cell_count = sum(len(instances[i].path) for i in phrase_ids)

    row: Dict[str, str] = {
        "score": str(score),
        "word_count": str(len(phrase_ids)),
        "cell_count": str(cell_count),
        "has_verbish": str(has_verbish(words)),
        "has_nounish": str(has_nounish(words)),
        "phrase": " ".join(words),
    }

    for slot in range(max_slots):
        key_idx = slot + 1
        if slot < len(phrase_ids):
            inst = instances[phrase_ids[slot]]
            row[f"word{key_idx}"] = inst.word
            row[f"path{key_idx}"] = path_to_coord_string(inst.path, cols)
            row[f"start{key_idx}"] = coord(inst.start, cols)
            row[f"end{key_idx}"] = coord(inst.end, cols)
            row[f"instance_id{key_idx}"] = str(inst.idx)
        else:
            row[f"word{key_idx}"] = ""
            row[f"path{key_idx}"] = ""
            row[f"start{key_idx}"] = ""
            row[f"end{key_idx}"] = ""
            row[f"instance_id{key_idx}"] = ""

    return row

def write_rows_to_csv(path: Path, rows: Iterable[Dict[str, str]], max_slots: int) -> int:
    header = ["score", "word_count", "cell_count", "has_verbish", "has_nounish", "phrase"]
    for i in range(1, max_slots + 1):
        header.extend([f"word{i}", f"instance_id{i}", f"start{i}", f"end{i}", f"path{i}"])

    count = 0
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
            count += 1
    return count

def write_bigram_csv(
    output_dir: Path,
    instances: List[WordInstance],
    out_edges: List[List[Tuple[int, int]]],
    cols: int,
    row_limit: int | None = None
) -> int:
    path = output_dir / "exact_bigrams.csv"

    def row_iter() -> Iterable[Dict[str, str]]:
        written = 0
        for inst in instances:
            base_score = initial_phrase_score(inst.word)
            for nxt_id, gain in out_edges[inst.idx]:
                score = base_score + gain
                yield phrase_to_row(instances, (inst.idx, nxt_id), score, cols, 2)
                written += 1
                if row_limit is not None and written >= row_limit:
                    return

    return write_rows_to_csv(path, row_iter(), 2)

def write_trigram_csv(
    output_dir: Path,
    instances: List[WordInstance],
    out_edges: List[List[Tuple[int, int]]],
    cols: int,
    row_limit: int | None = None
) -> int:
    path = output_dir / "exact_trigrams.csv"

    def row_iter() -> Iterable[Dict[str, str]]:
        written = 0
        for inst1 in instances:
            base_score = initial_phrase_score(inst1.word)
            used12 = inst1.mask
            for inst2_id, gain12 in out_edges[inst1.idx]:
                inst2 = instances[inst2_id]
                if used12 & inst2.mask:
                    continue
                used123 = used12 | inst2.mask
                score12 = base_score + gain12
                for inst3_id, gain23 in out_edges[inst2_id]:
                    inst3 = instances[inst3_id]
                    if used123 & inst3.mask:
                        continue
                    score123 = score12 + gain23
                    yield phrase_to_row(instances, (inst1.idx, inst2_id, inst3_id), score123, cols, 3)
                    written += 1
                    if row_limit is not None and written >= row_limit:
                        return

    return write_rows_to_csv(path, row_iter(), 3)

def write_top_phrase_reports(
    output_dir: Path,
    instances: List[WordInstance],
    top_results: List[Tuple[int, Tuple[int, ...]]],
    cols: int,
    max_slots: int
) -> None:
    csv_path = output_dir / "top_phrases.csv"
    txt_path = output_dir / "top_phrases.txt"

    rows = [
        phrase_to_row(instances, phrase_ids, score, cols, max_slots)
        for score, phrase_ids in top_results
    ]
    write_rows_to_csv(csv_path, rows, max_slots)

    with txt_path.open("w", encoding="utf-8") as f:
        for rank, (score, phrase_ids) in enumerate(top_results, start=1):
            words = [instances[i].word for i in phrase_ids]
            f.write(f"#{rank} | score={score} | phrase={' '.join(words)}\n")
            for slot, inst_id in enumerate(phrase_ids, start=1):
                inst = instances[inst_id]
                f.write(f"  word{slot}: {inst.word}\n")
                f.write(f"  path{slot}: {path_to_coord_string(inst.path, cols)}\n")
            f.write("\n")

# =========================
# Exact top-K phrase search
# =========================

def exact_top_k_phrases(
    instances: List[WordInstance],
    out_edges: List[List[Tuple[int, int]]],
    ub: List[List[int]],
    max_words: int,
    min_words: int,
    top_k: int,
) -> Tuple[List[Tuple[int, Tuple[int, ...]]], int]:
    if top_k <= 0 or not instances:
        return [], 0

    heap: List[Tuple[int, int, Tuple[int, ...]]] = []
    serial = itertools.count()
    threshold_score = float("-inf")
    explored_states = 0

    def maybe_add_result(score: int, phrase_ids: Tuple[int, ...]) -> None:
        nonlocal threshold_score
        item = (score, next(serial), phrase_ids)
        if len(heap) < top_k:
            heapq.heappush(heap, item)
        else:
            if score > heap[0][0]:
                heapq.heapreplace(heap, item)
        if len(heap) == top_k:
            threshold_score = heap[0][0]

    seed_order = sorted(
        range(len(instances)),
        key=lambda idx: initial_phrase_score(instances[idx].word) + ub[idx][max_words - 1],
        reverse=True,
    )

    def dfs(last_id: int, used_mask: int, score: int, path_ids: List[int]) -> None:
        nonlocal explored_states

        explored_states += 1
        if PRINT_PROGRESS_EVERY and explored_states % PRINT_PROGRESS_EVERY == 0:
            print(f"[top-k] explored {explored_states:,} states; current cutoff score={threshold_score}")

        if MAX_TOPK_DFS_STATES is not None and explored_states > MAX_TOPK_DFS_STATES:
            raise RuntimeError(
                f"Stopped after {MAX_TOPK_DFS_STATES:,} DFS states. "
                "Set MAX_TOPK_DFS_STATES=None for exact search."
            )

        depth = len(path_ids)

        if depth >= min_words:
            maybe_add_result(score, tuple(path_ids))

        if depth >= max_words:
            return

        remaining = max_words - depth
        optimistic = score + ub[last_id][remaining]
        if len(heap) == top_k and optimistic <= threshold_score:
            return

        for nxt_id, gain in out_edges[last_id]:
            nxt = instances[nxt_id]
            if used_mask & nxt.mask:
                continue

            new_score = score + gain
            child_optimistic = new_score + ub[nxt_id][remaining - 1]
            if len(heap) == top_k and child_optimistic <= threshold_score:
                continue

            path_ids.append(nxt_id)
            dfs(nxt_id, used_mask | nxt.mask, new_score, path_ids)
            path_ids.pop()

    for seed_id in seed_order:
        seed = instances[seed_id]
        seed_score = initial_phrase_score(seed.word)
        seed_optimistic = seed_score + ub[seed_id][max_words - 1]
        if len(heap) == top_k and seed_optimistic <= threshold_score:
            break
        dfs(seed_id, seed.mask, seed_score, [seed_id])

    results = [(score, phrase_ids) for score, _, phrase_ids in heap]
    results.sort(
        key=lambda item: (
            -item[0],
            -len(item[1]),
            " ".join(instances[i].word for i in item[1]),
            item[1],
        )
    )
    return results, explored_states

# =========================
# Main
# =========================

def main() -> None:
    t0 = time.perf_counter()

    grid_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(DEFAULT_GRID_CSV)
    words_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(DEFAULT_WORDS_FILE)
    output_dir = Path(OUTPUT_DIR)

    if not grid_path.exists():
        raise FileNotFoundError(f"Grid CSV not found: {grid_path}")

    ensure_output_dir(output_dir)

    grid, rows, cols = load_grid(grid_path)
    letters = flatten_grid(grid)
    neighbors = build_neighbors(rows, cols)

    candidates = load_candidate_words(words_path)
    if not candidates:
        raise ValueError("No candidate words were loaded.")

    print(f"Grid: {rows} rows x {cols} cols ({rows * cols} cells)")
    print(f"Candidate words loaded: {len(candidates)}")
    print(f"Grid file: {grid_path}")
    print(f"Words file: {words_path if words_path.exists() else '(using DEFAULT_CANDIDATES in script)'}")
    print(f"Output dir: {output_dir}")

    t1 = time.perf_counter()
    trie = build_trie(candidates)
    instances, by_word = find_word_instances(letters, neighbors, trie)
    t2 = time.perf_counter()

    found_unique_words = len(by_word)
    print(f"Found {len(instances):,} exact word instances across {found_unique_words:,} unique candidate words in {t2 - t1:.2f}s")

    write_found_word_reports(output_dir, instances, by_word, cols)
    print(f"Wrote: {output_dir / 'found_word_instances.csv'}")
    print(f"Wrote: {output_dir / 'found_words_grouped.txt'}")

    if not instances:
        print("No candidate words were found on the grid. Done.")
        return

    t3 = time.perf_counter()
    out_edges, edge_count = build_transition_graph(instances, neighbors)
    t4 = time.perf_counter()
    print(f"Built exact transition graph with {edge_count:,} legal 2-word continuations in {t4 - t3:.2f}s")

    if WRITE_EXACT_BIGRAMS:
        t_big = time.perf_counter()
        bigram_rows = write_bigram_csv(output_dir, instances, out_edges, cols, MAX_BIGRAM_ROWS)
        print(f"Wrote: {output_dir / 'exact_bigrams.csv'} ({bigram_rows:,} rows) in {time.perf_counter() - t_big:.2f}s")

    if WRITE_EXACT_TRIGRAMS:
        t_tri = time.perf_counter()
        trigram_rows = write_trigram_csv(output_dir, instances, out_edges, cols, MAX_TRIGRAM_ROWS)
        print(f"Wrote: {output_dir / 'exact_trigrams.csv'} ({trigram_rows:,} rows) in {time.perf_counter() - t_tri:.2f}s")

    if TOP_K_PHRASES > 0 and MAX_WORDS_IN_PHRASE >= MIN_WORDS_IN_PHRASE:
        t5 = time.perf_counter()
        ub = compute_additional_score_upper_bounds(instances, out_edges, MAX_WORDS_IN_PHRASE - 1)
        top_results, explored = exact_top_k_phrases(
            instances=instances,
            out_edges=out_edges,
            ub=ub,
            max_words=MAX_WORDS_IN_PHRASE,
            min_words=MIN_WORDS_IN_PHRASE,
            top_k=TOP_K_PHRASES,
        )
        t6 = time.perf_counter()
        write_top_phrase_reports(output_dir, instances, top_results, cols, MAX_WORDS_IN_PHRASE)
        print(f"Top-K search explored {explored:,} DFS states in {t6 - t5:.2f}s")
        print(f"Wrote: {output_dir / 'top_phrases.csv'}")
        print(f"Wrote: {output_dir / 'top_phrases.txt'}")
    else:
        print("Skipping top-K phrase search because TOP_K_PHRASES <= 0 or MAX/MIN word settings are invalid.")

    print(f"Done in {time.perf_counter() - t0:.2f}s")

if __name__ == "__main__":
    main()
