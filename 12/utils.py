import re


def is_consistent(s, nums):
    matches = [len(match) for match in re.findall(r"\#+", s)]

    if any(x > y for x, y in zip(matches, nums)):
        return False

    if any(x != y for x, y in zip(matches[:-1], nums[:-1])):
        return False

    if sum(matches) > sum(nums):
        return False

    return True


def is_matching(s, nums):
    matches = [len(match) for match in re.findall(r"\#+", s)]
    return matches == nums


def count_arrangements(s, nums):
    nodes = [""]

    for char in s:
        if char in ".#":
            nodes = [n + char for n in nodes]
        else:
            nodes = [n + "#" for n in nodes] + [n + "." for n in nodes]
        nodes = [n for n in nodes if is_consistent(n, nums)]
        print(nodes)

    nodes = [n for n in nodes if is_matching(n, nums)]

    return len(nodes)
