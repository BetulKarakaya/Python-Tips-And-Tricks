class ClosestSumFinder:
    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target

    def find_closest_pair(self):
        if len(self.numbers) < 2:
            return []

        nums = sorted(self.numbers)
        left, right = 0, len(nums) - 1

        min_diff = float("inf")
        max_abs_diff = -1
        result = []

        while left < right:
            current_sum = nums[left] + nums[right]
            diff = abs(self.target - current_sum)
            abs_diff = abs(nums[left] - nums[right])

            # Better (closer) sum found
            if diff < min_diff or (diff == min_diff and abs_diff > max_abs_diff):
                min_diff = diff
                max_abs_diff = abs_diff
                result = [nums[left], nums[right]]

            if current_sum < self.target:
                left += 1
            elif current_sum > self.target:
                right -= 1
            else:
                # Exact match is the best possible
                return [nums[left], nums[right]]

        return result


def main():
    numbers = [5, 2, 7, 1, 4]
    target = 13

    finder = ClosestSumFinder(numbers, target)
    result = finder.find_closest_pair()

    print("Array:", numbers)
    print("Target:", target)
    print("Closest Pair:", result)


if __name__ == "__main__":
    main()
