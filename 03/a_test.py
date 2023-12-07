from pathlib import Path
from a import solve, getboundary, issymbol


def test_getboundary():
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    result_1 = getboundary(grid, 1, 1)
    assert result_1 == [1, 2, 3, 4, 6, 7, 8, 9]


def test_getboundary_2():
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    result = getboundary(grid, 0, 0)
    assert result == [2, 4, 5]


def test_getboundary_3():
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    result = getboundary(grid, 2, 2)
    assert result == [5, 6, 8]


def test_issymbol():
    assert issymbol(".") == False
    assert issymbol("9") == False
    assert issymbol("*") == True


def test_solve():
    path = (Path(__file__).parent / "./a_test.txt").resolve()
    result = solve(path)
    assert result == 4361, "the answer should be 4361"
