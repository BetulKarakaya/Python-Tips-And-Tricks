import time

class InvalidSizeError(Exception):
    def __init__(self, size, coffee_type=None):
        if coffee_type == "Turkish Coffee":
            message = f"🚨 Turkish Coffee can only be 'Small' size! You cannot select '{size}'."
        else:
            message = f"🚨 Invalid Size: '{size}' is not a valid option. Please choose Small, Medium, or Large."
        super().__init__(message)

class InvalidCoffeeTypeError(Exception):
    def __init__(self, coffee_type):
        super().__init__(f"🚨 Invalid Coffee Type: '{coffee_type}' is not on the menu! Try again. ☕")

class CoffeeOrder:
    menu = {
        "espresso": 30,
        "latte": 40,
        "cappuccino": 45,
        "mocha": 50,
        "turkish coffee": 35  
    }
    
    size_multiplier = {
        "small": 1,
        "medium": 1.5,
        "large": 2
    }

    def __init__(self, coffee_type, size):
        self.coffee_type = coffee_type.lower() 
        self.size = size.lower()

        if self.coffee_type not in self.menu:
            raise InvalidCoffeeTypeError(coffee_type.title())  

        if self.coffee_type == "turkish coffee" and self.size != "small":
            raise InvalidSizeError(self.size, "Turkish Coffee")

        if self.size not in self.size_multiplier:
            raise InvalidSizeError(self.size)

    def calculate_price(self):
        base_price = self.menu[self.coffee_type]
        return base_price * self.size_multiplier.get(self.size, 1)

    def make_coffee(self):
        print(f"\n🔄 Preparing your {self.size.capitalize()} {self.coffee_type.title()}...")
        time.sleep(2)
        print(f"✅ Your {self.size.capitalize()} {self.coffee_type.title()} is ready! ☕ Enjoy!\n")

    def display_order(self):
        print(f"📌 Order Summary:")
        print(f"   ☕ Coffee Type: {self.coffee_type.title()}")
        print(f"   📏 Size: {self.size.capitalize()}")
        print(f"   💰 Price: {self.calculate_price()} TL\n")

def main():
    print("☕ Welcome to Python Café! ☕\n")
    
    while True:
        try:
            coffee_type = input("👉 Choose your coffee (Espresso, Latte, Cappuccino, Mocha, Turkish Coffee): ")
            size = input("👉 Choose size (Small, Medium, Large): ")
            
            order = CoffeeOrder(coffee_type, size)
            order.display_order()
            order.make_coffee()
            
            another = input("Would you like another coffee? (yes/no): ").strip().lower()
            if another != "yes":
                print("👋 Have a great day! ☕")
                break

        except Exception as e:
            print(f"{e}\nTry again! 🚀")

if __name__ == "__main__":
    main()
