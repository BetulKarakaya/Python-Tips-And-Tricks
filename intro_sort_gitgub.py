import math

class IntroSort:
    def __init__(self, data):
        self.data = data

    def sort(self):
        max_depth = 2 * math.floor(math.log2(len(self.data)))
        self._introsort(0, len(self.data) - 1, max_depth)

    def _introsort(self, start, end, depth_limit):
        size = end - start + 1

        # 1. Small partition → Insertion Sort
        if size < 16:
            self._insertion_sort(start, end)
            return

        # 2. Depth limit reached → Heap Sort
        if depth_limit == 0:
            self._heap_sort(start, end)
            return

        # 3. Otherwise → Quick Sort partition
        pivot = self._partition(start, end)
        self._introsort(start, pivot - 1, depth_limit - 1)
        self._introsort(pivot + 1, end, depth_limit - 1)

    # ---------- Sorting helpers ----------

    def _partition(self, low, high):
        pivot = self.data[high]
        i = low

        for j in range(low, high):
            if self.data[j] <= pivot:
                self.data[i], self.data[j] = self.data[j], self.data[i]
                i += 1

        self.data[i], self.data[high] = self.data[high], self.data[i]
        return i

    def _insertion_sort(self, low, high):
        for i in range(low + 1, high + 1):
            key = self.data[i]
            j = i - 1
            while j >= low and self.data[j] > key:
                self.data[j + 1] = self.data[j]
                j -= 1
            self.data[j + 1] = key

    def _heap_sort(self, low, high):
        import heapq
        heap = self.data[low:high + 1]
        heapq.heapify(heap)

        for i in range(low, high + 1):
            self.data[i] = heapq.heappop(heap)


def main():
    data = [9, 3, 7, 1, 6, 2, 8, 5, 4]
    sorter = IntroSort(data)

    print("--- Original:", data)
    sorter.sort()
    print("--- Sorted:", data)


if __name__ == "__main__":
    main()
