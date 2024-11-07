"""Practice with Local Variables, Conditionals, and User Input"""

__author__ = "730478902"


def guess_a_number() -> None:
    """This function takes no inputs. Returns nothing. Displayed in terminal."""
    secret: int = 7  # I defined secret as an n=int type equal to 7.
    x = int(input("Guess a number:"))
    # Takes user input and sets it equal to x. I have to convert that type to an int.
    print("Your guess was " + str(x))
    if x == secret:
        print("You got it!")
    elif x < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print(
            "Your guess was too high! The secret number is " + str(secret)
        )  # Used the value secret and converted it to a string for concatenate=ing.
    return None


if __name__ == "__main__":
    guess_a_number()
