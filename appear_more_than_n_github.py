class Candidate:
    def __init__(self):
        self.value = None
        self.count = 0


class MoreThanNDKFinder:
    def __init__(self, numbers, k):
        self.numbers = numbers
        self.k = k
        self.n = len(numbers)

    def find_elements(self):
        if self.k < 2:
            return []

        # Step 1: Create k-1 candidates
        candidates = [Candidate() for _ in range(self.k - 1)]

        # Step 2: Moore’s Voting (candidate selection)
        for num in self.numbers:
            found = False

            # Case 1: number already a candidate
            for c in candidates:
                if c.value == num:
                    c.count += 1
                    found = True
                    break

            if found:
                continue

            # Case 2: empty slot exists
            for c in candidates:
                if c.count == 0:
                    c.value = num
                    c.count = 1
                    found = True
                    break

            # Case 3: no slot → decrement all
            if not found:
                for c in candidates:
                    c.count -= 1

        # Step 3: Verify actual counts
        result = []
        for c in candidates:
            if c.value is not None:
                actual = self.numbers.count(c.value)
                if actual > self.n // self.k:
                    result.append((c.value, actual))

        return result


def main():
    numbers = [3, 4, 2, 2, 1, 2, 3, 3]
    k = 4

    finder = MoreThanNDKFinder(numbers, k)
    result = finder.find_elements()

    print("Array:", numbers)
    if not result:
        print("No elements appear more than n/k times.")
    else:
        for value, count in result:
            print(f"Number: {value} → Count: {count}")


if __name__ == "__main__":
    main()
