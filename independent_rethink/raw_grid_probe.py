from __future__ import annotations

import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


DIRS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]


@dataclass(frozen=True)
class Match:
    text: str
    path: tuple[int, ...]


def load_grid(csv_path: Path) -> tuple[list[list[str]], int, int]:
    with csv_path.open(newline="", encoding="utf-8") as handle:
        grid = [[cell.strip().lower() for cell in row] for row in csv.reader(handle)]
    if not grid:
        raise ValueError("grid is empty")
    widths = {len(row) for row in grid}
    if len(widths) != 1:
        raise ValueError(f"grid is not rectangular: {sorted(widths)}")
    return grid, len(grid), len(grid[0])


def coord(cell: int, cols: int) -> str:
    row, col = divmod(cell, cols)
    letters = []
    idx = col + 1
    while idx:
        idx, rem = divmod(idx - 1, 26)
        letters.append(chr(ord("A") + rem))
    return f"{''.join(reversed(letters))}{row + 1}"


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


def flatten(grid: list[list[str]]) -> list[str]:
    return [cell for row in grid for cell in row]


def find_word(letters: list[str], neighbors: list[list[int]], word: str) -> list[Match]:
    word = word.lower()
    out: list[Match] = []
    path: list[int] = []

    def dfs(cell: int, idx: int, used: int) -> None:
        if letters[cell] != word[idx]:
            return
        used |= 1 << cell
        path.append(cell)
        if idx == len(word) - 1:
            out.append(Match(word, tuple(path)))
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


def find_phrase(letters: list[str], neighbors: list[list[int]], words: list[str]) -> list[dict]:
    by_word = [find_word(letters, neighbors, word) for word in words]
    out: list[dict] = []
    if any(not matches for matches in by_word):
        return out

    def rec(i: int, used: int, prev_end: int | None, chosen: list[Match]) -> None:
        if i == len(by_word):
            out.append(
                {
                    "phrase": " ".join(words),
                    "words": [m.text for m in chosen],
                    "paths": [list(m.path) for m in chosen],
                }
            )
            return
        for match in by_word[i]:
            mask = 0
            for cell in match.path:
                mask |= 1 << cell
            if used & mask:
                continue
            if prev_end is not None and match.path[0] not in neighbors[prev_end]:
                continue
            chosen.append(match)
            rec(i + 1, used | mask, match.path[-1], chosen)
            chosen.pop()

    rec(0, 0, None, [])
    return out


def render_path(path: list[int], cols: int) -> list[str]:
    return [coord(cell, cols) for cell in path]


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print("usage: raw_grid_probe.py GRID.csv word|phrase|batch-word|batch-phrase <tokens...>", file=sys.stderr)
        return 2
    grid_path = Path(argv[1])
    mode = argv[2]
    grid, rows, cols = load_grid(grid_path)
    letters = flatten(grid)
    neighbors = build_neighbors(rows, cols)

    if mode == "word":
        if len(argv) != 4:
            print("word mode takes exactly one token", file=sys.stderr)
            return 2
        matches = find_word(letters, neighbors, argv[3])
        payload = [
            {
                "word": m.text,
                "path_cells": list(m.path),
                "coords": render_path(list(m.path), cols),
            }
            for m in matches
        ]
        print(json.dumps(payload, indent=2))
        return 0

    if mode == "phrase":
        words = argv[3:]
        matches = find_phrase(letters, neighbors, words)
        for match in matches:
            match["coord_paths"] = [render_path(path, cols) for path in match["paths"]]
        print(json.dumps(matches, indent=2))
        return 0

    if mode == "batch-word":
        payload = []
        for word in argv[3:]:
            matches = find_word(letters, neighbors, word)
            payload.append(
                {
                    "word": word.lower(),
                    "count": len(matches),
                    "matches": [
                        {
                            "path_cells": list(m.path),
                            "coords": render_path(list(m.path), cols),
                        }
                        for m in matches
                    ],
                }
            )
        print(json.dumps(payload, indent=2))
        return 0

    if mode == "batch-phrase":
        payload = []
        for raw_phrase in argv[3:]:
            words = [token for token in raw_phrase.lower().split("_") if token]
            matches = find_phrase(letters, neighbors, words)
            for match in matches:
                match["coord_paths"] = [render_path(path, cols) for path in match["paths"]]
            payload.append(
                {
                    "phrase": " ".join(words),
                    "count": len(matches),
                    "matches": matches,
                }
            )
        print(json.dumps(payload, indent=2))
        return 0

    print(f"unknown mode: {mode}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
