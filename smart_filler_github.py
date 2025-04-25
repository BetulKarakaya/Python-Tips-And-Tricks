class SmartFiller:
    def __init__(self, sequence, fill_value="🔍 Guessing..."):
        self.sequence = sequence
        self.fill_value = fill_value

    def fill_missing(self):
        filled = []
        last_seen = self.fill_value
        for item in self.sequence:
            if item is None:
                filled.append(last_seen)
            else:
                last_seen = item
                filled.append(item)
        return filled

    def display(self):
        original = [str(item) if item else "None" for item in self.sequence]
        filled = self.fill_missing()
        print("🧩 Original: ", " | ".join(original))
        print("✨ Filled:   ", " | ".join(str(x) for x in filled))

def main():
    data = ["A", None, None, "B", None, "C", None, None, None]
    app = SmartFiller(data)
    app.display()

if __name__ == "__main__":
    main()
