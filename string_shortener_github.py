class StringShortener:
    def __init__(self, max_length=20):
        self.max_length = max_length

    def shorten(self, text):
        if len(text) <= self.max_length:
            return text
        else:
            return text[:self.max_length - 3] + "..."

    def display(self, text):
        print("📝 Original:", text)
        print("✂️ Shortened:", self.shorten(text))

def main():
    app = StringShortener(max_length=15)
    sentence = "Python makes coding fun and creative!"
    app.display(sentence)

if __name__ == "__main__":
    main()
