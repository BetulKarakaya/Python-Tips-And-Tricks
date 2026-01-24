class LargestPairSumFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_largest_pair_sum(self):
        n = len(self.numbers)

        if n < 2:
            return -1

        # Initialize the largest and second largest values
        if self.numbers[0] > self.numbers[1]:
            first = self.numbers[0]
            second = self.numbers[1]
        else:
            first = self.numbers[1]
            second = self.numbers[0]

        # Traverse remaining elements
        for i in range(2, n):
            current = self.numbers[i]

            if current > first:
                second = first
                first = current
            elif current > second:
                second = current

        return first + second


def main():
    numbers = [12, 34, 10, 6, 40]
    finder = LargestPairSumFinder(numbers)

    print("Array:", numbers)
    print("Max Pair Sum:", finder.find_largest_pair_sum())


if __name__ == "__main__":
    main()
