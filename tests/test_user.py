import pytest

from library_system.domain.book import Book, BookAlreadyBorrowedError
from library_system.domain.user import User, UserNotAlreadyBorrowedBookError


def test_validate_user_initialization():
    user = User(id="12345", name="John Doe", email="john.doe@example.com")
    assert user.id == "12345"
    assert user.name == "John Doe"
    assert user.email == "john.doe@example.com"

def test_validate_list_of_borrowed_books_initialization():
    user = User(id="12345", name="John Doe", email="john.doe@example.com")
    assert user.active_loans_book == 0

def test_validate_borrow_book():
    book = Book(title="1984", author="George Orwell", isbn="1234567890")
    user = User(id="12345", name="John Doe", email="john.doe@example.com")
    user.borrow_book(book)
    assert user.active_loans_book == 1

def test_validate_book_already_borrowed_error():
    book = Book(title="1984", author="George Orwell", isbn="1234567890")
    user = User(id="12345", name="John Doe", email="john.doe@example.com")
    user.borrow_book(book)
    with pytest.raises(BookAlreadyBorrowedError,
                       match="is already borrowed"):
        user.borrow_book(book)


def test_validate_return_book_not_borrowed_error():
    book = Book(title="Brave New World", author="Aldous Huxley", isbn="0987654321")
    user = User(id="12345", name="John Doe", email="john.doe@example.com")
    with pytest.raises(
        UserNotAlreadyBorrowedBookError, match="has not borrowed the book"):
        user.return_book(book)


def test_list_of_borrowed_books_returns_a_copy():
    book = Book(title="1984", author="George Orwell", isbn="1234567890")
    user = User(id="12345", name="John Doe", email="john.doe@example.com")
    user.borrow_book(book)

    borrowed_books = user.list_of_borrowed_books
    borrowed_books.append("fake book")  # modificar la copia

    assert "fake book" not in user.list_of_borrowed_books