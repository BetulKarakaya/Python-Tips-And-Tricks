import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import re

def analyze_text_frequency(text, top_n=5):
    """
    Analyzes the frequency of words in a given text and visualizes the top N most frequent words.
    
    Parameters:
    - text (str): The input text for analysis.
    - top_n (int): The number of most frequent words to display.
    
    Returns:
    - None
    """

    cleaned_text = re.sub(r'[^\w\s]', '', text).lower()

    words = cleaned_text.split()

  
    word_counts = Counter(words)
    most_common_words = word_counts.most_common(top_n)
    words, counts = zip(*most_common_words)

    plt.figure(figsize=(8, 6))
    plt.bar(words, counts, color='teal', alpha=0.8)
    plt.title("Most Frequent Words", fontsize=16, fontweight='bold')
    plt.xlabel("Words", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.yticks(np.arange(0, max(counts) +1, 1))
    plt.xticks(rotation = 45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.gca().set_axisbelow(True)
    plt.show()

def main():
    print("Welcome to the Text Frequency Analyzer!")
    sample_text = input("Enter a text to analyze: ")

    top_n = int(input("How many top frequent words would you like to visualize? (e.g., 5): "))
    analyze_text_frequency(sample_text, top_n)

if __name__ == "__main__":
    main()
