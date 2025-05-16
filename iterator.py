class LibraryIterator:
    """Available books ke liye custom iterator
    Ye class sirf available books ko iterate karta hai"""
    def __init__(self, books):
        """Constructor jo available books ko filter karta hai"""
        self.books = [book for book in books if book.is_available]  # Sirf available books
        self.index = 0  # Current position

    def __iter__(self):
        """Iterator object return karta hai"""
        return self

    def __next__(self):
        """Agli available book return karta hai
        Agar sab books khatam ho gaye hain to StopIteration raise karta hai"""
        if self.index >= len(self.books):
            raise StopIteration
        book = self.books[self.index]
        self.index += 1
        return book 