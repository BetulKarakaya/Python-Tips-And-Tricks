from collections import deque
import time

class FastOrderSystem:
    def __init__(self):
       
        self.orders = deque()  # FIFO order queue

    def add_order(self, order, priority=False):
        
        if priority:
            self.orders.appendleft(order)
            print(f"🔥 PRIORITY ORDER ADDED: {order} (Total Orders: {len(self.orders)})")
        else:
            self.orders.append(order)
            print(f"☑️ Order added: {order} (Total Orders: {len(self.orders)})")

    def process_order(self):
        
        if self.orders:
            completed = self.orders.popleft()
            print(f"✅ Order completed: {completed} (Remaining Orders: {len(self.orders)})")
        else:
            print("⚠️ No orders left to process!")

    def show_orders(self):
        
        if not self.orders:
            print("⚠️ No pending orders!")
        else:
            print("\nPending Orders:")
            for i, order in enumerate(self.orders, 1):
                print(f"🔹 {i}. {order}")

    def run(self):
       
        self.add_order("Burger")
        self.add_order("Pizza")
        self.add_order("Pasta", priority=True)  # Priority order
        
        self.show_orders()

        time.sleep(1)
        self.process_order()

        time.sleep(1)
        self.process_order()

        self.show_orders()

def main():
    app = FastOrderSystem()
    app.run()

if __name__ == "__main__":
    main()
