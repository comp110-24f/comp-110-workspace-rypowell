"""File to define Fish class."""


class Fish:
    """Defining the Fish class."""

    age: int

    def __init__(self):
        """Initializes fish class."""
        self.age = 0

    def one_day(self):
        """Simulates one day in the life of a fish."""
        self.age += 1
        return None
