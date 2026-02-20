class MedianOfSortedArrays:
    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.size = len(first)

    def find_median(self):
        left = 0
        right = self.size

        while left <= right:
            cut_first = (left + right) // 2
            cut_second = self.size - cut_first

            left_first = float("-inf") if cut_first == 0 else self.first[cut_first - 1]
            right_first = float("inf") if cut_first == self.size else self.first[cut_first]

            left_second = float("-inf") if cut_second == 0 else self.second[cut_second - 1]
            right_second = float("inf") if cut_second == self.size else self.second[cut_second]

            # Correct partition found
            if left_first <= right_second and left_second <= right_first:
                return (max(left_first, left_second) +
                        min(right_first, right_second)) / 2

            # Too many elements taken from first array
            if left_first > right_second:
                right = cut_first - 1
            else:
                left = cut_first + 1

        return 0.0


def main():
    first = [1, 12, 15, 26, 38]
    second = [2, 13, 17, 30, 45]

    finder = MedianOfSortedArrays(first, second)
    median = finder.find_median()

    print("First array:", first)
    print("Second array:", second)
    print("Median:", median)


if __name__ == "__main__":
    main()