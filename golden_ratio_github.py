import math

def fibonacci(limit):
    fib_sequence = [0, 1]  # Initial Fibonacci numbers
    
    # Generate Fibonacci sequence
    # Every time we add to our list, we take the first and second last element.
    for i in range(2, limit):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence

def golden_ratio(limit, fibonacci_list):
   
    if limit < 2:
        print("You need at least 2 limit to calculate the Golden Ratio.")
        return

    golden_ratios = []

    #The Golden Ratio is calculated as the ratio of the (i)-th element to the (i-1)-th 
    # element in the Fibonacci sequence. 
    # As the sequence progresses, the ratio (i / (i-1)) approaches the mathematical 
    # value of the Golden Ratio.

    for i in range(2, limit):
        # Calculate ratio of consecutive terms
        ratio = fibonacci_list[i] / fibonacci_list[i-1]
        golden_ratios.append(ratio)

    return golden_ratios
   

def main():
    
    print("Golden Ratio and Fibonacci Sequence Calculator".center(50, "-"))
    limit = int(input("Enter the number of terms to calculate (minimum 2): "))

    
    fibonacci_list = fibonacci(limit = limit)
    print("Fibonacci Sequence:")
    print(fibonacci_list)
    

    golden_ratios_list = golden_ratio(limit = limit, fibonacci_list = fibonacci_list)
    print("\nGolden Ratio Approximations:")
    for i, ratio in enumerate(golden_ratios_list, start=2):
        print(f"Term {i}/{i-1}: {ratio:.8f}")

    
    golden_ratio_reel = (1 + math.sqrt(5)) / 2
    print(f"\nThe mathematical Golden Ratio (φ) is approximately: {golden_ratio_reel:.8f}")
    
   
if __name__ == "__main__":
    main()
