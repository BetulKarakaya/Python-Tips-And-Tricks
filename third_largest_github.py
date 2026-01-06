class ThirdLargestFinder:
    def __init__(self,numbers):
        self.numbers = numbers
      
    def find_third_largest(self):
        first = second = third = float('-inf')

        for x in self.numbers:
            # If current element is greater than first
            if x > first:
                third = second
                second = first
                first = x
            # If x is between first and second
            elif x > second and x != first:
                third = second
                second = x
            # If x is between second and third
            elif x > third and x != second and x != first:
                third = x

        res = []
        if first == float('-inf'):
            return res
        res.append(first)
        if second == float('-inf'):
            return res
        res.append(second)
        if third == float('-inf'):
            return res
        res.append(third)

        return res

def main():
    numbers = [3, 7, 2, 9, 9, 3, 7, 9, 4]
    finder = ThirdLargestFinder(numbers)

    print("Array:", numbers)
    print("Sorted Array:", sorted(numbers))
    print("Third Largest element:", (finder.find_third_largest())[-1])


if __name__ == "__main__":
    main()