
import sys
from services.notes_service import NotesService
from db_connection import get_database_connection
from PyQt5.QtWidgets import QApplication

from gui.main_window import MainWindow


def main():
    note_service = NotesService()
    app = QApplication(sys.argv)
    mainwindow = MainWindow(note_service)
    mainwindow.show()
    app.exec_()


if __name__ == "__main__":
    main()
