import pandas as pd
import numpy as np

class DimensionalityReducer:
    """
    A class to perform data compression and feature reduction 
    using Singular Value Decomposition (SVD).
    """
    def __init__(self, data):
        # We must center the data (subtract mean) for PCA/SVD to work
        self.df = pd.DataFrame(data)
        self.centered_matrix = self.df - self.df.mean()

    def __str__(self):
        return f"Dataset ready for reduction: {self.df.shape[1]} features detected."

    def reduce_to_components(self, n_components=2):
        """
        TRICK: np.linalg.svd()
        Decomposes the matrix into U, S, and Vh. 
        Vh contains the 'Principal Components'—the directions 
        of maximum variance in your data.
        """
        # Perform Singular Value Decomposition
        U, S, Vh = np.linalg.svd(self.centered_matrix, full_matrices=False)
        
        # Project the original data onto the top N components
        reduced_data = np.dot(self.centered_matrix, Vh[:n_components].T)
        
        # Return as a clean DataFrame
        cols = [f'Principal_Component_{i+1}' for i in range(n_components)]
        return pd.DataFrame(reduced_data, columns=cols)

def main():
    # Sample Dataset: 4 features that are somewhat related
    data = {
        'Feature_A': [10, 20, 30, 40, 50],
        'Feature_B': [12, 22, 33, 41, 55],
        'Feature_C': [5, 10, 15, 20, 25],
        'Feature_D': [8, 18, 28, 38, 48]
    }

    # Initialize Reducer
    reducer = DimensionalityReducer(data=data)
    print(reducer)

    # Compress 4 columns into just 2
    compressed_df = reducer.reduce_to_components(n_components=2)

    # Display Results
    print("\n--- Compressed Data (Top 2 Principal Components) ---")
    print(compressed_df.round(4))

if __name__ == "__main__":
    main()