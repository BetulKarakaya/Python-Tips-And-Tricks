from itertools import permutations, combinations
# Permutations:
# Permutations represent all possible arrangements of a given set of items where the order matters.
# For example, given ['A', 'B', 'C'], permutations include:
# ('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A').

# Combinations:
# Combinations represent subsets of a given set of items where the order does NOT matter.
# For example, given ['A', 'B', 'C'], combinations of size 2 include:
# ('A', 'B'), ('A', 'C'), ('B', 'C').

# Key difference:
# In permutations, ('A', 'B') is different from ('B', 'A').
# In combinations, ('A', 'B') is the same as ('B', 'A').


# The list() function is used to create a list in Python.
# It can convert other iterable objects (like strings, tuples, sets, or dictionaries) into a list.
# Example:
# list("ABC") -> ['A', 'B', 'C']
# list((1, 2, 3)) -> [1, 2, 3]

def permutations_func(items): 
    # Generate all permutations (order matters)
    return list(permutations(items))

def combinations_func(items,r):
    # Generate all combinations of size r (order doesn't matter)
    return list(combinations(items, r))

if __name__ == "__main__":
   
    # A list of items
    items = ['🍎', '🍌', '🍇']

   
    all_permutations = permutations_func(items)
    all_combinations = combinations_func(items, 2)

    print("Items:", items)
    print("\nAll Permutations (Order Matters):")
    for perm in all_permutations:
        print(perm)

    print("\nAll Combinations of size 2 (Order Doesn't Matter):")
    for comb in all_combinations:
        print(comb)

    # Output:
    # Items: ['🍎', '🍌', '🍇']
    #
    # All Permutations (Order Matters):
    # ('🍎', '🍌', '🍇')
    # ('🍎', '🍇', '🍌')
    # ('🍌', '🍎', '🍇')
    # ('🍌', '🍇', '🍎')
    # ('🍇', '🍎', '🍌')
    # ('🍇', '🍌', '🍎')
    #
    # All Combinations of size 2 (Order Doesn't Matter):
    # ('🍎', '🍌')
    # ('🍎', '🍇')
    # ('🍌', '🍇')
