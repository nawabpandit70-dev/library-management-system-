"""Book class for the library management system."""


class Book:
    """Represents one book in the library."""

    def __init__(self, book_id, title, author, available=True):
        """Create a new book."""
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def display_info(self):
        """Return book details as a string."""
        if self.available:
            status = "Available"
        else:
            status = "Borrowed"

        return f"{self.book_id} | {self.title} | {self.author} | {status}"

    def borrow(self):
        """Borrow the book if available."""
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        """Return the book."""
        self.available = True

    def to_list(self):
        """Convert book data into a list."""
        return [self.book_id, self.title, self.author, self.available]
