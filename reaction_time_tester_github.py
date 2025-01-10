import time
import random

def reaction_time_test():
    
    # Generate a random floating-point number between 2 and 5.
    # random.uniform(a, b) creates a random number in the range [a, b],
    # where 'a' is the lower bound (inclusive) and 'b' is the upper bound (inclusive).
    # This ensures that the delay before the "GO!" signal will vary unpredictably
    # between 2 and 5 seconds, adding an element of surprise for the user.
    delay = random.uniform(2, 5)  
    time.sleep(delay)

    print("GO!")
    start_time = time.time()  # Start the timer
    input()  # Wait for the user to press Enter
    end_time = time.time()  # Stop the timer

    reaction_time = end_time - start_time
    print(f"Your reaction time is {reaction_time:.3f} seconds.")

def main():

    print("Welcome to the Reaction Time Tester!")
    print("When you see 'GO!', press Enter as fast as you can.") 
    input("Press Enter to start...")
    
    reaction_time_test()

if __name__ == "__main__":
    main()