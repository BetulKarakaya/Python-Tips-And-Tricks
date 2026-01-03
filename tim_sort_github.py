class TimSort:
    def __init__(self, data):
        self.data = data
        self.MIN_RUN = 32

    def sort(self):
        n = len(self.data)

        # 1. Sort small runs using Insertion Sort
        for start in range(0, n, self.MIN_RUN):
            end = min(start + self.MIN_RUN - 1, n - 1)
            self._insertion_sort(start, end)

        # 2. Merge runs
        size = self.MIN_RUN
        while size < n:
            for left in range(0, n, size * 2):
                mid = min(left + size - 1, n - 1)
                right = min(left + size * 2 - 1, n - 1)

                if mid < right:
                    self._merge(left, mid, right)

            size *= 2

    # ---------- Helpers ----------

    def _insertion_sort(self, left, right):
        for i in range(left + 1, right + 1):
            key = self.data[i]
            j = i - 1
            while j >= left and self.data[j] > key:
                self.data[j + 1] = self.data[j]
                j -= 1
            self.data[j + 1] = key

    def _merge(self, left, mid, right):
        left_part = self.data[left:mid + 1]
        right_part = self.data[mid + 1:right + 1]

        i = j = 0
        k = left

        while i < len(left_part) and j < len(right_part):
            if left_part[i] <= right_part[j]:
                self.data[k] = left_part[i]
                i += 1
            else:
                self.data[k] = right_part[j]
                j += 1
            k += 1

        while i < len(left_part):
            self.data[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            self.data[k] = right_part[j]
            j += 1
            k += 1


def main():
    data = [5, 21, 7, 23, 19, 1, 3, 12, 2, 15]
    sorter = TimSort(data)

    print("--- Original:", data)
    sorter.sort()
    print("--- Sorted:", data)


if __name__ == "__main__":
    main()
