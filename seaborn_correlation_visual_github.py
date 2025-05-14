import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class CorrelationVisualizer:
    def __init__(self, df: pd.DataFrame):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ Input must be a pandas DataFrame.")
        self.df = df.select_dtypes(include='number')  

    def show_correlation(self):
        corr = self.df.corr()
        print("Feature correlation matrix:\n", corr.round(2))

        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
        plt.title("Feature Correlation Heatmap")
        plt.tight_layout()
        plt.show()

def main():
    data = {
        "Age": [25, 32, 47, 51, 62],
        "Salary": [4000, 5200, 7100, 8000, 8500],
        "Experience": [1, 4, 10, 12, 15]
    }
    df = pd.DataFrame(data)

    app = CorrelationVisualizer(df)
    app.show_correlation()

if __name__ == "__main__":
    main()
