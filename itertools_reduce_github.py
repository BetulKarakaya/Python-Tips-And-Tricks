from functools import reduce

if __name__ == "__main__":
    
    # A list of numbers
    numbers = [3, 7, 12, 19, 21, 8, 15, 22, 18]

    # filter(): Filters the numbers list to keep only even numbers.
    # Lambda function x % 2 == 0 checks if the number is divisible by 2.
    # Filter: Keep only even numbers
    even_numbers = filter(lambda x: x % 2 == 0, numbers)

    # map(): Applies a function (x**2) to each item in the filtered list.
    # This generates a new list with the squares of the even numbers.
    # Map: Square each number
    squared_numbers = map(lambda x: x**2, even_numbers)

    """
    What is reduce?
    In Python, reduce performs an "accumulation" operation that sequentially 
    processes the elements of a list (or any iterable) and returns a single result.

    How does it work?
    reduce takes a function and applies it to the list elements sequentially.
    It performs an operation on the first two elements, gets the result, and then continues 
    processing this result with the third element. Thus, a chain process is created.
    reduce() comes from the functools module, so you need to import it first.
    """
    # reduce(): Accumulates the results of the mapped list by summing them up.
    # functools.reduce applies the lambda function x + y pairwise to the list.
    # Reduce: Sum up all squared numbers
    sum_of_squares = reduce(lambda x, y: x + y, squared_numbers)

    # Display the result
    print("The sum of squares of even numbers is:", sum_of_squares)
