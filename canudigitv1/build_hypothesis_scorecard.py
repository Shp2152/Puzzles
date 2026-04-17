from itertools import product
from pathlib import Path

from build_clause_graph_report import (
    OPERATIONS_DIR,
    build_clause_nodes,
    build_lexical_edges,
    build_spatial_edges,
    collect_outputs,
    collect_target_cores,
)


REPORT_PATH = OPERATIONS_DIR / "hypothesis_scorecard.md"


FAMILIES = {
    "start": {
        "weight": 2,
        "clauses": {"find start nine", "start nine", "add start nine"},
    },
    "action": {
        "weight": 2,
        "clauses": {"step integer six", "nine step six", "step six", "ten step six", "get step six"},
    },
    "total": {
        "weight": 2,
        "clauses": {"get nine total"},
    },
    "output": {
        "weight": 2,
        "clauses": {"step baseten integer", "baseten integer", "is integer baseten", "integer baseten"},
    },
    "payload": {
        "weight": 1,
        "clauses": {"three ten hundred"},
    },
    "representation": {
        "weight": 1,
        "clauses": {"decimal ten ten ten integer", "hexadecimal ten ten ten integer"},
    },
}


HYPOTHESES = (
    {
        "name": "H1 Procedure Skeleton",
        "summary": "Start at 9, apply a step-of-6 style rule, obtain a total, then report as a base-10 integer.",
        "roles": (
            ("start", ("find start nine", "start nine")),
            ("action", ("nine step six", "step integer six")),
            ("total", ("get nine total",)),
            ("output", ("step baseten integer", "baseten integer", "is integer baseten")),
        ),
        "explains_families": {"start", "action", "total", "output"},
        "unresolved_slots": (
            "What exact object/process is being stepped and totaled?",
        ),
    },
    {
        "name": "H2 Integer-Step Procedure",
        "summary": "Step through integers by 6 and report the result as a base-10 integer.",
        "roles": (
            ("start", ("find start nine", "start nine")),
            ("action", ("step integer six",)),
            ("output", ("step baseten integer", "baseten integer", "is integer baseten")),
        ),
        "explains_families": {"start", "action", "output"},
        "unresolved_slots": (
            "What quantity is totaled or targeted?",
            "Why does `get nine total` exist if total is not part of the procedure?",
        ),
    },
    {
        "name": "H3 Nine-Total Procedure",
        "summary": "Start from 9, get a total involving 9, and report as a base-10 integer.",
        "roles": (
            ("start", ("find start nine", "start nine")),
            ("total", ("get nine total",)),
            ("output", ("step baseten integer", "baseten integer", "is integer baseten")),
        ),
        "explains_families": {"start", "total", "output"},
        "unresolved_slots": (
            "What role does the step/6 family play?",
            "What operation turns the start value into the total?",
        ),
    },
    {
        "name": "H4 Representation-Normalization",
        "summary": "Interpret a representation-heavy numeric phrase and normalize it to a base-10 integer.",
        "roles": (
            ("representation", ("decimal ten ten ten integer", "hexadecimal ten ten ten integer")),
            ("output", ("baseten integer", "is integer baseten", "step baseten integer")),
        ),
        "explains_families": {"representation", "output"},
        "unresolved_slots": (
            "Why are the start/nine clauses present?",
            "Why are the step/6 clauses present?",
            "Why is `get nine total` present?",
        ),
    },
    {
        "name": "H5 Payload-Driven",
        "summary": "Treat `three ten hundred` as the payload and combine it with the base-10 output clue.",
        "roles": (
            ("payload", ("three ten hundred",)),
            ("output", ("baseten integer", "is integer baseten", "step baseten integer")),
        ),
        "explains_families": {"payload", "output"},
        "unresolved_slots": (
            "How should `three ten hundred` be interpreted numerically?",
            "Why are the start/nine clauses present?",
            "Why are the step/6 clauses present?",
            "Why is `get nine total` present?",
        ),
    },
    {
        "name": "H6 Payload-Slotted Procedure",
        "summary": "Use the start/step/total/output skeleton and assume `three ten hundred` fills the missing payload slot.",
        "roles": (
            ("start", ("find start nine", "start nine")),
            ("action", ("nine step six", "step integer six")),
            ("total", ("get nine total",)),
            ("output", ("step baseten integer", "baseten integer", "is integer baseten")),
            ("payload", ("three ten hundred",)),
        ),
        "explains_families": {"start", "action", "total", "output", "payload"},
        "unresolved_slots": (
            "How should `three ten hundred` be interpreted numerically?",
            "Why should the payload clause attach to the otherwise lower-right procedure?",
        ),
    },
)


def node_support_score(node):
    return (3 * node["max_required_count"]) + (2 * node["operation_support_count"]) + node["support_count"]


def build_edge_maps(nodes):
    lexical_edges = build_lexical_edges(nodes)
    spatial_edges = build_spatial_edges(nodes)
    lexical_map = {}
    spatial_map = {}

    for edge in lexical_edges:
        key = tuple(sorted((edge["left"], edge["right"])))
        lexical_map[key] = edge

    for edge in spatial_edges:
        key = tuple(sorted((edge["left"], edge["right"])))
        spatial_map[key] = edge

    return lexical_map, spatial_map


def bridge_score(left_core, right_core, lexical_map, spatial_map):
    key = tuple(sorted((left_core, right_core)))
    lexical = lexical_map.get(key)
    if lexical:
        if lexical["overlap"] > 0 or lexical["distance"] <= 1:
            return 3, lexical
        return 2, lexical
    spatial = spatial_map.get(key)
    if spatial:
        if spatial["overlap"] > 0 or spatial["distance"] <= 1:
            return 1, spatial
    return 0, None


def ignored_family_penalty(explained_families):
    penalty = 0
    ignored = []
    for family_name, info in FAMILIES.items():
        if family_name in explained_families:
            continue
        penalty += info["weight"]
        ignored.append(family_name)
    return penalty, ignored


def evaluate_hypothesis(hypothesis, nodes, lexical_map, spatial_map):
    chosen_groups = []
    missing_roles = []

    for role_name, candidates in hypothesis["roles"]:
        available = [nodes[name] for name in candidates if name in nodes]
        if not available:
            missing_roles.append(role_name)
            continue
        available.sort(key=node_support_score, reverse=True)
        chosen_groups.append((role_name, tuple(available)))

    best_selection = None
    best_selection_score = None
    role_names = [role_name for role_name, _ in chosen_groups]
    candidate_lists = [candidates for _, candidates in chosen_groups]

    if candidate_lists:
        for combination in product(*candidate_lists):
            chosen = list(zip(role_names, combination))
            raw_support = sum(node_support_score(node) for _, node in chosen)
            support_points = round((raw_support * 4) / len(chosen))
            bridge_points = 0
            bridge_details = []
            gap_penalty = 0

            for index in range(len(chosen) - 1):
                left_role, left_node = chosen[index]
                right_role, right_node = chosen[index + 1]
                points, edge = bridge_score(left_node["core"], right_node["core"], lexical_map, spatial_map)
                bridge_points += points
                if points == 0:
                    gap_penalty += 2
                bridge_details.append(
                    {
                        "left_role": left_role,
                        "left_core": left_node["core"],
                        "right_role": right_role,
                        "right_core": right_node["core"],
                        "points": points,
                        "edge": edge,
                    }
                )

            selection_score = (support_points + bridge_points - gap_penalty, support_points, bridge_points)
            if best_selection_score is None or selection_score > best_selection_score:
                best_selection_score = selection_score
                best_selection = {
                    "chosen": chosen,
                    "support_points": support_points,
                    "bridge_points": bridge_points,
                    "bridge_details": bridge_details,
                    "gap_penalty": gap_penalty,
                }
    else:
        best_selection = {
            "chosen": [],
            "support_points": 0,
            "bridge_points": 0,
            "bridge_details": [],
            "gap_penalty": 0,
        }

    unresolved_count = len(hypothesis["unresolved_slots"])
    assumption_penalty = unresolved_count * 4
    ignored_penalty, ignored_families = ignored_family_penalty(hypothesis["explains_families"])
    missing_role_penalty = len(missing_roles) * 6

    total_score = (
        best_selection["support_points"]
        + best_selection["bridge_points"]
        - best_selection["gap_penalty"]
        - assumption_penalty
        - ignored_penalty
        - missing_role_penalty
    )

    return {
        "name": hypothesis["name"],
        "summary": hypothesis["summary"],
        "chosen": best_selection["chosen"],
        "missing_roles": missing_roles,
        "support_points": best_selection["support_points"],
        "bridge_points": best_selection["bridge_points"],
        "gap_penalty": best_selection["gap_penalty"],
        "assumption_penalty": assumption_penalty,
        "ignored_penalty": ignored_penalty,
        "ignored_families": ignored_families,
        "missing_role_penalty": missing_role_penalty,
        "unresolved_slots": hypothesis["unresolved_slots"],
        "total_score": total_score,
        "bridge_details": best_selection["bridge_details"],
    }


def write_report(results):
    lines = [
        "# Hypothesis Scorecard",
        "",
        "This report compares a small number of concrete endgame procedure families.",
        "The goal is to rank stories by minimal assumptions first, while still rewarding strong clause support and bridge support.",
        "",
        "## Scoring Model",
        "",
        "For each hypothesis:",
        "",
        "- `support_points` rewards strong chosen clauses",
        "- `bridge_points` rewards lexical or spatial continuity between consecutive roles",
        "- `gap_penalty` penalizes consecutive roles that have no direct lexical or spatial support",
        "- `assumption_penalty` is `4 * unresolved_slots`",
        "- `ignored_penalty` penalizes strong clue families that the hypothesis leaves unexplained",
        "- `missing_role_penalty` penalizes any role the hypothesis could not fill from current clause evidence",
        "",
        "This is not a proof engine. It is a way to avoid re-reading the same graph and instead compare concrete procedure stories under one fixed rubric.",
        "",
        "## Ranked Hypotheses",
        "",
        "| Rank | Hypothesis | Total | Support | Bridges | Gap penalty | Assumption penalty | Ignored penalty | Missing-role penalty |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]

    for rank, result in enumerate(results, start=1):
        lines.append(
            f"| {rank} | {result['name']} | {result['total_score']} | {result['support_points']} | {result['bridge_points']} | "
            f"{result['gap_penalty']} | {result['assumption_penalty']} | {result['ignored_penalty']} | {result['missing_role_penalty']} |"
        )

    lines.extend(["", "## Details", ""])

    for rank, result in enumerate(results, start=1):
        lines.append(f"### {rank}. {result['name']}")
        lines.append("")
        lines.append(f"- summary: {result['summary']}")
        lines.append(f"- total score: {result['total_score']}")
        lines.append(
            f"- score breakdown: support={result['support_points']}, bridges={result['bridge_points']}, "
            f"gaps=-{result['gap_penalty']}, assumptions=-{result['assumption_penalty']}, ignored=-{result['ignored_penalty']}, "
            f"missing_roles=-{result['missing_role_penalty']}"
        )
        if result["chosen"]:
            lines.append("- chosen clauses:")
            for role_name, node in result["chosen"]:
                lines.append(
                    f"  {role_name}: `{node['core']}` (region={node['region']}, req={node['max_required_count']}, "
                    f"op_sup={node['operation_support_count']}, all_sup={node['support_count']})"
                )
        if result["bridge_details"]:
            lines.append("- bridges:")
            for item in result["bridge_details"]:
                if item["edge"] is None:
                    lines.append(
                        f"  {item['left_role']} -> {item['right_role']}: no direct lexical/spatial support"
                    )
                    continue
                shared = ", ".join(item["edge"]["shared_words"]) if item["edge"]["shared_words"] else "-"
                lines.append(
                    f"  {item['left_role']} -> {item['right_role']}: +{item['points']} "
                    f"(shared={shared}, overlap={item['edge']['overlap']}, distance={item['edge']['distance']})"
                )
        if result["unresolved_slots"]:
            lines.append("- unresolved slots:")
            for slot in result["unresolved_slots"]:
                lines.append(f"  {slot}")
        if result["ignored_families"]:
            lines.append(f"- ignored clue families: {', '.join(result['ignored_families'])}")
        if result["missing_roles"]:
            lines.append(f"- missing roles: {', '.join(result['missing_roles'])}")
        lines.append("")

    lines.extend(
        [
            "## Current Read",
            "",
            "What this ranking is meant to clarify:",
            "",
            "- If one procedure family clearly leads, the graph is becoming discriminative rather than descriptive.",
            "- If several families remain tied even after explicit penalties, the current modular story is still underconstrained.",
            "- `three ten hundred` should only be promoted if a payload-using hypothesis ranks well without exploding the assumption count.",
        ]
    )

    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    outputs = collect_outputs()
    target_cores = collect_target_cores(outputs)
    nodes = build_clause_nodes(outputs, target_cores)
    lexical_map, spatial_map = build_edge_maps(nodes)

    results = [evaluate_hypothesis(hypothesis, nodes, lexical_map, spatial_map) for hypothesis in HYPOTHESES]
    results.sort(key=lambda item: (item["total_score"], item["support_points"], item["bridge_points"]), reverse=True)
    write_report(results)
    print(f"Saved scorecard to {REPORT_PATH}")


if __name__ == "__main__":
    main()
