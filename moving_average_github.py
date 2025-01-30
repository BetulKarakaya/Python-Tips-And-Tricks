import numpy as np
import matplotlib.pyplot as plt



# Define a function to calculate moving average
def moving_average(data, window_size=10):
    """
    Computes the moving average of a given dataset using a sliding window.
    
    Parameters:
        data (array): Input dataset.
        window_size (int): Size of the moving window.
        
    Returns:
        np.array: Smoothed data using moving average.
    """
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')



def visualize(data, smoothed_data, window_size):
    
    # Plot original data vs. smoothed data
    plt.figure(figsize=(12, 5))
    plt.plot(data, label="Original Data", alpha=0.5)
    plt.plot(range(window_size -1, len(data)), smoothed_data, label="Smoothed Data (Moving Average)", color="red")
    plt.legend(loc="upper right")  
    plt.title("Moving Average Smoothing with NumPy")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.show()


def main():
    # Generate a random dataset (1000 data points)
    np.random.seed(42)  # For reproducibility
    data = np.random.normal(loc=50, scale=10, size=1000)  # Mean = 50, Std Dev = 10
    while(True):
        try:
            window_size = int(input("Please Enter Window Size To Smooth Data: "))
            smoothed_data = moving_average(data, window_size = window_size)
            visualize(data = data,smoothed_data = smoothed_data, window_size= window_size)
            break
        except Exception as e:
                    print(f"Error: {e}")

if __name__ == "__main__":
    main()