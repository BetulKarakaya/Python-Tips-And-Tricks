class Product:
    def __init__(self, code: str, name: str):
        self.code = code      # unique product ID
        self.name = name

    def __eq__(self, other):
        """
        Two products are considered equal if their unique product code matches.
        """
        return isinstance(other, Product) and self.code == other.code

    def __hash__(self):
        """
        Ensures that sets/dicts treat equal Product objects as identical.
        """
        return hash(self.code)

    def __repr__(self):
        return f"{self.name} (Code: {self.code})"


class Inventory:
    def __init__(self):
        self.products = set()

    def add_product(self, product: Product):
        print(f"- Adding: {product}")
        self.products.add(product)

    def show_inventory(self):
        print("\n--- Final Inventory (duplicates removed):")
        for p in self.products:
            print(" ", p)


def main():
    inv = Inventory()

    # Duplicate products by CODE (ID)
    inv.add_product(Product("AA101", "Laptop"))
    inv.add_product(Product("AA101", "Laptop - Warehouse B"))  # same code → duplicate
    inv.add_product(Product("BB202", "Mouse"))
    inv.add_product(Product("CC303", "Keyboard"))

    inv.show_inventory()


if __name__ == "__main__":
    main()
