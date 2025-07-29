class Order:
    def __init__(self):
        self._state = "pending"

    def get_status(self):
        return f"Current state: {self._state}"

    def approve(self):
        if self._state != "pending":
            raise ValueError("Only pending orders can be approved.")
        self._state = "approved"

    def ship(self):
        if self._state != "approved":
            raise ValueError("Only approved orders can be shipped.")
        self._state = "shipped"

    def deliver(self):
        if self._state != "shipped":
            raise ValueError("Only shipped orders can be delivered.")
        self._state = "delivered"

def main():
    order = Order()

    print(order.get_status())  # Current state: pending

    order.approve()
    print(order.get_status())  # Current state: approved

    order.ship()
    print(order.get_status())  # Current state: shipped

    order.deliver()
    print(order.get_status())  # Current state: delivered

    #order.ship()
    #print(order.get_status())  # Error

if __name__ == "__main__":
    main()