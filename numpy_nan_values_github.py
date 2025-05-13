import numpy as np

class CleanerArray:
    @staticmethod
    def clean_and_convert(data):
        try:
            arr = np.array(data, dtype=float)
        except ValueError:
            raise ValueError("❌ Make sure all items can be converted to float or are NaN.")
        
        #Replace NaN with column mean
        nan_mask = np.isnan(arr)
        mean_val = np.nanmean(arr)
        arr[nan_mask] = mean_val

        return arr

def main():
    raw_data = [1.5, 2.3, np.nan, 4.7, np.nan, 6.1]
    print("Raw data with NaNs:")
    print(raw_data)

    cleaned_array = CleanerArray.clean_and_convert(raw_data)
    print("\nCleaned NumPy array:")
    print(cleaned_array)

if __name__ == "__main__":
    main()
