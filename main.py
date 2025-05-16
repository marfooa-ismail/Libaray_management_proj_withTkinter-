from book import Book, EBook
from library import Library, DigitalLibrary

def print_menu():
    """Menu display karta hai"""
    print("\n=== Library Management System ===")
    print("1. Add a Book")           # Kitab add karna
    print("2. Remove a Book")        # Kitab remove karna
    print("3. Lend a Book")          # Kitab lend karna
    print("4. Return a Book")        # Kitab wapis karna
    print("5. List Available Books") # Available kitaben dekhna
    print("6. Search Books by Author") # Musannif ke naam se kitaben dhundna
    print("7. Add an EBook")         # Digital kitab add karna
    print("8. Exit")                 # Program se bahir jana
    print("===============================")

def get_book_info():
    """User se kitab ki information input leta hai"""
    title = input("Enter book title: ")      # Kitab ka naam
    author = input("Enter book author: ")    # Musannif ka naam
    isbn = input("Enter book ISBN: ")        # Kitab ka unique number
    return title, author, isbn

def get_ebook_info():
    """User se eBook ki information input leta hai"""
    title, author, isbn = get_book_info()
    size = float(input("Enter download size (MB): "))  # Kitab ka size
    return title, author, isbn, size

def main():
    """Main program jo library system ko run karta hai"""
    library = Library()              # Physical library
    digital_library = DigitalLibrary()  # Digital library
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-8): ")  # User ka choice
        
        if choice == '1':  # Kitab add karna
            title, author, isbn = get_book_info()
            book = Book(title, author, isbn)
            library.add_book(book)
            print(f"Book '{title}' added successfully!")
            
        elif choice == '2':  # Kitab remove karna
            isbn = input("Enter ISBN of book to remove: ")
            library.remove_book(isbn)
            print(f"Book with ISBN {isbn} removed successfully!")
            
        elif choice == '3':  # Kitab lend karna
            isbn = input("Enter ISBN of book to lend: ")
            library.lend_book(isbn)
            print(f"Book with ISBN {isbn} lent successfully!")
            
        elif choice == '4':  # Kitab wapis karna
            isbn = input("Enter ISBN of book to return: ")
            library.return_book(isbn)
            print(f"Book with ISBN {isbn} returned successfully!")
            
        elif choice == '5':  # Available kitaben dekhna
            print("\nAvailable Books in Physical Library:")
            for book in library:
                print(book)
                
            print("\nAvailable Books in Digital Library:")
            for book in digital_library:
                print(book)
                
        elif choice == '6':  # Musannif ke naam se kitaben dhundna
            author = input("Enter author name to search: ")
            print(f"\nBooks by {author} in Physical Library:")
            books = library.get_books_by_author(author)
            for book in books:
                print(book)
                
            print(f"\nBooks by {author} in Digital Library:")
            books = digital_library.get_books_by_author(author)
            for book in books:
                print(book)
                
        elif choice == '7':  # Digital kitab add karna
            title, author, isbn, size = get_ebook_info()
            ebook = EBook(title, author, isbn, size)
            digital_library.add_book(ebook)
            print(f"EBook '{title}' added successfully!")
            
        elif choice == '8':  # Program se bahir jana
            print("Thank you for using the Library Management System!")
            break
            
        else:  # Ghalat choice ka error
            print("Invalid choice! Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main() 