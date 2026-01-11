#Time: O(k log k)   Space: O(k)
import heapq

class KthSmallestFinder:
    def __init__(self, matrix, k):
        self.matrix = matrix
        self.k = k
        self.n = len(matrix)

    def find_kth_smallest(self):
        min_heap = []
        visited = set()

        # Start from top-left element
        heapq.heappush(min_heap, (self.matrix[0][0], 0, 0))
        visited.add((0, 0))

        count = 0

        while min_heap:
            value, row, col = heapq.heappop(min_heap)
            count += 1

            if count == self.k:
                return value

            # Move DOWN
            if row + 1 < self.n and (row + 1, col) not in visited:
                heapq.heappush(
                    min_heap,
                    (self.matrix[row + 1][col], row + 1, col)
                )
                visited.add((row + 1, col))

            # Move RIGHT
            if col + 1 < self.n and (row, col + 1) not in visited:
                heapq.heappush(
                    min_heap,
                    (self.matrix[row][col + 1], row, col + 1)
                )
                visited.add((row, col + 1))

        return -1

def main():
    matrix = [
        [1,  5,  9],
        [10, 11, 13],
        [12, 13, 15]
    ]

    k = 5
    finder = KthSmallestFinder(matrix, k)

    print("Matrix:")
    for row in matrix:
        print(row)

    print(f"\n{k}th smallest element:", finder.find_kth_smallest())


if __name__ == "__main__":
    main()
