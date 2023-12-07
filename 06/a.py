from pathlib import Path
import re

lines = (Path(__file__).parent / "input.txt").read_text().split("\n")
T = [int(t) for t in re.findall(r"(\d+)", lines[0])]
D = [int(d) for d in re.findall(r"(\d+)", lines[1])]
a = 1
for t, d in zip(T, D):
    t0, t1 = [(t + i * (t**2 - 4 * d) ** 0.5) / 2 for i in [-1, 1]]
    a *= int(t1) - int(t0) - (t1 == int(t1))
print(a)
