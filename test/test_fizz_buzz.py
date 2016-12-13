from ..fizzbuzz import resolve


def test_echo():
    cases = [1, 2, 4, 7, 8, 11]
    for value in cases:
        assert resolve(value) == value


def test_fizz():
    cases = [3, 6, 9, 12]
    for value in cases:
        assert resolve(value) == "FiZz"


def test_buzz():
    cases = [5, 10]
    for value in cases:
        assert resolve(value) == "BuZz"


def test_fizzbuzz():
    cases = [15]
    for value in cases:
        assert resolve(value) == "FiZzBuZz"
