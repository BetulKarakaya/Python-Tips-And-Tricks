import heapq

# O(n log k) Time and O(n) Space

class TopKFrequentFinder:
    def __init__(self, numbers, k):
        self.numbers = numbers
        self.k = k

    def find_top_k(self):
        # Count frequencies
        freq_map = {}
        for num in self.numbers:
            freq_map[num] = freq_map.get(num, 0) + 1

        # Min-heap: (frequency, number)
        min_heap = []

        for num, freq in freq_map.items():
            heapq.heappush(min_heap, (freq, num))

            # Keep heap size at most k
            if len(min_heap) > self.k:
                heapq.heappop(min_heap)

        # Extract elements (highest frequency last in heap)
        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap)[1])

        # Optional: return in descending frequency order
        return result[::-1]


def main():
    numbers = [3, 1, 4, 4, 5, 2, 6, 1]
    k = 2

    finder = TopKFrequentFinder(numbers, k)
    result = finder.find_top_k()

    print("Top K frequent elements:")
    for val in result:
        print(val, end=" ")


if __name__ == "__main__":
    main()
