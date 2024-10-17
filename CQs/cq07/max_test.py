from CQs.cq07.find_max import find_and_remove_max

__author__ = "730484742"


def test1_find_and_remove_max() -> None:
    a: list[int] = [4, 5, 6, 7, 8]
    assert find_and_remove_max(a) == 8


def test2_find_and_remove_max() -> None:
    b: list[int] = [1, 5, 9, 7, 8]
    find_and_remove_max(b)
    assert b == [1, 5, 7, 8]


def test3_find_and_remove_max() -> None:
    c: list[int] = [-1, -2, -3, -4]
    assert find_and_remove_max(c) == -1
