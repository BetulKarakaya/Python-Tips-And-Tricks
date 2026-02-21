class MedianOfTwoSortedArrays:
    def __init__(self, first, second):
        # Always binary search on the smaller array
        if len(first) <= len(second):
            self.small = first
            self.large = second
        else:
            self.small = second
            self.large = first

        self.n = len(self.small)
        self.m = len(self.large)

    def find_median(self):
        left = 0
        right = self.n

        while left <= right:
            cut_small = (left + right) // 2
            cut_large = (self.n + self.m + 1) // 2 - cut_small

            left_small = float("-inf") if cut_small == 0 else self.small[cut_small - 1]
            right_small = float("inf") if cut_small == self.n else self.small[cut_small]

            left_large = float("-inf") if cut_large == 0 else self.large[cut_large - 1]
            right_large = float("inf") if cut_large == self.m else self.large[cut_large]

            # Correct partition
            if left_small <= right_large and left_large <= right_small:
                total = self.n + self.m

                if total % 2 == 0:
                    return (max(left_small, left_large) +
                            min(right_small, right_large)) / 2
                else:
                    return max(left_small, left_large)

            # Too many elements taken from small array
            if left_small > right_large:
                right = cut_small - 1
            else:
                left = cut_small + 1

        return 0.0


def main():
    first = [-5, 3, 6, 12, 15]
    second = [-12, -10, -6, -3, 4, 10]

    finder = MedianOfTwoSortedArrays(first, second)
    median = finder.find_median()

    print("First array:", first)
    print("Second array:", second)
    print("Median:", median)


if __name__ == "__main__":
    main()