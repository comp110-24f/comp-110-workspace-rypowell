"""Plan a tea party using small functions to orchestrate the execution of the program."""

__author__: str = "730484742"


def main_planner(guests: int) -> None:
    """Bring together all functions"""
    print("A Cozy Tea Party for", guests, "People")
    print("Tea Bags:", tea_bags(guests))
    print("Treats:", treats(guests))
    print(
        "Cost:", str("$") + str(cost(tea_bags(guests), treats(guests)))
    )  # Defines a function to print out the returns of all functions in one comprehensive summary.
    # Return type is None since we are only printing and not returning any outputs to the function caller.


# Cost wasn't working because it was expecting 2 variables and I was only giving it 1.

# Initially tried to use variable assignment (I was in a class that mainly
# used R and we used a lot of variable assignment) with equalling tea_count and calling
# tea_bags(guests) to try and store it. Autograder said no so I tried calling
# tea_bags and treats within cost and it worked.

# Autograder kept docking points because I had spaces in between the words and colons.
# Took me a bit too long to realize.

# Looked on the discussion board to figure out how to put the $ with no spaces.


def tea_bags(people: int) -> int:
    """Calculate amount of tea bags needed"""
    return (
        people * 2
    )  # Multiplies the amount of people attending by 2. Returns value to function caller.


def treats(people: int) -> int:
    """Calculate amount of treats need"""
    return int(
        tea_bags(people=people) * 1.5
    )  # Takes the value held by people in tea_bags and multiplies it by 1.5.


# Converts to an int and returns to function caller.


# Took out round() which I was originally using and just put int() instead.

# Read closely on the error it was giving me for keyword argument and realized that with the return
# given by treats, it was treating people as its own parameter instead of taking
# into account the parameter from tea_bags.


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate total cost for amount of tea bags and treats"""
    return (tea_count * 0.5) + (
        treat_count * 0.75
    )  # Multiplies the inputted counts by 0.5 for tea_count and by 0.75 for treat_count.


# Returns to function caller. Outputs to a float due to decimals being involved.


# Tried both equalling people to tea_count/treat_count and calling functions
# until I realized the solution was way simpler than that.

if __name__ == "__main__":
    main_planner(
        guests=int(input("How many guests are attending your tea party? "))
    )  # Makes program runnable.
