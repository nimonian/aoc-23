from pathlib import Path
from utils import get_tilings, overwrite

path = Path(__file__).parent / "input.txt"
lines = path.read_text().splitlines()
answer = 0


def compare(s, candidate):
    for x, y in zip(s, candidate):
        if x != y and x != "?":
            return False
    return True


for line in lines:
    # parse the data
    parts = line.split(" ")
    s = parts[0]
    nums = [int(x) for x in parts[1].split(",")]

    # create the tiles
    tiles = ["#" * n for n in nums]
    for i in range(len(tiles) - 1):
        tiles[i] += "."

    # get the tiling offsets
    tilings = get_tilings(len(s), tuple(len(tile) for tile in tiles))

    # check validity
    for tiling in tilings:
        candidate = ["." for _ in s]
        for tile, offset in zip(tiles, tiling):
            candidate = overwrite(candidate, tile, offset)
        candidate = "".join(candidate)

        answer += compare(s, candidate)

print(answer)
