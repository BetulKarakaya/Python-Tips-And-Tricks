import sys

class RegularPerson:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class SlottedPerson:
    __slots__ = ['name', 'age']
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

def main():
    print("--- Memory Size Comparison ---")
    
    regular = RegularPerson("Betül", 25)
    slotted = SlottedPerson("Betül", 25)

    print(f"RegularPerson: {sys.getsizeof(regular)} bytes")
    print(f"SlottedPerson: {sys.getsizeof(slotted)} bytes")
    
    # Try adding new attribute to both
    print("\n--- Trying to add new attribute ---")
    
    regular.city = "Ankara"
    print(f"regular.city = {regular.city}")
    print(f"RegularPerson (after adding city): {sys.getsizeof(regular)} bytes")

    try:
        slotted.city = "Ankara"  #Error
    except AttributeError as e:
        print(f"Can't add 'city' to SlottedPerson: {e}")

if __name__ == "__main__":
    main()
