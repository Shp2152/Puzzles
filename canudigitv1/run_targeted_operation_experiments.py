import re
import subprocess
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SCRIPT_DIR / "operation_experiments"


EXPERIMENTS = (
    {
        "name": "op_find_start_nine",
        "words": ("find", "start", "nine"),
        "note": "Upper-right instruction candidate.",
    },
    {
        "name": "op_start_nine",
        "words": ("start", "nine"),
        "note": "Minimal start-anchor test.",
    },
    {
        "name": "op_step_six",
        "words": ("step", "six"),
        "note": "Lower-right stepping anchor.",
    },
    {
        "name": "op_nine_step_six",
        "words": ("nine", "step", "six"),
        "note": "Explicit step-size reading.",
    },
    {
        "name": "op_get_total",
        "words": ("get", "total"),
        "note": "Potential accumulation instruction.",
    },
    {
        "name": "op_get_nine_total",
        "words": ("get", "nine", "total"),
        "note": "Explicit accumulation reading.",
    },
    {
        "name": "op_add_start_nine",
        "words": ("add", "start", "nine"),
        "note": "Alternate instruction-style branch.",
    },
    {
        "name": "op_step_integer_six",
        "words": ("step", "integer", "six"),
        "note": "Operation + output-region test in the lower-right cluster.",
    },
    {
        "name": "op_step_baseten_integer",
        "words": ("step", "baseten", "integer"),
        "note": "Direct lower-right rule + output-label test.",
    },
    {
        "name": "op_step_baseten_integer_six",
        "words": ("step", "baseten", "integer", "six"),
        "note": "Direct lower-right rule + output + step-size test.",
    },
    {
        "name": "op_into_integer_six",
        "words": ("into", "integer", "six"),
        "note": "Alternate motion phrasing in the lower-right cluster.",
    },
    {
        "name": "op_point_integer",
        "words": ("point", "integer"),
        "note": "Suppressed operation candidate near the lower-right cluster.",
    },
    {
        "name": "op_open_integer",
        "words": ("open", "integer"),
        "note": "Another suppressed operation candidate near the lower-right cluster.",
    },
    {
        "name": "op_baseten_integer",
        "words": ("baseten", "integer"),
        "note": "Output-normalization clue.",
    },
    {
        "name": "op_get_total_baseten_integer",
        "words": ("get", "total", "baseten", "integer"),
        "note": "Accumulation phrase merged with output-label test.",
    },
    {
        "name": "op_three_ten_hundred",
        "words": ("three", "ten", "hundred"),
        "note": "Upper-left numeric payload cluster.",
    },
    {
        "name": "op_payload_to_output",
        "words": ("three", "ten", "hundred", "baseten", "integer"),
        "note": "Cross-island payload-to-output test.",
    },
    {
        "name": "op_story_chain",
        "words": ("start", "nine", "step", "six", "total"),
        "note": "Explicit algorithmic chain without output label.",
    },
    {
        "name": "op_start_nine_baseten_integer",
        "words": ("start", "nine", "baseten", "integer"),
        "note": "Upper-right start fragment merged with lower-right output-label test.",
    },
    {
        "name": "op_story_chain_with_output",
        "words": ("start", "nine", "step", "six", "total", "baseten", "integer"),
        "note": "Full explicit algorithmic chain with output label.",
    },
)


CORE_RE = re.compile(r"^CORE: (.+)$")
BEST_RE = re.compile(r"^BEST_PHRASE: (.+)$")
STATS_RE = re.compile(r"^(states_visited|mandatory_prunes|must_have_words)=(.+)$")


def parse_output(path):
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    summary = {
        "has_results": "No phrase candidates satisfied the current settings." not in text,
        "stats": [],
        "cores": [],
    }

    for line in lines:
        match = STATS_RE.match(line)
        if match:
            summary["stats"].append(f"{match.group(1)}={match.group(2)}")

    in_core_section = False
    current_core = None
    for line in lines:
        if line == "=== TOP CONTENT CORES ===":
            in_core_section = True
            continue
        if in_core_section and line.startswith("=== ") and line != "=== TOP CONTENT CORES ===":
            break
        if not in_core_section:
            continue

        match = CORE_RE.match(line)
        if match:
            current_core = {"core": match.group(1), "best_phrase": None}
            summary["cores"].append(current_core)
            continue

        match = BEST_RE.match(line)
        if match and current_core is not None:
            current_core["best_phrase"] = match.group(1)

    summary["cores"] = summary["cores"][:5]
    return summary


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
        "# Targeted Operation Experiments",
        "",
        "Batch run for the current instruction-layer hypothesis.",
        "",
    ]

    for experiment, output_path, parsed in results:
        lines.append(f"## {experiment['name']}")
        lines.append("")
        lines.append(f"- words: `{', '.join(experiment['words'])}`")
        lines.append(f"- note: {experiment['note']}")
        lines.append(f"- output: `{output_path.name}`")
        if parsed["stats"]:
            lines.append(f"- stats: `{' | '.join(parsed['stats'])}`")
        lines.append(f"- has_results: {'yes' if parsed['has_results'] else 'no'}")
        if parsed["cores"]:
            for item in parsed["cores"][:3]:
                lines.append(f"- core: `{item['core']}`")
                if item["best_phrase"]:
                    lines.append(f"- best_phrase: `{item['best_phrase']}`")
        else:
            lines.append("- core: none")
        lines.append("")

    summary_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return summary_path


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    results = []
    for experiment in EXPERIMENTS:
        output_path, parsed = run_experiment(experiment)
        results.append((experiment, output_path, parsed))
    summary_path = write_summary(results)
    print(f"Saved experiment outputs to {OUTPUT_DIR}")
    print(f"Saved summary to {summary_path}")


if __name__ == "__main__":
    main()
