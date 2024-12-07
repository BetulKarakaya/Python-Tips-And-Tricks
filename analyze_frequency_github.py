from collections import Counter  # Import Counter to count word frequencies

def analyze_frequency(raw_input):
    # Splitting and cleaning the text
    words = raw_input.split()  # Splitting the text into words based on spaces
    cleaned_words = [word.strip(".,!?").lower() for word in words]  # Removing punctuation and converting to lowercase

    # Counting the word frequencies
    word_counts = Counter(cleaned_words)  # Using Counter to count occurrences of each word

    return word_counts

if __name__ == "__main__":
    print("Hello! This program analyzes the words in your given text.")
    user_text = input("Please enter a text: ") 

    analyzed_text = analyze_frequency(user_text)

    print("\nWord Analysis Results:")
    for word, count in analyzed_text.items():  # Iterating through each word and its count
        print(f"{word}: {count}")

    # Ending the program with a friendly message
    print("\nThank you! Your text has been analyzed. 😄")