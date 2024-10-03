"""Completing CQ03"""

__author__ = "730484742"


def num_instances(phrase: str, search_char: str) -> None:
    count: int = 0  # Count number of times character appears in word
    index: int = 0  # Allows us to move character by character
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
            index += 1
        else:
            index += 1
    print(count)


# In the while loop, the index allows us to count the amount of characters we've looked at.
# Once the index is equal to the length of phrase, the loop exits out.
# If the character we're currently looking at matches the character we want to find, 1 is added to the count and the index.
# Otherwise, 1 is still added to the index to prevent an infinite loop (I had an infinite loop going for a while).
# The count of the instances of the character is then printed.
