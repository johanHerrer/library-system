class BookAlreadyBorrowedError(Exception):
    """Raised when trying to borrow a book that is already borrowed."""

class BookNotBorrowedError(Exception):
    """Raised when trying to return a book that is not borrowed."""

class Book:
    def __init__(self, title, author, isbn):
        # Initialize a Book instance with title, author, and ISBN.
        self.title = title
        self.author = author
        self.isbn = isbn
        self._is_borrowed = False


    @property
    def is_borrowed(self) -> bool:
        # Return the borrowing status of the book.
        return self._is_borrowed

    def __repr__(self) -> str:
        # Return a string representation of the Book instance.
        status = "borrowed" if self.is_borrowed else "available"
        return f"Book(title={self.title!r}, author={self.author!r}, status={status})"

    def borrow(self):
        # Mark the book as borrowed if it is not already borrowed.
        if self.is_borrowed:
            raise BookAlreadyBorrowedError(
                f"The book '{self.title}' is already borrowed"
                )
        self._is_borrowed = True

    def return_book(self):
        # Mark the book as returned if it is currently borrowed.
        if not self.is_borrowed:
            raise BookNotBorrowedError(
                f"The book '{self.title}' is not borrowed."
                )
        self._is_borrowed = False
        