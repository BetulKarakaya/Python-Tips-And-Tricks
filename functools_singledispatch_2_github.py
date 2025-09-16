from functools import singledispatch

@singledispatch
def handle_order(data):
    """Default handler if no type matches."""
    print(f"❌ Unsupported order type: {type(data)}")

@handle_order.register
def _(data: str):
    print(f"Processing single product order: {data}")

@handle_order.register
def _(data: int):
    print(f"Processing bulk order of {data} items")

@handle_order.register
def _(data: list):
    print(f"Multiple products in order: {', '.join(map(str, data))}")

@handle_order.register
def _(data: dict):
    print("Detailed order:")
    for k, v in data.items():
        print(f" - {k}: {v}")

def main():
    handle_order("Laptop")                       # string → single product
    handle_order(10)                             # int → bulk order
    handle_order(["Mouse", "Keyboard", "Monitor"])  # list → multiple items
    handle_order({"id": 123, "product": "Phone", "qty": 2})  # dict → detailed order
    handle_order(3.14)                           # unsupported type

if __name__ == "__main__":
    main()
