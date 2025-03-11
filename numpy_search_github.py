import numpy as np
import pandas as pd

class InventorySearch:
    def __init__(self, num_items=100):
        
        np.random.seed(100)
        self.num_items = num_items
        
       
        self.product_ids = np.random.randint(1000, 2000, size=num_items)
        self.stock_levels = np.random.randint(0, 101, size=num_items)
        self.prices = np.random.uniform(10, 500, size=num_items).round(2)
        
        self.inventory = np.column_stack((self.product_ids, self.stock_levels, self.prices))

    def search_by_price(self, min_price, max_price):
       
        indexes = np.where(np.logical_and(self.inventory[:, 2] >= min_price, self.inventory[:, 2] <= max_price))
        return self.inventory[indexes]

    def search_low_stock(self, threshold=10):
        
        indexes = np.where(self.inventory[:, 1] < threshold)
        return self.inventory[indexes]

    def search_by_product_id(self, product_id):
        
        index = np.where(self.inventory[:, 0] == product_id)
        return self.inventory[index] if index[0].size > 0 else None

    def display_inventory(self):
        
        df = pd.DataFrame(self.inventory, columns=["Product ID", "Stock", "Price"])
        print(df.head(10))  

def main():
    shop = InventorySearch()
    
    print("\n\n","Full Inventory (First 10 items):".center(100,"-"),"\n")
    shop.display_inventory()

    
    min_price, max_price = 50, 150
    filtered_by_price = shop.search_by_price(min_price, max_price)
    print("\n\n",f"Products between {min_price}-{max_price} TL:".center(100,"-"),"\n\n", pd.DataFrame(filtered_by_price, columns=["Product ID", "Stock", "Price"]).to_string())

    
    low_stock_threshold = 10
    low_stock_items = shop.search_low_stock(low_stock_threshold)
    print("\n\n",f"Products with stock below {low_stock_threshold}:".center(100,"-"),"\n\n", pd.DataFrame(low_stock_items, columns=["Product ID", "Stock", "Price"]).to_string())

  
    product_id_to_search = 1565
    product_info = shop.search_by_product_id(product_id_to_search)
    print(f"\n Searching for Product ID {product_id_to_search}: {product_info if product_info is not None else 'Not Found'}")


if __name__ == "__main__":
    main()
