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


def enumerate_phrases(
    by_word: dict[str, list[WordInstance]],
    neighbors: list[list[int]],
    min_words: int,
    max_words: int,
) -> list[dict]:
    vocab = sorted(by_word)
    out: list[dict] = []

    def emit(chosen: list[WordInstance]) -> None:
        out.append(
            {
                "phrase": " ".join(item.word for item in chosen),
                "words": [item.word for item in chosen],
                "path_cells": [list(item.path) for item in chosen],
            }
        )

    def rec(chosen: list[WordInstance], used: int, prev_end: int | None) -> None:
        if min_words <= len(chosen) <= max_words:
            emit(chosen)
        if len(chosen) == max_words:
            return
        for word in vocab:
            for inst in by_word[word]:
                if used & inst.mask:
                    continue
                if prev_end is not None and inst.start not in neighbors[prev_end]:
                    continue
                chosen.append(inst)
                rec(chosen, used | inst.mask, inst.end,)
                chosen.pop()

    rec([], 0, None)
    return out


def phrase_count_summary(phrases: list[dict]) -> list[dict]:
    counts: dict[str, int] = {}
    for phrase in phrases:
        counts[phrase["phrase"]] = counts.get(phrase["phrase"], 0) + 1
    summary = [{"phrase": phrase, "count": count} for phrase, count in counts.items()]
    summary.sort(key=lambda item: (-len(item["phrase"].split()), -item["count"], item["phrase"]))
    return summary


def render_phrase_coords(phrases: list[dict], cols: int) -> list[dict]:
    rendered = []
    for phrase in phrases:
        item = dict(phrase)
        item["coord_paths"] = [
            [coord(cell, cols) for cell in path]
            for path in phrase["path_cells"]
        ]
        rendered.append(item)
    return rendered


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("grid", type=Path)
    parser.add_argument("--words", nargs="+", required=True)
    parser.add_argument("--min-words", type=int, default=1)
    parser.add_argument("--max-words", type=int, default=4)
    parser.add_argument("--mode", choices=["words", "phrases", "summary"], default="summary")
    parser.add_argument("--phrase-text", action="append", default=[])
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    grid, rows, cols = load_grid(args.grid)
    letters = flatten(grid)
    neighbors = build_neighbors(rows, cols)

    by_word = {
        word.lower(): find_word_instances(letters, neighbors, word.lower())
        for word in args.words
    }

    if args.mode == "words":
        payload = []
        for word in sorted(by_word):
            payload.append(
                {
                    "word": word,
                    "count": len(by_word[word]),
                    "matches": [
                        {
                            "path_cells": list(inst.path),
                            "coords": [coord(cell, cols) for cell in inst.path],
                        }
                        for inst in by_word[word]
                    ],
                }
            )
        print(json.dumps(payload, indent=2))
        return 0

    phrases = enumerate_phrases(by_word, neighbors, args.min_words, args.max_words)
    rendered = render_phrase_coords(phrases, cols)

    if args.phrase_text:
        keep = set(args.phrase_text)
        rendered = [item for item in rendered if item["phrase"] in keep]

    if args.mode == "phrases":
        print(json.dumps(rendered, indent=2))
        return 0

    print(json.dumps(phrase_count_summary(rendered), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
