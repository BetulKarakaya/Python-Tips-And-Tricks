from datetime import datetime, timedelta

def borrow_book(book_title, borrow_days):
    """
    Simulates borrowing a book from a library.
    Calculates the return date based on the borrowing period.
    """
    try:
        # Ensure the borrow_days is a positive integer
        if borrow_days <= 0:
            raise ValueError("The borrowing period must be at least 1 day.")
        
        # Calculate the return date
        borrow_date = datetime.now()
        ## Adds the specified number of days (borrow_days) to the current date to calculate the return date
        return_date = borrow_date + timedelta(days=borrow_days)

        # Print borrowing details
        print(f"\nYou borrowed: '{book_title}'")
        print(f"Borrow Date: {borrow_date.strftime('%d-%m-%Y %H:%M:%S')}")
        print(f"Return Date: {return_date.strftime('%d-%m-%Y %H:%M:%S')}\n")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")



def main():
    
    #books we have
    books = ["1984", "The Great Gatsby", "To Kill a Mockingbird", "Moby Dick", "The Lord of the Rings"]

    print("Welcome to the Library!")
    print("Available books:")
    for index, book in enumerate(books, start=1):
        print(f"{index}. {book}")

    try:
        # User selects a book
        book_choice = int(input("\nEnter the number of the book you want to borrow: "))
        if book_choice < 1 or book_choice > len(books):
            raise IndexError("Invalid book choice. Please select a valid number.")
        
        # User enters borrowing period
        borrow_days = int(input("How many days do you want to borrow the book for? "))
        borrow_book(books[book_choice - 1], borrow_days)
        
    except ValueError:
        print("Please enter a valid number.")
    except IndexError as ie:
        print(f"Error: {ie}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    main()