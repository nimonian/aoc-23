from pathlib import Path
import time

file = Path(__file__).parent / "input.txt"
lines = file.read_text().splitlines()
grid = [list(line) for line in lines]

row_range = range(len(grid))
col_range = range(len(grid[0]))

up, down, left, right = (-1, 0), (1, 0), (0, -1), (0, 1)

cells = {
    ".": {up: [up], down: [down], left: [left], right: [right]},
    "/": {up: [right], down: [left], left: [down], right: [up]},
    "\\": {up: [left], down: [right], left: [up], right: [down]},
    "|": {up: [up], down: [down], left: [up, down], right: [up, down]},
    "-": {up: [right, left], down: [right, left], left: [left], right: [right]},
}

paths = [{"p": (0, 0), "v": right}]
visited = {(0, 0): [right]}  # (0,0) visited moving right

while paths:
    path = paths.pop()
    r0, c0 = path["p"]
    for dr, dc in cells[grid[r0][c0]][path["v"]]:
        r, c = r0 + dr, c0 + dc

        if (dr, dc) in visited.get((r, c), []):
            continue  # we've been here in this direction before

        if r not in row_range or c not in col_range:
            continue  # out of bounds

        visited[(r, c)] = visited.get((r, c), []) + [(dr, dc)]
        paths.insert(0, {"p": (r, c), "v": (dr, dc)})

print(len(visited))


def draw_grid():
    grid = []
    for r in row_range:
        line = ""
        for c in col_range:
            if (r, c) in visited:
                line += "#"
            else:
                line += "."
        grid.append(line)

    path = Path(__file__).parent / "output.txt"
    path.write_text("\n".join(grid))


draw_grid()
