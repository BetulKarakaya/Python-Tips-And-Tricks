import sys


class ArithmeticProgressionMissingFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def _find_missing_recursive(self, left, right, diff):
        # No missing element in this range
        if left >= right:
            return sys.maxsize

        mid = (left + right) // 2

        # Missing element is right after mid
        if self.numbers[mid + 1] - self.numbers[mid] != diff:
            return self.numbers[mid] + diff

        # Missing element is right before mid
        if mid > 0 and self.numbers[mid] - self.numbers[mid - 1] != diff:
            return self.numbers[mid - 1] + diff

        # Left side is valid → search right half
        if self.numbers[mid] == self.numbers[0] + mid * diff:
            return self._find_missing_recursive(mid + 1, right, diff)

        # Otherwise search left half
        return self._find_missing_recursive(left, mid - 1, diff)

    def find_missing(self):
        n = len(self.numbers)

        # Possible common differences
        d1 = self.numbers[1] - self.numbers[0]
        d2 = self.numbers[-1] - self.numbers[-2]
        d3 = (self.numbers[-1] - self.numbers[0]) // n

        # Determine correct common difference
        if d1 == d2:
            diff = d1
        elif d1 == d3:
            diff = d1
        else:
            diff = d2

        # All elements are the same
        if diff == 0:
            return self.numbers[0]

        result = self._find_missing_recursive(0, n - 1, diff)

        # Missing element is after the last element
        return self.numbers[0] + n * diff if result == sys.maxsize else result


def main():
    numbers = [2, 4, 8, 10, 12, 14]
    finder = ArithmeticProgressionMissingFinder(numbers)

    print("Array:", numbers)
    print("Missing element:", finder.find_missing())


if __name__ == "__main__":
    main()
