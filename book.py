class Book:
    """Book class jo har book ki information store karti hai"""
    def __init__(self, title, author, isbn, is_available=True):
        self.title = title      # Kitab ka naam
        self.author = author    # Musannif ka naam
        self.isbn = isbn        # Kitab ka unique number
        self.is_available = is_available  # Kitab available hai ya nahi

    def __str__(self):
        """Kitab ki information ko string format main convert karta hai"""
        status = "Available" if self.is_available else "Not Available"
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {status}"

class EBook(Book):
    """Digital books ke liye extended Book class"""
    def __init__(self, title, author, isbn, ebook_url, is_available=True):
        """EBook ka constructor"""
        super().__init__(title, author, isbn, is_available)
        self.ebook_url = ebook_url  # Kitab ka URL
    
    def __str__(self):
        """EBook ki information ko string format main convert karta hai"""
        return f"{super().__str__()}, URL: {self.ebook_url}" 