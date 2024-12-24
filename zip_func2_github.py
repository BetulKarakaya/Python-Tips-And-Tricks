def pair_lists(list1, list2):
    """
    Pair items with quantities using zip().
    The function returns a list of tuples so it can be reused.
    """
    return list(zip(list1, list2))

def unpair_lists(zipped):
    """
    Unpair the zipped list back into two separate lists using zip(*).
    """
    list1, list2 = zip(*zipped)
    return list1, list2

def main():
    # 🍎 Inventory: Items and Quantities in a Grocery Store
    items = ["Apples", "Bananas", "Carrots", "Dates", "Eggplants"]
    quantities = [10, 25, 30, 15, 8]

    # Pairing items and quantities
    inventory = pair_lists(items, quantities)

    # Display the inventory in a table format
    print("📦 Grocery Store Inventory 📦")
    print("-" * 30)
    print(f"{'Item':<15}{'Quantity':<10}")
    print("-" * 30)

    for item, quantity in inventory:
        print(f"{item:<15}{quantity:<10}")

    # Bonus: Reverse zip to separate items and quantities back
    print("\n✨ Back to separate lists! ✨")
    new_items, new_quantities = unpair_lists(inventory)
    print("Items:", list(new_items))
    print("Quantities:", list(new_quantities))

if __name__ == "__main__":
    main()