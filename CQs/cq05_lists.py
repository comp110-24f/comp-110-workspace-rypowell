"Mutating functions."

__author__ = "730484742"


def manual_append(a: list[int], b: int) -> None:
    a.append(b)


def double(c: list[int]) -> None:
    idx: int = 0
    while idx < len(c):
        c[idx] = c[idx] * 2
        idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)

# My theory is that the same value will be print for both list variables
# My theory was correct
