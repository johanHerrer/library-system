import pytest
from freezegun import freeze_time

from library_system.domain.book import Book
from library_system.domain.loan import Loan, LoanAlreadyReturnedError
from library_system.domain.user import User


def test_loan_is_not_overdue_when_created():
    book = Book(title="1984", author="George Orwell", isbn="1234567890")
    user = User(id="1", name="Ana", email="ana@email.com")

    with freeze_time("2024-01-01"):
        loan = Loan(book, user)
        assert loan.is_active
        assert not loan.is_overdue
        assert loan.late_fee == 0.0

def test_loan_is_overdue_after_due_date():
    book = Book(title="1984", author="George Orwell", isbn="1234567890")
    user = User(id="1", name="Ana", email="ana@email.com")

    with freeze_time("2024-01-01"):
        loan = Loan(book, user)

    with freeze_time("2024-01-21"):
        assert loan.is_active
        assert loan.is_overdue
        assert loan.late_fee == 3.0

def test_loan_cannot_be_returned_twice():
    book = Book(title="1984", author="George Orwell", isbn="1234567890")
    user = User(id="1", name="Ana", email="ana@email.com")

    with freeze_time("2024-01-01"):
        loan = Loan(book, user)
        loan.mark_returned()

        with pytest.raises(LoanAlreadyReturnedError, match="already been returned"):
            loan.mark_returned()