if __name__ == "__main__":

    # Returns the number of occurrences of a given character or substring
    
    text = "Hello World World"

    print(text.count("l")) # Output: 4
    print(text.count("o")) # Output: 3
    print(text.count("World")) # Output: 2
    print(text.count("world")) # Output: 0
