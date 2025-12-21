8class Book:
    """
    A class representing a Book with title, author, and publication year.
    Implements several magic methods for enhanced functionality.
    """
    
    def __init__(self, title: str, author: str, year: int) -> None:
        """
        Constructor for Book class.
        
        Args:
            title: The title of the book (str)
            author: The author of the book (str)
            year: The publication year of the book (int)
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self) -> None:
        """
        Destructor for Book class.
        Prints a message when the object is deleted.
        """
        print(f"Deleting {self.title}")
    
    def __str__(self) -> str:
        """
        String representation of the Book.
        Returns a user-friendly string format.
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self) -> str:
        """
        Official representation of the Book.
        Returns a string that can recreate the Book instance.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
__init__