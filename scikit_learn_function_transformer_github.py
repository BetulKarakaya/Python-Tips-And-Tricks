import numpy as np
import pandas as pd
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import Pipeline

class MLPreprocessingBridge:
    """
    A class to demonstrate how to bridge custom NumPy logic
    into the Scikit-Learn ecosystem.
    """
    def __init__(self):
        # We define a custom log transformation (log1p handles zeros safely)
        self.log_transformer = FunctionTransformer(np.log1p, validate=True)

    def build_pipeline(self):
        """
        TRICK: FunctionTransformer in a Pipeline.
        This ensures our custom math is applied automatically 
        during both training and prediction.
        """
        pipeline = Pipeline([
            ('log_transform', self.log_transformer)
        ])
        return pipeline

def main():
    raw_data = np.array([[10], [100], [1000], [10000]], dtype=float)
    
    bridge = MLPreprocessingBridge()
    pipe = bridge.build_pipeline()
    
    processed_data = pipe.fit_transform(raw_data)

    print("--- Scikit-Learn Custom Transformation ---")
    results = pd.DataFrame({
        "Original": raw_data.flatten(),
        "Log_Transformed": processed_data.flatten()
    })
    print(results.round(4))

if __name__ == "__main__":
    main()