# book_class.py

class Book:
    def init(self, title: str, author: str, year: int):
        """Constructor to initialize a Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def del(self):
        """Destructor to indicate when a Book instance is deleted."""
        print(f"Deleting {self.title}")

    def str(self):
        """String representation for user-friendly display."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def repr(self):
        """Official representation for recreating the Book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"