def rotate(M):
    h, w = len(M), len(M[0])
    return [[M[h - 1 - c][r] for c in range(h)] for r in range(w)]


def tilt(M):
    for r, row in enumerate(M):
        _row = []
        count = 0
        i = -1

        j = 0
        while j < len(row):
            if row[j] == "#":
                _row += ["O"] * count
                _row += ["."] * (j - i - 1 - count)
                _row.append("#")
                i = j
                count = 0

            if row[j] == "O":
                count += 1

            j += 1

        _row += ["O"] * count
        _row += ["."] * (j - i - 1 - count)
        M[r] = _row
    return M


def calculate_load(dish):
    load = 0
    for r, row in enumerate(dish):
        for char in row:
            if char == "O":
                load += len(dish) - r

    return load


def pretty_print(dish):
    for row in dish:
        print("".join(row))
    print()
