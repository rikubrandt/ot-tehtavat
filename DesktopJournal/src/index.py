
import sys
from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow

from services.notes_service import NotesService


def main():
    note_service = NotesService()
    app = QApplication(sys.argv)
    mainwindow = MainWindow(note_service)
    mainwindow.show()
    app.exec_()


if __name__ == "__main__":
    main()
