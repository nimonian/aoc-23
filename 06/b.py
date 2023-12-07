from pathlib import Path
import re

txt = (Path(__file__).parent / "input.txt").read_text().replace(" ", "")
t, d = [int(x) for x in re.findall(r"(\d+)", txt)]
t0, t1 = [(t + i * (t**2 - 4 * d) ** 0.5) / 2 for i in [-1, 1]]
print(int(t1) - int(t0) - (t1 == int(t1)))
