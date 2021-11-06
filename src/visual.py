# Kelby Hubbard
# Started: 2021-11-05
# Updated: 
# visual.py

# GUI for PyAddressBook
# This application uses and requires PyQt (PyQt5)

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QWidget,    
    QAbstractItemView,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QLineEdit,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QMessageBox,
)

from .table import ContactsTableModel

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

        self.contactsTableModel = ContactsTableModel()
        self.initUI()

    # Initialize main window UI
    def initUI(self):
        # Create Search Bar Widget
        self.searchBar = QLineEdit("Search")

        # Create Table View Widget
        self.table = QTableView()
        self.table.setModel(self.contactsTableModel.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)

        # Create Buttons
        self.addButton = QPushButton("Add Contact")
        self.addButton.clicked.connect(self.openAddDialog)
        self.deleteButton = QPushButton("Delete")
        self.deleteButton.clicked.connect(self.deleteContact)
        
        # GUI Layout
        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(self.addButton)
        buttonLayout.addWidget(self.deleteButton)
        buttonLayout.addStretch()
        layout = QVBoxLayout()
        layout.addWidget(self.searchBar)
        layout.addWidget(self.table)
        self.layout.addLayout(layout)
        self.layout.addLayout(buttonLayout)
    
    def openAddDialog(self):
        dialog = AddDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.contactsTableModel.addContact(dialog.data)
            self.table.resizeColumnsToContents()
    
    def deleteContact(self):
        row = self.table.currentIndex().row()
        if row < 0:
            return
        
        messageBox = QMessageBox.warning(
            self,
            "Delete Contact",
            "Are you sure you'd like to remove the selected contact?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            self.contactsTableModel.deleteContact(row)

# Add contact dialog
class AddDialog(QDialog):
    
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("Add Contact")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None

        self.setupUI()

    # Sets up Add Contact Dialog GUI
    def setupUI(self):
        self.nameField = QLineEdit()
        self.nameField.setObjectName("Name")
        self.jobField = QLineEdit()
        self.jobField.setObjectName("Job")
        self.emailField = QLineEdit()
        self.emailField.setObjectName("Email")
        # Data Fields Layout
        layout = QFormLayout()
        layout.addRow("Name:", self.nameField)
        layout.addRow("Job:", self.jobField)
        layout.addRow("Email:", self.emailField)
        self.layout.addLayout(layout)
        # Add standard buttons to the dialog and connect them
        self.buttonsBox = QDialogButtonBox(self)
        self.buttonsBox.setOrientation(Qt.Horizontal)
        self.buttonsBox.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        self.buttonsBox.accepted.connect(self.accept)
        self.buttonsBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonsBox)
    
    def accept(self):
        """Accept the data provided through the dialog."""
        self.data = []
        for field in (self.nameField, self.jobField, self.emailField):
            if not field.text():
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"You must provide a contact's {field.objectName()}",
                )
                self.data = None  # Reset .data
                return

            self.data.append(field.text())

        if not self.data:
            return

        super().accept()

