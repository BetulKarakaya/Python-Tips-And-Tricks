class RoundingDemo:
    def __init__(self, number: float):
        self.number = number

    def round_default(self):
        """Round to the nearest integer (default)."""
        return round(self.number)

    def round_with_digits(self, digits: int):
        """Round to a specific number of decimal places."""
        return round(self.number, digits)

def main():
    num = 12.34567
    demo = RoundingDemo(num)

    print(f"🔢 Original number: {demo.number}")
    print(f"➡️ Rounded (default): {demo.round_default()}")
    print(f"➡️ Rounded (2 decimal places): {demo.round_with_digits(2)}")
    print(f"➡️ Rounded (3 decimal places): {demo.round_with_digits(3)}")

if __name__ == "__main__":
    main()
