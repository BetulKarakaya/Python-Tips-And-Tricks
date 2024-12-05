def unique_word_lengths(text):
    # Calculate lenght of each word in a text
    
    # Split the text into words
    words = text.split()
    
    # Use a set to get unique words (case-insensitive comparison)
    unique_words = set(word.lower() for word in words)
    
    # Simple and effective way to create a dictionary with word lengths
    lengths = {word: len(word) for word in unique_words}
    
    return lengths


if __name__ == "__main__":

    example_text = """Hello, I'm Betül. Here I am again! 
    In this Python code, we identify the unique words in a text and 
    calculate their lengths. In its current form, 
    it's a simple text analysis code. A code like this could be 
    further enhanced for better text analysis by adding word frequency counts. 
    Wishing you days full of coding fun! :D"""
    
    #You can input your own text
    #example_text = input("Input A text To Analysis: ")
    result = unique_word_lengths(example_text)

    print("Input Text:\n", example_text)
    print("\nUnique Word Lengths:\n", result)
