"""Practice with for...in...loops"""

pets: list[str] = ["Louie", "Bo", "Bear"]
for elem in pets:
    print("Good boy, " + elem + "!")
    # Or you can use f-strings.
    # print(f"Good boy, {elem}!")

"""Printing every element in names with their index and value."""

names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for index in range(0, len(names)):
    print(str(index) + ": " + names[index])
