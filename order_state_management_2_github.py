class Order:
    allowed_transitions = {
        "created": ["paid"],
        "paid": ["shipped"],
        "shipped": ["delivered"],
        "delivered": []
    }

    def __init__(self, order_id, status="created"):
        self.order_id = order_id
        self.status = status

    def update_status(self, new_status):
        if new_status in self.allowed_transitions[self.status]:
            print(f"Order {self.order_id}: status changed from {self.status} to {new_status}")
            self.status = new_status
        else:
            raise ValueError(f"Invalid transition from {self.status} to {new_status}")

    def __str__(self):
        return f"[Order #{self.order_id}] - Status: {self.status}"


def main():

    order = Order(order_id=1001)
    print(order)

    order.update_status("paid")
    print(order)

    order.update_status("shipped")
    print(order)

    order.update_status("delivered")
    print(order)

    # Error
    try:
        order.update_status("paid")
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
   main() 