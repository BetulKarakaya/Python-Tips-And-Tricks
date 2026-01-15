# Binary Search - O(log n) Time and O(1) Space

class FloorCeilingFinder:
    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target

    def find_floor_and_ceiling(self):
        lo = 0
        hi = len(self.numbers) - 1

        floor_index = -1
        ceiling_index = -1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if self.numbers[mid] == self.target:
                # Exact match → both floor & ceiling
                return mid, mid

            elif self.numbers[mid] < self.target:
                # Possible floor found, go right
                floor_index = mid
                lo = mid + 1

            else:
                # Possible ceiling found, go left
                ceiling_index = mid
                hi = mid - 1

        return floor_index, ceiling_index


def main():
    numbers = [1, 2, 8, 10, 10, 12, 19]
    target = 9

    finder = FloorCeilingFinder(numbers, target)
    floor_i, ceil_i = finder.find_floor_and_ceiling()

    print("Array:", numbers)
    print("Target:", target)

    if floor_i == -1:
        print("Floor: Not found")
    else:
        print("Floor:", numbers[floor_i])

    if ceil_i == -1:
        print("Ceiling: Not found")
    else:
        print("Ceiling:", numbers[ceil_i])


if __name__ == "__main__":
    main()
