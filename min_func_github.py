# This Python script demonstrates the usage of the min() function.
# The min() function returns the smallest item in an iterable (such as a list, tuple, or set).
# It can also accept multiple arguments and return the smallest one.
# If the iterable is empty, a ValueError is raised.

# Example 1: Finding the smallest item in a list
numbers = [5, 2, 8, 1, 3]
smallest_number = min(numbers)
print("The smallest number in the list is:", smallest_number)

# Example 2: Finding the smallest item among multiple arguments
smallest_argument = min(5, 2, 8, 1, 3)
print("The smallest argument is:", smallest_argument)

# Example 3: Handling empty iterable
empty_list = []
try:
    smallest_empty = min(empty_list)
    print("The smallest item in the empty list is:", smallest_empty)
except ValueError:
    print("The list is empty. Cannot find the smallest item.")
