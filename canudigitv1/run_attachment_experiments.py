import subprocess
import sys
from pathlib import Path

from run_targeted_operation_experiments import parse_output


SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SCRIPT_DIR / "attachment_experiments"


EXPERIMENTS = (
    {
        "name": "attach_output_hexadecimal",
        "group": "representation",
        "role": "output",
        "words": ("baseten", "integer", "hexadecimal"),
        "note": "Can hexadecimal attach directly to the base-10 output clause?",
    },
    {
        "name": "attach_output_decimal",
        "group": "representation",
        "role": "output",
        "words": ("baseten", "integer", "decimal"),
        "note": "Can decimal attach directly to the base-10 output clause?",
    },
    {
        "name": "attach_action_output_hexadecimal",
        "group": "representation",
        "role": "action_output",
        "words": ("step", "baseten", "integer", "hexadecimal"),
        "note": "Can hexadecimal attach to the strongest lower-right output/action clause?",
    },
    {
        "name": "attach_action_output_decimal",
        "group": "representation",
        "role": "action_output",
        "words": ("step", "baseten", "integer", "decimal"),
        "note": "Can decimal attach to the strongest lower-right output/action clause?",
    },
    {
        "name": "attach_action_hexadecimal",
        "group": "representation",
        "role": "action",
        "words": ("step", "integer", "six", "hexadecimal"),
        "note": "Can hexadecimal attach to the step-by-six clause?",
    },
    {
        "name": "attach_action_decimal",
        "group": "representation",
        "role": "action",
        "words": ("step", "integer", "six", "decimal"),
        "note": "Can decimal attach to the step-by-six clause?",
    },
    {
        "name": "attach_start_hexadecimal",
        "group": "representation",
        "role": "start",
        "words": ("start", "nine", "hexadecimal"),
        "note": "Can hexadecimal attach to the upper-right start clause?",
    },
    {
        "name": "attach_start_decimal",
        "group": "representation",
        "role": "start",
        "words": ("start", "nine", "decimal"),
        "note": "Can decimal attach to the upper-right start clause?",
    },
    {
        "name": "attach_total_hexadecimal",
        "group": "representation",
        "role": "total",
        "words": ("get", "nine", "total", "hexadecimal"),
        "note": "Can hexadecimal attach to the total clause?",
    },
    {
        "name": "attach_total_decimal",
        "group": "representation",
        "role": "total",
        "words": ("get", "nine", "total", "decimal"),
        "note": "Can decimal attach to the total clause?",
    },
    {
        "name": "attach_payload_start",
        "group": "payload",
        "role": "start",
        "words": ("start", "nine", "three", "ten", "hundred"),
        "note": "Can the payload attach directly to the start clause?",
    },
    {
        "name": "attach_payload_action",
        "group": "payload",
        "role": "action",
        "words": ("nine", "step", "six", "three", "ten", "hundred"),
        "note": "Can the payload attach to the step clause?",
    },
    {
        "name": "attach_payload_total",
        "group": "payload",
        "role": "total",
        "words": ("get", "nine", "total", "three", "ten", "hundred"),
        "note": "Can the payload attach to the total clause?",
    },
    {
        "name": "attach_payload_output",
        "group": "payload",
        "role": "output",
        "words": ("baseten", "integer", "three", "ten", "hundred"),
        "note": "Can the payload attach directly to the output clause?",
    },
    {
        "name": "attach_payload_action_output",
        "group": "payload",
        "role": "action_output",
        "words": ("step", "baseten", "integer", "three", "ten", "hundred"),
        "note": "Can the payload attach to the strongest lower-right action/output clause?",
    },
)


def run_experiment(experiment):
    output_path = OUTPUT_DIR / f"{experiment['name']}.txt"
    command = [
        sys.executable,
        "canudig.py",
        "--min-words",
        "2",
        "--max-words",
        "8",
        "--top-k",
        "250",
        "--must-have-all",
        ",".join(experiment["words"]),
        "--output",
        str(output_path),
    ]
    subprocess.run(command, check=True, cwd=SCRIPT_DIR)
    return output_path, parse_output(output_path)


def write_summary(results):
    summary_path = OUTPUT_DIR / "summary.md"
    lines = [
        "# Attachment Experiments",
        "",
        "These runs test whether unresolved clue families can attach directly to specific roles in the current winning skeleton.",
        "",
        "Winning skeleton under current minimal-assumption scoring:",
        "",
        "- `find start nine`",
        "- `nine step six`",
        "- `get nine total`",
        "- `step baseten integer`",
        "",
    ]

    for group in ("representation", "payload"):
        lines.append(f"## {group.title()} Attachments")
        lines.append("")
        for experiment, output_path, parsed in results:
            if experiment["group"] != group:
                continue
            lines.append(f"### {experiment['name']}")
            lines.append("")
            lines.append(f"- role: {experiment['role']}")
            lines.append(f"- words: `{', '.join(experiment['words'])}`")
            lines.append(f"- note: {experiment['note']}")
            lines.append(f"- output: `{output_path.name}`")
            lines.append(f"- has_results: {'yes' if parsed['has_results'] else 'no'}")
            if parsed["cores"]:
                for item in parsed["cores"][:3]:
                    lines.append(f"- core: `{item['core']}`")
                    if item["best_phrase"]:
                        lines.append(f"- best_phrase: `{item['best_phrase']}`")
            else:
                lines.append("- core: none")
            lines.append("")

    success_by_group = {}
    for group in ("representation", "payload"):
        success_by_group[group] = [experiment["name"] for experiment, _, parsed in results if experiment["group"] == group and parsed["has_results"]]

    lines.extend(
        [
            "## Current Read",
            "",
            f"- successful representation attachments: {', '.join(success_by_group['representation']) if success_by_group['representation'] else 'none'}",
            f"- successful payload attachments: {', '.join(success_by_group['payload']) if success_by_group['payload'] else 'none'}",
            "- If a family has no successful attachments, it is currently better treated as a separate or confirmatory layer rather than an integrated step of the winning skeleton.",
        ]
    )

    summary_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return summary_path


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    results = []
    for experiment in EXPERIMENTS:
        output_path, parsed = run_experiment(experiment)
        results.append((experiment, output_path, parsed))
    summary_path = write_summary(results)
    print(f"Saved attachment outputs to {OUTPUT_DIR}")
    print(f"Saved summary to {summary_path}")


if __name__ == "__main__":
    main()
