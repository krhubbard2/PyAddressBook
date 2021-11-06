# Kelby Hubbard
# Started: 2021-11-05
# Updated: 
# table.py

from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel

class ContactsTableModel:
    def __init__(self):
        self.model = self._createModel()


    @staticmethod
    # Create and set up table model
    def _createModel():
        tableModel = QSqlTableModel()
        tableModel.setTable("contacts")
        # Saves any changes immediately
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tableModel.select()
        headers = ("ID", "Name", "Job", "Email", "Phone Number", "Address", "City", "State")
        for columnIndex, header in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)
        return tableModel
    
    # Add contact to db
    def addContact(self, data):
        rows = self.model.rowCount()
        self.model.insertRows(rows, 1)
        for column, field in enumerate(data):
            self.model.setData(self.model.index(rows, column + 1), field)
        self.model.submitAll()
        self.model.select()
    
    # Delete contact from db
    def deleteContact(self, data):
        self.model.removeRow(data)
        self.model.submitAll()
        self.model.select()
