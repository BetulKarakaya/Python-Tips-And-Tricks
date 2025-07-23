from dataclasses import dataclass
import sys

# 1. Customer class with slots for memory efficiency
@dataclass(slots=True)
class Customer:
    id: int
    name: str
    balance: float

# 2. Version without slots
@dataclass
class CustomerLoose:
    id: int
    name: str
    balance: float

def main():
    # Object with slots
    c1 = Customer(1, "Betül", 1500.0)
    # Object without slots
    c2 = CustomerLoose(2, "Ali", 1000.0)

    print("Object with slots:")
    print(f"Name: {c1.name}, Balance: {c1.balance}")
    print("Size in memory:", sys.getsizeof(c1))

    print("\nObject without slots:")
    print(f"Name: {c2.name}, Balance: {c2.balance}")
    print("Size in memory:", sys.getsizeof(c2))

    print("\nTrying to add a dynamic attribute to the slot-enabled object:")
    try:
        c1.city = "Ankara"  # Expecting AttributeError
    except AttributeError as e:
        print("Error:", e)

    print("\nAdding a dynamic attribute to the object without slots:")
    c2.city = "Istanbul"
    print("New attribute added:", c2.city)

if __name__ == "__main__":
    main()
