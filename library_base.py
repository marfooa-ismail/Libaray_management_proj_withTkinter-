from abc import ABC, abstractmethod
from book import Book

print("Starting GUI...")

class LibraryBase(ABC):
    """Library ka base class with abstract methods
    Ye class library ki basic functionality define karta hai"""
    def __init__(self):
        """Constructor jo books ki empty list create karta hai"""
        self.books = []  # Kitabon ki list

    @abstractmethod
    def add_book(self, book):
        """Nayi kitab add karne ka abstract method"""
        pass

    @abstractmethod
    def remove_book(self, isbn):
        """Kitab remove karne ka abstract method"""
        pass

    @abstractmethod
    def lend_book(self, isbn):
        """Kitab lend karne ka abstract method"""
        pass

    @abstractmethod
    def return_book(self, isbn):
        """Kitab wapis karne ka abstract method"""
        pass 