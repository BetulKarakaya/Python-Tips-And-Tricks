# using Hash Set in O(n) Time and O(n) Space
import sys

class FirstRepeatingNumberFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_repeating_number(self):
        s = set()

        # If an element is already present, return it
        # else insert it
        minEle = sys.maxsize
        for i in range(len(self.numbers) - 1, -1, -1):
            if self.numbers[i] in s:
                minEle = min(minEle, self.numbers[i])
            s.add(self.numbers[i])
           
        # If no element repeats
        return -1 if minEle == sys.maxsize else minEle


def main():
    numbers =  [10, 5, 3, 4, 3, 5, 6]
    finder = FirstRepeatingNumberFinder(numbers)
    result = finder.find_repeating_number()
    
    print("Array:", numbers)
    if result == -1:
        print("No repeating found!")
    else:
        print("First Repeating Number:", result)


if __name__ == "__main__":
    main()
