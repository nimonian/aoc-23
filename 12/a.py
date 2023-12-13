from pathlib import Path
from utils import count_arrangements

path = Path(__file__).parent / "input.txt"
lines = path.read_text().splitlines()
answer = 0


for line in lines:
    parts = line.split(" ")
    s = parts[0]
    nums = [int(x) for x in parts[1].split(",")]
    answer += count_arrangements(s, nums)


print(answer)
