from library_system.domain.book import Book


class BookNotFoundError(Exception):
    """Raised when a book is not found in the library."""

class Library:
    def __init__(self):
        self._books: list[Book] = []

    @property
    def book_count(self) -> int:
        return len(self._books)

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def find_by_title(self, title: str) -> Book:
        for book in self._books:
            if book.title == title:
                return book
        raise BookNotFoundError("No book found")