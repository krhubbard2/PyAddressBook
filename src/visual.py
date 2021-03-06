# Kelby Hubbard
# Started: 2021-11-05
# Updated: 
# visual.py

# GUI for PyAddressBook


from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlQueryModel
from PyQt5.QtWidgets import (
    QGridLayout,
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
    QLabel,
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
        self.label = QLabel('Search:', self)
        self.searchBar = QLineEdit()
        # TODO: Make working search bar
        self.searchBar.setText("Under Construction...")
        # self.searchBar.textChanged.connect(self.search)

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
        searchLayout = QHBoxLayout()
        searchLayout.addWidget(self.label)
        searchLayout.addWidget(self.searchBar)
        tableLayout = QVBoxLayout()
        tableLayout.addWidget(self.table)
        gridLayout = QGridLayout()
        gridLayout.addLayout(searchLayout, 0, 0)
        gridLayout.addLayout(tableLayout, 1, 0)
        gridLayout.addLayout(buttonLayout, 0, 1)
        gridLayout.setRowStretch(1,4)
        self.layout.addLayout(gridLayout)

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
        self.phoneField = QLineEdit()
        self.phoneField.setObjectName("Phone Number")
        self.addressField = QLineEdit()
        self.addressField.setObjectName("Address")
        self.cityField = QLineEdit()
        self.cityField.setObjectName("City")
        self.stateField = QLineEdit()
        self.stateField.setObjectName("State")
        # Data Fields Layout
        layout = QFormLayout()
        layout.addRow("Name:", self.nameField)
        layout.addRow("Job:", self.jobField)
        layout.addRow("Email:", self.emailField)
        layout.addRow("Phone Number:", self.phoneField)
        layout.addRow("Address:", self.addressField)
        layout.addRow("City", self.cityField)
        layout.addRow("State:", self.stateField)
        
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
        if not self.nameField.text() or not self.emailField.text():
            QMessageBox.critical(
                    self,
                    "Error!",
                    f"You must provide at least contact's name and email.",
                )
            self.data = None 
            return

        for field in (self.nameField, self.jobField, self.emailField, self.phoneField, self.addressField, self.cityField, self.stateField):
            self.data.append(field.text())

        if not self.data:
            return

        super().accept()

