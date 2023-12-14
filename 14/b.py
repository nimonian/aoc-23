# 102347 too high
from pathlib import Path
from time import time
from utils import rotate, tilt, calculate_load


path = Path(__file__).parent / "input.txt"
dish = path.read_text().splitlines()
dish = [list(row) for row in dish]
cycles = 10**9

then = time()


def cycle(dish):
    for _ in range(4):
        dish = rotate(dish)
        dish = tilt(dish)
    return dish


# get N on the bottom
dish = rotate(rotate(dish))

# find cycle
slow = cycle(dish)
fast = cycle(slow)

i = 1
while fast != slow:
    slow = cycle(slow)
    fast = cycle(cycle(fast))
    i += 1

# find cycles mod period
r = cycles % i

for _ in range(r):
    slow = cycle(slow)

slow = rotate(rotate(slow))
print(calculate_load(slow))
print(time() - then, "s")
