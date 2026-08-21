from library_system.domain.book import Book


class UserNotAlreadyBorrowedBookError(Exception):
    """Raised when trying to return a book that the user has not borrowed."""


class User:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email
        self._list_of_borrowed_books = []

    def __repr__(self) -> str:
        # Return a string representation of the User instance.
        return f"User(id={self.id}, name={self.name!r}, email={self.email!r})"

    @property
    def active_loans_book(self) -> int:
        # Return the number of books currently borrowed by the user.
        return len(self._list_of_borrowed_books)

    @property
    def list_of_borrowed_books(self) -> list:
        # Return a copy of the list of borrowed books to prevent external modification.
        return self._list_of_borrowed_books.copy()

    def borrow_book(self, book: Book) -> None:
        # Delegates borrowing validation to Book.borrow()
        book.borrow()
        self._list_of_borrowed_books.append(book)       

    def return_book(self, book: Book) -> None:
        # Check if the user has borrowed the book before returning it.

        if book not in self._list_of_borrowed_books:
            raise UserNotAlreadyBorrowedBookError(
                f"User {self.name} has not borrowed the book '{book.title}'."
                )
        book.return_book()
        self._list_of_borrowed_books.remove(book)