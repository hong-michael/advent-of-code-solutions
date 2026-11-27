"""Advent of Code minimal starter template.

Copy this file into a day folder (e.g. 2025/day01/solution.py), then fill in part1/part2.
Add helpers as you find yourself rewriting the same parsing code; see template.py for ideas.

    python solution.py              # checks EXAMPLES, then solves input.txt
    python solution.py sample.txt   # just solves a different file, no checks
"""
import re
import sys
from pathlib import Path


def read_input(name="input.txt"):
    # Resolve relative to this script, so it works no matter which folder you run it from
    return (Path(__file__).parent / name).read_text().rstrip("\n")


def lines(text):
    """'a\\nb\\nc' -> ['a', 'b', 'c']"""
    return text.splitlines()


def ints(s):
    """Every integer in a string, including negatives: 'x=-3, y=14' -> [-3, 14]"""
    return [int(n) for n in re.findall(r"-?\d+", s)]


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
