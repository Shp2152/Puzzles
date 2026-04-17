from pathlib import Path

from build_clause_graph_report import (
    OPERATIONS_DIR,
    build_clause_nodes,
    build_lexical_edges,
    build_spatial_edges,
    collect_outputs,
    collect_target_cores,
)
from build_hypothesis_scorecard import node_support_score


REPORT_PATH = OPERATIONS_DIR / "missing_slot_discriminator.md"
ATTACHMENT_DIR = Path(__file__).resolve().parent / "attachment_experiments"

WINNING_SKELETON = (
    ("start", "find start nine"),
    ("action", "nine step six"),
    ("total", "get nine total"),
    ("output", "step baseten integer"),
)

FILLER_FAMILIES = (
    {
        "name": "Integer Object",
        "clauses": (
            "step integer six",
            "is integer six",
            "step baseten integer",
            "baseten integer",
            "is integer baseten",
            "integer baseten",
        ),
        "attachment_outputs": (),
        "assumptions": (
            "Still must explain exactly what total is computed over the stepped integers.",
        ),
    },
    {
        "name": "Representation-Coded Object",
        "clauses": (
            "hexadecimal ten ten ten integer",
            "decimal ten ten ten integer",
        ),
        "attachment_outputs": (
            "attach_output_hexadecimal",
            "attach_output_decimal",
            "attach_action_output_hexadecimal",
            "attach_action_output_decimal",
            "attach_action_hexadecimal",
            "attach_action_decimal",
            "attach_start_hexadecimal",
            "attach_start_decimal",
            "attach_total_hexadecimal",
            "attach_total_decimal",
        ),
        "assumptions": (
            "Must decide which representation clause is the active one (`hexadecimal` vs `decimal`).",
            "Must explain why no direct attachment experiment to the winning skeleton succeeds.",
            "Must explain whether the representation family is an input object, a second-stage interpretation, or merely confirmation.",
        ),
    },
    {
        "name": "Three-Ten-Hundred Payload",
        "clauses": (
            "three ten hundred",
        ),
        "attachment_outputs": (
            "attach_payload_start",
            "attach_payload_action",
            "attach_payload_total",
            "attach_payload_output",
            "attach_payload_action_output",
        ),
        "assumptions": (
            "Must decide how `three ten hundred` should be interpreted numerically.",
            "Must explain why no direct attachment experiment to the winning skeleton succeeds.",
            "Must explain why the upper-left payload should plug into the otherwise lower-right procedure.",
        ),
    },
)


def build_edge_maps(nodes):
    lexical_map = {}
    spatial_map = {}
    for edge in build_lexical_edges(nodes):
        lexical_map[tuple(sorted((edge["left"], edge["right"])))] = edge
    for edge in build_spatial_edges(nodes):
        spatial_map[tuple(sorted((edge["left"], edge["right"])))] = edge
    return lexical_map, spatial_map


def role_link_score(filler_core, role_core, lexical_map, spatial_map):
    key = tuple(sorted((filler_core, role_core)))
    lexical = lexical_map.get(key)
    if lexical:
        if lexical["overlap"] > 0 or lexical["distance"] <= 1:
            return 3, lexical, "lexical"
        return 2, lexical, "lexical"
    spatial = spatial_map.get(key)
    if spatial and (spatial["overlap"] > 0 or spatial["distance"] <= 1):
        return 1, spatial, "spatial"
    return 0, None, None


def attachment_success_count(names):
    successes = 0
    details = []
    for name in names:
        path = ATTACHMENT_DIR / f"{name}.txt"
        text = path.read_text(encoding="utf-8")
        ok = "No phrase candidates satisfied the current settings." not in text
        details.append((name, ok))
        if ok:
            successes += 1
    return successes, details


def family_clause_strength(node):
    if node is None:
        return 0
    return node_support_score(node) + (node["best_score"] // 15)


def evaluate_family(family, nodes, lexical_map, spatial_map):
    available = [nodes[core] for core in family["clauses"] if core in nodes]
    available.sort(key=family_clause_strength, reverse=True)

    best_clause = available[0] if available else None
    best_clause_score = family_clause_strength(best_clause) if best_clause else 0

    role_links = []
    role_points = 0
    for role_name, role_core in WINNING_SKELETON:
        best = None
        for node in available:
            points, edge, edge_kind = role_link_score(node["core"], role_core, lexical_map, spatial_map)
            candidate = (points, family_clause_strength(node), node["core"], edge_kind, edge)
            if best is None or candidate > best:
                best = candidate
        if best is None:
            role_links.append({"role": role_name, "role_core": role_core, "points": 0, "family_core": None, "edge_kind": None, "edge": None})
            continue
        role_points += best[0]
        role_links.append(
            {
                "role": role_name,
                "role_core": role_core,
                "points": best[0],
                "family_core": best[2],
                "edge_kind": best[3],
                "edge": best[4],
            }
        )

    attachment_successes, attachment_details = attachment_success_count(family["attachment_outputs"])
    attachment_points = attachment_successes * 4
    attachment_failure_penalty = 0
    if family["attachment_outputs"] and attachment_successes == 0:
        attachment_failure_penalty = 6

    assumption_penalty = len(family["assumptions"]) * 4
    total_score = best_clause_score + role_points + attachment_points - attachment_failure_penalty - assumption_penalty

    return {
        "name": family["name"],
        "best_clause": best_clause,
        "best_clause_score": best_clause_score,
        "role_points": role_points,
        "attachment_points": attachment_points,
        "attachment_failure_penalty": attachment_failure_penalty,
        "attachment_details": attachment_details,
        "assumption_penalty": assumption_penalty,
        "assumptions": family["assumptions"],
        "role_links": role_links,
        "total_score": total_score,
    }


def describe_edge(link):
    edge = link["edge"]
    if edge is None:
        return "none"
    shared = ", ".join(edge["shared_words"]) if edge["shared_words"] else "-"
    return f"{link['edge_kind']} shared={shared} overlap={edge['overlap']} distance={edge['distance']}"


def write_report(results):
    lines = [
        "# Missing Slot Discriminator",
        "",
        "This report compares candidate fillers for the single unresolved slot in the current winning skeleton:",
        "",
        "- `find start nine`",
        "- `nine step six`",
        "- `get nine total`",
        "- `step baseten integer`",
        "",
        "Question being ranked:",
        "",
        "- What exact object or value is being stepped / totaled?",
        "",
        "## Scoring Model",
        "",
        "For each filler family:",
        "",
        "- `best_clause_score` uses the strongest local clause in that family",
        "- `role_points` measures how well the family connects to the fixed skeleton roles",
        "- `attachment_points` rewards successful direct attachment experiments",
        "- `attachment_failure_penalty` penalizes families with direct attachment experiments that all failed",
        "- `assumption_penalty` penalizes extra interpretation choices needed to use the family as the missing filler",
        "",
        "## Ranked Fillers",
        "",
        "| Rank | Filler family | Total | Best clause | Role points | Attachment points | Attachment failure penalty | Assumption penalty |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for rank, result in enumerate(results, start=1):
        lines.append(
            f"| {rank} | {result['name']} | {result['total_score']} | {result['best_clause_score']} | {result['role_points']} | "
            f"{result['attachment_points']} | {result['attachment_failure_penalty']} | {result['assumption_penalty']} |"
        )

    lines.extend(["", "## Details", ""])
    for rank, result in enumerate(results, start=1):
        lines.append(f"### {rank}. {result['name']}")
        lines.append("")
        lines.append(f"- total score: {result['total_score']}")
        if result["best_clause"] is not None:
            lines.append(
                f"- strongest local clause: `{result['best_clause']['core']}` "
                f"(support_score={result['best_clause_score']}, region={result['best_clause']['region']})"
            )
        lines.append(
            f"- score breakdown: best_clause={result['best_clause_score']}, role_links={result['role_points']}, "
            f"attachments={result['attachment_points']}, attachment_failure=-{result['attachment_failure_penalty']}, "
            f"assumptions=-{result['assumption_penalty']}"
        )
        lines.append("- role compatibility:")
        for link in result["role_links"]:
            family_core = f"`{link['family_core']}`" if link["family_core"] else "none"
            lines.append(
                f"  {link['role']}: {family_core} -> `{link['role_core']}` | +{link['points']} | {describe_edge(link)}"
            )
        if result["attachment_details"]:
            lines.append("- direct attachment experiments:")
            for name, ok in result["attachment_details"]:
                lines.append(f"  {name}: {'success' if ok else 'failed'}")
        lines.append("- added assumptions:")
        for assumption in result["assumptions"]:
            lines.append(f"  {assumption}")
        lines.append("")

    lines.extend(
        [
            "## Current Read",
            "",
            "Interpret this ranking cautiously:",
            "",
            "- A higher score means a family fills the missing slot with fewer new assumptions and better integration into the current skeleton.",
            "- A low score does not mean the family is fake. It can still be intentional while operating as a separate or later clue layer.",
        ]
    )

    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    outputs = collect_outputs()
    target_cores = collect_target_cores(outputs)
    nodes = build_clause_nodes(outputs, target_cores)
    lexical_map, spatial_map = build_edge_maps(nodes)

    results = [evaluate_family(family, nodes, lexical_map, spatial_map) for family in FILLER_FAMILIES]
    results.sort(key=lambda item: (item["total_score"], item["best_clause_score"], item["role_points"]), reverse=True)
    write_report(results)
    print(f"Saved discriminator to {REPORT_PATH}")


if __name__ == "__main__":
    main()
