from pathlib import Path
from time import time

then = time()

file = (Path(__file__).parent / "./input.txt").resolve(0)
M = file.read_text().splitlines()

empty_rows = set(range(len(M)))
empty_cols = set(range(len(M[0])))

stars = []
for r, row in enumerate(M):
    for c, char in enumerate(row):
        if char == "#":
            stars.append((r, c))
            empty_rows.discard(r)
            empty_cols.discard(c)


D = 0
for i, s1 in enumerate(stars):
    for s2 in stars[i + 1 :]:
        dr = range(min(s1[0], s2[0]), max(s1[0], s2[0]))
        dc = range(min(s1[1], s2[1]), max(s1[1], s2[1]))

        D += len(dr) + len(dc)
        D += sum(1 for x in empty_rows if x in dr)
        D += sum(1 for x in empty_cols if x in dc)

print(D)
print(time() - then, "s")
