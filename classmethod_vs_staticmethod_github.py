class Calculator:
    # Class variable to track total calculations
    total_calculations = 0  # Keeps track of how many calculations have been performed

    @staticmethod
    def add(a, b):
        """
        Performs addition of two numbers.
        - Does not depend on any class or instance variables.
        - Static methods are used for simple, independent operations.
        """
        return a + b

    @classmethod
    def increment_calculations(cls):
        """
        Increments the class variable 'total_calculations'.
        - Uses the 'cls' parameter to access and modify class-level data.
        - Ideal for operations that need to track or modify the state of the class itself.
        """
        cls.total_calculations += 1
        return f"Total calculations so far: {cls.total_calculations}"

# Main program
if __name__ == "__main__":
    # Use the static method to add numbers
    result = Calculator.add(5, 7)  # Addition of two numbers
    print(f"Addition Result: {result}")  # Output: 12

    # Call the class method to update and display calculation count
    print(Calculator.increment_calculations())  # Increment and print count: 1

    # Perform another calculation using static method
    another_result = Calculator.add(10, 20)
    print(f"Another Addition Result: {another_result}")  # Output: 30

    # Increment and display calculation count again
    print(Calculator.increment_calculations())  # Increment and print count: 2
