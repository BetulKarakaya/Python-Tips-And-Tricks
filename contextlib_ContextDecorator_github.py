import time
from contextlib import ContextDecorator

class TimedTask(ContextDecorator):
    """Measure how long a code block or function takes using both decorator and context manager."""
    def __init__(self, task_name: str):
        self.task_name = task_name

    def __enter__(self):
        self.start = time.time()
        print(f"🟢 Started: {self.task_name}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed = time.time() - self.start
        print(f"🔴 Finished: {self.task_name} (-- {elapsed:.4f}s)\n")
        return False  # Don't suppress exceptions

    # Optional reusable decorator method
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            with self:
                return func(*args, **kwargs)
        return wrapper


# Example usage — both as a decorator and as a context manager
@TimedTask("Simulated Calculation")
def heavy_task():
    total = sum(i * i for i in range(10_000_00))
    return total


def main():
    # Using as decorator
    result = heavy_task()

    # Using as context manager
    with TimedTask("Data Preparation"):
        time.sleep(1.2)
        print("- Preparing data...")

if __name__ == "__main__":
    main()
