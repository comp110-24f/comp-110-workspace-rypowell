"Summing the elements of a list using different loops"

__author__ = "730484742"


def w_sum(vals: list[float]) -> float:
    "Using a while loop"
    idx: int = 0
    sum: float = 0.0
    if len(vals) == 0:
        return 0.0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    "Using a for loop"
    sum2: float = 0.0
    if len(vals) == 0:
        return 0.0
    for elem in vals:
        sum2 += elem
    return sum2


def f_range_sum(vals: list[float]) -> float:
    "Using a for loop with range()"
    sum3: float = 0.0
    if len(vals) == 0:
        return 0.0
    for elem in range(0, len(vals)):
        sum3 += vals[elem]
    return sum3
