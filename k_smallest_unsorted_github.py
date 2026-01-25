import heapq

class KthSmallestFinder:
    def __init__(self, numbers, k):
        self.numbers = numbers
        self.k = k

    def find_kth_smallest(self):
        max_heap = []

        for num in self.numbers:
            # Use negative values to simulate max-heap
            heapq.heappush(max_heap, -num)

            # Keep only k elements in heap
            if len(max_heap) > self.k:
                heapq.heappop(max_heap)

        # Top of the heap is the k-th smallest element
        return -max_heap[0]


def main():
    numbers = [7, 10, 4, 3, 20, 15]
    k = 3

    finder = KthSmallestFinder(numbers, k)

    print("Array:", numbers)
    print(f"{k}th Smallest Element:", finder.find_kth_smallest())


if __name__ == "__main__":
    main()
