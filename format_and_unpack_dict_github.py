def main():
    introduction = "👋👋👋 Hello World, My name is {first_name} {middle_name} {last_name} AKA the {aka}."
    opening_speech = "👨‍💻 Today I will talk about some subjects like {}."
    
    full_name = {
        "first_name": "Linus",
        "middle_name": "Benedict",
        "last_name": "Torvalds",
        "aka": "Mr.Linux",
    }

    subjects = ["Linux", "Open Source Community", "Enterpreneurship"]
  
    # We can unpack dictionaries using the ** operator. 
    # This is commonly used to merge dictionaries or pass arguments to functions.
    # We easily match the keys and values ​​in the format field with the ** expression.
    print(introduction.format(**full_name))

    # With ", ".join, we combine all the elements in the list with ", " and turn them into strings.
    print(opening_speech.format(", ".join(subjects)))
    
if __name__ == "__main__":
    main()