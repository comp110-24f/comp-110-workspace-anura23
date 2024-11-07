"""Practice with functions"""

from random import randint

print(randint(3, 17))
print("Hello")


# Function Definition: This will include parameters.
def sum(num1: int, num2: int) -> int:
    """return the sum of num1 and num2"""
    return num1 + num2


# Function Call
print(sum(num1=2, num2=13))  # These are arguments. They are in your function call.
