from collections import defaultdict, Counter

class InventoryManager:
    def __init__(self):
        
        self.inventory = defaultdict(int)  # Default value for missing items is 0
        self.sales = Counter()  # Track sold items
    
    def add_stock(self, product, quantity):
        
        self.inventory[product] += quantity
        print(f"✅ Added {quantity} units of {product}. Total stock: {self.inventory[product]}")
    
    def sell_item(self, product, quantity):
        
        if self.inventory[product] >= quantity:
            self.inventory[product] -= quantity
            self.sales[product] += quantity
            print(f"🛒  Sold {quantity} units of {product}. Remaining stock: {self.inventory[product]}")
        else:
            print(f"☢️  Not enough stock for {product}. Available: {self.inventory[product]}")
    
    def most_sold_items(self, top_n=3):
        
        top_items = self.sales.most_common(top_n)
        print(f"\n\n🏆  Top {top_n} best-selling items:")
        for i, item in enumerate(top_items):
            print(f"{i+1}. {item[0]} sold {item[1]} units.")
    
    def display_inventory(self):
        
        print("\n\n📦 Inventory Overview:")
        for product, quantity in self.inventory.items():
            print(f"- {product}: {quantity} units")
    
    def run_simulation(self):
       
        self.add_stock("Laptop", 10)
        self.add_stock("Mouse", 50)
        self.add_stock("Keyboard", 30)
        
        self.sell_item("Laptop", 30)
        self.sell_item("Mouse", 25)
        self.sell_item("Keyboard", 10)
        
        self.most_sold_items()
        self.display_inventory()

def main():
    app = InventoryManager()
    app.run_simulation()

if __name__ == "__main__":
    main()
