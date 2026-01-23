class PartitionElementFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_partition_element(self):
        n = len(self.numbers)

        if n < 3:
            return -1

        # left_max[i] holds the maximum value from index 0 to i
        left_max = [0] * n
        left_max[0] = self.numbers[0]

        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], self.numbers[i])

        # right_min keeps track of minimum value on the right side
        right_min = self.numbers[-1]

        # check elements from right to left (excluding edges)
        for i in range(n - 2, 0, -1):
            if (
                self.numbers[i] >= left_max[i - 1]
                and self.numbers[i] <= right_min
            ):
                return self.numbers[i]

            right_min = min(right_min, self.numbers[i])

        return -1


def main():
    numbers = [5, 1, 4, 3, 6, 8, 10, 7, 9]
    finder = PartitionElementFinder(numbers)

    print("Array:", numbers)
    print("Required Element:", finder.find_partition_element())


if __name__ == "__main__":
    main()
