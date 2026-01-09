# O(n) Time and O(1) Extra Space

class MissingAndRepeatingFinder:
    def __init__(self, numbers):
        self.numbers = numbers.copy() 
    
    def find_missing_repeating_number(self):
        n = len(self.numbers)
        repeating = -1

        # Mark visited indices
        for i in range(n):
            val = abs(self.numbers[i])

            if self.numbers[val - 1] > 0:
                self.numbers[val - 1] = -self.numbers[val - 1]
            else:
                repeating = val

        missing = -1

        # Find index which is still positive
        for i in range(n):
            if self.numbers[i] > 0:
                missing = i + 1
                break

        return [repeating, missing]


def main():
    numbers = [1, 2, 3, 4, 4, 6, 7] 
    finder = MissingAndRepeatingFinder(numbers)
    result = finder.find_missing_repeating_number()
    
    print("Array:", numbers)
    print("Repeating Number:", result[0])
    print("Missing Number:", result[1])


if __name__ == "__main__":
    main()
