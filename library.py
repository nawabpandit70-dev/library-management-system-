"""Library class for the library management system."""

import csv
from book import Book
from members import Member
from loan import Loan


class Library:
    """Represents the library system."""

    def __init__(self):
        """Create empty lists."""
        self.books = []
        self.members = []
        self.loans = []

    def add_book(self, book):
        """Add a book."""
        self.books.append(book)

    def add_member(self, member):
        """Add a member."""
        self.members.append(member)

    def find_book(self, book_id):
        """Find a book by ID."""
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_member(self, member_id):
        """Find a member by ID."""
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def find_loan(self, loan_id):
        """Find a loan by ID."""
        for loan in self.loans:
            if loan.loan_id == loan_id:
                return loan
        return None

    def borrow_book(self, loan_id, book_id, member_id):
        """Borrow a book."""
        book = self.find_book(book_id)
        member = self.find_member(member_id)

        if book is None:
            return "Book not found."

        if member is None:
            return "Member not found."

        if not book.available:
            return "Book is already borrowed."

        if not member.can_borrow():
            return "Member cannot borrow more books."

        book.borrow()
        member.borrow_book()

        loan = Loan(loan_id, book_id, member_id)
        self.loans.append(loan)

        return "Book borrowed successfully."

    def return_book(self, loan_id):
        """Return a borrowed book."""
        loan = self.find_loan(loan_id)

        if loan is None:
            return "Loan not found."

        if not loan.is_active():
            return "Book already returned."

        book = self.find_book(loan.book_id)
        member = self.find_member(loan.member_id)

        if book is not None:
            book.return_book()

        if member is not None:
            member.return_book()

        loan.close_loan()
        return "Book returned successfully."

    def display_books(self):
        """Show all books."""
        if not self.books:
            return "No books available."

        result = []
        for book in self.books:
            result.append(book.display_info())
        return "\n".join(result)

    def display_members(self):
        """Show all members."""
        if not self.members:
            return "No members available."

        result = []
        for member in self.members:
            result.append(member.display_info())
        return "\n".join(result)

    def display_loans(self):
        """Show all loans."""
        if not self.loans:
            return "No loans available."

        result = []
        for loan in self.loans:
            result.append(loan.display_info())
        return "\n".join(result)

    def save_books(self):
        """Save books into books.csv."""
        with open("books.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["book_id", "title", "author", "available"])

            for book in self.books:
                writer.writerow(book.to_list())

    def save_members(self):
        """Save members into members.csv."""
        with open("members.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["member_id", "name", "email", "borrowed_count"])

            for member in self.members:
                writer.writerow(member.to_list())

    def save_loans(self):
        """Save loans into loans.csv."""
        with open("loans.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["loan_id", "book_id", "member_id", "status"])

            for loan in self.loans:
                writer.writerow(loan.to_list())

    def load_books(self):
        """Load books from books.csv."""
        try:
            with open("books.csv", "r") as file:
                reader = csv.reader(file)
                next(reader, None)

                for row in reader:
                    if len(row) == 4:
                        book = Book(row[0], row[1], row[2], row[3] == "True")
                        self.books.append(book)
        except FileNotFoundError:
            print("No books file found.")

    def load_members(self):
        """Load members from members.csv."""
        try:
            with open("members.csv", "r") as file:
                reader = csv.reader(file)
                next(reader, None)

                for row in reader:
                    if len(row) == 4:
                        member = Member(row[0], row[1], row[2], int(row[3]))
                        self.members.append(member)
        except FileNotFoundError:
            print("No members file found.")

    def load_loans(self):
        """Load loans from loans.csv."""
        try:
            with open("loans.csv", "r") as file:
                reader = csv.reader(file)
                next(reader, None)

                for row in reader:
                    if len(row) == 4:
                        loan = Loan(row[0], row[1], row[2], row[3])
                        self.loans.append(loan)
        except FileNotFoundError:
            print("No loans file found.")
