class SecondLargestFinder:
    def __init__(self,numbers):
        self.numbers = numbers
        # Sort the array in non-decreasing order
        self.sorted_array = sorted(self.numbers)

    def find_second_largest(self):
    
        n = len(self.numbers)
        # start from second last element as last element is the largest
        for i in range(n - 2, -1, -1):
            # return the first element which is not equal to the 
            # largest element
            if self.sorted_array[i] < self.sorted_array[n - 1]:
                return self.sorted_array[i]
        
        # If no second largest element was found, return -1
        return -1


def main():
    numbers = [3, 7, 2, 9, 9, 4]
    finder = SecondLargestFinder(numbers)

    print("Array:", numbers)
    print("Sorted Array:", sorted(numbers))
    print("Second Largest element:", finder.find_second_largest())


if __name__ == "__main__":
    main()
   