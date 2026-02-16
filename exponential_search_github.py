class ExponentialSearchFinder:
    def __init__(self, numbers):
        self.numbers = numbers
        self.size = len(numbers)

    def search(self, target):
        if self.size == 0:
            return -1

        # Step 1: find search bounds by exponential growth
        bound = 1
        while bound < self.size and self.numbers[bound] < target:
            bound *= 2

        left = bound // 2
        right = min(bound, self.size - 1)

        # Step 2: binary search within the found range
        return self._binary_search(left, right, target)

    def _binary_search(self, left, right, target):
        while left <= right:
            mid = (left + right) // 2

            if self.numbers[mid] == target:
                return mid

            if self.numbers[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


def main():
    numbers = [2, 3, 4, 10, 40]
    target = 10

    finder = ExponentialSearchFinder(numbers)
    index = finder.search(target)

    print("Array:", numbers)
    if index != -1:
        print(f"Target {target} found at index {index}")
    else:
        print("Target not found")


if __name__ == "__main__":
    main()