"Using dictionaries for various tasks."

__author__ = "730484742"


def invert(a: dict[str, str]) -> dict[str, str]:
    "Inverting dictionaries with keys becoming values and vice versa."
    inverted_dict = {}
    for key in a:
        value = a[
            key
        ]  # Creates a local variable to store the values in the dictionary "a"
        if (
            value in inverted_dict
        ):  # If multiple values are found as keys in the new inverted dictionary, a KeyError is raised
            raise KeyError("Duplicate keys found")
        inverted_dict[value] = (
            key  # Value is assigned as the keys with keys as the values
        )
    return inverted_dict


def favorite_color(b: dict[str, str]) -> str:
    "Counting up what the most popular color is."
    if len(b) == 0:  # Returns empty string if the input dictionary is empty
        return ""

    color_values = []
    for key in b:
        color_values.append(b[key])  # Stores all color values in list

    color_count: dict[str, int] = (
        {}
    )  # I realized that these still needed to be initialized as empty dictionaries, but with their types enumerated beforehand
    for color in color_values:
        if color in color_count:
            color_count[
                color
            ] += 1  # Stores the colors from color values as keys and increments the count if the color is present more than once
        else:
            color_count[color] = (
                1  # Adds colors that only occur once and sets the count to 1
            )

    most_popular_color: str = ""  # The most popular color starts as an empty string
    max_count = 0
    for color in color_values:  # Iterates through color_values to check each color
        if color_count[color] > max_count:
            most_popular_color = color  # Updates most_popular_color if the count is higher than max_count
            max_count = color_count[
                color
            ]  # Updates max_count to the count of the most_popular_color

    return most_popular_color


def count(c: list[str]) -> dict[str, int]:
    "Counting up the instances of words in a list."
    new_dict: dict[str, int] = {}
    for elem in c:
        if elem in new_dict:
            new_dict[elem] += 1
        else:
            new_dict[elem] = 1
    return new_dict


def alphabetizer(d: list[str]) -> dict[str, list[str]]:
    "Alphabetizing the words in a list."
    alphabet_dict: dict[str, list[str]] = {}
    for elem in d:
        first_letter = elem[
            0
        ].lower()  # Creates a variable that is the first letter of the word in lowercase, resets every time the loop runs

        if (
            first_letter not in alphabet_dict
        ):  # If that first letter isn't already a key, it is created as a key and assigned a value of an empty list
            alphabet_dict[first_letter] = []

        alphabet_dict[first_letter].append(
            elem
        )  # Appends the word to the list of its first letter

    return alphabet_dict


def update_attendance(
    days_of_week: dict[str, list[str]], day: str, student: str
) -> None:
    "Using a dictionary to keep track of attendance."
    if day in days_of_week:  # Checks if day is already a key in days_of_week
        if student not in days_of_week[day]:
            days_of_week[day].append(
                student
            )  # If the student is not already counted for the day, they are appended to the list for that day
    else:
        days_of_week[day] = [
            student
        ]  # If a new day is inputted, it is created as a key and that student is put into a new list with their name
