# Trick: Swapping two variables without using a temporary variable

def stylish_swap(a, b):
    print(f"Before swap: a = {a}, b = {b}")
    a, b = b, a
    print(f"After swap: a = {a}, b = {b}")
    return a, b

def main():
    try:
        print("Welcome to Stylish Swapper App!")
        a = int(input("Enter first number (a): "))
        b = int(input("Enter second number (b): "))
        stylish_swap(a, b)
    except ValueError:
        print("⚠️ Please enter valid integers only!")

if __name__ == "__main__":
    main()
