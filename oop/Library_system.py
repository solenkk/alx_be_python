#!/usr/bin/env python3

class Book:
    """Base class representing a general book."""
    
    def __init__(self, title: str, author: str):
        """
        Initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
    
    def get_info(self) -> str:
        """Return formatted information about the book."""
        return f"{self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""
    
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initialize an EBook instance.
        
        Args:
            title (str): The title of the ebook
            author (str): The author of the ebook
            file_size (int): The file size in kilobytes
        """
        # Call the parent class constructor
        super().__init__(title, author)
        self.file_size = file_size
    
    def get_info(self) -> str:
        """Return formatted information about the ebook."""
        return f"{self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a physical printed book."""
    
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initialize a PrintBook instance.
        
        Args:
            title (str): The title of the print book
            author (str): The author of the print book
            page_count (int): The number of pages
        """
        # Call the parent class constructor
        super().__init__(title, author)
        self.page_count = page_count
    
    def get_info(self) -> str:
        """Return formatted information about the print book."""
        return f"{self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Library class demonstrating composition by managing a collection of books."""
    
    def __init__(self):
        """Initialize a Library instance with an empty book list."""
        self.books = []
    
    def add_book(self, book):
        """
        Add a book to the library.
        
        Args:
            book (Book, EBook, or PrintBook): Book instance to add
        """
        self.books.append(book)
        print(f"Added book: {book.title}")
    
    def list_books(self):
        """List all books in the library with their details."""
        if not self.books:
            print("The library is empty.")
            return
        
        print("\nLibrary Catalog:")
        print("-" * 40)
        
        for book in self.books:
            # Determine book type and format output accordingly
            if isinstance(book, EBook):
                print(f"EBook: {book.get_info()}")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.get_info()}")
            elif isinstance(book, Book):
                print(f"Book: {book.get_info()}") 
        print("-" * 40)