if __name__ == "__main__":
    
    # Generates a dictionary where all keys have the same initial value.
    keys = ["name", "age", "city"]
    default_dict = dict.fromkeys(keys, "Unknown")
    print(default_dict)  # Output: {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}

