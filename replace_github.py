if __name__ == "__main__":
    
    # Replaces a specific expression within the text
    
    text = "Hello World World"
    replaced_text = text.replace("World", "Python")
    print(replaced_text)  # Output: Hello Python

    # The code tries to replace "World!!!" with "Python" in the string "Hello World World".
    # Since "World!!!" does not exist in the original string, no replacement occurs,
    # and the original string remains unchanged.
    # Output: Hello World World
    replaced_text = text.replace("World!!!", "Python")
    print(replaced_text)  # Output: Hello World World
