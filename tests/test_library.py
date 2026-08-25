import pytest

from library_system.domain.book import Book
from library_system.domain.library import BookNotFoundError, Library


def test_library_starts_empty():
    library = Library()
    assert library.book_count == 0


def test_add_book_increases_count():
    library = Library()
    book = Book(title="1984", author="George Orwell", isbn="1234567890")

    library.add_book(book)

    assert library.book_count == 1

def test_find_by_title_returns_the_matching_book():
    library = Library()
    book = Book(title="1984", author="George Orwell", isbn="1234567890")
    library.add_book(book)

    result = library.find_by_title("1984")

    assert result is book
      

def test_find_by_title_not_matching_book():
    library = Library()
    with pytest.raises(BookNotFoundError):
        library.find_by_title("Nonexistent Book")