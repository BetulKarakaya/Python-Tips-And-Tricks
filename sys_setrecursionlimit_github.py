import sys
import time

class RecursionTester:
    """Demonstrates how to safely modify Python's recursion limit."""

    def __init__(self):
        self.original_limit = sys.getrecursionlimit()

    def show_current_limit(self):
        print(f"-- Current recursion limit: {sys.getrecursionlimit()}")

    def increase_limit(self, new_limit: int):
        """Increase recursion depth limit."""
        sys.setrecursionlimit(new_limit)
        print(f"-- Recursion limit increased to: {new_limit}")

    def deep_recursion(self, n):
        """A simple recursive function for testing."""
        if n == 0:
            return "- Reached the base case!"
        return self.deep_recursion(n - 1)

    def run_test(self, depth: int):
        try:
            print(f"\n- Testing recursion with depth = {depth}")
            result = self.deep_recursion(depth)
            print(result)
        except RecursionError:
            print("!! RecursionError: Maximum recursion depth exceeded!")
        finally:
            # Reset to original limit
            sys.setrecursionlimit(self.original_limit)
            print(f"-- Recursion limit reset to {self.original_limit}")


def main():
    tester = RecursionTester()
    tester.show_current_limit()
    tester.increase_limit(3000)
    tester.run_test(2500)   # Works fine with increased limit
    tester.run_test(4000)   # Still safe — shows error gracefully


if __name__ == "__main__":
    main()
