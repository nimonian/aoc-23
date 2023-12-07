import re


def input(path):
    with open(path) as f:
        for line in f:
            yield line.strip().lower()


def solve(path):
    a = 0
    for line in input(path):
        nums = re.findall(r"(\d)", line)
        a += int(nums[0] + nums[-1])

    return a


if __name__ == "__main__":
    print(solve("./a.txt"))
