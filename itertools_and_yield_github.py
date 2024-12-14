import itertools
import time

def infinite_colors():
    """
    Cycles through a list of colors infinitely using 'yield'.
    """
    colors = ['🔴', '🟢', '🔵', '🟡', '🟣']  # A list of colors (you can use text, if you have problem with emojis)
    while True:
        for color in colors:
            yield color   # Yield returns the current value and pauses the function here
            # Explanation:
            # - 'yield' is like a "pause and return" in a function.
            # - It doesn't terminate the function like 'return' but pauses it, saving the state.
            # - When the function is called again, it resumes from this exact point.
            # - This is especially useful for infinite or very large sequences where storing
            #   all values in memory at once would be inefficient.

def main():
    # Create the generator
    color_gen = infinite_colors()

    # Print colors in an loop with a delay
    for _ in range(20):
        print(next(color_gen))  # Print the next color
        time.sleep(0.5)  # Pause for half a second

if __name__ == "__main__":
    main()