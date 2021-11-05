# Kelby Hubbard
# Started: 2021-11-05
# Updated: 
# database.py

# Used to provide connection to database

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

# Create contacts table in database
def createContactsTable():
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            name VARCHAR(40) NOT NULL,
            job VARCHAR(50),
            email VARCHAR(40) NOT NULL
        )
        """
    )

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
    
    createContactsTable()
    return True