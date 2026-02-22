class AlmostSortedSearch:
    def __init__(self, numbers):
        self.numbers = numbers
        self.size = len(numbers)

    def search(self, target):
        left = 0
        right = self.size - 1

        while left <= right:
            mid = (left + right) // 2

            # Check mid and its neighbors
            if self.numbers[mid] == target:
                return mid

            if mid - 1 >= left and self.numbers[mid - 1] == target:
                return mid - 1

            if mid + 1 <= right and self.numbers[mid + 1] == target:
                return mid + 1

            # Move search space
            if self.numbers[mid] > target:
                right = mid - 2
            else:
                left = mid + 2

        return -1


def main():
    numbers = [10, 3, 40, 20, 50, 80, 70]
    target = 40

    finder = AlmostSortedSearch(numbers)
    index = finder.search(target)

    print("Array:", numbers)
    print("Target:", target)
    print("Index:", index)


if __name__ == "__main__":
    main()