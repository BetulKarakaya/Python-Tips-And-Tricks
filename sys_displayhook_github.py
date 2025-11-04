import sys

class CustomDisplayHook:
    """Customize how Python displays evaluated expressions using sys.displayhook."""

    def __init__(self):
        self.original_hook = sys.displayhook

    def fancy_display(self, value):
        """A custom hook that prints results with a visual twist."""
        if value is not None:
            print(f" Result => {value!r}")
            sys._last_value = value  # keep compatibility with normal behavior

    def activate(self):
        sys.displayhook = self.fancy_display
        print(" Custom display hook activated!")

    def restore(self):
        sys.displayhook = self.original_hook
        print(" Display hook restored to default.")

def main():
    hook = CustomDisplayHook()
    hook.activate()

    # Simulating interactive output
    hook.fancy_display(42)
    hook.fancy_display("Betül is coding ")

    hook.restore()

if __name__ == "__main__":
    main()
