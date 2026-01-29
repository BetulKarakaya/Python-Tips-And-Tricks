# O(log n) Time and O(1) Space
# A peak element is greater than its neighbors

class PeakElementFinder:
    def __init__(self, numbers):
        self.numbers = numbers
        self.n = len(numbers)

    def find_peak_index(self):
        # If there is only one element, it is a peak
        if self.n == 1:
            return 0

        # Check first element
        if self.numbers[0] > self.numbers[1]:
            return 0

        # Check last element
        if self.numbers[self.n - 1] > self.numbers[self.n - 2]:
            return self.n - 1

        lo, hi = 1, self.n - 2

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            # If mid is greater than both neighbors → peak found
            if (self.numbers[mid] > self.numbers[mid - 1] and
                self.numbers[mid] > self.numbers[mid + 1]):
                return mid

            # Peak lies on the right side
            if self.numbers[mid] < self.numbers[mid + 1]:
                lo = mid + 1
            # Peak lies on the left side
            else:
                hi = mid - 1

        return -1


def main():
    numbers = [1, 2, 4, 5, 7, 8, 3, 2, 4, 1]
    finder = PeakElementFinder(numbers)

    peak_index = finder.find_peak_index()
    print("Array:", numbers)
    print("Peak index:", peak_index)
    print("Peak value:", numbers[peak_index])


if __name__ == "__main__":
    main()
