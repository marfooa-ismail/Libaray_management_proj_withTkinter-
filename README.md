# Library Management System (PyQt6 Version)

A modern desktop application for managing a library's book collection, built with PyQt6.

## Features

- Add books (physical and eBooks)
- Remove, lend, and return books
- eBook URL field is only enabled when the eBook checkbox is checked
- Input validation for eBook URLs
- Modern, user-friendly interface

## Setup

1. **Create and activate a virtual environment** (recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python main.py
   ```

## Usage

- Fill in the book details and click **Add Book**
- Use the buttons to **lend**, **return**, or **remove** books
- The **eBook** checkbox enables the URL field for eBooks only

## Project Structure

- `main.py`: Main PyQt6 GUI
- `book.py`, `library.py`, `library_base.py`, `iterator.py`: Backend logic
- `requirements.txt`: Dependencies

## Screenshots

