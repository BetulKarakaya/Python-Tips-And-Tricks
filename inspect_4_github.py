import inspect
import os

class ClassAnalyzer:
    """Analyze a class to extract methods, their parameters, and source info."""

    def __init__(self, cls):
        self.cls = cls

    def analyze(self):
        print(f"Analyzing class: {self.cls.__name__}\n")
        methods = inspect.getmembers(self.cls, predicate=inspect.isfunction)

        if not methods:
            print("❌ No methods found in this class.")
            return

        for name, func in methods:
            sig = inspect.signature(func)
            file = inspect.getsourcefile(func)
            line = inspect.getsourcelines(func)[1]
            print(f"- Method: {name}")
            print(f"   ├─ Signature: {sig}")
            print(f"   ├─ Defined in: {os.path.basename(file)} (line {line})")
            print(f"   └─ Docstring: {inspect.getdoc(func) or 'No documentation.'}\n")


# Example target class
class PaymentProcessor:
    """Handles payment operations for online transactions."""

    def process_payment(self, user_id: int, amount: float, method: str = "CreditCard"):
        """Process a user's payment transaction."""
        pass

    def refund(self, transaction_id: str, reason: str = "User request"):
        """Refund a completed transaction."""
        pass

    def generate_invoice(self, user_id: int):
        """Generate an invoice for the user's last transaction."""
        pass


def main():
    analyzer = ClassAnalyzer(PaymentProcessor)
    analyzer.analyze()


if __name__ == "__main__":
    main()
