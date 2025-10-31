import sys

class MemoryProfiler:
    """Measures memory usage of different Python objects."""

    def __init__(self):
        self.results = {}

    def analyze(self, label: str, obj):
        """Store and print the memory size of an object."""
        size = sys.getsizeof(obj)
        self.results[label] = size
        print(f"* Object: {label:<10} | Size: {size} bytes")

    def summary(self):
        """Display the total and comparative summary."""
        print("\n-- Memory Usage Summary:")
        total = sum(self.results.values())
        for name, size in self.results.items():
            percent = (size / total) * 100
            print(f" - {name:<10}: {size} bytes ({percent:.2f}%)")
        print(f"\n-- Total: {total} bytes")


def main():
    profiler = MemoryProfiler()

    # Different data structures
    numbers = list(range(1000))
    text = "Python " * 200
    dictionary = {str(i): i for i in range(300)}
    tuple_data = tuple(numbers)

    profiler.analyze("List", numbers)
    profiler.analyze("String", text)
    profiler.analyze("Dict", dictionary)
    profiler.analyze("Tuple", tuple_data)

    profiler.summary()


if __name__ == "__main__":
    main()
