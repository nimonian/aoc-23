from time import time
from pathlib import Path
import re
from math import gcd
from functools import reduce

then = time()

path = (Path(__file__).parent / "./input.txt").resolve()
lines = path.read_text().split("\n\n")

# get directions
rl = lines[0]
rl = [0 if dir == "L" else 1 for dir in rl]

# get nodes
nodes = lines[1].split("\n")
nodes = [re.findall(r"([A-Z]+)", node) for node in nodes]
nodes = {node[0]: (node[1], node[2]) for node in nodes}

locs = [loc for loc in nodes.keys() if loc[-1] == "A"]
results = []


# least common multiple
def lcm(x, y):
    return x * y // gcd(x, y)


def lcm_list(nums):
    return reduce(lcm, nums)


for loc in locs:
    count = 0
    while loc[-1] != "Z":
        dir = rl[count % len(rl)]
        loc = nodes[loc][dir]
        count += 1
    results.append(count)

print(lcm_list(results))
print(time() - then, "s")
