"""Examples of dictionary syntax with Ice Cream Shop order tallies."""

# Dictionary type is dict[key_type, value_type]

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

# len evalutes to the number of entries.
print(len(ice_cream))  # -> print 3

# add key-value entry by directly assigning to key.

ice_cream["mint"] = 3

# We can access entries by their key.

print(ice_cream["chocolate"])  # should print 12.

# test if "pbj" is a key in ice_cream.
# can use this bool statemnt as the conditional in an if statement.

has_pbj: bool = "pbj" in ice_cream

# removing an element from a dictionary.
# still use pop like with lists.
# this line of code does return value associated with that key.

ice_cream.pop("strawberry")

# to iterate over every key in a loop, us for...in...

for flavor in ice_cream:
    tally: int = ice_cream[flavor]
    print(f"{flavor} has {tally} orders.")
