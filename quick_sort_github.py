def quick_sort(numbers: list[int]) -> list[int]:
    # Base case: empty or single-element list is already sorted
    if len(numbers) <= 1:
        return numbers

    # Choose pivot (middle element → readable & safe)
    pivot = numbers[len(numbers) // 2]

    # Partition step
    left = [n for n in numbers if n < pivot]
    middle = [n for n in numbers if n == pivot]
    right = [n for n in numbers if n > pivot]

    # Recursively sort left and right
    return quick_sort(left) + middle + quick_sort(right)


def main():
    data = [7, 3, 1, 9, 5, 3, 8]
    print("Original:", data)
    print("Sorted:  ", quick_sort(data))


if __name__ == "__main__":
    main()
