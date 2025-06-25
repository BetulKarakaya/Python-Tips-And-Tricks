from itertools import groupby
from operator import itemgetter

class OrderTracker:
    def __init__(self, orders):
        self.orders = sorted(orders, key=itemgetter("category"))

    def group_by_category(self):
        grouped = groupby(self.orders, key=itemgetter("category"))
        for category, items in grouped:
            print(f"\n- Category: {category}")
            for item in items:
                print(f" * {item['product']} — {item['quantity']} pcs")
def main():
    orders = [
        {"product": "Milk", "category": "Dairy", "quantity": 2},
        {"product": "Bread", "category": "Bakery", "quantity": 1},
        {"product": "Yogurt", "category": "Dairy", "quantity": 3},
        {"product": "Apple", "category": "Fruit", "quantity": 4},
        {"product": "Croissant", "category": "Bakery", "quantity": 2},
        {"product": "Cheese", "category": "Dairy", "quantity": 1},
    ]

    tracker = OrderTracker(orders)
    tracker.group_by_category()

if __name__ == "__main__":
    main()