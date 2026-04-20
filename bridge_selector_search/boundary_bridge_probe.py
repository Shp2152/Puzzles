from __future__ import annotations

import argparse
import csv
import json
from dataclasses import dataclass
from pathlib import Path


DIRS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]

EXTRA_WORDS = {
    "baseten",
    "hexadecimal",
    "binary",
    "decimal",
    "ones",
    "tens",
    "hundred",
    "hundreds",
    "integer",
    "start",
    "step",
    "total",
    "find",
    "into",
    "three",
    "nine",
    "get",
    "add",
    "base",
    "the",
    "go",
    "six",
    "by",
    "to",
    "from",
    "as",
    "or",
}


@dataclass(frozen=True)
class WordInstance:
    word: str
    path: tuple[int, ...]

    @property
    def start(self) -> int:
        return self.path[0]

    @property
    def end(self) -> int:
        return self.path[-1]

    @property
    def mask(self) -> int:
        out = 0
        for cell in self.path:
            out |= 1 << cell
        return out


@dataclass(frozen=True)
class PhraseInstance:
    phrase: tuple[WordInstance, ...]

    @property
    def words(self) -> list[str]:
        return [item.word for item in self.phrase]

    @property
    def text(self) -> str:
        return " ".join(self.words)

    @property
    def first(self) -> WordInstance:
        return self.phrase[0]

    @property
    def last(self) -> WordInstance:
        return self.phrase[-1]

    @property
    def mask(self) -> int:
        out = 0
        for item in self.phrase:
            out |= item.mask
        return out


def load_grid(csv_path: Path) -> tuple[list[list[str]], int, int]:
    with csv_path.open(newline="", encoding="utf-8") as handle:
        grid = [[cell.strip().lower() for cell in row] for row in csv.reader(handle)]
    if not grid:
        raise ValueError("grid is empty")
    widths = {len(row) for row in grid}
    if len(widths) != 1:
        raise ValueError(f"grid is not rectangular: {sorted(widths)}")
    return grid, len(grid), len(grid[0])


def flatten(grid: list[list[str]]) -> list[str]:
    return [cell for row in grid for cell in row]


def excel_col(col_idx: int) -> str:
    col_idx += 1
    letters: list[str] = []
    while col_idx:
        col_idx, rem = divmod(col_idx - 1, 26)
        letters.append(chr(ord("A") + rem))
    return "".join(reversed(letters))


def coord(cell: int, cols: int) -> str:
    row, col = divmod(cell, cols)
    return f"{excel_col(col)}{row + 1}"


def build_neighbors(rows: int, cols: int) -> list[list[int]]:
    neighbors: list[list[int]] = [[] for _ in range(rows * cols)]
    for r in range(rows):
        for c in range(cols):
            here = r * cols + c
            for dr, dc in DIRS:
                rr = r + dr
                cc = c + dc
                if 0 <= rr < rows and 0 <= cc < cols:
                    neighbors[here].append(rr * cols + cc)
    return neighbors


def load_dictionary(dictionary_path: Path, min_len: int, max_len: int) -> set[str]:
    words: set[str] = set()
    with dictionary_path.open(encoding="utf-8") as handle:
        for raw in handle:
            raw_word = raw.strip()
            if raw_word != raw_word.lower():
                continue
            word = raw_word.lower()
            if not word.isalpha():
                continue
            if not (min_len <= len(word) <= max_len):
                continue
            words.add(word)
    words.update(word for word in EXTRA_WORDS if 2 <= len(word) <= max_len)
    return words


def build_trie(words: set[str]) -> dict:
    root: dict = {}
    for word in words:
        node = root
        for ch in word:
            node = node.setdefault(ch, {})
        node["$"] = word
    return root


def enumerate_words(
    letters: list[str],
    neighbors: list[list[int]],
    trie: dict,
    max_len: int,
) -> dict[str, list[WordInstance]]:
    found: dict[tuple[str, tuple[int, ...]], WordInstance] = {}
    path: list[int] = []

    def dfs(cell: int, node: dict, used: int) -> None:
        ch = letters[cell]
        if ch not in node:
            return
        next_node = node[ch]
        used |= 1 << cell
        path.append(cell)
        word = next_node.get("$")
        if word is not None:
            inst = WordInstance(word, tuple(path))
            found[(word, inst.path)] = inst
        if len(path) < max_len:
            for nxt in neighbors[cell]:
                if used & (1 << nxt):
                    continue
                dfs(nxt, next_node, used)
        path.pop()

    for cell in range(len(letters)):
        dfs(cell, trie, 0)

    by_word: dict[str, list[WordInstance]] = {}
    for (_, _), inst in found.items():
        by_word.setdefault(inst.word, []).append(inst)
    for word in by_word:
        by_word[word].sort(key=lambda inst: inst.path)
    return by_word


def find_phrase_instances(by_word: dict[str, list[WordInstance]], neighbors: list[list[int]], words: list[str]) -> list[PhraseInstance]:
    word_lists = []
    for word in words:
        matches = by_word.get(word.lower(), [])
        if not matches:
            return []
        word_lists.append(matches)

    out: list[PhraseInstance] = []

    def rec(i: int, used: int, prev_end: int | None, chosen: list[WordInstance]) -> None:
        if i == len(word_lists):
            out.append(PhraseInstance(tuple(chosen)))
            return
        for inst in word_lists[i]:
            if used & inst.mask:
                continue
            if prev_end is not None and inst.start not in neighbors[prev_end]:
                continue
            chosen.append(inst)
            rec(i + 1, used | inst.mask, inst.end, chosen)
            chosen.pop()

    rec(0, 0, None, [])
    return out


def render_inst(inst: WordInstance, cols: int) -> dict:
    return {
        "word": inst.word,
        "path_cells": list(inst.path),
        "coords": [coord(cell, cols) for cell in inst.path],
    }


def render_phrase(inst: PhraseInstance, cols: int) -> dict:
    return {
        "phrase": inst.text,
        "words": inst.words,
        "path_cells": [list(word.path) for word in inst.phrase],
        "coord_paths": [[coord(cell, cols) for cell in word.path] for word in inst.phrase],
    }


def expand_before(
    base: PhraseInstance,
    by_word: dict[str, list[WordInstance]],
    neighbors: list[list[int]],
    max_extra_words: int,
) -> list[PhraseInstance]:
    out: list[PhraseInstance] = []
    vocab = sorted(by_word)

    def rec(current_phrase: list[WordInstance], used: int, first_start: int, depth: int) -> None:
        if depth > 0:
            out.append(PhraseInstance(tuple(current_phrase + list(base.phrase))))
        if depth == max_extra_words:
            return
        for word in vocab:
            for inst in by_word[word]:
                if used & inst.mask:
                    continue
                if first_start not in neighbors[inst.end]:
                    continue
                current_phrase.insert(0, inst)
                rec(current_phrase, used | inst.mask, inst.start, depth + 1)
                current_phrase.pop(0)

    rec([], base.mask, base.first.start, 0)
    return out


def expand_after(
    base: PhraseInstance,
    by_word: dict[str, list[WordInstance]],
    neighbors: list[list[int]],
    max_extra_words: int,
) -> list[PhraseInstance]:
    out: list[PhraseInstance] = []
    vocab = sorted(by_word)

    def rec(current_phrase: list[WordInstance], used: int, prev_end: int, depth: int) -> None:
        if depth > 0:
            out.append(PhraseInstance(tuple(list(base.phrase) + current_phrase)))
        if depth == max_extra_words:
            return
        for word in vocab:
            for inst in by_word[word]:
                if used & inst.mask:
                    continue
                if inst.start not in neighbors[prev_end]:
                    continue
                current_phrase.append(inst)
                rec(current_phrase, used | inst.mask, inst.end, depth + 1)
                current_phrase.pop()

    rec([], base.mask, base.last.end, 0)
    return out


def unique_phrases(instances: list[PhraseInstance]) -> list[PhraseInstance]:
    seen: set[tuple[tuple[int, ...], ...]] = set()
    out: list[PhraseInstance] = []
    for inst in instances:
        key = tuple(word.path for word in inst.phrase)
        if key in seen:
            continue
        seen.add(key)
        out.append(inst)
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("grid", type=Path)
    parser.add_argument("mode", choices=["words", "phrase", "expand"])
    parser.add_argument("tokens", nargs="*")
    parser.add_argument("--dictionary", type=Path, default=Path("/usr/share/dict/words"))
    parser.add_argument("--min-len", type=int, default=3)
    parser.add_argument("--max-len", type=int, default=12)
    parser.add_argument("--max-extra-words", type=int, default=4)
    args = parser.parse_args()

    grid, rows, cols = load_grid(args.grid)
    letters = flatten(grid)
    neighbors = build_neighbors(rows, cols)
    words = load_dictionary(args.dictionary, args.min_len, args.max_len)
    trie = build_trie(words)
    by_word = enumerate_words(letters, neighbors, trie, args.max_len)

    if args.mode == "words":
        payload = []
        for word in sorted(by_word):
            payload.append(
                {
                    "word": word,
                    "count": len(by_word[word]),
                    "matches": [render_inst(inst, cols) for inst in by_word[word]],
                }
            )
        print(json.dumps(payload, indent=2))
        return 0

    if not args.tokens:
        raise SystemExit("phrase and expand modes need phrase tokens")

    phrase_instances = find_phrase_instances(by_word, neighbors, [token.lower() for token in args.tokens])

    if args.mode == "phrase":
        print(json.dumps([render_phrase(inst, cols) for inst in phrase_instances], indent=2))
        return 0

    payload = []
    for base in phrase_instances:
        before = unique_phrases(expand_before(base, by_word, neighbors, args.max_extra_words))
        after = unique_phrases(expand_after(base, by_word, neighbors, args.max_extra_words))
        payload.append(
            {
                "base": render_phrase(base, cols),
                "before_expansions": [render_phrase(inst, cols) for inst in before],
                "after_expansions": [render_phrase(inst, cols) for inst in after],
            }
        )
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
