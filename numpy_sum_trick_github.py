import numpy as np
import time

class ListTricks:
    def __init__(self, size=10**6):
        self.size = size
        self.numbers = list(range(self.size))
        self.numpy_numbers = np.arange(self.size)

    def sum_trick(self):
       
        start_time = time.time()
        sum_python = sum(self.numbers)
        python_time = time.time() - start_time
        
        start_time = time.time()
        sum_numpy = np.sum(self.numpy_numbers)
        numpy_time = time.time() - start_time
        
        print(f"🐍 Built-in sum(): {python_time:.6f} sec")
        print(f"⚡ NumPy sum(): {numpy_time:.6f} sec")
        print(f"🚀 Speed Gain: {python_time / numpy_time:.2f}x faster with NumPy!\n")

    
    def run(self):
        print("Comparison of Python sum() and numpy.sum()".center(100,"-"))
        self.sum_trick()
       

if __name__ == "__main__":
    app = ListTricks()
    app.run()
