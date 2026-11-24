"""Advent of Code minimal starter template.

Copy this file into a day folder (e.g. 2025/day01/solution.py), then fill in part1/part2.
Add helpers as you find yourself rewriting the same parsing code; see template.py for ideas.

    python solution.py              # reads input.txt next to this file
    python solution.py sample.txt   # reads a different file, e.g. the example from the puzzle
"""
import re
import sys
from pathlib import Path


def read_input():
    # Resolve relative to this script, so it works no matter which folder you run it from
    name = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    return (Path(__file__).parent / name).read_text().rstrip("\n")


def lines(text):
    """'a\\nb\\nc' -> ['a', 'b', 'c']"""
    return text.splitlines()


def ints(s):
    """Every integer in a string, including negatives: 'x=-3, y=14' -> [-3, 14]"""
    return [int(n) for n in re.findall(r"-?\d+", s)]


def part1(data):
    result = 0
    return result


def part2(data):
    result = 0
    return result


if __name__ == "__main__":
    data = lines(read_input())
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
