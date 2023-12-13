from pathlib import Path
from utils import find_symmetry


file = Path(__file__).parent / "input.txt"
patterns = [pattern.splitlines() for pattern in file.read_text().split("\n\n")]
multipliers = {"r": 100, "c": 1}

answer = 0
for pattern in patterns:
    sym = find_symmetry(pattern)
    answer += sym[1] * multipliers[sym[0]]

print(answer)
