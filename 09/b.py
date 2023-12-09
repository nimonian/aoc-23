from pathlib import Path
from sympy import Matrix

path = Path(__file__).parent / "input.txt"
lines = path.read_text().split("\n")

answer = 0

for line in lines:
    sample = [int(d) for d in line.split(" ")]

    diffs, n = sample, 0
    while set(diffs) != set([0]):
        diffs = [y - x for x, y in zip(diffs[:-1], diffs[1:])]
        n += 1

    A = Matrix([[x**k for k in range(n)] for x in range(n)])
    B, v = A.inv(), Matrix(sample[:n])

    answer += sum([c * (-1) ** i for i, c in enumerate(B * v)])

print(answer, "\n")
