if __name__ == "__main__":

    text = "Hello World World"

    # Centers the text within the specified width, 
    # padding with the chosen fill character if needed.
    print(text.center(30,"*")) # Output: "******Hello World World*******"

    # Aligns the text to the left within the specified width, 
    # padding with the chosen fill character if needed.
    print(text.ljust(30, '*'))  # Output: "Hello World World*************"

    # Aligns the text to the right within the specified width, 
    # padding with the chosen fill character if needed.
    print(text.rjust(30, '*'))  # Output: "*************Hello World World"
