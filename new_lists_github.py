"""
Mutable Default Parameter Trap
A common mistake for beginners + the correct usage example.
Written in a clean and professional style.
"""

# --------------------------------------------
# Wrong usage: bag=[] is shared across all calls
# --------------------------------------------
def add_item_wrong(item, bag=[]):
    """Incorrect example: The default list is shared by all function calls."""
    bag.append(item)
    return bag


# --------------------------------------------
# Correct usage: bag=None creates a new list for each call
# --------------------------------------------
def add_item(item, bag=None):
    """Correct example: A new list is created every time the function is called."""
    if bag is None:
        bag = []
    bag.append(item)
    return bag


# --------------------------------------------
# Test code
# --------------------------------------------
def main():
    print("=== WRONG USAGE ===")
    print(add_item_wrong("apple"))   # ['apple']
    print(add_item_wrong("pear"))    # ['apple', 'pear'] -> Unexpected behavior

    print("\n=== CORRECT USAGE ===")
    print(add_item("apple"))         # ['apple']
    print(add_item("pear"))          # ['pear'] -> New list each call

    # Additional tests for clarity
    print("\n=== EXTRA TESTS ===")
    a = add_item("cherry")
    b = add_item("banana")
    print("a:", a)  # ['cherry']
    print("b:", b)  # ['banana']
    print("Lists a and b are completely independent.")


if __name__ == "__main__":
    main()
