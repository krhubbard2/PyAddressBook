# Kelby Hubbard
# Started: 2021-11-05
# Updated: 
# visual.py

# GUI for PyAddressBook
# This application uses and requires PyQt (PyQt5)

from PyQt5.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QWidget,    
    QAbstractItemView,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QLineEdit,
)

# Main Window
class Window(QMainWindow):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("PyAddressBook")
        self.resize(800, 450)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.initUI()

    # Initialize main window UI
    def initUI(self):
        # Create Search Bar Widget
        self.searchBar = QLineEdit("Search")
        # Create Table View Widget
        self.table = QTableView()
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()
        # Create Buttons
        self.addButton = QPushButton("Add Contact")
        self.deleteButton = QPushButton("Delete")
        # GUI Layout
        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(self.addButton)
        buttonLayout.addWidget(self.deleteButton)
        layout = QVBoxLayout()
        layout.addWidget(self.searchBar)
        layout.addWidget(self.table)
        self.layout.addLayout(layout)
        self.layout.addLayout(buttonLayout)