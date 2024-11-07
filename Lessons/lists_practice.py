"""Basic syntax about lists"""

my_numbers: list[float] = list()  # can also do [] -> literal

# string analogies - my_name: str = ()  literal
# my_name: str = str()  # constructor

# Adding items to list
my_numbers.append(1.5)
my_numbers.append(2.3)

print(my_numbers)

# Creating an already populated list - add the values 102, 86, 94
game_points: list[int] = [102, 86, 94]
print(game_points)

# Practice Indexing from a list - how do we access 94?
print(game_points[2])
last_game: int = game_points[2]
print(last_game)

# Practice Modifying by Index
game_points[1] = 72
print(game_points)

# cannot modify strings like I do with lists.
# This is because lists are mutable types. Strings are immutable types.

# Identifying the length of a list.
print(len(game_points))

# Removing an item from a list. Remove 72 from game_points.
game_points.pop(1)
print(game_points)


# Writing a function to print every element in input list.
def display(input_list: list[int]) -> None:
    """Writing a function to print every element in input_list."""
    index: int = 0
    while index < len(input_list):
        print(input_list[index])
        index = index + 1


display(input_list=game_points)

random_names: list[str] = ["Kaki", "gjdd", "saff"]
print(["Kaki", "gjdd", "saff"][0])
