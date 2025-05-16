from book import Book, EBook
from library_base import LibraryBase
from iterator import LibraryIterator

class Library(LibraryBase):
    """Main Library class jo sari functionality implement karti hai
    Ye class physical books ko manage karta hai"""
    
    def add_book(self, book):
        """Nayi kitab add karne ka function"""
        self.books.append(book)

    def remove_book(self, isbn):
        """Kitab remove karne ka function"""
        self.books = [book for book in self.books if book.isbn != isbn]

    def lend_book(self, isbn):
        """Kitab lend karne ka function"""
        book = self._find_book(isbn)
        if book:
            book.is_available = False

    def return_book(self, isbn):
        """Kitab wapis karne ka function"""
        book = self._find_book(isbn)
        if book:
            book.is_available = True

    def _find_book(self, isbn):
        """ISBN se kitab dhundne ka function"""
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def __iter__(self):
        """Available books ke liye iterator return karta hai"""
        return LibraryIterator(self.books)

    def get_books_by_author(self, author):
        """Specific musannif ki kitaben dhundne ka function"""
        return [book for book in self.books if book.author.lower() == author.lower()]

class DigitalLibrary(Library):
    """Digital Library class jo Library se inherit karti hai
    Ye class sirf eBooks ko manage karta hai"""
    
    def add_book(self, book):
        """Digital kitab add karne ka function"""
        super().add_book(book) 