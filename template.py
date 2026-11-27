"""Advent of Code starter template.

Copy this file into a day folder (e.g. 2025/day01/solution.py), then fill in part1/part2.

    python solution.py              # checks EXAMPLES, then solves input.txt
    python solution.py sample.txt   # just solves a different file, no checks
"""
import re
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path


# ---------- Input ----------

def read_input(name="input.txt"):
    # Resolve relative to this script, so it works no matter which folder you run it from
    return (Path(__file__).parent / name).read_text().rstrip("\n")


# ---------- Parsing helpers ----------

def lines(text):
    """'a\\nb\\nc' -> ['a', 'b', 'c']"""
    return text.splitlines()


def blocks(text):
    """Sections separated by blank lines -> list of lists of lines."""
    return [block.splitlines() for block in text.split("\n\n")]


def ints(s):
    """Every integer in a string, including negatives: 'x=-3, y=14' -> [-3, 14]"""
    return [int(n) for n in re.findall(r"-?\d+", s)]


def int_lines(text):
    """One list of ints per line: '1 2 3\\n4 5 6' -> [[1, 2, 3], [4, 5, 6]]"""
    return [ints(line) for line in lines(text)]


def grid(text):
    """Character grid as a dict {(row, col): char}. Missing keys are out of bounds."""
    return {(r, c): ch for r, line in enumerate(lines(text)) for c, ch in enumerate(line)}


def find_all(g, target):
    """All positions in a grid holding a given character."""
    return [pos for pos, ch in g.items() if ch == target]


# ---------- Grid movement ----------

# (row, col) offsets: up, right, down, left
DIRS4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIRS8 = DIRS4 + [(-1, -1), (-1, 1), (1, 1), (1, -1)]


def neighbors(pos, g=None, dirs=DIRS4):
    """Adjacent positions; if a grid is given, only those inside it."""
    r, c = pos
    for dr, dc in dirs:
        nxt = (r + dr, c + dc)
        if g is None or nxt in g:
            yield nxt


# ---------- Solution ----------

def parse(text):
    return lines(text)


def part1(data):
    result = 0
    return result


def part2(data):
    result = 0
    return result


# Example inputs saved from the puzzle page, with the answers the puzzle gives for them.
# Leave an answer as None to skip checking that part (e.g. before part 2 is unlocked).
# If part 2 uses a different example, add it as another entry: "sample2.txt": (None, 42)
EXAMPLES = {
    "sample.txt": (None, None),
}


def check_examples():
    for name, expected in EXAMPLES.items():
        if expected == (None, None):
            continue
        if not (Path(__file__).parent / name).exists():
            print(f"{name}: file not found, skipping")
            continue
        data = parse(read_input(name))
        for part, solve, want in [(1, part1, expected[0]), (2, part2, expected[1])]:
            if want is None:
                continue
            got = solve(data)
            status = "PASS" if str(got) == str(want) else f"FAIL (expected {want})"
            print(f"{name} part {part}: {got}  {status}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        data = parse(read_input(sys.argv[1]))
    else:
        check_examples()
        data = parse(read_input())
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
