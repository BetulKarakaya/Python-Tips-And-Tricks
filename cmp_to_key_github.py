from functools import cmp_to_key


class ProductSorter:
    def __init__(self, products):
        self.products = products

    def compare_products(self, a, b):
        """
        Custom comparison rule:
        1. Higher rating comes first
        2. If ratings are equal, lower price comes first
        """

        # Compare rating (descending)
        if a["rating"] > b["rating"]:
            return -1
        if a["rating"] < b["rating"]:
            return 1

        # If ratings equal → compare price (ascending)
        if a["price"] < b["price"]:
            return -1
        if a["price"] > b["price"]:
            return 1

        return 0

    def sort_products(self):
        return sorted(self.products, key=cmp_to_key(self.compare_products))


def main():

    products = [
        {"name": "Keyboard", "price": 50, "rating": 4.5},
        {"name": "Mouse", "price": 25, "rating": 4.5},
        {"name": "Monitor", "price": 300, "rating": 4.8},
        {"name": "USB Cable", "price": 10, "rating": 4.2},
    ]

    sorter = ProductSorter(products)
    sorted_products = sorter.sort_products()

    for product in sorted_products:
        print(product)


if __name__ == "__main__":
    main()