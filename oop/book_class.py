# book_class.py

class Book:
    def __init__(self, title, author, year):
        """Constructor: Initialize the book attributes."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Called when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Informal string representation (user-friendly)."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation (developer-friendly)."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
