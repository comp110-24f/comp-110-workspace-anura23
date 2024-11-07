"""Some Scope examples"""


def remove_chars(msg: str, char: str) -> str:
    """Returns a copy of msg with all instances of char removed."""
    copy: str = ""  # Set up empty str to copy values over.
    index: int = 0  # local variables: copy, index, msg, char.
    while index < len(msg):
        if char != msg[index]:  # if letter is not char, add to copy.
            copy = copy + msg[index]  # also copy = copy += msg[index]. Concatenate.
        index = index + 1  # also index += 1
    return copy


if __name__ == "__main__":
    word: str = "yoyo"  # created a global variable called word with the value "yoyo"
    # Global variables can be accessed outside the function, unlike local variables.
    print(remove_chars(msg=word, char="y"))
    # print the result of calling remove_chars with word and "y"
    print(remove_chars(word, "o"))
    # prints result of calling remove_chars with word and "o" using positional arguments

# We will not actually be removing letters from msg since str types are inmutable.
# We will copy over the characters we want to keep.
# Save the characters that are non-char and make new string.
