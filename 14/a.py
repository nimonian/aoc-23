from pathlib import Path
from utils import rotate, tilt, calculate_load

path = Path(__file__).parent / "input.txt"
dish = path.read_text().splitlines()
dish = [list(row) for row in dish]

# get N on the left
for _ in range(3):
    dish = rotate(dish)

dish = tilt(dish)

# get N back on top
dish = rotate(dish)

print(calculate_load(dish))
