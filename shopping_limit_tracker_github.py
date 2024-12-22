def shopping_spree(items):
    """
    Simulates a shopping spree where we keep track of the total spending 
    and stop once a budget limit is reached.
    """
    budget = 50 
    total_spent = 0 
    
    print("Welcome to the Shopping Spree Tracker!\n")
    
    for item, price in items:
        # Use the assignment expression to update total_spent and check the budget
        if (total_spent := total_spent + price) > budget:
            print(f"Oops! Buying {item} for ${price:.2f} exceeds your budget of ${budget}.")
            print(f"Current total spent: ${total_spent:.2f}")
            break
        print(f"Bought {item} for ${price:.2f}. Total spent: ${total_spent:.2f}")
    else:
        print("\nCongratulations! You stayed within your budget.")

if __name__ == "__main__":
    
    # List of (ItemName, Price) -> We create a list of items and their prices, 
    # allowing us to add multiple items or even the same item with different prices.
    items_to_buy = [
        ("T-shirt", 15.99),
        ("Hat", 10.49),
        ("Socks", 5.99),
        ("Shoes", 40.00),  # Exceeds the budget
        ("Watch", 25.00)
    ]

    shopping_spree(items_to_buy)
