from pathlib import Path

from a import *

path = (Path(__file__).parent / "./test_input.txt").resolve()


def test_get_seeds():
    almanac = input(path)
    result = get_seeds(almanac)
    assert result == [79, 14, 55, 13], "The seeds are correct"


def test_get_map():
    almanac = input(path)
    m = get_map(almanac[1])
    assert m[98] == 50
    assert m[99] == 51
    assert m[96] == 98
    assert m[97] == 99


def test_do_map():
    almanac = input(path)
    m = get_map(almanac[1])
    assert do_map(0, m) == 0
    assert do_map(1, m) == 1
    assert do_map(48, m) == 48
    assert do_map(49, m) == 49
    assert do_map(50, m) == 52
    assert do_map(51, m) == 53
    assert do_map(96, m) == 98
    assert do_map(97, m) == 99
    assert do_map(98, m) == 50
    assert do_map(99, m) == 51


def test_solve():
    result = solve(path)
    assert result == 35, "The answer is 35"
