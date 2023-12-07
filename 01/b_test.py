from pathlib import Path
from b import solve


def test_solve():
    path = (Path(__file__).parent / "./b_test.txt").resolve()
    result = solve(path)
    assert result == 281, "the answer should be 281"
