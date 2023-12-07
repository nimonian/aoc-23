from pathlib import Path
from a import solve


def test_solve():
    path = (Path(__file__).parent / "./a_test.txt").resolve()
    result = solve(path)
    assert result == 142, "the answer should be 142"
