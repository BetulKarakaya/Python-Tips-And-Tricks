def bucket_sort(numbers):
    """
    Bucket Sort for floating point numbers between 0 and 1
    """
    bucket_count = len(numbers)
    buckets = [[] for _ in range(bucket_count)]

    # 1. Distribute numbers into buckets
    for num in numbers:
        index = int(num * bucket_count)
        buckets[index].append(num)

    # 2. Sort each bucket (using built-in sort)
    for bucket in buckets:
        bucket.sort()

    # 3. Merge buckets
    sorted_numbers = []
    for bucket in buckets:
        sorted_numbers.extend(bucket)

    return sorted_numbers


def main():
    data = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]

    print("--- Original array:")
    print(data)

    sorted_data = bucket_sort(data)

    print("\n--- Sorted array:")
    print(sorted_data)


if __name__ == "__main__":
    main()
