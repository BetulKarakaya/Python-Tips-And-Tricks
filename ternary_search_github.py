class TernaryMinIndexFinder:
    def __init__(self, numbers):
        self.numbers = numbers
        self.size = len(numbers)

    def find_min_index(self):
        left = 0
        right = self.size - 1
        candidate = -1

        while left <= right:
            # split range into three parts
            mid_left = left + (right - left) // 3
            mid_right = right - (right - left) // 3

            if self.numbers[mid_left] == self.numbers[mid_right]:
                candidate = mid_left
                left = mid_left + 1
                right = mid_right - 1

            elif self.numbers[mid_left] < self.numbers[mid_right]:
                candidate = mid_left
                right = mid_right - 1

            else:
                candidate = mid_right
                left = mid_left + 1

        return candidate


def main():
    numbers = [9, 7, 1, 2, 3, 6, 10]

    finder = TernaryMinIndexFinder(numbers)
    index = finder.find_min_index()

    print("Array:", numbers)
    print("Minimum element index:", index)
    print("Minimum element value:", numbers[index])


if __name__ == "__main__":
    main()