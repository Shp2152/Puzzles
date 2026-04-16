import csv
import string
from collections import defaultdict
from pathlib import Path

import cmudict


SCRIPT_DIR = Path(__file__).resolve().parent
CSV_PATH = SCRIPT_DIR / "can u dig it.csv"
ALL_WORDS_CSV = SCRIPT_DIR / "all_found_words.csv"
ALL_WORD_INSTANCES_CSV = SCRIPT_DIR / "all_found_word_instances.csv"
CHEMISTRY_TERM_CHECK_CSV = SCRIPT_DIR / "chemistry_term_check.csv"
CHEMISTRY_FOUND_WORDS_CSV = SCRIPT_DIR / "chemistry_found_words.csv"
MAX_WORD_LEN = 20

DIRS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]

PERIODIC_ELEMENTS = [
    "hydrogen", "helium", "lithium", "beryllium", "boron", "carbon",
    "nitrogen", "oxygen", "fluorine", "neon", "sodium", "magnesium",
    "aluminum", "silicon", "phosphorus", "sulfur", "chlorine", "argon",
    "potassium", "calcium", "scandium", "titanium", "vanadium", "chromium",
    "manganese", "iron", "cobalt", "nickel", "copper", "zinc", "gallium",
    "germanium", "arsenic", "selenium", "bromine", "krypton", "rubidium",
    "strontium", "yttrium", "zirconium", "niobium", "molybdenum",
    "technetium", "ruthenium", "rhodium", "palladium", "silver", "cadmium",
    "indium", "tin", "antimony", "tellurium", "iodine", "xenon", "cesium",
    "barium", "lanthanum", "cerium", "praseodymium", "neodymium",
    "promethium", "samarium", "europium", "gadolinium", "terbium",
    "dysprosium", "holmium", "erbium", "thulium", "ytterbium", "lutetium",
    "hafnium", "tantalum", "tungsten", "rhenium", "osmium", "iridium",
    "platinum", "gold", "mercury", "thallium", "lead", "bismuth",
    "polonium", "astatine", "radon", "francium", "radium", "actinium",
    "thorium", "protactinium", "uranium", "neptunium", "plutonium",
    "americium", "curium", "berkelium", "californium", "einsteinium",
    "fermium", "mendelevium", "nobelium", "lawrencium", "rutherfordium",
    "dubnium", "seaborgium", "bohrium", "hassium", "meitnerium",
    "darmstadtium", "roentgenium", "copernicium", "nihonium", "flerovium",
    "moscovium", "livermorium", "tennessine", "oganesson",
]

ELEMENT_VARIANTS = [
    "aluminium", "sulphur", "caesium",
]

CHEMISTRY_CORE_TERMS = [
    "atom", "atoms", "bond", "bonds", "compound", "compounds", "electron",
    "electrons", "element", "elements", "gas", "gases", "ion", "ions",
    "isotope", "isotopes", "metal", "metals", "molecule", "molecules",
    "noble", "orbit", "orbits", "periodic", "proton", "protons",
    "react", "reaction", "reactions", "salt", "salts", "table", "valence",
]


def build_element_stems():
    stems = set()
    for element in PERIODIC_ELEMENTS:
        if element.endswith("ium") and len(element) > 6:
            stems.add(element[:-3])
    return sorted(stems)


CHEMISTRY_BINS = {
    "periodic_elements": PERIODIC_ELEMENTS,
    "element_variants": ELEMENT_VARIANTS,
    "element_ium_stems": build_element_stems(),
    "core_chemistry_terms": CHEMISTRY_CORE_TERMS,
}


def load_grid():
    with CSV_PATH.open(newline="", encoding="utf-8") as handle:
        grid = [row for row in csv.reader(handle)]

    rows = len(grid)
    cols = len(grid[0])
    col_labels = string.ascii_uppercase[:cols]

    neighbors = {}
    for r in range(rows):
        for c in range(cols):
            nbrs = []
            for dr, dc in DIRS:
                rr = r + dr
                cc = c + dc
                if 0 <= rr < rows and 0 <= cc < cols:
                    nbrs.append((rr, cc))
            neighbors[(r, c)] = nbrs

    return grid, rows, cols, col_labels, neighbors


def coord(r, c, col_labels):
    return f"{col_labels[c]}{r + 1}"


def path_to_coords(path, col_labels):
    return [coord(r, c, col_labels) for r, c in path]


def build_dictionary():
    raw_words = set(word.lower() for word in cmudict.dict().keys())

    words = set()
    for word in raw_words:
        normalized = word.replace("'", "")
        if normalized.isalpha() and len(normalized) >= 3:
            words.add(normalized)

    prefixes = set()
    for word in words:
        for idx in range(1, len(word) + 1):
            prefixes.add(word[:idx])

    return words, prefixes


def find_all_words(grid, neighbors, words, prefixes):
    word_paths = defaultdict(list)

    def dfs_word(r, c, used, current, path):
        ch = grid[r][c].lower()
        current += ch
        path = path + [(r, c)]
        used = used | {(r, c)}

        if current not in prefixes:
            return

        if current in words:
            word_paths[current].append(path)

        if len(current) >= MAX_WORD_LEN:
            return

        for rr, cc in neighbors[(r, c)]:
            if (rr, cc) not in used:
                dfs_word(rr, cc, used, current, path)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c].isalpha():
                dfs_word(r, c, set(), "", [])

    return word_paths


def write_all_words_csv(all_found, col_labels):
    with ALL_WORDS_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["word", "length", "total_paths", "sample_path"])
        for word, paths in all_found:
            sample_path = " -> ".join(path_to_coords(paths[0], col_labels))
            writer.writerow([word, len(word), len(paths), sample_path])


def write_all_word_instances_csv(all_found, col_labels):
    with ALL_WORD_INSTANCES_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["word", "path_index", "length", "path"])
        for word, paths in all_found:
            for idx, path in enumerate(paths, start=1):
                writer.writerow([word, idx, len(word), " -> ".join(path_to_coords(path, col_labels))])


def compare_chemistry_bins(word_paths, col_labels):
    found_rows = []
    check_rows = []

    for bin_name, terms in CHEMISTRY_BINS.items():
        for term in terms:
            paths = word_paths.get(term, [])
            found = bool(paths)
            sample_path = ""
            if found:
                sample_path = " -> ".join(path_to_coords(paths[0], col_labels))
                found_rows.append({
                    "bin": bin_name,
                    "term": term,
                    "length": len(term),
                    "total_paths": len(paths),
                    "sample_path": sample_path,
                })
            check_rows.append({
                "bin": bin_name,
                "term": term,
                "length": len(term),
                "found": found,
                "total_paths": len(paths),
                "sample_path": sample_path,
            })

    check_rows.sort(key=lambda row: (row["bin"], not row["found"], -row["length"], row["term"]))
    found_rows.sort(key=lambda row: (row["bin"], -row["length"], row["term"]))
    return check_rows, found_rows


def write_chemistry_check_csv(check_rows):
    with CHEMISTRY_TERM_CHECK_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["bin", "term", "length", "found", "total_paths", "sample_path"])
        for row in check_rows:
            writer.writerow([
                row["bin"],
                row["term"],
                row["length"],
                "yes" if row["found"] else "no",
                row["total_paths"],
                row["sample_path"],
            ])


def write_chemistry_found_csv(found_rows):
    with CHEMISTRY_FOUND_WORDS_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["bin", "term", "length", "total_paths", "sample_path"])
        for row in found_rows:
            writer.writerow([
                row["bin"],
                row["term"],
                row["length"],
                row["total_paths"],
                row["sample_path"],
            ])


def print_summary(all_found, found_rows, check_rows):
    print(f"Found {len(all_found)} unique words.")
    print(f"Saved unique-word summary to {ALL_WORDS_CSV.name}")
    print(f"Saved per-path word instances to {ALL_WORD_INSTANCES_CSV.name}")
    print(f"Saved chemistry term audit to {CHEMISTRY_TERM_CHECK_CSV.name}")
    print(f"Saved found chemistry terms to {CHEMISTRY_FOUND_WORDS_CSV.name}")

    print("\n=== LONGEST WORDS FOUND ===")
    for word, paths in all_found[:50]:
        print(f"{word} | length={len(word)} | total_paths={len(paths)}")

    print("\n=== CHEMISTRY TERMS FOUND ===")
    if not found_rows:
        print("No chemistry terms from the configured bins were found.")
    else:
        for row in found_rows[:100]:
            print(f"{row['bin']} | {row['term']} | length={row['length']} | total_paths={row['total_paths']}")

    print("\n=== CHEMISTRY BIN COUNTS ===")
    by_bin = defaultdict(lambda: {"found": 0, "total": 0})
    for row in check_rows:
        by_bin[row["bin"]]["total"] += 1
        if row["found"]:
            by_bin[row["bin"]]["found"] += 1
    for bin_name in CHEMISTRY_BINS:
        counts = by_bin[bin_name]
        print(f"{bin_name}: {counts['found']} found / {counts['total']} checked")


def main():
    grid, _, _, col_labels, neighbors = load_grid()
    words, prefixes = build_dictionary()
    word_paths = find_all_words(grid, neighbors, words, prefixes)

    all_found = sorted(word_paths.items(), key=lambda item: (-len(item[0]), item[0]))
    write_all_words_csv(all_found, col_labels)
    write_all_word_instances_csv(all_found, col_labels)

    check_rows, found_rows = compare_chemistry_bins(word_paths, col_labels)
    write_chemistry_check_csv(check_rows)
    write_chemistry_found_csv(found_rows)
    print_summary(all_found, found_rows, check_rows)


if __name__ == "__main__":
    main()
