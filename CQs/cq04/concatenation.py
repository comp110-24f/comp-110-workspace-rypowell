"A function to concatenate two strings"

__author__ = "730484742"


def concat(input1: str, input2: str) -> str:
    print(input1 + input2)
    return input1 + input2


word1: str = "happy"
word2: str = "tuesday"

if __name__ == "__main__":
    print(concat(word1, word2))
