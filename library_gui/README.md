# Library Management System GUI

A modern desktop application for managing a library's book collection, built with PyQt6.

## Features

- Add books (both physical and eBooks)
- Remove books
- Lend and return books
- Modern and intuitive user interface
- Book status tracking with color indicators
- Input validation

## Setup

1. Install Python 3.8 or higher
2. Install PyQt6:
```bash
pip install PyQt6
```

3. Run the application:
```bash
python main.py
```

## Usage

1. Adding a Book:
   - Fill in the title, author, and ISBN
   - Select the book type (Physical Book or eBook)
   - Click "Add Book"

2. Managing Books:
   - Select a book from the table by clicking on it
   - Use the action buttons at the bottom to:
     - Lend the selected book (turns red when lent)
     - Return the selected book (turns green when available)
     - Remove the selected book

## Interface

- Clean, modern design with proper spacing and styling
- Input form at the top for adding new books
- Table view in the middle showing all books
- Action buttons at the bottom for managing selected books
- Color-coded status indicators
- Input validation and error messages 