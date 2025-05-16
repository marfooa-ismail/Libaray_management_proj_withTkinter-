import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                            QHBoxLayout, QLabel, QLineEdit, QPushButton,
                            QTableWidget, QTableWidgetItem, QMessageBox,
                            QHeaderView, QFrame, QComboBox)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon, QColor

class LibraryGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.books = []
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Library Management System')
        self.setMinimumSize(1000, 700)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QLabel {
                font-size: 14px;
                color: #2c3e50;
                font-weight: bold;
            }
            QLineEdit {
                padding: 8px;
                border: 2px solid #bdc3c7;
                border-radius: 5px;
                font-size: 13px;
                background-color: white;
            }
            QLineEdit:focus {
                border: 2px solid #3498db;
            }
            QPushButton {
                padding: 10px 20px;
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 13px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QTableWidget {
                border: 2px solid #bdc3c7;
                border-radius: 5px;
                background-color: white;
                gridline-color: #ecf0f1;
            }
            QHeaderView::section {
                background-color: #3498db;
                color: white;
                padding: 8px;
                border: none;
                font-weight: bold;
            }
            QComboBox {
                padding: 8px;
                border: 2px solid #bdc3c7;
                border-radius: 5px;
                background-color: white;
                min-width: 150px;
            }
            QComboBox:focus {
                border: 2px solid #3498db;
            }
        """)

        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Create header
        header_label = QLabel('Library Management System')
        header_label.setStyleSheet("""
            font-size: 24px;
            color: #2c3e50;
            font-weight: bold;
            padding: 10px;
        """)
        header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(header_label)

        # Create input form
        form_frame = QFrame()
        form_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                padding: 20px;
            }
        """)
        form_layout = QVBoxLayout(form_frame)

        # Input fields
        input_layout = QHBoxLayout()
        
        # Title input
        title_layout = QVBoxLayout()
        title_label = QLabel('Title:')
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText('Enter book title')
        title_layout.addWidget(title_label)
        title_layout.addWidget(self.title_input)
        input_layout.addLayout(title_layout)

        # Author input
        author_layout = QVBoxLayout()
        author_label = QLabel('Author:')
        self.author_input = QLineEdit()
        self.author_input.setPlaceholderText('Enter author name')
        author_layout.addWidget(author_label)
        author_layout.addWidget(self.author_input)
        input_layout.addLayout(author_layout)

        # ISBN input
        isbn_layout = QVBoxLayout()
        isbn_label = QLabel('ISBN:')
        self.isbn_input = QLineEdit()
        self.isbn_input.setPlaceholderText('Enter ISBN')
        isbn_layout.addWidget(isbn_label)
        isbn_layout.addWidget(self.isbn_input)
        input_layout.addLayout(isbn_layout)

        # Book type selection
        type_layout = QVBoxLayout()
        type_label = QLabel('Type:')
        self.type_combo = QComboBox()
        self.type_combo.addItems(['Physical Book', 'eBook'])
        type_layout.addWidget(type_label)
        type_layout.addWidget(self.type_combo)
        input_layout.addLayout(type_layout)

        form_layout.addLayout(input_layout)

        # Add button
        button_layout = QHBoxLayout()
        self.add_button = QPushButton('Add Book')
        self.add_button.clicked.connect(self.add_book)
        button_layout.addStretch()
        button_layout.addWidget(self.add_button)
        form_layout.addLayout(button_layout)

        main_layout.addWidget(form_frame)

        # Create table
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['Title', 'Author', 'ISBN', 'Type', 'Status'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        main_layout.addWidget(self.table)

        # Create action buttons
        action_layout = QHBoxLayout()
        
        self.lend_button = QPushButton('Lend Selected')
        self.return_button = QPushButton('Return Selected')
        self.remove_button = QPushButton('Remove Selected')
        
        self.lend_button.clicked.connect(self.lend_book)
        self.return_button.clicked.connect(self.return_book)
        self.remove_button.clicked.connect(self.remove_book)
        
        action_layout.addWidget(self.lend_button)
        action_layout.addWidget(self.return_button)
        action_layout.addWidget(self.remove_button)
        
        main_layout.addLayout(action_layout)

    def add_book(self):
        title = self.title_input.text().strip()
        author = self.author_input.text().strip()
        isbn = self.isbn_input.text().strip()
        book_type = self.type_combo.currentText()

        if not all([title, author, isbn]):
            QMessageBox.warning(self, 'Error', 'Please fill in all fields')
            return

        # Check if ISBN already exists
        for row in range(self.table.rowCount()):
            if self.table.item(row, 2).text() == isbn:
                QMessageBox.warning(self, 'Error', 'Book with this ISBN already exists')
                return

        # Add to table
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(title))
        self.table.setItem(row, 1, QTableWidgetItem(author))
        self.table.setItem(row, 2, QTableWidgetItem(isbn))
        self.table.setItem(row, 3, QTableWidgetItem(book_type))
        self.table.setItem(row, 4, QTableWidgetItem('Available'))

        # Clear inputs
        self.title_input.clear()
        self.author_input.clear()
        self.isbn_input.clear()
        self.type_combo.setCurrentIndex(0)

    def lend_book(self):
        selected_rows = self.table.selectedItems()
        if not selected_rows:
            QMessageBox.warning(self, 'Error', 'Please select a book to lend')
            return

        row = selected_rows[0].row()
        status_item = self.table.item(row, 4)
        
        if status_item.text() == 'Available':
            status_item.setText('Lent')
            status_item.setForeground(QColor('#e74c3c'))
        else:
            QMessageBox.warning(self, 'Error', 'This book is already lent')

    def return_book(self):
        selected_rows = self.table.selectedItems()
        if not selected_rows:
            QMessageBox.warning(self, 'Error', 'Please select a book to return')
            return

        row = selected_rows[0].row()
        status_item = self.table.item(row, 4)
        
        if status_item.text() == 'Lent':
            status_item.setText('Available')
            status_item.setForeground(QColor('#27ae60'))
        else:
            QMessageBox.warning(self, 'Error', 'This book is already available')

    def remove_book(self):
        selected_rows = self.table.selectedItems()
        if not selected_rows:
            QMessageBox.warning(self, 'Error', 'Please select a book to remove')
            return

        row = selected_rows[0].row()
        self.table.removeRow(row)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LibraryGUI()
    window.show()
    sys.exit(app.exec()) 