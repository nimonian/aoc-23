from pathlib import Path

path = Path(__file__).parent / "test_input.txt"
grid = [list(line) for line in path.read_text().splitlines()]
grid = [[int(x) for x in line] for line in grid]

up, down, left, right = (-1, 0), (1, 0), (0, -1), (0, 1)

rows = range(0, len(grid))
cols = range(0, len(grid[0]))


Q = {(r, c): float("inf") for c in cols for r in rows}
Q[(0, 0)] = grid[0][0]

while Q:
    u = min(Q, key=Q.get)

    for dr, dc in [up, down, left, right]:
        r, c = u[0] + dr, u[1] + dc

        if (r, c) not in Q:
            continue

        if Q[(r, c)] > Q[u] + grid[r][c]:
            Q[(r, c)] = Q[u] + grid[r][c]

    grid[u[0]][u[1]] = Q[u]
    del Q[u]

for line in grid:
    print(line)
