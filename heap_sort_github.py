def heapify(numbers, n, i):
    """
    Ensure the subtree rooted at index i obeys max-heap property.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and numbers[left] > numbers[largest]:
        largest = left

    if right < n and numbers[right] > numbers[largest]:
        largest = right

    if largest != i:
        numbers[i], numbers[largest] = numbers[largest], numbers[i]
        heapify(numbers, n, largest)


def heap_sort(numbers):
    n = len(numbers)

    # 1- Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(numbers, n, i)

    # 2- Extract elements one by one
    for i in range(n - 1, 0, -1):
        numbers[0], numbers[i] = numbers[i], numbers[0]
        heapify(numbers, i, 0)

    return numbers


def main():
    data = [8, 3, 5, 2, 9, 1]
    print("--- Original array:", data)

    heap_sort(data)
    print("--- Sorted array:", data)


if __name__ == "__main__":
    main()
