import numpy as np
import pandas as pd

class RiskModeler:
    """
    A class to demonstrate advanced piecewise transformations
    on high-volume student data.
    """
    def __init__(self, scores):
        self.scores = np.array(scores)

    def calculate_dynamic_risk(self):
        """
        TRICK: np.piecewise() with functional mappings.
        Segments:
        1. Low (0-4): Logarithmic scaling (diminishing impact)
        2. Medium (4-7): Linear scaling
        3. High (7-10): Exponential scaling (accelerated risk)
        """
        # 1. Define Conditions
        conditions = [
            (self.scores < 4),
            (self.scores >= 4) & (self.scores < 7),
            (self.scores >= 7)
        ]

        # 2. Define Functions for each segment
        functions = [
            lambda x: np.log1p(x),           # Logarithmic (smooth start)
            lambda x: x * 1.2,               # Linear (steady growth)
            lambda x: np.power(x, 1.5)       # Exponential (critical jump)
        ]

        # 3. Apply piece-by-piece
        return np.piecewise(self.scores, conditions, functions)

def main():
    # Simulate 1,000,000 student depression or expectation scores
    np.random.seed(42)
    sample_scores = np.random.uniform(0, 10, 1000000)

    modeler = RiskModeler(sample_scores)
    risk_output = modeler.calculate_dynamic_risk()

    # Create a summary to see the transformation
    results = pd.DataFrame({
        "Original_Score": sample_scores,
        "Adjusted_Risk": risk_output
    })

    print("--- Piecewise Transformation Sample ---")
    print(results.head(15).round(3))

if __name__ == "__main__":
    main()