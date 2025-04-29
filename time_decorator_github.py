import time
from functools import wraps

"""Advanced Trick: A custom decorator to time function execution
This script demonstrates how to create and use a custom Python decorator to measure 
and display how long a function takes to execute. The `timer_decorator` wraps any 
function, prints a message before and after its execution, and reports the total 
duration in seconds. This technique is particularly useful for performance profiling, 
debugging bottlenecks, and optimizing time-consuming operations like data processing, 
API requests, file downloads, and more.

The `@wraps` from `functools` ensures that the metadata of the original function 
(e.g., its name and docstring) is preserved after decoration.

Example functions:
- `process_data`: Simulates a time-consuming task using `time.sleep`.
- `download_file`: Simulates a file download.

Run this script to see how the decorator tracks execution time for both tasks.
"""
def timer_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"⏱️ Running '{func.__name__}'...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"✅ Done in {end - start:.4f} seconds.\n")
        return result
    return wrapper

@timer_decorator
def process_data():
    print("🔄 Simulating data processing...")
    time.sleep(1.2)  # Simulate heavy task
    return "📊 Data processed."

@timer_decorator
def download_file():
    print("🌐 Simulating file download...")
    time.sleep(0.8)  # Simulate another task
    return "📁 File downloaded."

def main():
    result1 = process_data()
    result2 = download_file()
    print(result1)
    print(result2)

if __name__ == "__main__":
    main()
