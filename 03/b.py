def get_nums(line: str):
    nums = []
    i = 0
    while i < len(line):
        if line[i].isdigit():
            j = 0
            while i + j < len(line) and line[i + j].isdigit():
                j += 1
            nums.append((i, i + j - 1))
            i = i + j
        else:
            i += 1
    return nums


def get_num(r, num, grid):
    digits = grid[r][num[0] : num[1] + 1]
    return int("".join(digits))


def get_boundary(r: int, num: list, grid):
    boundary = []
    top = r > 0
    bottom = r < len(grid) - 1
    left = num[0] > 0
    right = num[-1] < len(grid[r]) - 1

    if top:
        boundary += [(r - 1, c) for c in range(num[0], num[1] + 1)]

    if bottom:
        boundary += [(r + 1, c) for c in range(num[0], num[1] + 1)]

    if left:
        boundary.append((r, num[0] - 1))
        if top:
            boundary.append((r - 1, num[0] - 1))
        if bottom:
            boundary.append((r + 1, num[0] - 1))

    if right:
        boundary.append((r, num[-1] + 1))
        if top:
            boundary.append((r - 1, num[-1] + 1))
        if bottom:
            boundary.append((r + 1, num[-1] + 1))

    return boundary


def input(path: str):
    grid = []
    with open(path) as f:
        for line in f:
            grid.append(list(line.strip()))
    return grid


def solve(path: str):
    grid = input(path)
    memo = {}

    for r in range(len(grid)):
        nums = get_nums(grid[r])

        for num in nums:
            boundary = get_boundary(r, num, grid)
            for _r, _c in boundary:
                k = f"({_r},{_c})"
                if grid[_r][_c] == "*":
                    if k in memo:
                        memo[k].append(get_num(r, num, grid))
                    else:
                        memo[k] = [get_num(r, num, grid)]

    answer = 0
    for k in memo:
        if len(memo[k]) == 2:
            answer += memo[k][0] * memo[k][1]

    return answer


if __name__ == "__main__":
    print(solve("./input.txt"))
