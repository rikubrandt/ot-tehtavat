from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from gui.components.mainwindow import Ui_Notes


class MainWindow(QMainWindow, Ui_Notes):
    def __init__(self, note_service):
        super().__init__()
        self.setupUi(self)

        self.note_service = note_service
        self.add_button = self.findChild(QPushButton, "pushButton")
        self.search_button = self.findChild(QPushButton, "pushButton_2")
        self.delete_button = self.findChild(QPushButton, "pushButton_3")
        self.textfield = self.findChild(QTextEdit, "textEdit")
        self.listview = self.findChild(QListWidget, "listWidget")

        self.add_button.clicked.connect(self.add_note)
        self.delete_button.clicked.connect(self.delete_note)
        self.search_button.clicked.connect(self.search)
        self.show_notes(self.setup_notes())

    def setup_notes(self):
        return self.note_service.get_notes()

    def show_notes(self, notes):
        self.listview.clear()
        if notes is not None:
            for row in notes:
                item = QListWidgetItem(row["time"]+" "+row["text"])
                item.setData(Qt.UserRole, row["id"])
                self.listview.addItem(item)

    def add_note(self):
        text = self.textfield.toPlainText()
        self.note_service.create_note(text)
        self.show_notes(self.setup_notes())
        self.textfield.clear()

    def delete_note(self):
        note = self.listview.selectedItems()[0]
        id = int(note.data(Qt.UserRole))
        self.note_service.delete_note(id)
        self.show_notes(self.setup_notes())

    def search(self):
        text = self.textfield.toPlainText()
        if text and not text.isspace():

            # Search for tag
            if len(text.split()) == 1 and text[0] == "#":
                self.show_notes(self.note_service.search_by_tag(text))
            else:
                self.show_notes(self.note_service.search_by_keyword(text))
        else:
            self.show_notes(self.setup_notes())
