from functools import lru_cache
import time

class DataProcessor:
    def __init__(self, source_name):
        self.source_name = source_name

    @property
    @lru_cache(maxsize=1)
    def processed_data(self):
        # Simulate a time-consuming process (e.g., loading or processing data)
        print(f"🔄 Loading and processing data from {self.source_name}...")
        time.sleep(3)  # Expensive operation simulation
        return f"✅ Data from {self.source_name} is processed and ready."

    def __str__(self):
        return f"DataProcessor for source: {self.source_name}"

# Example usage
processor = DataProcessor("Sensor_A")

print("First access (takes time):")
print(processor.processed_data)  # Simulates heavy computation

print("\nSecond access (instant):")
print(processor.processed_data)  # Returns cached result
