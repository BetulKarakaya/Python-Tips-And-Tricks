class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            value = self.current
            self.current -= 1
            return value

    def __str__(self):
        return f"Countdown starting from {self.current + 1}"

def main():
    counter = Countdown(5)

    for number in counter:
        print(f"{number}")

    print("Countdown finished!")

if __name__ == "__main__":
    main()
