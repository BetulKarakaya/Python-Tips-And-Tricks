if __name__ == "__main__":

    text = "Learn Python with fun Python examples"

    # partition() - Splits the string into three parts: before, separator, 
    # and after the first occurrence of the separator.
    before_separator, separator, after_separator = text.partition("Python")
    
    print("Before the separator:", before_separator)    # Output: "Learn "
    print("Separator:", separator)                      # Output: "Python"
    print("After the separator:", after_separator)      # Output: " with fun Python examples"
    print()

    # rpartition() - Similar to partition(), 
    # but starts splitting from the last occurrence of the separator.
    before_separator, separator, after_separator = text.rpartition("Python")
    print("Using rpartition():")
    print("Before the separator:", before_separator)       # Output: "Learn Python with fun "
    print("Separator:", separator)                         # Output: "Python"
    print("After the separator:", after_separator)         # Output: " examples"
    print()

    # lpartition() - A custom version of partition that operates similarly but isn't built-in.
    # Simulating lpartition by using partition() as it always splits from the left.
    before_separator, separator, after_separator = text.partition("Python")
    print("Using lpartition (same as partition):")
    print("Before the separator:", before_separator)    # Output: "Learn "
    print("Separator:", separator)                      # Output: "Python"
    print("After the separator:", after_separator)      # Output: " with fun Python examples"
