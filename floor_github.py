# Binary Search - O(log n) Time and O(1) Space

class FloorFinder:
    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target

    def find_floor_index(self):
        """
        Finds the index of the largest element <= target using binary search.
        """
        lo = 0
        hi = len(self.numbers) - 1
        result = -1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if self.numbers[mid] > self.target:
                hi = mid - 1
            else:
                # Possible floor found, search right part for a bigger one
                result = mid
                lo = mid + 1

        return result


def main():
    numbers = [1, 2, 8, 10, 10, 12, 19]
    floor_val = 9

    finder = FloorFinder(numbers, floor_val)
    index = finder.find_floor_index()

    print("Array:", numbers)

    if index == -1:
        print(f"Floor of {floor_val} doesn't exist in array")
    else:
        print(f"Floor of {floor_val} is {numbers[index]} at index {index}")


if __name__ == "__main__":
    main()
