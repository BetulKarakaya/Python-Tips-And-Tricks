class RotatedArrayMaxFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_maximum(self):
        lo = 0
        hi = len(self.numbers) - 1

        while lo < hi:
            # If current range is already sorted,
            # the largest element is at hi
            if self.numbers[lo] < self.numbers[hi]:
                return self.numbers[hi]

            mid = lo + (hi - lo) // 2

            # If mid element is greater than next one,
            # mid is the maximum
            if self.numbers[mid] > self.numbers[mid + 1]:
                return self.numbers[mid]

            # Maximum is in the right half
            if self.numbers[mid] < self.numbers[hi]:
                hi = mid
            else:
                lo = mid + 1

        return self.numbers[lo]


def main():
    numbers = [5, 6, 7, 1, 2, 3, 4]
    finder = RotatedArrayMaxFinder(numbers)

    print("Array:", numbers)
    print("Maximum element:", finder.find_maximum())


if __name__ == "__main__":
    main()
