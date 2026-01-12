#Time Complexity: O(n1 + n2 + n3)   Space Complexity: O(1) (without output)
class CommonElementsFinder:
    def __init__(self, arr1, arr2, arr3):
        self.arr1 = arr1
        self.arr2 = arr2
        self.arr3 = arr3

    def find_common_elements(self):
        i = j = k = 0
        result = []

        while i < len(self.arr1) and j < len(self.arr2) and k < len(self.arr3):
            a, b, c = self.arr1[i], self.arr2[j], self.arr3[k]

            # If all three are equal → common element
            if a == b == c:
                if not result or result[-1] != a:   # avoid duplicates
                    result.append(a)
                i += 1
                j += 1
                k += 1

            # Move the pointer with the smallest value
            elif a < b:
                i += 1
            elif b < c:
                j += 1
            else:
                k += 1

        return result if result else [-1]


def main():
    arr1 = [1, 5, 10, 20, 40, 80]
    arr2 = [6, 7, 20, 80, 100]
    arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

    finder = CommonElementsFinder(arr1, arr2, arr3)
    result = finder.find_common_elements()

    print("Common Elements:", result)


if __name__ == "__main__":
    main()
