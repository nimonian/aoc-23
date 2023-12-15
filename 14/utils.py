def rotate(M, n=1):
    for _ in range(n):
        M = list(zip(*M[::-1]))
    return M


def tilt(M):
    for r, row in enumerate(M):
        _row = []

        count, i, j = 0, -1, 0
        while j < len(row):
            if row[j] == "#":
                _row += list("O" * count + "." * (j - i - 1 - count) + "#")
                count, i = 0, j

            if row[j] == "O":
                count += 1

            j += 1

        M[r] = _row + list("O" * count + "." * (j - i - 1 - count))
    return M


def load(dish):
    load = 0
    for r, row in enumerate(dish):
        for char in row:
            if char == "O":
                load += len(dish) - r

    return load
