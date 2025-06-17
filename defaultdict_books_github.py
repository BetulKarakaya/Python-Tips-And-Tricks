from collections import defaultdict

class BookCategorizer:
    def __init__(self, books_data, group_by):
        self.books_data = books_data
        self.group_by = group_by
        self.grouped = {}

    def group_books(self):
        """Group books by a given key ('author' or 'genre')."""
        grouped = defaultdict(list)
        for book in self.books_data:
            grouped[book[self.group_by]].append(book["title"])
        self.grouped = dict(grouped)

    def display_grouped_books(self):
        """Display grouped book titles under their respective categories."""
        print(f"\nBooks grouped by {self.group_by.capitalize()}:\n")
        for group, titles in self.grouped.items():
            print(f"{group}:")
            for title in titles:
                print(f"  - {title}")

def main():
    books = [
        {"title": "1984", "author": "George Orwell", "genre": "Dystopia"},
        {"title": "Animal Farm", "author": "George Orwell", "genre": "Political Satire"},
        {"title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Romance"},
        {"title": "Emma", "author": "Jane Austen", "genre": "Romance"},
        {"title": "Brave New World", "author": "Aldous Huxley", "genre": "Dystopia"},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Classic"},
    ]

    group_by = input("How would you like to group the books? (author/genre): ").strip().lower()

    if group_by in ("author", "genre"):
        categorizer = BookCategorizer(books, group_by)
        categorizer.group_books()
        categorizer.display_grouped_books()
    else:
        print("Invalid option. Please choose 'author' or 'genre'.")

if __name__ == "__main__":
    main()
