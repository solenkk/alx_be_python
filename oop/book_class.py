class Book:
    """
    A class to represent a Book with title, author, and publication year.
    This class implements several magic methods for object lifecycle management.
    """
    
    def __init__(self, title: str, author: str, year: int):
        """
        Constructor method to initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """
        Destructor method that prints a message when the object is deleted.
        """
        print(f"Deleting {self.title}")
    
    def __str__(self) -> str:
        """
        Returns a user-friendly string representation of the Book.
        
        Returns:
            str: String in format "title by author, published in year"
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self) -> str:
        """
        Returns an official string representation that can recreate the Book instance.
        
        Returns:
            str: String in format "Book('title', 'author', year)"
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"