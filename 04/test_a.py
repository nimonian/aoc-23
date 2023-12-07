from a import solve


def test_solve():
    result = solve("./test_input.txt")
    assert result == 13, "The answer is 13"
