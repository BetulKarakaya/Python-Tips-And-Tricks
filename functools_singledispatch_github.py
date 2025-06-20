from functools import singledispatch

@singledispatch
def process(data):
    """Default processor."""
    print(f"- Cannot process type: {type(data)}")

@process.register
def _(data: str):
    print(f"- Processing string: '{data.capitalize()}'")

@process.register
def _(data: int):
    print(f"- Squared number: {data ** 2}")

@process.register
def _(data: list):
    print(f"- List of {len(data)} items: {data}")

@process.register
def _(data: dict):
    print("- Dictionary keys:")
    for k in data:
        print(f" - {k}")

def main():
    process("bEtüL")           #uppercase string
    process(5)                 #square
    process([1, 2, 3])         #list
    process({"a": 1, "b": 2})  #dict
    process(3.14)              #fallback for unsupported types

if __name__ == "__main__":
    main()