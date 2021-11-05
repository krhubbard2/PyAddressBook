# Kelby Hubbard
# Started: 2021-11-05
# Updated: 
# database.py

# Used to provide connection to database

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase

# Create / open db connection
def createConnection(dbName):
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(dbName)

    # If db connection fails
    if not connection.open():
        QMessageBox.warning(
            None,
            "PyAddressBook",
            f"Database Error: {connection.lastError().text()}",
        )
        return False
        
    return True