import re


class Batch:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def overlaps(self, batch):
        return self.start <= batch.end and self.end >= batch.start


class Func(Batch):
    def __init__(self, start, end, add=0):
        super().__init__(start, end)
        self.add = add

    def apply(self, x):
        return x + self.add


def get_identities(map):
    map = sorted(map, key=lambda f: f.start)

    from_neg_inf = Func(float("-inf"), map[0].start - 1)
    to_pos_inf = Func(map[-1].end + 1, float("inf"))

    identities = [from_neg_inf, to_pos_inf]

    for i in range(1, len(map) - 1):
        end, start = map[i].end, map[i + 1].start

        if start - end > 1:
            identities.append(Func(start, end))

    return identities


with open("./input.txt") as f:
    seeds, *almanac = f.read().split("\n\n")

seeds = [int(s) for s in re.findall(r"(\d+)", seeds)]

maps = []

for map in almanac:
    map = map.strip().split("\n")[1:]
    map = [[int(s) for s in re.findall(r"(\d+)", line)] for line in map]
    map = [Func(x, x + r - 1, y - x) for y, x, r in map]
    maps.append(map + get_identities(map))

batches = [Batch(s, s + r) for s, r in zip(seeds[::2], seeds[1::2])]

for map in maps:
    mapped = []

    for batch in batches:
        funcs = [f for f in map if f.overlaps(batch)]

        for f in funcs:
            start = f.apply(max(batch.start, f.start))
            end = f.apply(min(batch.end, f.end))
            mapped.append(Batch(start, end))

    batches = mapped

print(min(batch.start for batch in batches))
