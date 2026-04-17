from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
REPORT_PATH = SCRIPT_DIR / "operation_experiments" / "detached_clue_integration.md"

START = 9
STEP = 6


def term_from_term_index(term_index):
    return START + STEP * (term_index - 1)


def sum_first_terms(term_count):
    return term_count * (2 * START + (term_count - 1) * STEP) // 2


def count_terms_leq(bound):
    if bound < START:
        return 0
    return ((bound - START) // STEP) + 1


def last_term_leq(bound):
    count = count_terms_leq(bound)
    return term_from_term_index(count) if count else None


def sum_terms_leq(bound):
    count = count_terms_leq(bound)
    return sum_first_terms(count) if count else 0


DIRECT_REPRESENTATION_VALUES = (
    {
        "name": "hexadecimal ten ten ten",
        "value": int("AAA", 16),
        "why": "Interpret `ten ten ten` as `A A A` under the `hexadecimal` label.",
    },
    {
        "name": "decimal ten ten ten",
        "value": int("101010", 10),
        "why": "Interpret `ten ten ten` literally as decimal `10 10 10`.",
    },
)

INTEGRATIONS = (
    {
        "name": "3 terms total",
        "family": "payload",
        "value": sum_first_terms(3),
        "formula": "sum of first 3 terms of 9, 15, 21, ...",
        "uses": "Treat `three` as term-count.",
    },
    {
        "name": "10 terms total",
        "family": "payload",
        "value": sum_first_terms(10),
        "formula": "sum of first 10 terms of 9, 15, 21, ...",
        "uses": "Treat `ten` as term-count.",
    },
    {
        "name": "100 terms total",
        "family": "payload",
        "value": sum_first_terms(100),
        "formula": "sum of first 100 terms of 9, 15, 21, ...",
        "uses": "Treat `hundred` as term-count.",
    },
    {
        "name": "Total up to 100",
        "family": "payload",
        "value": sum_terms_leq(100),
        "formula": "sum terms <= 100 in the 9 + 6k sequence",
        "uses": "Treat `hundred` as upper bound.",
    },
    {
        "name": "Count up to 100",
        "family": "payload",
        "value": count_terms_leq(100),
        "formula": "count terms <= 100 in the 9 + 6k sequence",
        "uses": "Treat `hundred` as upper bound and count instead of total.",
    },
    {
        "name": "Last term up to 100",
        "family": "payload",
        "value": last_term_leq(100),
        "formula": "last term <= 100 in the 9 + 6k sequence",
        "uses": "Treat `hundred` as upper bound and keep the terminal term.",
    },
    {
        "name": "Hex ten terms total",
        "family": "representation",
        "value": sum_first_terms(16),
        "formula": "sum of first 16 terms of 9, 15, 21, ...",
        "uses": "Treat `hexadecimal ten` as decimal 16 terms.",
    },
    {
        "name": "Hex ten count to 100",
        "family": "representation",
        "value": count_terms_leq(100),
        "formula": "count terms <= 100 in the 9 + 6k sequence",
        "uses": "Observe that the count to 100 is 16, i.e. hexadecimal ten.",
    },
)


def score_row(row):
    score = 0
    if row["family"] == "representation" and row["name"] == "Hex ten count to 100":
        score += 6
    if row["family"] == "representation" and row["name"] == "Hex ten terms total":
        score += 5
    if row["family"] == "payload" and row["name"] == "Total up to 100":
        score += 6
    if row["family"] == "payload" and row["name"] == "10 terms total":
        score += 5
    if row["family"] == "payload" and row["name"] == "3 terms total":
        score += 2

    decimal_text = str(row["value"])
    hex_text = hex(row["value"])[2:].upper()

    if hex_text == "360":
        score += 6
    if row["value"] == 360:
        score += 4
    if row["value"] == 16:
        score += 5
    if row["value"] == 864:
        score += 4
    if decimal_text in {"360", "864", "16", "45"}:
        score += 1
    return score


def write_report():
    rows = []
    for item in INTEGRATIONS:
        rows.append(
            {
                **item,
                "decimal": item["value"],
                "hex": hex(item["value"])[2:].upper(),
            }
        )

    rows.sort(key=score_row, reverse=True)

    lines = [
        "# Detached Clue Integration",
        "",
        "This report forces detached clues into a few natural arithmetic-progression interpretations of the current skeleton.",
        "",
        "Fixed skeleton used here:",
        "",
        "- start = 9",
        "- step = 6",
        "- seek some total / count / terminal value",
        "- output as base-10 integer",
        "",
        "Detached clues being forced in:",
        "",
        "- `three ten hundred` as counts or bounds",
        "- `hexadecimal` / `decimal` as representation-derived counts or values",
        "",
        "## Ranked Integrations",
        "",
        "| Rank | Construction | Family | Decimal | Hex | Score | Interpretation |",
        "| ---: | --- | --- | ---: | --- | ---: | --- |",
    ]

    for index, row in enumerate(rows, start=1):
        lines.append(
            f"| {index} | {row['name']} | {row['family']} | {row['decimal']} | `{row['hex']}` | {score_row(row)} | {row['uses']} |"
        )

    lines.extend(["", "## Direct Representation Values", ""])
    for item in DIRECT_REPRESENTATION_VALUES:
        lines.append(f"- `{item['name']}` -> `{item['value']}` (hex `{hex(item['value'])[2:].upper()}`): {item['why']}")

    lines.extend(["", "## Details", ""])
    for index, row in enumerate(rows, start=1):
        lines.append(f"### {index}. {row['name']}")
        lines.append("")
        lines.append(f"- decimal value: `{row['decimal']}`")
        lines.append(f"- hex value: `{row['hex']}`")
        lines.append(f"- formula: {row['formula']}")
        lines.append(f"- clue use: {row['uses']}")
        lines.append(f"- heuristic score: {score_row(row)}")
        lines.append("")

    lines.extend(
        [
            "## Current Read",
            "",
            "The most notable constructions from this forced-integration pass are:",
            "",
            "- `10 terms total = 360`",
            "- `total up to 100 = 864 = 0x360`",
            "- `count up to 100 = 16 = hexadecimal ten`",
            "- `hex ten terms total = 864`",
            "",
            "These are not proved solutions. They are the first somewhat usable constructions that let the detached layers interact with the step-6 skeleton in a nontrivial way.",
        ]
    )

    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    write_report()
    print(f"Saved report to {REPORT_PATH}")


if __name__ == "__main__":
    main()
