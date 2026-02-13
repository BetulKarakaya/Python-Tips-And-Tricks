import math


class JumpSearchFinder:
    def __init__(self, numbers):
        self.numbers = numbers
        self.size = len(numbers)

    def search(self, target):
        if self.size == 0:
            return -1

        jump = int(math.sqrt(self.size))
        left = 0
        right = jump

        # Step 1: Find the block where target may exist
        while right < self.size and self.numbers[right - 1] < target:
            left = right
            right += jump

        # Step 2: Linear search inside the block
        for i in range(left, min(right, self.size)):
            if self.numbers[i] == target:
                return i

        return -1


def main():
    numbers = [
        0, 1, 1, 2, 3, 5, 8, 13,
        21, 34, 55, 89, 144, 233,
        377, 610
    ]

    target = 55

    finder = JumpSearchFinder(numbers)
    index = finder.search(target)

    print("Array:", numbers)
    if index != -1:
        print(f"Target {target} found at index {index}")
    else:
        print("Target not found")


if __name__ == "__main__":
    main()