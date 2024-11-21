import itertools

if __name__ == "__main__":
    # 'cycle' function creates an infinite loop of the given iterable.
    # In this example, a list of colors will be repeatedly cycled.
    colors = ["red", "blue", "green"]

    # The 'cycle' function returns an iterator, which provides the next item each time it's called.
    cycled_colors = itertools.cycle(colors)

    # The loop will run 6 times, but 'cycled_colors' is an infinite iterator,
    # so it can continue indefinitely. Here, we only fetch 6 colors.
    for _ in range(6):
        # The next() function retrieves the next item from the iterator.
        print(next(cycled_colors))
        # The first 3 outputs are from the original list.
        # After that, the list restarts from the beginning in a cycle.

    # Output:
    # red
    # blue
    # green
    # red
    # blue
    # green
