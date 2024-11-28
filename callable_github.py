class Greeting:
    def __call__(self, name):
        
        # This class defines a custom callable object.
        # Adding the __call__ method allows instances of this class 
        # to behave like functions when called.
        return f"Hello, {name}! Welcome to the callable world!"

# Regular function
def add(a, b):
    # A standard function in Python is always callable.
    return a + b

# Normal object
class NonCallable:
    # This class does NOT implement the __call__ method.
    # Instances of this class cannot behave like functions.
    pass

if __name__ == "__main__":
    # Create instances
    greeting = Greeting()
    non_callable = NonCallable()

    # Test callable objects
    print("Is 'greeting' callable?", callable(greeting))  # True, since __call__ is defined
    print("Is 'add' callable?", callable(add))  # True, since it's a function
    print("Is 'non_callable' callable?", callable(non_callable))  # False, it's a regular object

    # Use the callable object
    if callable(greeting):
        print(greeting("Betül"))  # "Hello, Betül! Welcome to the callable world!"
