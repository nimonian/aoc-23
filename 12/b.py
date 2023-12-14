from pathlib import Path
from utils import count_arrangements
from time import time

path = Path(__file__).parent / "input.txt"
lines = path.read_text().splitlines()
answer = 0

t0 = time()


for case, line in enumerate(lines):
    parts = line.split(" ")
    s = "?".join([parts[0]] * 5)
    nums = [int(x) for x in parts[1].split(",")] * 5
    a = count_arrangements(s, nums)
    print(line, a, time() - t0)
    answer += count_arrangements(s, nums)


print(answer)
