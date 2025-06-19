from functools import partial

class DiscountCalculator:
    def __init__(self, tax_rate=0.18):
        self.tax_rate = tax_rate

    def calculate_price(self, price, discount, tax=None):
        """Calculate final price after discount and tax."""
        if tax is None:
            tax = self.tax_rate
        final = (price - (price * discount)) * (1 + tax)
        return round(final, 2)


def main():
    calculator = DiscountCalculator()

    black_friday_price = partial(calculator.calculate_price, discount=0.50)
    student_price = partial(calculator.calculate_price, discount=0.20)
    taxfree_price = partial(calculator.calculate_price, tax=0)

    print("- Black Friday:", black_friday_price(100))
    print("- Student:", student_price(100))
    print("- Tax-Free:", taxfree_price(100, discount=0.10))

if __name__ == "__main__":
    main()
