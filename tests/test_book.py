import pytest

from library_system.domain.book import (
    Book,
    BookAlreadyBorrowedError,
    BookNotBorrowedError,
)


def test_validate_book_initialization():
    # Create a Book instance and validate its attributes and initial state.
    book = Book(title="1984", author="George Orwell", isbn="1234567890")
    assert book.title == "1984"
    assert book.author == "George Orwell"
    assert book.isbn == "1234567890"
    assert not book.is_borrowed

def test_validate_book_borrow():
    # Create a Book instance, borrow it, and validate its borrowed state.
    book = Book(title="1984", author="George Orwell", isbn="1234567890")
    book.borrow()
    assert book.is_borrowed

def test_validate_book_borrow_already_borrowed():
    # Create a Book instance, borrow it, and attempt 
    # to borrow it again to validate error handling.
    book = Book(title="1984", author="George Orwell", isbn="1234567890")
    book.borrow()
    with pytest.raises(BookAlreadyBorrowedError, 
                       match="is already borrowed"):
        book.borrow()

def test_validate_book_not_borrowed_return():
    # Create a Book instance and attempt to return it without 
    # borrowing to validate error handling.
    book = Book(title="1984", author="George Orwell", isbn="1234567890")
    with pytest.raises(BookNotBorrowedError, 
                       match="is not borrowed"):
        book.return_book()

def test_validate_book_return():
    # Create a Book instance, borrow it, return it, and validate its returned state.
    book = Book(title="1984", author="George Orwell", isbn="1234567890")
    book.borrow()
    book.return_book()
    assert not book.is_borrowed