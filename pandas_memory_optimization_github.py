import pandas as pd
import numpy as np

class MemoryOptimizer:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def optimize(self):
        optimized_df = self.df.copy()
        for col in optimized_df.select_dtypes(include=['int', 'float']).columns:
            col_min = optimized_df[col].min()
            if pd.api.types.is_integer_dtype(optimized_df[col]):
                if col_min >= 0:
                    optimized_df[col] = pd.to_numeric(optimized_df[col], downcast='unsigned')
                else:
                    optimized_df[col] = pd.to_numeric(optimized_df[col], downcast='integer')
            else:
                optimized_df[col] = pd.to_numeric(optimized_df[col], downcast='float')
        return optimized_df

def main():
    data = {
        'A': np.random.randint(0, 1000, size=10000),
        'B': np.random.randn(10000) * 100
    }
    df = pd.DataFrame(data)

    print("Before optimization:")
    print(df.info())

    optimizer = MemoryOptimizer(df)
    optimized_df = optimizer.optimize()

    print("\nAfter optimization:")
    print(optimized_df.info())

if __name__ == "__main__":
    main()
