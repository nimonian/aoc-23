from utils import input, to_nums, count_matches


def solve(path):
    answer = 0
    for line in input(path):
        win, mine = [to_nums(s) for s in line.split(":")[1].split("|")]
        n = count_matches(win, mine)
        if n:
            answer += 2 ** (n - 1)
    return answer


if __name__ == "__main__":
    print(solve("./input.txt"))
