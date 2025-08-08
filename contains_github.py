class MyList:
    def __init__(self, items):
        self.items = items

    def __contains__(self, item):
        # Case-insensitive membership check
        return item.lower() in (x.lower() for x in self.items)


def main():
    fruits = MyList(["Apple", "Banana", "Cherry"])

    print("apple" in fruits)   # True
    print("BANANA" in fruits)  # True
    print("Mango" in fruits)   # False

if __name__ == "__main__":
    main()