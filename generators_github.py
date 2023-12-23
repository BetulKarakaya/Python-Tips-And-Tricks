import sys
import time

# Utilizing a generator to efficiently produce square numbers on-the-fly,
# saving memory by yielding one value at a time instead of creating an entire list.

# Leveraging a generator to dynamically yield square numbers, harnessing the power of the 'yield' keyword to produce values on demand,
# optimizing memory usage by generating and returning each value individually.

def square_numbers_list(n):
    # Creating a list of square numbers using list comprehension
    numbers_list = [x ** 2 for x in range(n)]
    return numbers_list

def square_numbers_generator(n):
    # Creating a generator for square numbers
    for i in range(n):
        yield i ** 2

if __name__ == "__main__":

    for n in (500,5000,50000,500000):

        list_version = square_numbers_list(n)
        # Memory usage and execution time for the list
        print(f"\nMemory usage for list: {sys.getsizeof(list_version)} bytes ,n equals {n}")

    for n in (500,5000,50000,500000):

        generator_version = square_numbers_generator(n)
        # Memory usage and execution time for the generator
        print(f"\nMemory usage for generator: {sys.getsizeof(generator_version)} bytes ,n equals {n} ")



