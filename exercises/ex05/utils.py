"Implementing list utility functions."

__author__ = "730484742"


def only_evens(a: list[int]) -> list[int]:
    "Finds only even numbers in a list."
    new_list: list[int] = []

    for elem in a:
        if elem % 2 == 0:  # Makes sure number is even
            new_list.append(elem)  # Adds to new list

    return new_list


def sub(b: list[int], start_index: int, end_index: int) -> list[int]:
    "Creates a sublist from an inputted list."
    new_list2: list[int] = []

    if start_index < 0:
        start_index = 0  # If start index is negative, sets start index at the 1st element in the list
    if end_index > len(b):
        end_index = len(
            b
        )  # If end index is greater than the length of the list, the end index is set at the last element of the list
    if len(b) == 0 or start_index >= len(b) or end_index <= 0:
        return []  # Multiple cases which will return an empty list

    for idx in range(start_index, end_index):
        new_list2.append(b[idx])

    return new_list2


def add_at_index(c: list[int], element_to_add: int, index_to_add: int) -> None:
    "Places a new number at a given index."
    if index_to_add < 0 or index_to_add > len(c):
        raise IndexError("Index is out of bounds for the input list")

    if (
        len(c) == 0
    ):  # If the length of the list is 0, it simply adds the desired element
        c.append(element_to_add)
        return

    c.append(
        c[len(c) - 1]
    )  # Adds the last value in a list to lengthen list, will be left out below

    for idx in range(
        len(c) - 1, index_to_add, -1
    ):  # Iterates backwards in order to shift items to the right.
        c[idx] = c[
            idx - 1
        ]  # Every element after the desired index is shifted to the right, assigning the
        # value at the previous index to the current index

    c[index_to_add] = element_to_add  # Sets the value to add at the desired index
