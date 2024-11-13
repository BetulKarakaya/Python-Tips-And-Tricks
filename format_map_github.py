if __name__ == "__main__":

    # Uses format_map() to replace placeholders in a string with values from a given dictionary, 
    # allowing dynamic insertion of values based on key names in the format {key}.

    text = "Hello {planet}, It's {name}"
    print(text.format_map({"planet" : "World","name": "Betül"}))  
    # Output: "Hello World, It's Betül"
