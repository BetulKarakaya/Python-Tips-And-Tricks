def letter_frequency_graph(text):
    """
    Counts the frequency of each letter in the given text
    and prints a simple ASCII graph of the frequencies.
    """
    # Normalize the text to lowercase and filter out non-letters
    text = ''.join(char.lower() for char in text if char.isalpha())
    
    # Count the occurrences of each letter
    # Use set() to extract unique elements, ensuring no duplicates.
    frequency = {letter: text.count(letter) for letter in set(text)}

    print("📊 Letter Frequency Graph 📊")
    print("-" * 30)
    for letter, count in sorted(frequency.items()):
        # Print letter and frequency as a bar graph
        print(f"{letter}: {'█' * count}")

if __name__ == "__main__":
    print("Welcome to the Letter Frequency Analyzer!")
    sample_text = input("Enter a sentence or text to analyze: ")
    letter_frequency_graph(sample_text)
