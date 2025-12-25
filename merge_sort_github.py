def merge_sort(numbers):
    # Base case: single element is already sorted
    if len(numbers) <= 1:
        return numbers

    mid = len(numbers) // 2
    left = merge_sort(numbers[:mid])
    right = merge_sort(numbers[mid:])

    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    # Compare elements from both halves
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


def main():
    data = [8, 3, 5, 2, 9, 1]
    print("--- Original array:", data)

    sorted_data = merge_sort(data)
    print("--- Sorted array:", sorted_data)


if __name__ == "__main__":
    main()
