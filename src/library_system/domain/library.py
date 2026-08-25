from library_system.domain.book import Book


class BookNotFoundError(Exception):
    """Raised when a book is not found in the library."""

class BookCantNotBeRemovedError(Exception):
    """Raised when trying to remove a book that is currently borrowed."""

class Library:
    def __init__(self):
        self._books: list[Book] = []

    @property
    def book_count(self) -> int:
        # Return the number of books in the library's collection
        return len(self._books)

    def add_book(self, book: Book) -> None:
        # Add a book to the library's collection
        self._books.append(book)

    def find_by_title(self, title: str) -> Book:
        # Search for a book by its title in the library's collection
        for book in self._books:
            if book.title == title:
                return book
        raise BookNotFoundError("No book found")

    def list_available_books(self) -> list[Book]:
        # Return a list of books that are currently available (not borrowed)
        return [book for book in self._books if not book.is_borrowed] 

    def remove_book(self, book: Book) -> None:
        # Remove a book from the library's collection if it is not borrowed
    
        if book not in self._books:
            raise BookNotFoundError("Book not found in the library")
        if book.is_borrowed:
                    raise BookCantNotBeRemovedError("Cannot remove a borrowed book")
        self._books.remove(book)