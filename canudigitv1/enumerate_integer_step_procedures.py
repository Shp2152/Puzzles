from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
REPORT_PATH = SCRIPT_DIR / "operation_experiments" / "integer_step_procedures.md"

START = 9
STEP = 6


def term_from_term_index(term_index):
    return START + STEP * (term_index - 1)


def term_after_steps(step_count):
    return START + STEP * step_count


def sum_first_terms(term_count):
    return term_count * (2 * START + (term_count - 1) * STEP) // 2


def sum_after_steps(step_count):
    return sum_first_terms(step_count + 1)


PROCEDURES = (
    {
        "name": "Last term of first 9 terms",
        "kind": "term",
        "formula": "term_9 = 9 + 6*(9-1)",
        "value": term_from_term_index(9),
        "uses": "start nine, nine as term-count, step six",
        "assumptions": 2,
        "fit": "weak on `total` because it returns a term, not a total",
    },
    {
        "name": "Last term after 9 steps",
        "kind": "term",
        "formula": "term_after_9_steps = 9 + 6*9",
        "value": term_after_steps(9),
        "uses": "start nine, nine as step-count, step six",
        "assumptions": 2,
        "fit": "weak on `total` because it returns a term, not a total",
    },
    {
        "name": "Total of first 9 terms",
        "kind": "total",
        "formula": "sum_9_terms = 9*(2*9 + 8*6)/2",
        "value": sum_first_terms(9),
        "uses": "start nine, nine as term-count, step six, get total",
        "assumptions": 1,
        "fit": "strongest minimal-assumption total reading if `nine total` means total of 9 terms",
    },
    {
        "name": "Total after 9 steps",
        "kind": "total",
        "formula": "sum_after_9_steps = sum of first 10 terms",
        "value": sum_after_steps(9),
        "uses": "start nine, nine as step-count, step six, get total",
        "assumptions": 1,
        "fit": "strong if `nine step six` means 9 steps of size 6",
    },
)


def score_candidate(candidate):
    score = 0
    if candidate["kind"] == "total":
        score += 5
    score += 3
    score -= 2 * candidate["assumptions"]
    return score


def write_report():
    ordered = sorted(PROCEDURES, key=score_candidate, reverse=True)
    lines = [
        "# Integer-Step Procedures",
        "",
        "Minimal-assumption procedure candidates built only from the current winning skeleton:",
        "",
        "- `find start nine`",
        "- `nine step six`",
        "- `get nine total`",
        "- `step baseten integer`",
        "",
        "These candidates deliberately avoid using detached layers like `hexadecimal`, `decimal`, or `three ten hundred`.",
        "",
        "## Ranked Candidates",
        "",
        "| Rank | Candidate | Value | Formula | Score | Notes |",
        "| ---: | --- | ---: | --- | ---: | --- |",
    ]

    for index, candidate in enumerate(ordered, start=1):
        lines.append(
            f"| {index} | {candidate['name']} | {candidate['value']} | `{candidate['formula']}` | {score_candidate(candidate)} | {candidate['fit']} |"
        )

    lines.extend(["", "## Details", ""])

    for index, candidate in enumerate(ordered, start=1):
        hex_value = hex(candidate["value"])
        lines.append(f"### {index}. {candidate['name']}")
        lines.append("")
        lines.append(f"- value: `{candidate['value']}`")
        lines.append(f"- hex: `{hex_value}`")
        lines.append(f"- formula: `{candidate['formula']}`")
        lines.append(f"- clue use: {candidate['uses']}")
        lines.append(f"- assumption count: {candidate['assumptions']}")
        lines.append(f"- fit note: {candidate['fit']}")
        lines.append("")

    lines.extend(
        [
            "## Current Read",
            "",
            "The two strongest minimal-assumption concrete readings are:",
            "",
            "- total of first 9 terms = `297`",
            "- total after 9 steps = `360`",
            "",
            "These use the current procedure skeleton more directly than the term-only readings because they satisfy `get ... total` without adding extra machinery.",
        ]
    )

    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    write_report()
    print(f"Saved report to {REPORT_PATH}")


if __name__ == "__main__":
    main()
