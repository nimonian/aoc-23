import re

with open("./input.txt") as f:
    almanac = f.read().strip().split("\n\n")
    seeds = [int(s) for s in re.findall(r"(\d+)", almanac[0])]
    maps = []
    for i in range(1, len(almanac)):
        txt = almanac[i].strip().split("\n")[1:]
        m = [[int(s) for s in re.findall(r"(\d+)", line)] for line in txt]
        maps.append(m)


a = float("inf")
for s in seeds:
    for m in maps:
        for y, x, r in m:
            if x <= s < x + r:
                s += y - x
                break
    a = min(s, a)

print(a)
