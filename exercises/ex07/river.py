"""File to define River class."""

__author__ = "730484742"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Defining the River class."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checking the ages of the fish and the bears."""
        surviving_fish = []
        surviving_bears = []

        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(
                    fish
                )  # For any fish with an age of 3 or less, they are added to a list of surviving fish.
        self.fish = (
            surviving_fish  # The list of fish is updated to the list of surviving fish.
        )

        for bears in self.bears:
            if bears.age <= 5:
                surviving_bears.append(
                    bears
                )  # For any bear with an age of 5 or less, they are added to a list of surviving bears.
        self.bears = surviving_bears  # The list of bears is updated to the list of surviving bears.
        return None

    def bears_eating(self):
        """Simulation of bears eating."""
        for bears in self.bears:
            if (
                len(self.fish) >= 5
            ):  # If there are more than 5 fish in the river, each bear eats 3 fish
                bears.eat(3)
                self.remove_fish(3)
        return None

    def check_hunger(self):
        """Checking the hunger of the bears."""
        surviving_bears2 = []
        for bears in self.bears:
            if (
                bears.hunger_score >= 0
            ):  # If a bear has a hunger score that is greater than or equal to 0, they survive
                surviving_bears2.append(
                    bears
                )  # Surviving bears are added to a new list
        self.bears = surviving_bears2  # The list of bears is updated to the list of surviving bears
        return None

    def repopulate_fish(self):
        """Repopulating the fish."""
        num_fish = len(self.fish)
        new_fish = (num_fish // 2) * 4  # Each pair of fish produces 4 offspring

        for _ in range(new_fish):
            self.fish.append(Fish())  # New fish are added to the list of fish
        return None

    def repopulate_bears(self):
        """Repopulating the bears."""
        num_bears = len(self.bears)
        new_bears = num_bears // 2  # Each pair of bears produces 1 offspring

        for _ in range(new_bears):
            self.bears.append(Bear())  # New bears are added to the list of bears
        return None

    def view_river(self):
        """Viewing the simulation of the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulates one week of the river."""
        for _ in range(7):
            self.one_river_day()  # Simulates 7 river days

    def remove_fish(self, amount: int):
        """Removing fish from the river."""
        for _ in range(0, amount):
            self.fish.pop(0)  # Removes the frontmost fish
        return None
