import heapq

class KLargestFinder:
    def __init__(self, numbers, k):
        self.numbers = numbers
        self.k = k

    def find_k_largest(self):
        # Create a min-heap with first k elements
        min_heap = self.numbers[:self.k]
        heapq.heapify(min_heap)

        # Process remaining elements
        for x in self.numbers[self.k:]:
            if x > min_heap[0]:
                heapq.heapreplace(min_heap, x)

        # Extract elements from heap (ascending order)
        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap))

        # Convert to descending order
        return result[::-1]


def main():
    numbers = [1, 23, 12, 9, 30, 2, 50]
    k = 3

    finder = KLargestFinder(numbers, k)
    result = finder.find_k_largest()

    print("Array:", numbers)
    print(f"{k} Largest Elements:", result)


if __name__ == "__main__":
    main()
