"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730484742"


def input_word() -> str:
    "This function takes an inputted word and measures the length."
    "If the length is not within accepted parameters, it gives an error and exits the function early."
    user_input_word: str = str(input("Enter a 5-character word"))
    if len(user_input_word) > 5:
        print(
            "Error: Word must contain 5 characters."
        )  # Print this statement first so user knows what they did wrong.
        exit()
        print(user_input_word)
    elif len(user_input_word) < 5:
        print("Error: Word must contain 5 characters.")  # Same as above.
        exit()
        print(user_input_word)
    else:
        print(user_input_word)
        return user_input_word


def input_letter() -> str:
    "This function takes the length of an inputted character and measures the length."
    "If the input includes multiple characters, the function returns an error and exits early."
    user_input_char: str = str(input("Enter a single character"))
    if len(user_input_char) > 1:
        print("Error: Character must be a single character.")
        exit()
        print(user_input_char)
    else:
        print(user_input_char)
        return user_input_char


def contains_char(word: str, letter: str) -> None:
    "This function scans the inputted word for the inputted character."
    "If the character is found at any of the 5 indices, a statement is printed to relay that it's been found."
    print("Searching for", str(letter), "in", str(word))
    if (
        letter == word[0]
    ):  # Use == instead of = to avoid program mistaking it for variable assignment.
        print(
            letter, "found at index 0"
        )  # Don't use elif, because if a character is found in multiple indices,
        # using elif will not count all the instances once the first condition is satisfied.
        # Using commas instead of plus signs helps to prevent no spaces being present
    if letter == word[1]:
        print(letter, "found at index 1")
    if letter == word[2]:
        print(letter, "found at index 2")
    if letter == word[3]:
        print(letter, "found at index 3")
    if letter == word[4]:
        print(letter, "found at index 4")  # No else statement needed,
        # the instance count below helps to communicate if the character isn't found

    instance_count = (
        0  # This count keeps track of how many times a character appears in a word.
    )
    if letter == word[0]:
        instance_count += 1
    if (
        letter == word[1]
    ):  # Don't use elif, because if a character is found in multiple indices,
        # using elif will not count all the instances once the first condition is satisfied.
        instance_count += 1
    if letter == word[2]:
        instance_count += 1
    if letter == word[3]:
        instance_count += 1
    if letter == word[4]:
        instance_count += 1

    if (
        instance_count == 0
    ):  # This series of if and elif statements helps to consolidate and communicate how many
        # times a character appears in a word.
        print("No instances of", letter, "found in", word)
    elif instance_count == 1:
        print("1 instance of", letter, "found in", word)
    elif instance_count > 1:
        print(str(instance_count), "instances of", letter, "found in", word)


def main() -> None:
    "This function brings everything together and is a simple way to run all functions defined prior."
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
