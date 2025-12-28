def cycle_sort(numbers):
    """
    Cycle Sort minimizes the number of writes by placing each element
    directly into its correct position.
    """
    n = len(numbers)

    for cycle_start in range(n - 1):
        item = numbers[cycle_start]
        pos = cycle_start

        # Find the correct position for item
        for i in range(cycle_start + 1, n):
            if numbers[i] < item:
                pos += 1

        # If item is already in correct position
        if pos == cycle_start:
            continue

        # Skip duplicates
        while item == numbers[pos]:
            pos += 1

        # Place item to its correct position
        numbers[pos], item = item, numbers[pos]

        # Rotate the rest of the cycle
        while pos != cycle_start:
            pos = cycle_start

            for i in range(cycle_start + 1, n):
                if numbers[i] < item:
                    pos += 1

            while item == numbers[pos]:
                pos += 1

            numbers[pos], item = item, numbers[pos]

    return numbers


def main():
    data = [8, 3, 5, 2, 9, 1]
    print("--- Original array:", data)

    cycle_sort(data)
    print("--- Sorted array:", data)


if __name__ == "__main__":
    main()
