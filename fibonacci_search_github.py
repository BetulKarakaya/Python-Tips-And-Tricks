class FibonacciSearch:
    def __init__(self, numbers):
        self.numbers = numbers
        self.size = len(numbers)

    def search(self, target):
        # Initialize fibonacci numbers
        fib_prev = 0
        fib_curr = 1
        fib_next = fib_prev + fib_curr

        # Find the smallest fibonacci number >= size
        while fib_next < self.size:
            fib_prev = fib_curr
            fib_curr = fib_next
            fib_next = fib_prev + fib_curr

        # Marks eliminated range from the front
        offset = -1

        while fib_next > 1:
            index = min(offset + fib_prev, self.size - 1)

            if self.numbers[index] < target:
                fib_next = fib_curr
                fib_curr = fib_prev
                fib_prev = fib_next - fib_curr
                offset = index

            elif self.numbers[index] > target:
                fib_next = fib_prev
                fib_curr = fib_curr - fib_prev
                fib_prev = fib_next - fib_curr

            else:
                return index

        # Check last possible position
        if fib_curr and offset + 1 < self.size and self.numbers[offset + 1] == target:
            return offset + 1

        return -1


def main():
    numbers = [2, 3, 4, 10, 40]
    target = 10

    finder = FibonacciSearch(numbers)
    index = finder.search(target)

    print("Array:", numbers)
    print("Target:", target)
    print("Index:", index)


if __name__ == "__main__":
    main()