"""Practice with conditionals"""


def less_than_10(num: int) -> None:
    """Tell me if a number is less than 10"""
    if num < 10:
        print("small number")
    else:
        print("large number")


less_than_10(num=13)
print("Have a nice day!")


def should_I_eat(hungry: bool) -> None:
    """Tells me whether or not to eat based on hunger level."""
    if hungry:  # conditional/boolean expression#
        print("Eat some food")  # this is the 'then' block#
    else:
        print("do yo work! You got so much to do")


print("I am proud of you")

should_I_eat(hungry=True)
# If a print statement is put here, it will show None because the function will be called and it will try to print the return value.


def check_first_letter(word: str, letter: str) -> str:
    """Will check whether the first letter of input does match the letter."""
    if word[0] == letter:
        return "match"
    else:
        return "no match"


print(check_first_letter(word="biology", letter="b"))
print(check_first_letter(word="chemistry", letter="d"))
