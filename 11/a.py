from pathlib import Path
from time import time

then = time()

file = (Path(__file__).parent / "./input.txt").resolve(0)
M = file.read_text().splitlines()

dot_rows = set(range(len(M)))
dot_cols = set(range(len(M[0])))

stars = []
for r, row in enumerate(M):
    for c, char in enumerate(row):
        if char == "#":
            stars.append((r, c))
            dot_rows.discard(r)
            dot_cols.discard(c)


D = 0  # the total distance
for i, s1 in enumerate(stars):
    for s2 in stars[i + 1 :]:
        dr = range(min(s1[0], s2[0]), max(s1[0], s2[0]))
        dc = range(min(s1[1], s2[1]), max(s1[1], s2[1]))
        D += len(dr) + len(dc)

        for r in dot_rows:
            if r in dr:
                D += 1

        for c in dot_cols:
            if c in dc:
                D += 1

print(D)
print(time() - then, "s")
