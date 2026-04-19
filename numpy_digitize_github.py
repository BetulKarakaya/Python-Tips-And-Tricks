import numpy as np
import pandas as pd

class DataBinner:
    """
    A class to perform lightning-fast discretization of 
    continuous numerical data using NumPy.
    """
    def __init__(self, data):
        self.data = np.array(data)

    def __str__(self):
        return f"Binner initialized with {len(self.data)} data points."

    def categorize(self, thresholds, labels):
        """
        TRICK: np.digitize()
        It returns an array of indices, where each index indicates 
        which 'bin' the value belongs to based on the thresholds.
        """
        # np.digitize maps values to bin indices
        # bins=[18, 30, 60] creates intervals: (-inf, 18), [18, 30), [30, 60), [60, +inf)
        indices = np.digitize(self.data, bins=thresholds)
        
        # Map indices to your custom labels
        return np.array(labels)[indices]

def main():
    # 1. Create 1 million random ages
    ages = np.random.randint(0, 100, 1000000)
    
    # 2. Define Thresholds and Labels
    # We define 3 boundaries, which creates 4 categories
    thresholds = [18, 30, 60]
    labels = ["Child", "Young Adult", "Adult", "Senior"]

    # 3. Initialize and Run
    binner = DataBinner(ages)
    print(binner)
    
    categorized_data = binner.categorize(thresholds, labels)

    # 4. Display a sample of the results
    print("\n--- Categorization Sample (First 10) ---")
    sample_df = pd.DataFrame({
        "Original_Age": ages[:10],
        "Category": categorized_data[:10]
    })
    print(sample_df)

if __name__ == "__main__":
    main()