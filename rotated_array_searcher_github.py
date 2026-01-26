class RotatedArraySearcher:
    def __init__(self, numbers, key):
        self.numbers = numbers
        self.key = key

    def search_key(self):
        lo = 0
        hi = len(self.numbers) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            # Key found
            if self.numbers[mid] == self.key:
                return mid

            # Left half is sorted
            if self.numbers[lo] <= self.numbers[mid]:
                if self.numbers[lo] <= self.key < self.numbers[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1

            # Right half is sorted
            else:
                if self.numbers[mid] < self.key <= self.numbers[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return -1


def main():
    numbers = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    key = 3

    searcher = RotatedArraySearcher(numbers, key)
    index = searcher.search_key()

    print("Array:", numbers)
    print("Key:", key)
    print("Index:", index)


if __name__ == "__main__":
    main()
