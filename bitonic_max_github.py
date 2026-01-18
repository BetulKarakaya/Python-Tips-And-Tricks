# Python program to find bitonic point in an array using Binary Search
# O(log n) Time and O(1) Space
# Note: Bitonic Point is a point in bitonic sequence before which elements 
# are strictly increasing and after which elements are strictly decreasing.


class BitonicMaxFinder:
    def __init__(self, numbers):
        self.numbers = numbers
        self.length = len(self.numbers)
    
    def find_maximum(self):

        # Check if the first element is maximum
        if self.length == 1 or self.numbers[0] > self.numbers[1]:
            return self.numbers[0]

        # Check if the last element is maximum
        if self.numbers[self.length - 1] > self.numbers[self.length - 2]:
            return self.numbers[self.length - 1]

        # Search Space for binary Search
        lo, hi = 1, self.length - 2

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            # If the element at mid is maximum then return it
            if self.numbers[mid] > self.numbers[mid - 1] and self.numbers[mid] > self.numbers[mid + 1]:
                return self.numbers[mid]

            # If next element is greater, then maximum
            # element will exist in the right subarray
            if self.numbers[mid] < self.numbers[mid + 1]:
                lo = mid + 1

            # Otherwise, it will exist in left subarray
            else:
                hi = mid - 1

        return self.numbers[hi]


if __name__ == "__main__":
    numbers  = [4, 5,8, 9, 11, 17, 29, 35, 44, 62, 52, 37]
    finder = BitonicMaxFinder(numbers)
    max = finder.find_maximum()
    print(f"Bitonic Maximum Value is {max}")