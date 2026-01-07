class MissingNumberFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_missing_number(self):
        left = 0
        right = len(self.numbers) - 1

        while left <= right:
            mid = (left + right) // 2

            if self.numbers[mid] == mid:
                left = mid + 1
            else:
                right = mid - 1

        return left


def main():
    numbers = [0, 1, 2, 4, 5]
    finder = MissingNumberFinder(numbers)

    print("Array:", numbers)
    print("Missing number:", finder.find_missing_number())


if __name__ == "__main__":
    main()
