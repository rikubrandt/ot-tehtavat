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
        self.textfield = self.findChild(QTextEdit, "textEdit")
        self.listview = self.findChild(QListWidget, "listWidget")

        notes = self.setupNotes()

        self.showNotes(notes)

    def setupNotes(self):
        return self.note_service.get_notes()

    def showNotes(self, notes):
        for row in notes:
            self.listview.addItem(row["time"]+" "+row["text"])

    def addNote(self):
        pass
