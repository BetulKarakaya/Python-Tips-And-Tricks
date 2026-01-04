class LargestFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_largest(self):
        largest = self.numbers[0]

        for num in self.numbers:
            if num > largest:
                largest = num

        return largest


def main():
    numbers = [3, 7, 2, 9, 4]
    finder = LargestFinder(numbers)

    print("Array:", numbers)
    print("Largest element:", finder.find_largest())


if __name__ == "__main__":
    main()
