from datetime import datetime

class Order:
    """Represents a single customer order."""
    def __init__(self, product, price):
        self.product = product
        self.price = price
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")

    def __str__(self):
        return f"{self.product} - ${self.price} ({self.date})"


class Customer:
    """Customer that stores a list of orders and becomes iterable with __iter__."""
    def __init__(self, name):
        self.name = name
        self._orders = []   # hidden internal order list

    def add_order(self, product, price):
        order = Order(product, price)
        self._orders.append(order)
        print(f"- Order added: {order}")

    def __iter__(self):
        """Allows looping through orders directly from the Customer object."""
        return iter(self._orders)

    def total_spent(self):
        return sum(order.price for order in self._orders)


def main():
    cust = Customer("Betül")

    # add orders like a real app
    cust.add_order("Laptop", 23000)
    cust.add_order("Wireless Mouse", 450)
    cust.add_order("Headphones", 1700)

    print("\n-- Order History (iterating over customer):")
    for order in cust:
        print(" -", order)

    print(f"\n# Total Spent by {cust.name}: ${cust.total_spent()}")


if __name__ == "__main__":
    main()
