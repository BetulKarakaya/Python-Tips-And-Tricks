from collections import Counter


if __name__ == "__main__":

    # Define the list with repeated numbers
    sample_list = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4, 1, 2, 2, 1, 4, 3, 2, 2, 2, 2]

    # Count occurrences of each number using Counter
    # Counter creates a dictionary-like object where keys are list elements and values are their counts
    element_counts = Counter(sample_list)
    # Example output: Counter({2: 8, 4: 6, 1: 4, 3: 3})

    # Find the most frequent element using max with the key parameter
    # We extract the element with the highest count value in Counter
    most_frequent = max(element_counts, key=element_counts.get)
    # max(..., key=element_counts.get) retrieves the key with the largest associated value
    # Example: For Counter({2: 8, 4: 6, 1: 4, 3: 3}), it returns 2

    # Print the full frequency count (for transparency)
    print("Frequency of each element:", element_counts)

    # Print the most frequent element
    print("The most frequent element is:", most_frequent)
