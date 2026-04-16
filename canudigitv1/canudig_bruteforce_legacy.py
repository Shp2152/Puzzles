import csv
import string
from collections import defaultdict
import cmudict

CSV_PATH = r"C:\Users\nancy\OneDrive\Desktop\Puzzles\can u dig it.csv"

# ---------- load grid ----------
with open(CSV_PATH, newline="", encoding="utf-8") as f:
    grid = [row for row in csv.reader(f)]

R = len(grid)
C = len(grid[0])
COLS = string.ascii_uppercase[:C]


def coord(r, c):
    return f"{COLS[c]}{r+1}"


def path_to_coords(path):
    return [coord(r, c) for r, c in path]


# ---------- adjacency ----------
DIRS = [(-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)]

neighbors = {}
for r in range(R):
    for c in range(C):
        nbrs = []
        for dr, dc in DIRS:
            rr, cc = r + dr, c + dc
            if 0 <= rr < R and 0 <= cc < C:
                nbrs.append((rr, cc))
        neighbors[(r, c)] = nbrs

# ---------- dictionary ----------
raw_words = set(w.lower() for w in cmudict.dict().keys())

# keep alphabetic words only; drop apostrophes etc.
WORDS = set()
for w in raw_words:
    w2 = w.replace("'", "")
    if w2.isalpha() and len(w2) >= 3:
        WORDS.add(w2)

PREFIXES = set()
for w in WORDS:
    for i in range(1, len(w) + 1):
        PREFIXES.add(w[:i])

# ---------- find all word paths ----------
# stores word -> list of paths
word_paths = defaultdict(list)


def dfs_word(r, c, used, current, path, max_len=20):
    ch = grid[r][c].lower()
    current += ch
    path = path + [(r, c)]
    used = used | {(r, c)}

    if current not in PREFIXES:
        return

    if current in WORDS:
        word_paths[current].append(path)

    if len(current) >= max_len:
        return

    for rr, cc in neighbors[(r, c)]:
        if (rr, cc) not in used:
            dfs_word(rr, cc, used, current, path, max_len=max_len)


for r in range(R):
    for c in range(C):
        cell = grid[r][c]
        if cell.isalpha():
            dfs_word(r, c, set(), "", [], max_len=20)

# ---------- display words ----------
all_found = sorted(word_paths.items(), key=lambda kv: (-len(kv[0]), kv[0]))

print("=== LONGEST WORDS FOUND ===")
for word, paths in all_found[:500]:
    p = paths[0]
    print(f"{word} | length={len(word)} | path={' -> '.join(path_to_coords(p))} | total_paths={len(paths)}")

# ---------- heuristic POS ----------
COMMON_VERBS = {
    "is", "are", "was", "were", "be", "by", "been", "being",
    "do", "does", "did", "have", "has", "had",
    "find", "spray", "get", "start", "tune", "open", "point",
}
COMMON_NOUNS = {
    "start", "integer", "integers", "decimals", "hundreds", "nineteen", "end", "aluminum", "hexadecimal",
    "spray", "point", "six",
}


def guess_pos(word):
    tags = set()
    if word in COMMON_VERBS:
        tags.add("VERB")
    if word in COMMON_NOUNS:
        tags.add("NOUN")

    if word.endswith("ing") or word.endswith("ed"):
        tags.add("VERB")
    if word.endswith("tion") or word.endswith("ment") or word.endswith("ness") or word.endswith("ity"):
        tags.add("NOUN")
    if word.endswith("er") or word.endswith("or"):
        tags.add("NOUN")

    return tags


# ---------- chain words into phrases ----------
starts_by_letter = defaultdict(list)
for word, paths in word_paths.items():
    for p in paths:
        starts_by_letter[(word[0], p[0])].append((word, p))

all_word_instances = []
for word, paths in word_paths.items():
    for p in paths:
        all_word_instances.append((word, p))

instances_by_start = defaultdict(list)
for word, p in all_word_instances:
    instances_by_start[p[0]].append((word, p))


def chainable(prev_path, next_path, used_cells):
    if next_path[0] not in neighbors[prev_path[-1]]:
        return False
    if any(cell in used_cells for cell in next_path):
        return False
    return True


phrase_results = []


def dfs_phrase(words_so_far, paths_so_far, used_cells, max_words=6):
    if len(words_so_far) >= 2:
        text = " ".join(words_so_far)
        coords = []
        for p in paths_so_far:
            coords.extend(path_to_coords(p))
        pos_tags = set()
        for w in words_so_far:
            pos_tags |= guess_pos(w)
        phrase_results.append({
            "text": text,
            "words": list(words_so_far),
            "paths": [list(p) for p in paths_so_far],
            "coord_seq": coords,
            "letters_used": sum(len(p) for p in paths_so_far),
            "has_noun": "NOUN" in pos_tags,
            "has_verb": "VERB" in pos_tags
        })

    if len(words_so_far) >= max_words:
        return

    last_path = paths_so_far[-1]
    last_end = last_path[-1]
    cand_starts = neighbors[last_end]
    for s in cand_starts:
        for next_word, next_path in instances_by_start[s]:
            if chainable(last_path, next_path, used_cells):
                dfs_phrase(
                    words_so_far + [next_word],
                    paths_so_far + [next_path],
                    used_cells | set(next_path),
                    max_words=max_words
                )


seed_instances = []
for word, paths in word_paths.items():
    if len(word) >= 4:
        for p in paths:
            seed_instances.append((word, p))

for word, p in seed_instances:
    dfs_phrase([word], [p], set(p), max_words=6)

# ---------- report 1: longest unbroken paths ----------
longest_phrases = sorted(
    phrase_results,
    key=lambda x: (-x["letters_used"], -len(x["words"]), x["text"])
)

print("\n=== LONGEST UNBROKEN PATHS OF WORDS ===")
for item in longest_phrases[:100]:
    print(f"\nTEXT: {item['text']}")
    print(f"LETTERS USED: {item['letters_used']}")
    for w, p in zip(item["words"], item["paths"]):
        print(f"  WORD: {w}")
        print(f"  PATH: {' -> '.join(path_to_coords(p))}")

# ---------- report 2: noun+verb phrases ----------
nv_phrases = [x for x in phrase_results if x["has_noun"] and x["has_verb"]]
nv_phrases = sorted(
    nv_phrases,
    key=lambda x: (-x["letters_used"], -len(x["words"]), x["text"])
)

print("\n=== PHRASES WITH AT LEAST ONE NOUN AND ONE VERB ===")
for item in nv_phrases[:100]:
    print(f"\nTEXT: {item['text']}")
    print(f"LETTERS USED: {item['letters_used']}")
    for w, p in zip(item["words"], item["paths"]):
        print(f"  WORD: {w}")
        print(f"  PATH: {' -> '.join(path_to_coords(p))}")
