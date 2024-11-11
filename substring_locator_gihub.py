if __name__ == "__main__":

    # Both find() and index() locate the position of a specified substring within a string.
    # However, they differ in their behavior when the substring is not found:
    # - find(): Returns -1 if the substring is not found.
    # - index(): Raises a ValueError if the substring is not found.

    # Additionally, if the substring appears multiple times, both methods return the position
    # of the first occurrence only.

    text = "Hello World World"

    # Example 1: When the substring is found
    position_find = text.find("World")   # Returns 6 (first occurrence)
    position_index = text.index("World") # Returns 6 (first occurrence)

    # Example 2: When the substring is NOT found
    position_not_found_find = text.find("Python")  # Returns -1
    # position_not_found_index = text.index("Python") # Raises ValueError

    print("Using find():", position_find)     # Output: 6
    print("Using index():", position_index)   # Output: 6
    print("Using find() when not found:", position_not_found_find)  # Output: -1

    # Uncommenting the line below would raise a ValueError
    # print("Using index() when not found:", position_not_found_index)

    # In both cases, only the first occurrence of "World" is found at index 6.
    # To find subsequent occurrences, additional logic is required.
