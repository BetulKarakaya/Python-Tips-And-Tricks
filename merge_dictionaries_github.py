
if __name__ == "__main__":


    # Python dictionaries provide a flexible and efficient way to store key-value pairs,
    # allowing you to organize and retrieve data with a unique identifier (key).
    # They are commonly used for fast lookups, mappings, and data organization in Python.
    # dictionary = {"key":value, "another_key":another_value,..............}
    # specific value = dictionary["key"]     This return the value of that key


    dictionary_1 = {"item1" : 1, "item2" : "2", "item3": "3a"}
    dictionary_2 = {"item4" : 44, "item5" : "55", "item6": "sixty"}

    merged_dictionary = {**dictionary_1,**dictionary_2}
    print(merged_dictionary)

    merged_dictionary2 = {**dictionary_2,**dictionary_1}
    print(merged_dictionary2)
