from pathlib import Path
from utils import h

file = Path(__file__).parent / "input.txt"
S = file.read_text().split(",")

print(sum(h(s) for s in S))
