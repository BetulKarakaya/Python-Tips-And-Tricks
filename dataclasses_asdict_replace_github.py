from dataclasses import dataclass, asdict, replace

@dataclass
class Customer:
    id: int
    name: str
    balance: float
    city: str

class CustomerManager:
    def __init__(self, customer: Customer):
        self.customer = customer

    def to_dict(self):
        """Convert dataclass to dictionary easily."""
        data = asdict(self.customer)
        print("Customer data as dictionary:", data)
        return data

    def update_info(self, **kwargs):
        """Create a new updated copy using replace()."""
        updated_customer = replace(self.customer, **kwargs)
        print("Updated customer:", updated_customer)
        return updated_customer

def main():
    customer = Customer(1, "Jane", 1500.0, "London")
    manager = CustomerManager(customer)

    manager.to_dict()  # Convert to dict
    manager.update_info(balance=2000.0, city="NY")  # Create updated copy

if __name__ == "__main__":
    main()
