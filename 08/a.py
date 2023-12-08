from time import time
from pathlib import Path
import re

then = time()

path = (Path(__file__).parent / "./input.txt").resolve()
lines = path.read_text().split("\n\n")

# get directions
rl = lines[0]
rl = [0 if dir == "L" else 1 for dir in rl]

# get and parse nodes
nodes = lines[1].split("\n")
nodes = [re.findall(r"([A-Z]+)", node) for node in nodes]
nodes = {node[0]: (node[1], node[2]) for node in nodes}

loc = "AAA"
count = 0

while loc != "ZZZ":
    dir = rl[count % len(rl)]
    loc = nodes[loc][dir]
    count += 1

print(count)
print(time() - then, "s")
