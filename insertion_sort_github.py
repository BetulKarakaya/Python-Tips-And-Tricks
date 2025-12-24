def insertion_sort(numbers):
    print("- Initial array:", numbers)

    for i in range(1, len(numbers)):
        current = numbers[i]
        j = i - 1

        print(f"\n* Taking element {current} at index {i}")

        while j >= 0 and numbers[j] > current:
            numbers[j + 1] = numbers[j]
            j -= 1
            print("  Shifting:", numbers)

        numbers[j + 1] = current
        print("  Inserted:", numbers)

    return numbers


def main():
    data = [8, 3, 5, 2, 9, 1]
    sorted_data = insertion_sort(data)
    print("\n- Final sorted array:", sorted_data)


if __name__ == "__main__":
    main()
