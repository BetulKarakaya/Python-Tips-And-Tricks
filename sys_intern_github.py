import sys
import time
import random
import string

class StringInterningDemo:
    def __init__(self, size=200000):
        # Random string list
        self.words = [
            "".join(random.choices(string.ascii_letters, k=20)) for _ in range(size)
        ]

    def without_interning(self):
        start = time.time()
        unique = set(self.words)
        print(f"\n- Unique words (no interning): {len(unique)}")
        print(f"- Time: {time.time() - start:.4f}s")

    def with_interning(self):
        start = time.time()
        interned_words = [sys.intern(word) for word in self.words]
        unique = set(interned_words)
        print(f"\n- Unique words (with interning): {len(unique)}")
        print(f"- Time: {time.time() - start:.4f}s")

def main():
    demo = StringInterningDemo()
    demo.without_interning()
    demo.with_interning()

if __name__ == "__main__":
    main()
