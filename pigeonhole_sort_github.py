def pigeonhole_sort(numbers):
    """
    Pigeonhole Sort for integers with a small value range
    """
    if not numbers:
        return numbers

    minimum = min(numbers)
    maximum = max(numbers)
    size = maximum - minimum + 1

    # 1. Create pigeonholes
    holes = [[] for _ in range(size)]

    # 2. Place numbers into their holes
    for num in numbers:
        index = num - minimum
        holes[index].append(num)

    # 3. Collect numbers from holes
    sorted_numbers = []
    for hole in holes:
        sorted_numbers.extend(hole)

    return sorted_numbers


def main():
    data = [8, 3, 2, 7, 4, 6, 8, 1, 5, 3]

    print("--- Original array:")
    print(data)

    sorted_data = pigeonhole_sort(data)

    print("\n--- Sorted array:")
    print(sorted_data)


if __name__ == "__main__":
    main()