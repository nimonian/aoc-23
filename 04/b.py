import re
from utils import input, to_nums, count_matches


def solve(path):
    cards = input(path)
    memo = {k + 1: 1 for k in range(len(cards))}
    for card, line in enumerate(input(path)):
        card = card + 1
        win, mine = [to_nums(s) for s in line.split(":")[1].split("|")]
        n = count_matches(win, mine)
        for i in range(card + 1, min(len(cards) + 1, card + n + 1)):
            memo[i] += memo[card]
    return sum(memo.values())


if __name__ == "__main__":
    print(solve("./input.txt"))
