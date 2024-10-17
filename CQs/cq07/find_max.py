__author__ = "730484742"


def find_and_remove_max(a: list[int]) -> int:
    if len(a) == 0:
        return -1

    highest_value: int = a[0]
    for elem in a:
        if elem > highest_value:
            highest_value = elem

    idx: int = 0
    while idx < len(a):
        if a[idx] == highest_value:
            a.pop(idx)
        else:
            idx += 1  # Realized that when an element is popped, the list can skip elements because the list length decreases

    return highest_value
