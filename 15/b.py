from pathlib import Path
import re
from utils import h

path = Path(__file__).parent / "input.txt"

seeds = path.read_text().split(",")
boxes = [[] for _ in range(256)]

for seed in seeds:
    label = re.match(r"([a-z]+)", seed).group(0)
    k = h(label)
    box = boxes[k]

    if "=" in seed:
        lens = (label, int(seed[-1]))

        replaced = False
        for i, _lens in enumerate(box):
            if _lens[0] == label:
                box[i] = lens
                replaced = True
                break

        if not replaced:
            box.append(lens)

    else:
        boxes[k] = [b for b in boxes[k] if b[0] != label]

power = 0
for i, box in enumerate(boxes):
    for j, lens in enumerate(box):
        power += (i + 1) * (j + 1) * lens[1]

print(power)
