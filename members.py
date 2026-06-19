"""Member class for the library management system."""


class Member:
    """Represents one library member."""

    def __init__(self, member_id, name, email, borrowed_count=0):
        """Create a new member."""
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_count = borrowed_count

    def display_info(self):
        """Return member details as a string."""
        return (
            f"{self.member_id} | {self.name} | "
            f"{self.email} | Borrowed: {self.borrowed_count}"
        )

    def can_borrow(self):
        """Check if member can borrow more books."""
        return self.borrowed_count < 3

    def borrow_book(self):
        """Increase borrowed count."""
        if self.can_borrow():
            self.borrowed_count += 1
            return True
        return False

    def return_book(self):
        """Decrease borrowed count."""
        if self.borrowed_count > 0:
            self.borrowed_count -= 1

    def to_list(self):
        """Convert member data into a list."""
        return [self.member_id, self.name, self.email, self.borrowed_count]
    
