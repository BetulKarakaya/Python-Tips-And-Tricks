# Binary Search - O(log n) Time and O(1) Space

class CeilingFinder:
    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target

    def find_ceiling_index(self):
        """
        Finds the index of the smallest element >= target using binary search.
        """
        lo = 0
        hi = len(self.numbers) - 1
        result = -1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if self.numbers[mid] < self.target:
                lo = mid + 1
            else:
                # Possible ceiling found, search left part for smaller one
                result = mid
                hi = mid - 1

        return result


def main():
    numbers = [1, 2, 8, 10, 10, 12, 19]
    ceiling_val = 3

    finder = CeilingFinder(numbers, ceiling_val)
    index = finder.find_ceiling_index()

    print("Array:", numbers)

    if index == -1:
        print(f"Ceiling of {ceiling_val} doesn't exist in array")
    else:
        print(f"Ceiling of {ceiling_val} is {numbers[index]} at index {index}")


if __name__ == "__main__":
    main()
