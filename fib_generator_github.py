def fibonacci_list(n):
    """
    Generates a Fibonacci sequence as a list up to n elements.
    
    - Uses a list to store all Fibonacci numbers.
    - Memory-intensive for large n since all values are stored.
    """
    # Start with the first two Fibonacci numbers: 0 and 1
    fib_list = [0, 1]
    # Generate the rest of the sequence up to n elements
    for _ in range(2, n):  # Start from index 2 since the first two are already defined
        fib_list.append(fib_list[-1] + fib_list[-2])  # Add the sum of the last two numbers
    return fib_list  # Return the full list

def fibonacci_generator(n):
    """
    Generates Fibonacci numbers using a generator, up to n elements.
    
    - Uses 'yield' to produce one value at a time.
    - Efficient for large n as it doesn't store all values in memory.
    """
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    # Use a loop to generate up to n numbers
    for _ in range(n):
        yield a  # Produce the current value of 'a'
        a, b = b, a + b  # Update 'a' and 'b' to the next two Fibonacci numbers

if __name__ == "__main__":
    # Define how many elements you want in the Fibonacci sequence
    num_elements = 10

    # Generate Fibonacci sequence using a list
    fib_list = fibonacci_list(num_elements)
    print("Fibonacci using list:", fib_list)  # Print the full list of Fibonacci numbers

    # Generate Fibonacci sequence using a generator
    fib_gen = fibonacci_generator(num_elements)
    print("Fibonacci using generator:", list(fib_gen))  # Convert the generator to a list and print it
