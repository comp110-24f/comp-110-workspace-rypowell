"""File to define Bear class."""


class Bear:
    """Defining the Bear class."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes bear class."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        """Simulating one day of a bears life."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Bear wants to eat some fish."""
        self.hunger_score += num_fish
