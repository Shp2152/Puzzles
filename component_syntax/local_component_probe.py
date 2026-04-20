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
    words: tuple[WordInstance, ...]

    @property
    def text(self) -> str:
        return " ".join(word.word for word in self.words)

    @property
    def mask(self) -> int:
        out = 0
        for word in self.words:
            out |= word.mask
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


def find_word_instances(letters: list[str], neighbors: list[list[int]], word: str) -> list[WordInstance]:
    word = word.lower()
    out: list[WordInstance] = []
    path: list[int] = []

    def dfs(cell: int, idx: int, used: int) -> None:
        if letters[cell] != word[idx]:
            return
        used |= 1 << cell
        path.append(cell)
        if idx == len(word) - 1:
            out.append(WordInstance(word, tuple(path)))
            path.pop()
            return
        for nxt in neighbors[cell]:
            if used & (1 << nxt):
                continue
            dfs(nxt, idx + 1, used)
        path.pop()

    for cell, ch in enumerate(letters):
        if ch == word[0]:
            dfs(cell, 0, 0)
    return out


def phrase_instances(by_word: dict[str, list[WordInstance]], neighbors: list[list[int]], words: list[str]) -> list[PhraseInstance]:
    ordered = []
    for word in words:
        matches = by_word.get(word.lower(), [])
        if not matches:
            return []
        ordered.append(matches)

    out: list[PhraseInstance] = []

    def rec(i: int, used: int, prev_end: int | None, chosen: list[WordInstance]) -> None:
        if i == len(ordered):
            out.append(PhraseInstance(tuple(chosen)))
            return
        for inst in ordered[i]:
            if used & inst.mask:
                continue
            if prev_end is not None and inst.start not in neighbors[prev_end]:
                continue
            chosen.append(inst)
            rec(i + 1, used | inst.mask, inst.end, chosen)
            chosen.pop()

    rec(0, 0, None, [])
    return out


def enumerate_phrases(by_word: dict[str, list[WordInstance]], neighbors: list[list[int]], vocab: list[str], min_words: int, max_words: int) -> list[PhraseInstance]:
    out: list[PhraseInstance] = []
    sorted_vocab = [word.lower() for word in vocab]

    def rec(chosen: list[WordInstance], used: int, prev_end: int | None) -> None:
        if min_words <= len(chosen) <= max_words:
            out.append(PhraseInstance(tuple(chosen)))
        if len(chosen) == max_words:
            return
        for word in sorted_vocab:
            for inst in by_word.get(word, []):
                if used & inst.mask:
                    continue
                if prev_end is not None and inst.start not in neighbors[prev_end]:
                    continue
                chosen.append(inst)
                rec(chosen, used | inst.mask, inst.end)
                chosen.pop()

    rec([], 0, None)
    return out


def render_word(inst: WordInstance, cols: int) -> dict:
    return {
        "word": inst.word,
        "path_cells": list(inst.path),
        "coords": [coord(cell, cols) for cell in inst.path],
    }


def render_phrase(inst: PhraseInstance, cols: int) -> dict:
    return {
        "phrase": inst.text,
        "words": [word.word for word in inst.words],
        "path_cells": [list(word.path) for word in inst.words],
        "coord_paths": [[coord(cell, cols) for cell in word.path] for word in inst.words],
    }


def phrase_summary(instances: list[PhraseInstance]) -> list[dict]:
    counts: dict[str, int] = {}
    for inst in instances:
        counts[inst.text] = counts.get(inst.text, 0) + 1
    out = [{"phrase": phrase, "count": count} for phrase, count in counts.items()]
    out.sort(key=lambda item: (-len(item["phrase"].split()), -item["count"], item["phrase"]))
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("grid", type=Path)
    parser.add_argument("mode", choices=["words", "phrase", "summary", "phrases"])
    parser.add_argument("tokens", nargs="*")
    parser.add_argument("--vocab", nargs="*", default=[])
    parser.add_argument("--min-words", type=int, default=1)
    parser.add_argument("--max-words", type=int, default=5)
    parser.add_argument("--must-contain", nargs="*", default=[])
    args = parser.parse_args()

    grid, rows, cols = load_grid(args.grid)
    letters = flatten(grid)
    neighbors = build_neighbors(rows, cols)

    vocab = sorted(set(word.lower() for word in (args.vocab or args.tokens)))
    by_word = {word: find_word_instances(letters, neighbors, word) for word in vocab}

    if args.mode == "words":
        payload = []
        for word in vocab:
            payload.append({
                "word": word,
                "count": len(by_word[word]),
                "matches": [render_word(inst, cols) for inst in by_word[word]],
            })
        print(json.dumps(payload, indent=2))
        return 0

    if args.mode == "phrase":
        phrases = phrase_instances(by_word, neighbors, [token.lower() for token in args.tokens])
        print(json.dumps([render_phrase(inst, cols) for inst in phrases], indent=2))
        return 0

    phrases = enumerate_phrases(by_word, neighbors, vocab, args.min_words, args.max_words)
    if args.must_contain:
        required = set(word.lower() for word in args.must_contain)
        phrases = [inst for inst in phrases if required.issubset(set(inst.text.split()))]

    if args.mode == "phrases":
        print(json.dumps([render_phrase(inst, cols) for inst in phrases], indent=2))
        return 0

    print(json.dumps(phrase_summary(phrases), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
