import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # 1. Creating a Sample Data Set (Right-skewed distribution)
    data = np.random.exponential(scale=2, size=1000)
    df = pd.DataFrame(data, columns=['Values'])

    # 2. Skewness and Kurtosis Calculation
    skew_val = df['Values'].skew()
    kurt_val = df['Values'].kurt()

    # 3. Visualization
    plt.figure(figsize=(10, 6))

    # Histogram and Density Graph
    sns.histplot(df['Values'], kde=True, color='skyblue', stat="density", linewidth=0)

    info_text = f'Skewness: {skew_val:.2f}\nKurtosis: {kurt_val:.2f}'
    plt.gca().text(0.95, 0.95, info_text, transform=plt.gca().transAxes, 
                fontsize=12, verticalalignment='top', horizontalalignment='right',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))

    plt.title('Data Distribution: Skewness and Kurtosis Analysis', fontsize=14)
    plt.xlabel('Value Range')
    plt.ylabel('Intensity')
    plt.grid(axis='y', alpha=0.3)

    plt.show()

if __name__ == "__main__":
    main()