class InterpolationSearchFinder:
    def __init__(self, numbers):
        self.numbers = numbers
        self.size = len(numbers)

    def search(self, target):
        low = 0
        high = self.size - 1

        while (
            low <= high
            and self.numbers[low] <= target
            and self.numbers[high] >= target
        ):
            # Avoid division by zero
            if self.numbers[low] == self.numbers[high]:
                return low if self.numbers[low] == target else -1

            # Estimate probable position
            pos = low + (
                (target - self.numbers[low]) * (high - low)
            ) // (self.numbers[high] - self.numbers[low])

            if self.numbers[pos] == target:
                return pos

            if self.numbers[pos] < target:
                low = pos + 1
            else:
                high = pos - 1

        return -1


def main():
    numbers = [
        10, 12, 13, 16, 18, 19,
        20, 21, 22, 23, 24,
        33, 35, 42, 47
    ]

    target = 18

    finder = InterpolationSearchFinder(numbers)
    index = finder.search(target)

    print("Array:", numbers)
    if index != -1:
        print(f"Target {target} found at index {index}")
    else:
        print("Target not found")


if __name__ == "__main__":
    main()