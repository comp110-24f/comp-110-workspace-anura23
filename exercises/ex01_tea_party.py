"""This is a program to help plan how many tea bags and treats I will need, and the total cost, for the tea party I will be hosting."""

__author__: str = "730478902"


def main_planner(guests: int) -> None:
    """Function to serve as entrypoint of tea party program by integrating the three functions below into one function call."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


# What is seen above are a series of print statements that will display the number of tea bags and treats needed, the total cost, and a string confirming party attendance.
# These statements were created by concatenating string statements.
# An important part of this was that each of the functions below returned ints or floats when called. I had to convert these ints into strings so that I could concatenate the function call results with the existing string text.
# This main function is placed at the top, above all of the function. This would allow myself, or any observer, to quickly gain information on what function calls constitute this tea party program.


def tea_bags(people: int) -> int:
    """Function that outputs the number of tea bags needed based on party attendance."""
    return people * 2


# This return statement will take the number of guests attending the party and then double it to compute the number of tea bags needed.


def treats(people: int) -> int:
    """Function that outputs the number of treats needed based on number of tea drinks consumed."""
    return int(tea_bags(people=people) * 1.5)
    # This return statement involves calling the tea_bags function to calculate the total number of treats needed, which is just 1.5 times the number of drinks consumed.
    # We call the tea_bags function so that in case somebody consumes more or less than 2 drinks, the code can be easily adjusted in one function, rather than throughout the code.


def cost(tea_count: int, treat_count: int) -> float:
    """Function that returns the total cost of the tea bags and treats needed for the party."""
    return (tea_count * 0.50) + (treat_count * 0.75)
    # This return statement involves calculating the total party cost to the organizer based on the calculated number of tea bags and treats needed from the previous two function calls.


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
# These two lines of code were provided by the instructors. This allows us to have an interactive feature whereby the user is prompted for a guest count.
# You must go to the Run section of the REPL trailhead to see this functionality. Will not be on the interact tab.
