# This Python script demonstrates the usage of the frozenset() function.
# A frozenset is an immutable set, which means its elements cannot be changed once assigned.
# Unlike set, frozenset can be used as a dictionary key or as an element of another set.
# The frozenset() function takes an iterable (like list, tuple, or set) as an argument and returns a new frozenset object.

# Create a list of unique elements
my_list = [1, 2, 3, 4, 5]

# Convert the list to a frozenset
my_frozenset = frozenset(my_list)

# Print the frozenset
print("Frozen set:", my_frozenset)

# Attempt to modify the frozenset (which will result in an AttributeError)
try:
    my_frozenset.add(6)
except AttributeError as e:
    print("Cannot modify a frozenset:", e)
