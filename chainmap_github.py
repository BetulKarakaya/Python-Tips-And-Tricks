from collections import ChainMap

class Prices:
    def __init__(self):
        # Default prices (applied if no discounts exist)
        self.default_prices = {
            "laptop": 15000,
            "phone": 8000,
            "tablet": 5000
        }

        # Membership-level prices (members get a discount)
        self.membership_prices = {
            "laptop": 14000,
            "phone": 7500
        }

        # Campaign prices (highest priority discounts)
        self.campaign_prices = {
            "laptop": 13000
        }

        # ChainMap combines the dictionaries in priority order
        self.final_prices = ChainMap(self.campaign_prices, 
                                     self.membership_prices,
                                     self.default_prices)

    def get_price(self, product):
        
        return self.final_prices.get(product, "⚠️ Product Could Not Be Found")

    def display_products(self):
        
       # Define column widths
        col_widths = [12, 15, 18, 18, 15]
        
        # Header row
        header = ["Product", "Normal Price", "Membership Price", "Campaign Price", "Final Price"]
        print("|".join(h.center(w) for h, w in zip(header, col_widths)))
        print("-" * sum(col_widths) + "-" * (len(col_widths) - 1))  # Table border
        
        # Get all unique product names
        all_products = set(self.default_prices.keys()) | set(self.membership_prices.keys()) | set(self.campaign_prices.keys())

        # Print product rows
        for product in all_products:
            row = [
                product.capitalize().center(col_widths[0]),
                str(self.default_prices.get(product, "-")).center(col_widths[1]),
                str(self.membership_prices.get(product, "-")).center(col_widths[2]),
                str(self.campaign_prices.get(product, "-")).center(col_widths[3]),
                str(self.final_prices.get(product, "-")).center(col_widths[4])
            ]
            print("|".join(row))

def main():
    app = Prices()
    app.display_products()  
    print("\n🔹 Price Queries 🔹")
    print(f"Laptop: {app.get_price('laptop')} USD")   # 13000 (Campaign price takes priority)
    print(f"Phone: {app.get_price('phone')} USD")     # 7500 (Membership price applies)
    print(f"Tablet: {app.get_price('tablet')} USD")   # 5000 (Default price applies)
    print(f"Monitor: {app.get_price('monitor')}")     # Product not found

if __name__ == "__main__":
    main()
