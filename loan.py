"""Loan class for the library management system."""


class Loan:
    """Represents one book loan."""

    def __init__(self, loan_id, book_id, member_id, status="Active"):
        """Create a new loan."""
        self.loan_id = loan_id
        self.book_id = book_id
        self.member_id = member_id
        self.status = status

    def display_info(self):
        """Return loan details as a string."""
        return (
            f"{self.loan_id} | Book: {self.book_id} | "
            f"Member: {self.member_id} | {self.status}"
        )

    def close_loan(self):
        """Mark loan as returned."""
        self.status = "Returned"

    def is_active(self):
        """Check if loan is active."""
        return self.status == "Active"

    def to_list(self):
        """Convert loan data into a list."""
        return [self.loan_id, self.book_id, self.member_id, self.status]
