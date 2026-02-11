class SentinelSearchFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def search(self, key):
        n = len(self.numbers)

        # Store last element
        last = self.numbers[n - 1]

        # Place the key as a sentinel at the end
        self.numbers[n - 1] = key

        index = 0
        while self.numbers[index] != key:
            index += 1

        # Restore the last element
        self.numbers[n - 1] = last

        # Check if key was found
        if index < n - 1 or self.numbers[n - 1] == key:
            return index
        else:
            return -1


def main():
    numbers = [10, 20, 180, 30, 60, 50, 110, 100, 70]
    key = 180

    finder = SentinelSearchFinder(numbers)
    index = finder.search(key)

    print("Array:", numbers)
    if index != -1:
        print(f"{key} is present at index {index}")
    else:
        print("Element not found")


if __name__ == "__main__":
    main()
