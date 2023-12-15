def h(s):
    n = 0

    for c in s:
        n += ord(c)
        n *= 17
        n %= 256

    return n


def print_boxes(boxes):
    for i, b in enumerate(boxes):
        if len(b):
            print(b)
