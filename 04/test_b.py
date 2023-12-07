from b import solve


def test_solve():
    result = solve("./test_input.txt")
    assert result == 30, "The answer is 30"
