from collections import Counter, defaultdict
from pathlib import Path
import re

from canudig_search import DEFAULT_BRIDGE_WORDS


SCRIPT_DIR = Path(__file__).resolve().parent
OPERATIONS_DIR = SCRIPT_DIR / "operation_experiments"
DEFAULT_OUTPUT_PATH = SCRIPT_DIR / "top_phrase_candidates.txt"
REPORT_PATH = OPERATIONS_DIR / "clause_graph_report.md"
DOT_PATH = OPERATIONS_DIR / "clause_graph.dot"

EXPLICIT_DEFAULT_CORES = (
    "decimal ten ten ten integer",
    "hexadecimal ten ten ten integer",
    "binary ten integer",
)

TEXT_RE = re.compile(r"^TEXT: (.+)$")
SCORE_RE = re.compile(
    r"^SCORE: (\d+) \| letters=(\d+) \| content_words=(\d+) \| bridge_words=(\d+) \| "
    r"noun=(True|False) \| verb=(True|False) \| path_variants_in_top_pool=(\d+)$"
)
WORD_RE = re.compile(r"^  ([a-z]+): (.+)$")
CORE_RE = re.compile(r"^CORE: (.+)$")
BEST_SCORE_RE = re.compile(
    r"^BEST_SCORE: (\d+) \| letters=(\d+) \| content_words=(\d+) \| phrase_texts=(\d+) \| "
    r"path_variants_in_best_phrase=(\d+)$"
)
BEST_PHRASE_RE = re.compile(r"^BEST_PHRASE: (.+)$")
MUST_RE = re.compile(r"^must_have_words=(.*)$")


def parse_coord(token):
    token = token.strip()
    col = ord(token[0]) - ord("A") + 1
    row = int(token[1:])
    return (col, row)


def parse_coord_path(text):
    return tuple(parse_coord(part) for part in text.split(" -> "))


def format_bbox(cells):
    cols = [cell[0] for cell in cells]
    rows = [cell[1] for cell in cells]
    left = chr(ord("A") + min(cols) - 1)
    right = chr(ord("A") + max(cols) - 1)
    top = min(rows)
    bottom = max(rows)
    return f"{left}{top}:{right}{bottom}"


def classify_region(cells):
    cols = [cell[0] for cell in cells]
    rows = [cell[1] for cell in cells]
    min_col = min(cols)
    max_col = max(cols)
    min_row = min(rows)
    max_row = max(rows)
    avg_col = sum(cols) / len(cols)
    avg_row = sum(rows) / len(rows)

    if min_row <= 4 and max_row >= 9:
        return "right-spanning"
    if avg_row <= 5.5 and avg_col >= 8:
        return "upper-right"
    if avg_row >= 9 and avg_col >= 8:
        return "lower-right"
    if avg_row <= 7 and avg_col <= 5.5:
        return "upper-left"
    if avg_row >= 8 and avg_col <= 6:
        return "lower-left"
    return "central/mixed"


def chebyshev(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))


def min_cell_distance(cells_a, cells_b):
    best = None
    for cell_a in cells_a:
        for cell_b in cells_b:
            distance = chebyshev(cell_a, cell_b)
            if best is None or distance < best:
                best = distance
    return best if best is not None else 999


def parse_solver_output(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    parsed = {
        "path": path,
        "must_have_words": (),
        "phrases": {},
        "top_content_cores": {},
        "has_results": True,
    }

    current_phrase = None
    current_core = None
    mode = None

    for line in lines:
        must_match = MUST_RE.match(line)
        if must_match:
            raw = must_match.group(1).strip()
            parsed["must_have_words"] = tuple(part.strip() for part in raw.split(",") if part.strip() and raw != "None")
            continue
        if line == "No phrase candidates satisfied the current settings.":
            parsed["has_results"] = False

        if line == "=== TOP PHRASE CANDIDATES ===":
            mode = "phrases"
            current_phrase = None
            continue
        if line == "=== TOP CONTENT CORES ===":
            mode = "cores"
            current_core = None
            continue
        if line.startswith("=== ") and line not in {"=== TOP PHRASE CANDIDATES ===", "=== TOP CONTENT CORES ==="}:
            if mode == "cores":
                mode = None
                break
            mode = None
            current_phrase = None
            continue

        if mode == "phrases":
            text_match = TEXT_RE.match(line)
            if text_match:
                current_phrase = {
                    "text": text_match.group(1),
                    "score": None,
                    "letters": None,
                    "content_words": None,
                    "bridge_words": None,
                    "variant_count": None,
                    "word_entries": [],
                }
                parsed["phrases"][current_phrase["text"]] = current_phrase
                continue

            if current_phrase is None:
                continue

            score_match = SCORE_RE.match(line)
            if score_match:
                current_phrase["score"] = int(score_match.group(1))
                current_phrase["letters"] = int(score_match.group(2))
                current_phrase["content_words"] = int(score_match.group(3))
                current_phrase["bridge_words"] = int(score_match.group(4))
                current_phrase["variant_count"] = int(score_match.group(7))
                continue

            word_match = WORD_RE.match(line)
            if word_match:
                current_phrase["word_entries"].append(
                    {
                        "word": word_match.group(1),
                        "coords_text": word_match.group(2),
                        "coords": parse_coord_path(word_match.group(2)),
                    }
                )
                continue

        if mode == "cores":
            core_match = CORE_RE.match(line)
            if core_match:
                current_core = {
                    "core": core_match.group(1),
                    "best_score": None,
                    "letters": None,
                    "content_words": None,
                    "phrase_texts": None,
                    "variant_count": None,
                    "best_phrase": None,
                }
                parsed["top_content_cores"][current_core["core"]] = current_core
                continue

            if current_core is None:
                continue

            best_score_match = BEST_SCORE_RE.match(line)
            if best_score_match:
                current_core["best_score"] = int(best_score_match.group(1))
                current_core["letters"] = int(best_score_match.group(2))
                current_core["content_words"] = int(best_score_match.group(3))
                current_core["phrase_texts"] = int(best_score_match.group(4))
                current_core["variant_count"] = int(best_score_match.group(5))
                continue

            best_phrase_match = BEST_PHRASE_RE.match(line)
            if best_phrase_match:
                current_core["best_phrase"] = best_phrase_match.group(1)
                continue

    return parsed


def content_entries_for_phrase(phrase):
    return [entry for entry in phrase["word_entries"] if entry["word"] not in DEFAULT_BRIDGE_WORDS]


def build_support_record(output_name, parsed, core_text, source_kind):
    core_info = parsed["top_content_cores"][core_text]
    phrase = parsed["phrases"].get(core_info["best_phrase"])
    content_entries = content_entries_for_phrase(phrase) if phrase else []
    content_cells = tuple(cell for entry in content_entries for cell in entry["coords"])
    content_words = tuple(entry["word"] for entry in content_entries)
    required_words = parsed["must_have_words"]
    return {
        "output_name": output_name,
        "source_kind": source_kind,
        "required_words": required_words,
        "required_count": len(required_words),
        "core": core_text,
        "best_phrase": core_info["best_phrase"],
        "best_score": core_info["best_score"],
        "phrase_texts": core_info["phrase_texts"],
        "variant_count": core_info["variant_count"],
        "content_words": content_words,
        "content_cells": content_cells,
        "bbox": format_bbox(content_cells) if content_cells else "-",
        "region": classify_region(content_cells) if content_cells else "unknown",
    }


def collect_outputs():
    outputs = {"default": parse_solver_output(DEFAULT_OUTPUT_PATH)}
    for path in sorted(OPERATIONS_DIR.glob("op_*.txt")):
        outputs[path.stem] = parse_solver_output(path)
    return outputs


def collect_target_cores(outputs):
    target_cores = set(EXPLICIT_DEFAULT_CORES)
    for name, parsed in outputs.items():
        if name == "default" or not parsed["has_results"]:
            continue
        target_cores.update(parsed["top_content_cores"].keys())
    return target_cores


def build_clause_nodes(outputs, target_cores):
    nodes = {}
    for core in sorted(target_cores):
        supports = []
        for output_name, parsed in outputs.items():
            if core not in parsed["top_content_cores"]:
                continue
            source_kind = "default" if output_name == "default" else "operation"
            supports.append(build_support_record(output_name, parsed, core, source_kind))

        if not supports:
            continue

        supports.sort(
            key=lambda item: (
                item["required_count"],
                1 if item["source_kind"] == "operation" else 0,
                item["best_score"],
                item["phrase_texts"],
                item["best_phrase"],
            ),
            reverse=True,
        )
        representative = supports[0]
        words = tuple(core.split())
        word_set = set(words)
        nodes[core] = {
            "core": core,
            "words": words,
            "word_set": word_set,
            "representative": representative,
            "supports": supports,
            "support_count": len(supports),
            "operation_support_count": sum(1 for item in supports if item["source_kind"] == "operation"),
            "max_required_count": max(item["required_count"] for item in supports),
            "best_score": max(item["best_score"] for item in supports),
            "region": representative["region"],
            "bbox": representative["bbox"],
            "cells": representative["content_cells"],
            "kind": classify_clause_kind(word_set),
        }
    return nodes


def classify_clause_kind(words):
    if words & {"decimal", "hexadecimal", "binary", "baseten"}:
        return "representation"
    if words & {"hundred", "hundreds", "three", "ten"} and not (words & {"integer", "baseten", "decimal", "hexadecimal", "binary"}):
        return "payload"
    if words & {"find", "start", "get", "add", "step", "into", "total"}:
        return "instruction"
    if words & {"integer", "six", "nine"}:
        return "hybrid"
    return "other"


def strength_tuple(node):
    return (
        node["max_required_count"],
        node["operation_support_count"],
        node["support_count"],
        node["best_score"],
        -len(node["words"]),
        node["core"],
    )


def build_lexical_edges(nodes):
    edges = []
    cores = sorted(nodes)
    for index, left_core in enumerate(cores):
        left = nodes[left_core]
        for right_core in cores[index + 1 :]:
            right = nodes[right_core]
            shared_words = tuple(sorted(left["word_set"] & right["word_set"]))
            if not shared_words:
                continue
            distance = min_cell_distance(left["cells"], right["cells"])
            overlap = len(set(left["cells"]) & set(right["cells"]))
            edges.append(
                {
                    "left": left_core,
                    "right": right_core,
                    "shared_words": shared_words,
                    "distance": distance,
                    "overlap": overlap,
                }
            )
    edges.sort(key=lambda item: (-len(item["shared_words"]), item["distance"], item["left"], item["right"]))
    return edges


def build_spatial_edges(nodes):
    edges = []
    cores = sorted(nodes)
    for index, left_core in enumerate(cores):
        left = nodes[left_core]
        for right_core in cores[index + 1 :]:
            right = nodes[right_core]
            distance = min_cell_distance(left["cells"], right["cells"])
            overlap = len(set(left["cells"]) & set(right["cells"]))
            if overlap == 0 and distance > 2:
                continue
            shared_words = tuple(sorted(left["word_set"] & right["word_set"]))
            edges.append(
                {
                    "left": left_core,
                    "right": right_core,
                    "shared_words": shared_words,
                    "distance": distance,
                    "overlap": overlap,
                }
            )
    edges.sort(key=lambda item: (-item["overlap"], item["distance"], item["left"], item["right"]))
    return edges


def build_word_hubs(nodes):
    counter = Counter()
    carriers = defaultdict(list)
    for core, node in nodes.items():
        for word in node["word_set"]:
            counter[word] += 1
            carriers[word].append(core)
    return counter, carriers


def build_failed_compositions(outputs, nodes):
    failed = []
    for output_name, parsed in outputs.items():
        if output_name == "default" or parsed["has_results"]:
            continue
        required = set(parsed["must_have_words"])
        supporting = []
        for core, node in nodes.items():
            shared = required & node["word_set"]
            if len(shared) >= 2:
                supporting.append((len(shared), core))
        supporting.sort(reverse=True)
        failed.append(
            {
                "output_name": output_name,
                "required_words": tuple(parsed["must_have_words"]),
                "nearby_cores": [core for _, core in supporting[:4]],
            }
        )
    failed.sort(key=lambda item: (-len(item["required_words"]), item["output_name"]))
    return failed


def dot_node_id(core):
    return re.sub(r"[^a-z0-9]+", "_", core.lower()).strip("_")


def write_dot(nodes, lexical_edges):
    kind_colors = {
        "instruction": "lightgoldenrod1",
        "representation": "lightblue",
        "payload": "mistyrose",
        "hybrid": "honeydew",
        "other": "white",
    }
    lines = [
        "graph clause_graph {",
        "  rankdir=LR;",
        "  node [shape=box, style=filled, fontname=Helvetica];",
    ]
    for core, node in sorted(nodes.items(), key=lambda item: strength_tuple(item[1]), reverse=True):
        label = f"{core}\\n{node['region']}\\nreq={node['max_required_count']} sup={node['support_count']}"
        fill = kind_colors.get(node["kind"], "white")
        lines.append(f'  {dot_node_id(core)} [label="{label}", fillcolor="{fill}"];')
    for edge in lexical_edges:
        label = ", ".join(edge["shared_words"])
        if edge["overlap"]:
            label += f" | ov={edge['overlap']}"
        elif edge["distance"] <= 2:
            label += f" | d={edge['distance']}"
        lines.append(f'  {dot_node_id(edge["left"])} -- {dot_node_id(edge["right"])} [label="{label}"];')
    lines.append("}")
    DOT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_report(nodes, lexical_edges, spatial_edges, word_hubs, carriers, failed_compositions):
    ordered_nodes = sorted(nodes.values(), key=strength_tuple, reverse=True)
    lines = [
        "# Clause Graph Report",
        "",
        "Candidate clause graph and overlap report built from the current default run plus the targeted operation-word experiments.",
        "",
        "## How Strength Is Measured",
        "",
        "Clause strength here is not just raw frequency in the sentence scorer.",
        "",
        "A clause is treated as stronger when several of these are true:",
        "",
        "- it survives as a `TOP CONTENT CORE`, not only as a fluent-looking full phrase",
        "- it survives a targeted `--must-have-all` experiment",
        "- it survives a more specific experiment with more required words",
        "- it appears in more than one output file or experiment",
        "- it keeps a high best-score while staying content-heavy",
        "",
        "In the tables below:",
        "",
        "- `req` means the largest number of required words in a successful supporting experiment",
        "- `op_sup` means how many successful operation experiments support the clause",
        "- `all_sup` means total supporting output files, including the default run",
        "",
        "## Candidate Clauses",
        "",
        "| Core | Kind | Region | req | op_sup | all_sup | Best score | Representative phrase | BBox |",
        "| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for node in ordered_nodes:
        rep = node["representative"]
        lines.append(
            f"| `{node['core']}` | {node['kind']} | {node['region']} | {node['max_required_count']} | "
            f"{node['operation_support_count']} | {node['support_count']} | {node['best_score']} | "
            f"`{rep['best_phrase']}` | `{node['bbox']}` |"
        )

    lines.extend(
        [
            "",
            "## Clause Details",
            "",
        ]
    )
    for node in ordered_nodes:
        rep = node["representative"]
        support_names = ", ".join(item["output_name"] for item in node["supports"])
        lines.append(f"### `{node['core']}`")
        lines.append("")
        lines.append(f"- kind: {node['kind']}")
        lines.append(f"- representative phrase: `{rep['best_phrase']}`")
        lines.append(f"- representative region: {node['region']}")
        lines.append(f"- representative bbox: `{node['bbox']}`")
        lines.append(
            f"- strength signals: req={node['max_required_count']}, op_sup={node['operation_support_count']}, "
            f"all_sup={node['support_count']}, best_score={node['best_score']}"
        )
        lines.append(f"- supporting outputs: `{support_names}`")
        lines.append("")

    lines.extend(
        [
            "## Lexical Bridges",
            "",
            "These edges connect clauses that share at least one content word. This is the main candidate clause graph.",
            "",
            "| Left | Right | Shared words | Spatial overlap | Min distance |",
            "| --- | --- | --- | ---: | ---: |",
        ]
    )
    for edge in lexical_edges:
        shared = ", ".join(edge["shared_words"])
        lines.append(
            f"| `{edge['left']}` | `{edge['right']}` | `{shared}` | {edge['overlap']} | {edge['distance']} |"
        )

    lines.extend(
        [
            "",
            "## Spatial Overlap Report",
            "",
            "These edges connect clauses whose representative content paths overlap or sit within distance 2, even if they do not share words.",
            "",
            "| Left | Right | Shared words | Spatial overlap | Min distance |",
            "| --- | --- | --- | ---: | ---: |",
        ]
    )
    for edge in spatial_edges:
        shared = ", ".join(edge["shared_words"]) if edge["shared_words"] else "-"
        lines.append(
            f"| `{edge['left']}` | `{edge['right']}` | `{shared}` | {edge['overlap']} | {edge['distance']} |"
        )

    lines.extend(
        [
            "",
            "## Word Hubs",
            "",
            "Words that appear in multiple candidate clauses are the most plausible semantic pivots.",
            "",
            "| Word | Clause count | Clauses |",
            "| --- | ---: | --- |",
        ]
    )
    for word, count in word_hubs.most_common():
        if count < 2:
            continue
        lines.append(f"| `{word}` | {count} | {', '.join(f'`{core}`' for core in sorted(carriers[word]))} |")

    lines.extend(
        [
            "",
            "## Failed Composition Tests",
            "",
            "These experiments required multiple words at once and produced no phrase. They are negative evidence against a single-sentence reading.",
            "",
            "| Failed required words | Nearby successful clauses |",
            "| --- | --- |",
        ]
    )
    for item in failed_compositions:
        nearby = ", ".join(f"`{core}`" for core in item["nearby_cores"]) if item["nearby_cores"] else "-"
        lines.append(f"| `{', '.join(item['required_words'])}` | {nearby} |")

    lines.extend(
        [
            "",
            "## Current Read",
            "",
            "What jumps out from the current graph:",
            "",
            "- `nine` is the strongest lexical bridge between the upper-right instruction family and the lower-right action/total family.",
            "- `step` and `integer` are the strongest lower-right pivots.",
            "- `baseten integer` and `step baseten integer` look like output-format clauses rather than payload clauses.",
            "- `three ten hundred` remains a payload candidate, but it is still not graph-connected to the output clauses by a successful joint phrase.",
            "- The failed composition tests strongly suggest that the puzzle is exposing several short clauses that must be composed conceptually, not one long readable sentence.",
            "",
            f"Graphviz file: `{DOT_PATH.name}`",
        ]
    )

    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    outputs = collect_outputs()
    target_cores = collect_target_cores(outputs)
    nodes = build_clause_nodes(outputs, target_cores)
    word_hubs, carriers = build_word_hubs(nodes)
    lexical_edges = build_lexical_edges(nodes)
    spatial_edges = build_spatial_edges(nodes)
    failed_compositions = build_failed_compositions(outputs, nodes)
    write_dot(nodes, lexical_edges)
    write_report(nodes, lexical_edges, spatial_edges, word_hubs, carriers, failed_compositions)
    print(f"Saved report to {REPORT_PATH}")
    print(f"Saved graph to {DOT_PATH}")


if __name__ == "__main__":
    main()
