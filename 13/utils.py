def is_symmetrical(L, k):
    if k not in range(1, len(L)):
        return False

    i, j = k - 1, k
    while i > -1 and j < len(L):
        if L[i] != L[j]:
            return False
        i, j = i - 1, j + 1

    return True


def find_symmetry(pattern, exclude=()):
    for r in range(len(pattern)):
        if ("r", r) not in exclude and is_symmetrical(pattern, r):
            return ("r", r)

    for c in range(len(pattern[0])):
        if ("c", c) not in exclude and all(is_symmetrical(row, c) for row in pattern):
            return ("c", c)
