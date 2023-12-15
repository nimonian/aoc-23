from pathlib import Path
from time import time
from utils import rotate, tilt, load

path = Path(__file__).parent / "input.txt"
dish = path.read_text().splitlines()
cycles = 10**9
then = time()


def cycle(dish):
    for _ in range(4):
        dish = tilt(rotate(dish))
    return dish


# get N on the bottom
dish = rotate(dish, 2)

# floyd cycle detection
dish = cycle(dish)
fast = cycle(dish)

i = 1
while fast != dish:
    dish = cycle(dish)
    fast = cycle(cycle(fast))
    i += 1

r = cycles % i

for _ in range(r):
    dish = cycle(dish)

dish = rotate(dish, 2)
print(load(dish))

print(time() - then, "s")
