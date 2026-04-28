import numpy as np

class EinsteinProcessor:
    """
    A class to demonstrate high-speed tensor operations 
    using Einstein Summation notation.
    """
    def __init__(self, data_matrix):
        self.A = np.array(data_matrix)

    def fast_dot_product(self, weights):
        """
        TRICK: np.einsum()
        Notation 'ij, j -> i' means:
        - Take matrix 'ij' (Rows i, Cols j)
        - Take vector 'j' (Cols j)
        - Multiply and sum over 'j'
        - Return 'i' (The resulting vector)
        """
        W = np.array(weights)
        return np.einsum('ij, j -> i', self.A, W)

    def calculate_outer_product(self, vec_b):
        """
        Notation 'i, j -> ij' creates a matrix where 
        every element (i,j) is A[i] * B[j].
        """
        B = np.array(vec_b)
        return np.einsum('i, j -> ij', self.A[0], B) # Using first row as vector

def main():
    # 1. Simulate a dataset: 5 samples, 3 features each
    features = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12],
        [13, 14, 15]
    ]
    
    # Weights for each feature
    weights = [0.5, 0.2, 0.3]

    processor = EinsteinProcessor(features)

    # Perform a Batch Dot Product (Weighted Sum)
    # Traditional: np.dot(features, weights)
    # Einstein Style:
    weighted_sums = processor.fast_dot_product(weights)

    print("Original Features Matrix (5x3):")
    print(np.array(features))
    print("\nApplied Weights:", weights)
    print("-" * 30)
    print("Weighted Sum Results (einsum 'ij, j -> i'):")
    print(weighted_sums)

if __name__ == "__main__":
    main()