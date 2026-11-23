"""Advent of Code starter template.

Copy this file into a day folder (e.g. 2025/day01/solution.py), then fill in part1/part2.

    python solution.py              # reads input.txt next to this file
    python solution.py sample.txt   # reads a different file, e.g. the example from the puzzle
"""
import re
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path


# ---------- Input ----------

def read_input():
    # Resolve relative to this script, so it works no matter which folder you run it from
    name = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
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


if __name__ == "__main__":
    data = parse(read_input())
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
