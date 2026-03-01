from functools import reduce, lru_cache, partial


class EcommerceAnalytics:
    def __init__(self, prices):
        self.prices = prices

    # Total revenue using reduce
    def calculate_total_revenue(self):
        return reduce(lambda x, y: x + y, self.prices, 0)

    # Expensive computation with caching
    @lru_cache(maxsize=None)
    def discounted_price(self, price, discount_rate):
        print("Calculating discount...")  # To show caching effect
        return price - (price * discount_rate)

    # Using partial to create fixed discount function
    def create_discount_function(self, discount_rate):
        return partial(self.discounted_price, discount_rate=discount_rate)


def main():
    prices = [1200, 800, 600, 400]

    analytics = EcommerceAnalytics(prices)

    # Total revenue
    total = analytics.calculate_total_revenue()
    print("Total Revenue:", total)

    # Create fixed 10% discount function
    discount_10 = analytics.create_discount_function(0.10)

    print("\nDiscounted Prices:")
    for price in prices:
        print(discount_10(price))

    # Call again to demonstrate caching
    print("\nCalling again to test caching:")
    print(discount_10(1200))  # This will not recalculate


if __name__ == "__main__":
    main()