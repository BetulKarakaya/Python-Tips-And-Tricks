from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    year: int
    available: bool = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"You have borrowed '{self.title}' by {self.author}.")
        else:
            print(f"'{self.title}' is currently unavailable.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"You have returned '{self.title}'.")
        else:
            print(f"'{self.title}' was not borrowed.")

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"'{self.title}' by {self.author} ({self.year}) - {status}"


def main():
    book1 = Book("1984", "George Orwell", 1949)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

    print(book1)
    book1.borrow()
    print(book1)

    book1.borrow()  # trying to borrow again
    book1.return_book()
    print(book1)

if __name__ == "__main__":
    main()