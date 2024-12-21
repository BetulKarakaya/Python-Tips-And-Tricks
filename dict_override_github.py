def main():
    # Menus from two restaurants
    first_menu = {
        "Burger": 5.99,
        "Pizza": 8.99,
        "Salad": 4.99,
        "Soup": 3.99
    }

    second_menu = {
        "Pizza": 7.99,  # Updated price
        "Steak": 14.99,
        "Salad": 5.49,  # Updated price
        "Dessert": 3.49
    }

    # Combine menus using the | operator
    # The | operator in dictionaries allows the values from the right-hand side to override 
    # those from the left-hand side. When two dictionaries are merged using this operator, 
    # the result is a single dictionary. However, if both sides contain the same keys, 
    # the values from the right-hand side will be used.
    combined_menu = first_menu | second_menu


    # Print the combined menu
    print("Welcome to the Fusion Restaurant! Here's our combined menu:")
    for item, price in combined_menu.items():
        print(f"{item}: ${price:.2f}")


if __name__ == "__main__":
    main()