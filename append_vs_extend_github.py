def main():
    print("\n--- append() ---")
    list_a = [1, 2, 3]
    list_a.append([4, 5])

    print("list_a:", list_a)
    # Result: [1, 2, 3, [4, 5]]

    print("\n--- extend() ---")
    list_b = [1, 2, 3]
    list_b.extend([4, 5])

    print("list_b:", list_b)
    # Result: [1, 2, 3, 4, 5]

    print("\n--- append() inside loop (common mistake) ---")
    numbers = [1, 2]
    for n in [3, 4]:
        numbers.append(n)

    print("numbers:", numbers)
    # Result: [1, 2, 3, 4]

    print("\n--- extend() with string (⚠️ surprise) ---")
    chars = ["a", "b"]
    chars.extend("cd")

    print("chars:", chars)
    # Result: ['a', 'b', 'c', 'd']


if __name__ == "__main__":
    main()
