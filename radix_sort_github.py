def counting_sort_by_digit(numbers, digit_place):
    """
    Stable counting sort used by Radix Sort
    digit_place = 1, 10, 100, ...
    """
    count = [0] * 10
    output = [0] * len(numbers)

    # Count digit frequency
    for num in numbers:
        digit = (num // digit_place) % 10
        count[digit] += 1

    # Prefix sum (positions)
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output (RIGHT → LEFT for stability)
    for i in range(len(numbers) - 1, -1, -1):
        digit = (numbers[i] // digit_place) % 10
        output[count[digit] - 1] = numbers[i]
        count[digit] -= 1

    return output


def radix_sort(numbers):
    """
    Radix Sort using LSD approach
    """
    max_number = max(numbers)
    digit_place = 1

    while max_number // digit_place > 0:
        numbers = counting_sort_by_digit(numbers, digit_place)
        digit_place *= 10

    return numbers


def main():
    data = [170, 45, 75, 90, 802, 24, 2, 66]

    print("--- Original array:", data)
    sorted_data = radix_sort(data)
    print("--- Sorted array:", sorted_data)


if __name__ == "__main__":
    main()
