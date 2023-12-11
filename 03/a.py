from typing import List


def input(path: str) -> List[List[str]]:
    grid = []
    with open(path) as f:
        for line in f:
            grid.append(list(line.strip()))
    return grid


def issymbol(char: str) -> bool:
    return (not char.isdigit()) and (char != ".")


def getboundary(grid, r, c):
    boundary = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if (
                -1 < (r + dr) < len(grid)
                and -1 < (c + dc) < len(grid[r])
                and not (dr == 0 and dc == 0)
            ):
                boundary.append(grid[r + dr][c + dc])
    return boundary


def solve(path: str) -> int:
    answer, grid = 0, input(path)

    for r in range(len(grid)):
        num, flag = "", 0

        for c in range(len(grid[r])):
            char = grid[r][c]

            if char.isdigit():
                num += char
                if flag == 0:
                    boundary = getboundary(grid, r, c)
                    flag = int(any(issymbol(b) for b in boundary))

            if not char.isdigit() or c == len(grid[r]) - 1:
                if len(num) > 0:
                    answer += int(num) * flag
                num, flag = "", 0

    return answer


if __name__ == "__main__":
    print(solve("./input.txt"))
