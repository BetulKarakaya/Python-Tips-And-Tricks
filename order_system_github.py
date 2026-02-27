from itertools import count, product, islice


class OrderSystem:
    def __init__(self, customers, products, prices):
        self.customers = customers
        self.products = products
        self.prices = prices
        self.order_id_generator = count(1000)  # Auto increment order ID

    def generate_orders(self, limit):
        orders = []

        # Pair products with prices
        product_catalog = list(zip(self.products, self.prices))

        # Create all possible customer-product combinations
        all_combinations = product(self.customers, product_catalog)

        # Limit number of generated orders
        for customer, (product_name, price) in islice(all_combinations, limit):
            order = {
                "order_id": next(self.order_id_generator),
                "customer": customer,
                "product": product_name,
                "price": price
            }
            orders.append(order)

        return orders


def main():
    customers = ["Alice", "Bob", "Charlie"]
    products = ["Laptop", "Phone", "Tablet"]
    prices = [1200, 800, 600]

    system = OrderSystem(customers, products, prices)
    orders = system.generate_orders(limit=5)

    print("Generated Orders:\n")
    for order in orders:
        print(order)


if __name__ == "__main__":
    main()