import re

r_max = 12
g_max = 13
b_max = 14


def input(path):
    with open(path) as f:
        for line in f:
            yield line.strip()


def solve(path):
    a = 0
    for line in input(path):
        R = map(int, re.findall(r"(\d+) red", line))
        if any(r > r_max for r in R):
            continue

        G = map(int, re.findall(r"(\d+) green", line))
        if any(g > g_max for g in G):
            continue

        B = map(int, re.findall(r"(\d+) blue", line))
        if any(b > b_max for b in B):
            continue

        n = int(re.search(r"Game (\d+)", line).group(1))
        a += n
    return a


if __name__ == "__main__":
    print(solve("./a.txt"))
