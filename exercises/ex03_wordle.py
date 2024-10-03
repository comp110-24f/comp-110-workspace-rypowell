"Wordle Game."

__author__ = "730484742"


def input_guess(secret_word_len: int) -> str:
    "Takes a guess from the user and measures the length of it."
    exit_mechanism: int = (
        0  # This variable ensures that the loop isn't infinite and only is added to if the user's input is the correct length.
    )
    while exit_mechanism == 0:
        user_input_word: str = str(input(f"Enter a {secret_word_len} character word: "))
        if len(user_input_word) == secret_word_len:
            print(user_input_word)
            exit_mechanism += 1
            return user_input_word  # Put after exit mechanism so it can be used later in the program
        else:
            print(f"That wasn't {secret_word_len} chars! Try again: {user_input_word}")


def contains_char(search_word: str, search_char: str) -> bool:
    "Ensures that the word contains the character being searched for."
    assert len(search_char) == 1
    idx: int = 0
    while idx < len(search_word):
        if search_word[idx] == search_char:
            return True
        idx += 1
    else:
        return False


def emojified(user_guess: str, secret_word: str) -> str:
    "Visualizes the comparison of the user guess to the secret word, including whether they guess the"
    "correct characters in the correct spots and correct characters in the word but not in the right spots."
    assert len(user_guess) == len(secret_word)

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    idx2: int = 0
    game_output: str = ""  # Empty string to store boxes into.

    while idx2 < len(user_guess):
        if user_guess[idx2] == secret_word[idx2]:  # Correct character at correct spot
            game_output += GREEN_BOX
        elif contains_char(
            secret_word, user_guess[idx2]
        ):  # Correct character but not in the right spot
            game_output += YELLOW_BOX
        else:  # Character not found in word
            game_output += WHITE_BOX
        idx2 += 1
    return game_output  # Used in main function below


def main(secret_word: str) -> None:
    "Brings all functions into one and makes game playable for user."
    total_turns: int = 6
    current_turn: int = 1

    while current_turn <= total_turns:
        print(f"=== Turn {current_turn}/{total_turns} ===")
        guess = input_guess(
            secret_word_len=len(secret_word)
        )  # Simplifies for use in the emojified function below

        print(emojified(guess, secret_word))

        if guess == secret_word:
            print(f"You won in {current_turn}/{total_turns} turns!")
            return  # Exits out of function, don't put any variable since the return type is None.
        else:
            current_turn += 1

    if (
        current_turn > total_turns
    ):  # Since the while loop has been exited and current_turn has a value of 7 in memory, this will be satisfied
        print(f"X/{total_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret_word="codes")
