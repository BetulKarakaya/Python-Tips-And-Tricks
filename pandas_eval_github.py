import pandas as pd
import numpy as np

class LargeScaleProcessor:
    """
    A class designed for high-performance arithmetic operations 
    on large DataFrames using optimized engines.
    """
    def __init__(self, size=1000000):
        # Creating a large dataset to demonstrate performance
        data = {
            'A': np.random.randn(size),
            'B': np.random.randn(size),
            'C': np.random.randn(size),
            'D': np.random.randn(size)
        }
        self.df = pd.DataFrame(data)

    def __str__(self):
        return f"Processor initialized with {len(self.df)} rows."

    def optimized_calculation(self):
        """
        Performs a complex arithmetic operation across multiple columns 
        using pd.eval() for maximum speed and memory efficiency.
        """
        # TRICK: Instead of df['A'] * df['B'] + ..., we use a string expression
        # This reduces memory 'shuffling' and is significantly faster for large data
        result = pd.eval("(self.df.A + self.df.B) / (self.df.C * self.df.D) ** 2")
        return result

def main():
    # Initialize processor with 1 million rows
    processor = LargeScaleProcessor(size=1000000)
    print(processor)

    # Execute optimized calculation
    print("Executing high-performance calculation...")
    result_array = processor.optimized_calculation()

    # Display a sample of the result
    print("\n--- Calculation Result (Head) ---")
    print(result_array[:5])

if __name__ == "__main__":
    main()