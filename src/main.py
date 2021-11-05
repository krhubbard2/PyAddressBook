# Kelby Hubbard
# Started: 2021-11-05
# Updated: 
# main.py

# Main source file for PyAddressBook

import sys

from PyQt5.QtWidgets import QApplication
from .visual import Window

# Main function for PyAddressBook
def main():
    # Create application
    app = QApplication(sys.argv)
    # Create main window
    main_window = Window()
    main_window.show()
    # Run main loop
    sys.exit(app.exec())
