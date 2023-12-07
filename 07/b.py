from pathlib import Path
from functools import cmp_to_key

input = Path(__file__).parent / "input.txt"
lines = [line.split(" ") for line in input.read_text().split("\n")]

values = {str(k): k for k in range(2, 10)}
values.update({k: 10 + i for i, k in enumerate("TJQKA")})
values["J"] = 1

scores = [(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 2, 2), (1, 1, 3), (2, 3), (1, 4), (5,)]


def get_signature(hand: str) -> dict:
    count = {}
    for card in hand:
        if card in count:
            count[card] += 1
        else:
            count[card] = 1

    if len(count.values()) == 1:
        return (5,)

    signature = sorted(count[card] for card in count.keys() if card != "J")
    signature[-1] += count["J"] if "J" in count else 0
    return tuple(signature)


def get_score(h):
    return scores.index(get_signature(h))


def compare(p1, p2):
    if p1["score"] > p2["score"]:
        return 1

    if p1["score"] < p2["score"]:
        return -1

    h1, h2 = [p["hand"] for p in [p1, p2]]
    for c1, c2 in zip(h1, h2):
        if values[c1] > values[c2]:
            return 1

        if values[c1] < values[c2]:
            return -1


def solve():
    players = [
        {"hand": line[0], "score": get_score(line[0]), "bid": int(line[1])}
        for line in lines
    ]

    players = sorted(players, key=cmp_to_key(compare))

    answer = sum((i + 1) * p["bid"] for i, p in enumerate(players))

    print(answer)


if __name__ == "__main__":
    solve()
