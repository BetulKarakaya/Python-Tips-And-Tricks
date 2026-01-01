def counting_sort(numbers):
    """
    Counting Sort for non-negative integers
    """
    if not numbers:
        return numbers

    maximum = max(numbers)

    # 1. Create count array
    count = [0] * (maximum + 1)

    # 2. Count occurrences
    for num in numbers:
        count[num] += 1

    # 3. Reconstruct sorted list
    sorted_numbers = []
    for value, freq in enumerate(count):
        sorted_numbers.extend([value] * freq)

    return sorted_numbers


def main():
    data = [4, 2, 2, 8, 3, 3, 1]

    print("--- Original array:")
    print(data)

    sorted_data = counting_sort(data)

    print("\n--- Sorted array:")
    print(sorted_data)


if __name__ == "__main__":
    main()
