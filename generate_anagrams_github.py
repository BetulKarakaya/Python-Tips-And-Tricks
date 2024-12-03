import itertools

def generate_anagrams(word):
    """
    Generates all possible anagrams for a given word.

    Parameters:
        word (str): The input word to generate anagrams from.

    Returns:
        list: A list of unique anagrams.
    """
    # Use itertools.permutations to create all possible letter arrangements
    permutations = itertools.permutations(word)

    # Join the tuples into strings and remove duplicates by converting to a set
    unique_anagrams = set(''.join(p) for p in permutations)

    # Return the sorted list of unique anagrams
    return sorted(unique_anagrams)


if __name__ == "__main__":
    # Example word for anagram generation
    word = input("Please enter a text: ").lower().strip()

    # Generate and display anagrams
    anagrams = generate_anagrams(word)
    length = len(anagrams)
    print(f"Total {length} anagram generated.💻\nAll anagrams for the word '{word}':")
    print(", ".join(anagrams))
