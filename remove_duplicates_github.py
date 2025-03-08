import numpy as np
import time

class NumpyTricks:
    
    def __init__(self, size=10**6):
        self.size = size
        self.numbers = list(range(self.size))
        self.numpy_numbers = np.arange(self.size)

    def remove_duplicates(self):
            """ The fastest way to remove duplicates from a list """
            numbers = np.random.randint(0, self.size // 2, self.size).tolist()
            
            start_time = time.time()
            unique_set = list(set(numbers))  # Using set()
            set_time = time.time() - start_time
            
            start_time = time.time()
            n_array = np.array(numbers)
            _, idx = np.unique(n_array, return_index=True)
            unique_numpy = n_array[np.sort(idx)].tolist()
            numpy_time = time.time() - start_time
            
            print(f"🛠️ set() method: {set_time:.6f} sec")
            print(f"⚡ NumPy unique(): {numpy_time:.6f} sec")
            print(f"🚀 NumPy is {set_time / numpy_time:.2f}x faster!\n")

    def run(self):
        self.remove_duplicates()
       

if __name__ == "__main__":
    app = NumpyTricks()
    app.run()
