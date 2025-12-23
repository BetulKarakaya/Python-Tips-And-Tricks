def merge_three(left, middle, right):
    """Merge three sorted lists into one sorted list."""
    result = []
    i = j = k = 0

    while i < len(left) or j < len(middle) or k < len(right):
        candidates = []

        if i < len(left):
            candidates.append((left[i], "l"))
        if j < len(middle):
            candidates.append((middle[j], "m"))
        if k < len(right):
            candidates.append((right[k], "r"))

        value, src = min(candidates)

        result.append(value)

        if src == "l":
            i += 1
        elif src == "m":
            j += 1
        else:
            k += 1

    return result


def three_way_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    if len(arr) < 3:
        return sorted(arr)

    third = len(arr) // 3

    left = three_way_merge_sort(arr[:third])
    middle = three_way_merge_sort(arr[third:2 * third])
    right = three_way_merge_sort(arr[2 * third:])

    return merge_three(left, middle, right)


def main():
    numbers = [38, 27, 43, 3, 9, 82, 10]
    print("Original list :", numbers)

    sorted_numbers = three_way_merge_sort(numbers)
    print("Sorted list   :", sorted_numbers)


if __name__ == "__main__":
    main()
