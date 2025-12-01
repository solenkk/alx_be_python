class Book:
    """Represents a book in the library with title, author, and availability status."""
    
    def __init__(self, title, author):
        """
        Initialize a new book.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability
    
    def check_out(self):
        """Mark the book as checked out (unavailable)."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True  # Successfully checked out
        return False  # Already checked out
    
    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True  # Successfully returned
        return False  # Wasn't checked out
    
    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out
    
    def __str__(self):
        """Return string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """Manages a collection of books."""
    
    def __init__(self):
        """Initialize an empty library."""
        self._books = []  # Private list to store book instances
    
    def add_book(self, book):
        """
        Add a book to the library.
        
        Args:
            book (Book): A Book instance to add to the library
        """
        self._books.append(book)
    
    def check_out_book(self, title):
        """
        Check out a book by its title.
        
        Args:
            title (str): The title of the book to check out
            
        Returns:
            bool: True if book was successfully checked out, False otherwise
        """
        for book in self._books:
            if book.title.lower() == title.lower():
                return book.check_out()
        return False  # Book not found
    
    def return_book(self, title):
        """
        Return a book by its title.
        
        Args:
            title (str): The title of the book to return
            
        Returns:
            bool: True if book was successfully returned, False otherwise
        """
        for book in self._books:
            if book.title.lower() == title.lower():
                return book.return_book()
        return False  # Book not found
    
    def list_available_books(self):
        """Print all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        
        if not available_books:
            print("No books available in the library.")
        else:
            for book in available_books:
                print(book)
