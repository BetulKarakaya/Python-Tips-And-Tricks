def is_palindrome(text):
    """
    Check if the given text is a palindrome (reads the same backward as forward).
    This function ignores spaces, punctuation, and capitalization.
    """
    # Remove spaces and non-alphanumeric characters, and convert to lowercase

    # The filter() function takes two arguments: a function and an iterable (e.g., a string, list, etc.).
    # It applies the given function to each element in the iterable and keeps only the elements 
    # for which the function returns True. 
    # In this case, filter(str.isalnum, text) keeps only alphanumeric characters from the text.

    clean_text = ''.join(filter(str.isalnum, text)).lower()
    
    # Reverse the text using a built-in function
    reversed_text = clean_text[::-1]
    
    # Check if the cleaned text is equal to its reverse
    return clean_text == reversed_text
def main():
    print("✨ Welcome to the Palindrome Checker! ✨")
    user_input = input("Enter a word or sentence: ")
    
    # Check if the input is a palindrome
    if is_palindrome(user_input):
        print("🎉 It's a palindrome! 🎉")
    else:
        print("❌ Not a palindrome. Try again!")

if __name__ == "__main__":
    main()