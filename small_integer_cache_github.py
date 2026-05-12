import sys

def memory_interning_trick():
    # Scenario A: Small integers (Interned)
    a = 256
    b = 256
    
    # Scenario B: Larger integers (Not Interned)
    x = 257
    y = 257

    print("--- The Memory Interning Mystery ---")
    
    # Comparing small integers
    print(f"Is 256 'is' 256? {a is b}")  # True: They share the same memory address
    print(f"Address A: {id(a)} | Address B: {id(b)}")

    # Comparing larger integers
    print(f"Is 257 'is' 257? {x is y}")  # False: They are distinct objects in memory
    print(f"Address X: {id(x)} | Address Y: {id(y)}")

    # Checking 'Value' vs 'Identity'
    print(f"Is 257 '==' 257? {x == y}")  # True: Their values are the same
    
if __name__ == "__main__":
    memory_interning_trick()