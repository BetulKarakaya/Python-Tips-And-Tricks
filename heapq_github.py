import heapq

class Order:
    def __init__(self, order_id, price, priority, timestamp):
        self.order_id = order_id
        self.price = price
        self.priority = priority
        self.timestamp = timestamp

    def __repr__(self):
        return f"Order(id={self.order_id}, price={self.price}, priority={self.priority})"


def main():
    orders = [
        Order(1, 250, 2, 10),
        Order(2, 100, 1, 20),
        Order(3, 400, 3, 5),
        Order(4, 150, 1, 15),
    ]

    priority_queue = []

    print("\nAdding orders to priority queue...")
    for order in orders:
        # (-priority) → highest priority comes first
        # timestamp → tie-breaker (earlier order first)
        heapq.heappush(priority_queue, (-order.priority, order.timestamp, order))
        print(f"  added → {order}")

    print("\nProcessing orders by priority:")
    while priority_queue:
        _, _, current_order = heapq.heappop(priority_queue)
        print(f"  processing → {current_order}")


if __name__ == "__main__":
    main()
