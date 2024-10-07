"Utilizing functions with lists."

__author__ = "730484742"


def all(int_list: list[int], int_search: int) -> bool:
    "Checking if all the integers in a given list of integers are the same."
    idx: int = 0
    if len(int_list) == 0:
        return False
    while idx < len(int_list):
        if int_list[idx] != int_search:
            return False  # If any value is different from the integer being searched for, False is returned
        idx += 1
    else:
        return True  # If all values are the same, True is returned. It's more so if no values are found to be different.


def max(int_list_2: list[int]) -> int:
    "Finding the maximum value in a list of integers."
    if len(int_list_2) == 0:
        raise ValueError("max() arg is an empty List")

    idx_2: int = (
        1  # Starts at the second value because the first value is the default max
    )
    highest_value: int = int_list_2[
        0
    ]  # Instead of starting just at 0, starts at the first value in the list
    while idx_2 < len(int_list_2):
        if int_list_2[idx_2] >= highest_value:
            highest_value = int_list_2[idx_2]
        idx_2 += 1

    return highest_value  # Took out print statement to see if it was the reason this function was returning None instead of the actual values, which worked.


def is_equal(int_list_3: list[int], int_list_4: list[int]) -> bool:
    "Checking if two lists of integers are the exact same."
    idx_3: int = 0
    if len(int_list_3) == len(
        int_list_4
    ):  # Only continues if the lengths of both lists are the same. They can't be exactly equal if they're different lengths.
        while idx_3 < len(int_list_3):
            if int_list_3[idx_3] != int_list_4[idx_3]:
                return False
            idx_3 += 1
        else:
            return True  # This while loop is the exact same as in the all() function.
    else:
        return False  # Connected to the first if statement.


def extend(int_list_5: list[int], int_list_6: list[int]) -> None:
    "Combining two lists of integers."
    idx_4: int = 0
    while idx_4 < len(int_list_6):
        int_list_5.append(
            int_list_6[idx_4]
        )  # Adds on each value from the second list onto the first list.
        idx_4 += 1
