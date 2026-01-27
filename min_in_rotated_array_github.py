class RotatedArrayMinFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_minimum(self):
        lo = 0
        hi = len(self.numbers) - 1

        while lo < hi:
            # If current range is already sorted,
            # the smallest element is at lo
            if self.numbers[lo] < self.numbers[hi]:
                return self.numbers[lo]

            mid = lo + (hi - lo) // 2

            # Minimum is in the right half
            if self.numbers[mid] > self.numbers[hi]:
                lo = mid + 1
            else:
                # Minimum could be at mid or in left half
                hi = mid

        return self.numbers[lo]


def main():
    numbers = [5, 6, 1, 2, 3, 4]
    finder = RotatedArrayMinFinder(numbers)

    print("Array:", numbers)
    print("Minimum element:", finder.find_minimum())


if __name__ == "__main__":
    main()
