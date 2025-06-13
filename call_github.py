class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value

    def __str__(self):
        return f"Multiplier with factor {self.factor}"

def main():
    double = Multiplier(2)
    triple = Multiplier(3)
    seven_times = Multiplier(7)

    print(double(5))    # Output: 10 (2 * 5)
    print(triple(5))    # Output: 15 (3 * 5)
    print(seven_times(8))   # Output: 56 (7 * 8)

if __name__ == "__main__":
    main()