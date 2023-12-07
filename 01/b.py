import re

digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def input(path):
    with open(path) as f:
        for line in f:
            yield line.strip().lower()


def find_substr(word, subs):
    results = []
    n = len(word)
    for sub in subs:
        x, i = len(sub), 0
        while i <= n - x:
            if word[i : i + x] == sub:
                results.append([sub, i])
            i += 1
    return results


def solve(path):
    b = 0
    for line in input(path):
        found = find_substr(line, digits.keys())
        found = [[digits[f[0]], f[1]] for f in found]
        found += find_substr(line, digits.values())
        found = sorted(found, key=lambda f: f[1])
        b += int(found[0][0] + found[-1][0])

    return b


if __name__ == "__main__":
    print(solve("./b.txt"))
