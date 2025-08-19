class Calculator:
    def add(self, *args):
        if len(args) == 2:
            print(f"Adding two numbers: {args[0]} + {args[1]} = {args[0] + args[1]}")
        elif len(args) == 3:
            print(f"Adding three numbers: {args[0]} + {args[1]} + {args[2]} = {args[0] + args[1] + args[2]}")
        else:
            print("Unsupported number of arguments.")

# Subclass overriding
class AdvancedCalculator(Calculator):
    def add(self, *args):
        print("Overridden method: Performing a secure addition check...")
        super().add(*args)


def main():
    c = Calculator()
    c.add(5, 10)
    c.add(1, 2, 3)

    ac = AdvancedCalculator()
    ac.add(7, 8)

if __name__ == "__main__":
    main()
