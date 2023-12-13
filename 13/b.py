from pathlib import Path
from utils import find_symmetry
from time import time

then = time()

file = Path(__file__).parent / "input.txt"
patterns = [pattern.splitlines() for pattern in file.read_text().split("\n\n")]
multipliers = {"r": 100, "c": 1}


def alternatives(pattern):
    for r, row in enumerate(pattern):
        for c, char in enumerate(row):
            alt = [list(row) for row in pattern]
            alt[r][c] = "#."[".#".index(char)]
            yield ["".join(_r) for _r in alt]


answer = 0
for pattern in patterns:
    old = find_symmetry(pattern)

    for alt in alternatives(pattern):
        sym = find_symmetry(alt, (old,))
        if sym:
            answer += sym[1] * multipliers[sym[0]]
            break

print(answer)
print(time() - then, "s")
