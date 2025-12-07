from dataclasses import dataclass

@dataclass(frozen=True)
class BookKey:
    """Immutable key: safe for hashing & dictionary usage."""
    isbn: str

class Book:
    """Mutable book object (title, author can be changed)."""
    def __init__(self, isbn: str, title: str, author: str):
        self.key = BookKey(isbn)   # immutable identifier
        self.title = title
        self.author = author

    def update_title(self, new_title: str):
        self.title = new_title

    def __repr__(self):
        return f"{self.title} — {self.author} (ISBN: {self.key.isbn})"


class Library:
    def __init__(self):
        # Dictionary keyed *safely* by BookKey
        self.catalog = {}

    def add_book(self, book: Book):
        print(f"- Adding book: {book}")
        self.catalog[book.key] = book

    def get_book(self, isbn: str):
        return self.catalog.get(BookKey(isbn), None)

    def show_all(self):
        print("\n--- Library Catalog:")
        for book in self.catalog.values():
            print(" -", book)


def main():
    b1 = Book("978-0132350884", "Clean Code", "Robert C. Martin")
    b2 = Book("978-0596009205", "Head First Python", "Paul Barry")

    library = Library()
    library.add_book(b1)
    library.add_book(b2)

    # update book title (mutable!)
    b1.update_title("Clean Code (Updated Edition)")

    library.show_all()

    print("\n--- Searching by ISBN:")
    result = library.get_book("978-0132350884")
    print("Found:", result)


if __name__ == "__main__":
    main()
