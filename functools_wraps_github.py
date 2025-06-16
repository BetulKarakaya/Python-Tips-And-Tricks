import time
from functools import wraps

def timing_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"Running '{func.__name__}'...")
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f"'{func.__name__}' completed in {duration:.4f} seconds.")
        return result
    return wrapper

@timing_logger
def compute_squares(n):
    return [i ** 2 for i in range(n)]

@timing_logger
def wait_a_bit(seconds):
    time.sleep(seconds)
    return f"Waited {seconds} seconds."

def main():
    # Call the decorated functions
    compute_squares(10**5)
    wait_a_bit(2)

if __name__ == "__main__":
    main()
