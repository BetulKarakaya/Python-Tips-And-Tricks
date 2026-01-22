class ZeroSumTripletsFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_triplets(self):
        res = []
        nums = sorted(self.numbers)
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicate fixed elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                if curr_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif curr_sum < 0:
                    left += 1
                else:
                    right -= 1

        return res


def main():
    numbers = [-1, 0, 1, 2, -1, -4]
    finder = ZeroSumTripletsFinder(numbers)

    print("Array:", numbers)
    print("Zero Sum Triplets:", finder.find_triplets())


if __name__ == "__main__":
    main()
