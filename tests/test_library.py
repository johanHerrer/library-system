import pytest

from library_system.domain.book import Book
from library_system.domain.library import BookNotFoundError, Library


def test_library_starts_empty():
    # Test that a new library instance starts with zero books
    library = Library()
    assert library.book_count == 0


def test_add_book_increases_count():
    # Test that adding a book to the library increases the book count
    library = Library()
    book = Book(title="1984", author="George Orwell", isbn="1234567890")

    library.add_book(book)

    assert library.book_count == 1

def test_find_by_title_returns_the_matching_book():
    # Test that finding a book by title returns the correct book instance
    library = Library()
    book = Book(title="1984", author="George Orwell", isbn="1234567890")
    library.add_book(book)

    result = library.find_by_title("1984")

    assert result is book
      

def test_find_by_title_not_matching_book():
    # Test that searching for a non-existent book title raises BookNotFoundError
    library = Library()
    with pytest.raises(BookNotFoundError):
        library.find_by_title("Nonexistent Book")

def test_list_available_books_excludes_borrowed_books():
    library = Library()
    book1 = Book(title="1984", author="George Orwell", isbn="1234567890")
    book2 = Book(title="Brave New World", author="Aldous Huxley", isbn="0987654321")
    library.add_book(book1)
    library.add_book(book2)
    book1.borrow()  # Mark book1 as borrowed

    result = library.list_available_books()

    assert book1 not in result 

def test_list_available_books_returns_empty_list_when_empty():
    library = Library()

    result = library.list_available_books()

    assert len(result) == 0