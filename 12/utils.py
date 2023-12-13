from functools import cache


@cache
def get_tilings(n, tiles):
    tilings = []

    if len(tiles) == 1:
        for i in range(n - tiles[0] + 1):
            tilings.append([i])

    else:
        for i in range(sum(tiles[:-1]), n - tiles[-1] + 1):
            tilings += [tiling + [i] for tiling in get_tilings(i, tiles[:-1])]

    return tilings


def overwrite(A, B, k):
    for i, b in enumerate(B):
        A[k + i] = b
    return A
