from contextlib import contextmanager
import inspect
import time

class ContextTracker:
    """Tracks entry and exit of code blocks with timing and source info."""

    @contextmanager
    def track(self, label: str):
        frame = inspect.currentframe().f_back
        func_name = frame.f_code.co_name
        file_name = frame.f_code.co_filename
        line_no = frame.f_lineno

        start = time.time()
        print(f"\n🔹 Entering '{label}' in {func_name}() [{file_name}:{line_no}]")
        try:
            yield
        finally:
            elapsed = time.time() - start
            print(f"🔸 Exiting '{label}' — Duration: {elapsed:.4f}s\n")


class DataPipeline:
    """Simulates a data processing pipeline."""

    def __init__(self):
        self.tracker = ContextTracker()

    def load_data(self):
        with self.tracker.track("Load Data"):
            time.sleep(1.2)
            print("- Data loaded successfully.")

    def process_data(self):
        with self.tracker.track("Process Data"):
            time.sleep(0.8)
            print("- Data processed with transformations.")

    def save_results(self):
        with self.tracker.track("Save Results"):
            time.sleep(0.5)
            print("- Results saved to database.")


def main():
    pipeline = DataPipeline()
    pipeline.load_data()
    pipeline.process_data()
    pipeline.save_results()


if __name__ == "__main__":
    main()
