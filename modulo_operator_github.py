def fizzbuzz():
    
    print("🎮 Welcome to the FizzBuzz Game! 🎮")
    range_limit = input("Please Enter FizzBuzz Upper Limit:")
    print("Numbers divisible by 3 will be 'Fizz', by 5 will be 'Buzz', and by both 3 and 5 will be 'FizzBuzz'!")

    # The modulo operator (%) calculates the remainder of a division.
    # For example: 
    #   10 % 3 = 1 because 10 divided by 3 gives a quotient of 3 and a remainder of 1.
    for number in range(1, int(range_limit)+1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

def main():
    fizzbuzz()
if __name__ == "__main__":
    main()
