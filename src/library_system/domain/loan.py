from datetime import UTC, datetime, timedelta

from library_system.domain.book import Book
from library_system.domain.user import User

LOAN_DURATION_DAYS = 14
LATE_FEE_PER_DAY = 0.50

class LoanAlreadyReturnedError(Exception):
    """Raised when trying to create a loan for a book that is already borrowed."""

class Loan:
    def __init__(self, book: Book, user: User):
        self.book = book
        self.user = user
        # Fecha de inicio del préstamo
        self.borrowed_at = datetime.now(UTC)
        # Fecha de vencimiento del préstamo
        self.due_date = self.borrowed_at + timedelta(days=LOAN_DURATION_DAYS)
        self._returned_at = None # None mientras el préstamo está activo

    @property
    def is_active(self) -> bool:
        # Check if the loan is still active (not returned).
        return self._returned_at is None

    @property
    def is_overdue(self) -> bool:
        # Check if the loan is overdue (active and past due date).
        today = datetime.now(UTC)
        # Check if the loan is active and if the current date is past the due date.
        return self.is_active and today > self.due_date

    def mark_returned(self):
        # Mark the loan as returned by setting the returned_at timestamp.
        today = datetime.now(UTC)
        if self._returned_at is not None:
            raise LoanAlreadyReturnedError("This loan has already been returned.")
        self._returned_at = today

    @property
    def late_fee(self) -> float:
        # Calculate the late fee based on the number of overdue days.
        if self.is_overdue:
            today = datetime.now(UTC)
            overdue_days = (today - self.due_date).days
            return overdue_days * LATE_FEE_PER_DAY
        return 0.0

    def __repr__(self) -> str:
        return (
            f"Loan(book={self.book.title!r}, user={self.user.name!r}, "
             f"borrowed_at={self.borrowed_at}, active={self.is_active})")