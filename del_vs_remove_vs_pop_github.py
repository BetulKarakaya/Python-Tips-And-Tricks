def main():
    numbers = [10, 20, 30, 40, 50]

    print("\nOriginal list:")
    print(numbers)

    print("\n--- remove(value) ---")
    nums_remove = numbers.copy()
    nums_remove.remove(30)   # Removes the VALUE 30
    print(nums_remove)
    # [10, 20, 40, 50]

    print("\n--- pop(index) ---")
    nums_pop = numbers.copy()
    removed_item = nums_pop.pop(2)  # Removes by INDEX
    print("Removed item:", removed_item)
    print(nums_pop)
    # Removed item: 30

    print("\n--- pop() without index ---")
    nums_pop_last = numbers.copy()
    last_item = nums_pop_last.pop()
    print("Removed item:", last_item)
    print(nums_pop_last)
    # Removes last element

    print("\n--- del index ---")
    nums_del = numbers.copy()
    del nums_del[2]
    print(nums_del)
    # [10, 20, 40, 50]

    print("\n--- del slice ---")
    nums_slice = numbers.copy()
    del nums_slice[1:4]
    print(nums_slice)
    # [10, 50]


if __name__ == "__main__":
    main()
