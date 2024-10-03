"""Practicing functions"""

__author__ = "730484742"


def mimic(message: str) -> str:
    """Repeat message back to you"""
    return message


def main() -> None:
    print(mimic(message=input("What is your message?")))
    """Printing result of mimic function"""


if __name__ == "__main__":
    main()
