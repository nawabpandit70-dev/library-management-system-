"""Main file for running the library management system."""

from book import Book
from members import Member
from library import Library


def show_menu():
    """Display the menu."""
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Show Books")
    print("6. Show Members")
    print("7. Show Loans")
    print("8. Save Data")
    print("9. Exit")


def main():
    """Run the library system."""
    library = Library()

    library.load_books()
    library.load_members()
    library.load_loans()

    while True:
        show_menu()

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 9.")
            continue

        if choice == 1:
            book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter author name: ")

            book = Book(book_id, title, author)
            library.add_book(book)
            print("Book added successfully.")

        elif choice == 2:
            member_id = input("Enter member ID: ")
            name = input("Enter member name: ")
            email = input("Enter member email: ")

            member = Member(member_id, name, email)
            library.add_member(member)
            print("Member added successfully.")

        elif choice == 3:
            loan_id = input("Enter loan ID: ")
            book_id = input("Enter book ID: ")
            member_id = input("Enter member ID: ")

            result = library.borrow_book(loan_id, book_id, member_id)
            print(result)

        elif choice == 4:
            loan_id = input("Enter loan ID: ")
            result = library.return_book(loan_id)
            print(result)

        elif choice == 5:
            print(library.display_books())

        elif choice == 6:
            print(library.display_members())

        elif choice == 7:
            print(library.display_loans())

        elif choice == 8:
            library.save_books()
            library.save_members()
            library.save_loans()
            print("Data saved successfully.")

        elif choice == 9:
            library.save_books()
            library.save_members()
            library.save_loans()
            print("Data saved. Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 9.")


if __name__ == "__main__":
    main()
