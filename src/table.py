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
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tableModel.select()
        headers = ("ID", "Name", "Job", "Email")
        for columnIndex, header in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)
        return tableModel
