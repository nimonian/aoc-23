import re


def input(path):
    with open(path) as f:
        for line in f:
            yield line.strip()


def solve(path):
    answer = 0
    for line in input(path):
        R = map(int, re.findall(r"(\d+) red", line))
        G = map(int, re.findall(r"(\d+) green", line))
        B = map(int, re.findall(r"(\d+) blue", line))
        answer += max(R) * max(G) * max(B)
    return answer


if __name__ == "__main__":
    print(solve("./b.txt"))
