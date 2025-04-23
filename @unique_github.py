from enum import Enum, unique

@unique
class IceCreamFlavor(Enum):
    VANILLA = 1
    CHOCOLATE = 2
    STRAWBERRY = 3
    MINT = 4
    COFFEE = 5  
    # Error line:
    #ANOTHER_VANILLA = 1 # ❌ This would throw an error because the value is 1 again!

def display_flavors():
    print("\n🍨 Available Ice Cream Flavors:\n")
    for flavor in IceCreamFlavor:
        print(f"• {flavor.name.title():<12} ➜ Code: {flavor.value}")

def get_flavor_by_value(value):
    try:
        flavor = IceCreamFlavor(value)
        print(f"\n✅ You selected: {flavor.name.title()}")
    except ValueError:
        print("\n⚠️ No flavor found with that code!")

def main():
    display_flavors()
    val = input("\n🔢 Enter the code of your favorite flavor: ").strip()
    if val.isdigit():
        get_flavor_by_value(int(val))
    else:
        print("⚠️ Please enter a valid number.")

if __name__ == "__main__":
    main()
