import re
from pathlib import Path


def input(path):
    path = (Path(__file__).parent / path).resolve()
    with open(path) as f:
        return [line.strip() for line in f]


def to_nums(s: str):
    nums = re.findall(r"(\d+)", s)
    return [int(d) for d in nums]


def count_matches(A: list, B: list):
    return len(set(A).intersection(set(B)))
