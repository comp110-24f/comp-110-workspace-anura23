"""Using a simple concat function to practice with importing"""

__author__ = "730478902"


def concat(input1: str, input2: str) -> str:
    """Returns the concatenation of two strings"""
    return input1 + input2


word1: str = "happy"
word2: str = "tuesday"

if __name__ == "__main__":
    print(concat(word1, word2))
