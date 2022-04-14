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

        self.show_notes()

    def setup_notes(self):
        return self.note_service.get_notes()

    def show_notes(self):
        self.listview.clear()
        notes = self.setup_notes()
        for row in notes:
            item = QListWidgetItem(row["time"]+" "+row["text"])
            item.setData(Qt.UserRole, row["id"])
            self.listview.addItem(item)

    def add_note(self):
        text = self.textfield.toPlainText()
        self.note_service.create_note(text)
        self.show_notes()
        self.textfield.clear()

    def delete_note(self):
        note = self.listview.selectedItems()[0]
        id = int(note.data(Qt.UserRole))
        self.note_service.delete_note(id)
        self.show_notes()
        

    def search(self):
        #TODO
        pass

