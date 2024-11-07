"""Practice with dictionary functions."""

__author__ = "730478902"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Returns a dictionary with inverted keys and values relative to input."""
    inverted_dict: dict[str, str] = {}
    # initialize an empty dict[str, str] to hold inverted key-value pairs
    for key in input_dict:  # iterate over every key in the inputted dictionary.
        if input_dict[key] in inverted_dict:
            raise KeyError("you have duplicate key values.")
        inverted_dict[input_dict[key]] = key
        # key of input_dict = value of inverted_dict
        # thereby, the value of input_dict at a key is given as the key to inverted_dict
    return (
        inverted_dict  # return populated dict with inverted key-value pairs from input.
    )


def favorite_color(color_preferences: dict[str, str]) -> str:
    """Returns the color that appears most frequently in the dictionary."""
    color_counts: dict[str, int] = {}
    # initialized an empty dict to store the counts of each color.
    max_count: int = 0
    # initialized a global variable that will keep track of the color's popularity.
    color: str = ""
    # an empty string that will hold the favorite color. this variable will be returned.
    for key in color_preferences:
        # for loop that counts the occurrence of each color by iterating over keys.
        if color_preferences[key] in color_counts:
            color_counts[color_preferences[key]] += 1
        # have to use color_preferences[key] as key -> is the value we want added.
        # python will add the value in the brackets as the key.
        # if that color is in color_counts -> add one to its frequency.
        if color_preferences[key] not in color_counts:
            color_counts[color_preferences[key]] = 1
        # again, we have to use color_preferences[key] as key -> evaluates to the color.
        # ifc color is not in color_counts, it is added to the dict with the value 1.
    for key in color_counts:
        # for loop to find the maximum count and associated color.
        # iterate by keys in the new dict we created containing color frequencies.
        if color_counts[key] > max_count:
            # initially set max_count = 0
            # if the frequency is greater than zero....
            max_count = color_counts[key]
            # redefine max_count as value associated with the color/key in color_counts.
            color = key
            # return the key associated with the maximum count (favorite color)
    return color


def count(item_list: list[str]) -> dict[str, int]:
    """Given list of values to count frequency of, dict with item frequency returned."""
    frequency_list: dict[str, int] = {}
    # we initialized an empty dictionary to store frequencies.
    for item in item_list:  # for loop to loop through every key/item in item_list.
        if (
            item in frequency_list
        ):  # Conditional to see if item is already present as a key in frequency_list.
            frequency_list[item] += 1
        else:  # however if item isn't already present, set its initial frequency to 1.
            frequency_list[item] = 1
    return frequency_list  # simply return the resultant populated dict[str, int]


def alphabetizer(word_jumble: list[str]) -> dict[str, list[str]]:
    """Return dict where each key is letter and each value = words starting w/ letter"""
    alphabetical: dict[str, list[str]] = {}
    # initialized an empty dictionary to store list of words with same first letter.
    for word in word_jumble:
        # iterate over every word/index in the input word_jumble list.
        first_letter = word[0].lower()
        # obtain lowercase first letter of the word by indexing first character.
        # .lower() function was provided to us.
        if first_letter not in alphabetical:
            alphabetical[first_letter] = []
        # conditional that defines an empty list for a new first_letter.
        # new first letters are those that have not already occurred in dict.
        # this empty list can be populated with words starting with same first letter.
        alphabetical[first_letter] += [word]
        # the list associated with some first_letter can be concatenated with the word.
        # this way, we also avoid using duplicate keys as we're only appending the value
    return alphabetical  # simply return the populated dict[str, list[str]]


def update_attendance(
    attendance_log: dict[str, list[str]], weekday: str, student: str
) -> None:
    """Function mutates and returns dict with student attendance each day."""
    if weekday in attendance_log:
        attendance_log[weekday].append(student)
    # if inputted day is already in list, just add student to existing day's headcount
    if weekday not in attendance_log:
        attendance_log[weekday] = [student]
    # if inputted day is not in list, we will add a new key/value pair.
    # new key-value pair is day entry with student's name as first element in list[str].
