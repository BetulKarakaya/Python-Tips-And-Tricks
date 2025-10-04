import numpy as np

class ShoppingCart:
    def __init__(self, items: dict):
        """
        Each key = product name
        Each value = [quantity, price_per_unit]
        """
        self.items = items

    def cost_per_product(self):
        """Calculate and return cost for each product (quantity * price)."""
        costs = {}
        for product, (qty, price) in self.items.items():
            costs[product] = np.prod([qty, price])
        return costs

    def total_cost(self):
        """Calculate the total cost of all products."""
        return np.sum(list(self.cost_per_product().values()))

    def display_cart(self):
        """Pretty print cart items with details."""
        print("Shopping Cart Summary:")
        print("-" * 40)
        for product, (qty, price) in self.items.items():
            print(f"{product:<10} | Qty: {qty:<2} | Unit Price: ${price:<3} | Total: ${qty * price}")
        print("-" * 40)
        print(f"Total Cost: ${self.total_cost()}")


def main():
    #Product list: name → [quantity, price_per_unit]
    cart_items = {
        "Apples": [3, 2],
        "Milk": [2, 5],
        "Bread": [4, 3]
    }

    cart = ShoppingCart(cart_items)
    cart.display_cart()


if __name__ == "__main__":
    main()
