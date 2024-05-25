# filter_example.py

def filter_positive_numbers(numbers):
    """
    Filters out positive numbers from a list of integers.

    Args:
    numbers (list): A list of integers.

    Returns:
    list: A list containing only the positive integers from the input list.
    """
    # Using filter to select only positive numbers
    positive_numbers = list(filter(lambda x: x > 0, numbers))
    return positive_numbers

if __name__ == "__main__":
    # Example list of integers
    sample_numbers = [-10, -5, 0, 5, 10, 15, -20]

    # Applying the filter_positive_numbers function
    result = filter_positive_numbers(sample_numbers)

    # Printing the result
    print(f"Original list: {sample_numbers}")
    print(f"Filtered positive numbers: {result}")
