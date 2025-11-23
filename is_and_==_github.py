"""
Difference between '==' and 'is'
Beginners often confuse these two, but they check different things.
"""

# --------------------------------------------
# Value equality (==) vs object identity (is)
# --------------------------------------------
def main():
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a  # c points to the same object as a

    print("=== VALUE EQUALITY (==) ===")
    print(a == b)  # True -> same values
    print(a == c)  # True -> same values

    print("\n=== OBJECT IDENTITY (is) ===")
    print(a is b)  # False -> different objects in memory
    print(a is c)  # True -> c is literally the same object as a

    # Additional clarity:
    print("\n=== MEMORY ADDRESSES ===")
    print(id(a), id(b), id(c))  # Only a and c share the same memory address


if __name__ == "__main__":
    main()
