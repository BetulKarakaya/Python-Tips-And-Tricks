coffee_type = "Latte"   # Global variable, customer order

def coffee_process():
    # Attempting to assign before using will cause UnboundLocalError
    # Uncomment to see the error:
    #print(f"Your order is {coffee_type}")  
    coffee_type = "Espresso"  # Enclosing scope
    def barista_prepare():
        print(f"Barista is preparing: {coffee_type}")  # Local search fails → Enclosing → Espresso

    barista_prepare()


def main():
    print(f"Customer ordered: {coffee_type}")   # Global: Latte
    coffee_process()

if __name__ == "__main__":
    main()
