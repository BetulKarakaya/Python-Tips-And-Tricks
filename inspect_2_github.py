import inspect

class CodeInspector:
    def __init__(self, obj):
        self.obj = obj

    def show_info(self):
        """Display detailed information about a function or class."""
        print(f"\n* Object Name: {self.obj.__name__}")
        print(f"* Source File: {inspect.getsourcefile(self.obj)}")
        print(f"* Lines of Code: {len(inspect.getsourcelines(self.obj)[0])}")

        # Display docstring if available
        doc = inspect.getdoc(self.obj)
        print(f"* Docstring: {doc if doc else 'No documentation provided.'}\n")

        # Display source preview
        print("-Source Preview:")
        print("".join(inspect.getsourcelines(self.obj)[0]))

        # If the object is a class, show its methods too
        if inspect.isclass(self.obj):
            print("\n-Class Methods:")
            methods = inspect.getmembers(self.obj, predicate=inspect.isfunction)
            for name, func in methods:
                print(f"  + {name}() → {inspect.getdoc(func) or 'No docstring.'}")


# Example class for inspection
class Calculator:
    """A simple calculator class for basic operations."""

    def add(self, x, y):
        """Return the sum of two numbers."""
        return x + y

    def multiply(self, x, y):
        """Return the product of two numbers."""
        return x * y


# Example function for inspection
def greet(name):
    """Return a personalized greeting message."""
    return f"Hello, {name}!"


def main():
    print("-Inspecting Function:")
    func_inspector = CodeInspector(greet)
    func_inspector.show_info()

    print("\n" + "=" * 50)
    
    print("\n-Inspecting Class:")
    class_inspector = CodeInspector(Calculator)
    class_inspector.show_info()


if __name__ == "__main__":
    main()
