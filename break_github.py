def search_for_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(f"Even number found: {number}")
            break
    else:
        # This block runs only if no break occurred
        print("No even number found.")

# Try both cases:
search_for_even([1, 3, 5])      # ➜ No even number found.
search_for_even([1, 3, 4, 5])   # ➜ Even number found: 4
