if __name__ == "__main__":
    
    # isalpha() -> Returns True if all characters in the string are alphabetic
    # isdigit() -> Returns True if all characters in the string are digits
    # isalnum() -> Returns True if the string contains only alphabetic and/or numeric characters (no spaces or special characters)

    alpha_text = "Hello"
    digit_text = "1234"
    alnum_text = "Hello123"

    print("Is all characters in the alphastring are alphabetic:", alpha_text.isalpha())  # Output: True
    print("Is all characters in the alphastring are digit:", alpha_text.isdigit())  # Output: False
    print("Is all characters in the alphastring are alphabetic or numeric characters:", alpha_text.isalnum())  # Output: True

    print("Is all characters in the digittext are alphabetic:", digit_text.isalpha())  # Output: False
    print("Is all characters in the digittext are digit:", digit_text.isdigit())  # Output: True
    print("Is all characters in the digittext are alphabetic or numeric characters:", digit_text.isalnum())  # Output: True

    print("Is all characters in the alnumtext are alphabetic:", alnum_text.isalpha())  # Output: False
    print("Is all characters in the alnumtext are digit:", alnum_text.isdigit())  # Output: False
    print("Is all characters in the alnumtext are alphabetic or numeric characters:", alnum_text.isalnum())  # Output: True
