def sum_of_evens(numbers):
    
    # Filter out only the even numbers using filter() and a lambda function
    # filter(function, iterable) filters elements in the iterable based on the function's condition.
    # It returns only those elements for which the function evaluates to True.
    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    total = sum(even_numbers)
    return total

def main():
    
    print("🔢 Sum of Even Numbers 🔢")
    user_input = input("Enter a list of numbers separated by spaces: ")
    
    # Convert the input string to a list of integers
    # map(function, iterable) applies the given function to every element in the iterable.
    # It returns a map object, which can be converted to a list or other iterables.
    numbers = list(map(int, user_input.split()))
    print(f"\n✨ The sum of even numbers in your list is: {sum_of_evens(numbers)}")

if __name__ == "__main__":
    main()