import pytest

from library_system.domain.book import Book
from library_system.domain.library import (
    BookCantNotBeRemovedError,
    BookNotFoundError,
    Library,
)


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
    # Test that listing available books excludes those that are currently borrowed
    library = Library()
    book1 = Book(title="1984", author="George Orwell", isbn="1234567890")
    book2 = Book(title="Brave New World", author="Aldous Huxley", isbn="0987654321")
    library.add_book(book1)
    library.add_book(book2)
    book1.borrow()  # Mark book1 as borrowed

    result = library.list_available_books()

    assert book1 not in result 

def test_list_available_books_returns_empty_list_when_empty():
    # Test that listing available books in an empty library returns an empty list
    library = Library()

    result = library.list_available_books()

    assert len(result) == 0


def test_remove_book_exists_in_library():
    # Test that a book can be removed from the library's collection
    library = Library()
    book = Book(title="1984", author="George Orwell", isbn="1234567890")
    library.add_book(book)
    library.remove_book(book)
    assert book not in library._books 

def test_remove_book_not_exists_in_library():
    # Test that attempting to remove a book not in the library raises BookNotFoundError
    library = Library()
    book = Book(title="1984", author="George Orwell", isbn="1234567890")
    with pytest.raises(BookNotFoundError):
        library.remove_book(book)

def test_remove_book_that_is_borrowed():
    # Test that attempting to remove a borrowed book raises BookCantNotBeRemovedError
    library = Library()
    book = Book(title="1984", author="George Orwell", isbn="1234567890")
    library.add_book(book)
    book.borrow()
    with pytest.raises(BookCantNotBeRemovedError):
        library.remove_book(book) 


def test_get_stats_returns_correct_counts_and_titles():
    library = Library()
    book1 = Book(title="1984", author="George Orwell", isbn="1234567890")
    book2 = Book(title="Brave New World", author="Aldous Huxley", isbn="0987654321")
    library.add_book(book1)
    library.add_book(book2)
    book1.borrow()

    stats = library.get_stats()

    assert stats["borrowed"] == 1
    assert stats["available"] == 1
    assert stats["borrowed_titles"] == ["1984"]