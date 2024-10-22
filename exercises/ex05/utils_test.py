from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest

"Testing only_evens"


def test_edge_only_evens() -> None:
    a: list[int] = [107, 96, 27, 34]
    assert only_evens(a) == [96, 34]


def test_return_only_evens() -> None:
    b: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(b) == [2, 4, 6]


def test_nonmutate_only_evens() -> None:
    c: list[int] = [4, 7, 2, 10, 22]
    only_evens(c)
    assert c == [4, 7, 2, 10, 22]


"Testing sub"


def test_edge_sub() -> None:
    d: list[int] = [15, 25, 35, 45]
    assert sub(d, -3, 10) == [15, 25, 35, 45]


def test_return_sub() -> None:
    e: list[int] = [12, 24, 36, 48, 60, 72]
    assert sub(e, 1, 5) == [24, 36, 48, 60]


def test_nonmutate_sub() -> None:
    f: list[int] = [1, 2, 3, 4, 5]
    sub(f, 1, 4)
    assert f == [1, 2, 3, 4, 5]


"Testing add_at_index"


def test_edge_add_at_index() -> None:
    g: list[int] = [12, 24, 48, 60]
    add_at_index(g, 36, 2)
    assert g == [12, 24, 36, 48, 60]


def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    h: list[int] = [1, 2]
    with pytest.raises(IndexError):
        add_at_index(h, 1, 3)
        # an IndexError is raised for the case when the add_at_index is given an index
        # that is greater than the length of our list


def test_return_add_at_index() -> None:
    i: list[int] = [5, 10, 15]
    assert add_at_index(i, 20, 3) == None


def test_mutate_add_at_index() -> None:
    j: list[int] = [6, 12, 18, 24]
    add_at_index(j, 30, 4)
    assert j == [6, 12, 18, 24, 30]
