if __name__ == "__main__":

    text = "   Hello World   "
    stripped_text = text.strip()
    left_stripped = text.lstrip()
    right_stripped = text.rstrip()

    print(stripped_text)   # Output: "Hello World"
    print(left_stripped)   # Output: "Hello World   "
    print(right_stripped)  # Output: "   Hello World"
