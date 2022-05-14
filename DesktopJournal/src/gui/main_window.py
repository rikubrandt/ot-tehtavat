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
        self.export_button = self.findChild(QPushButton, "pushButton_4")
        self.textfield = self.findChild(QTextEdit, "textEdit")
        self.listview = self.findChild(QListWidget, "listWidget")
        self.listview.setWordWrap(True)
        self.add_button.clicked.connect(self.add_note)
        self.delete_button.clicked.connect(self.delete_note)
        self.search_button.clicked.connect(self.search)
        self.export_button.clicked.connect(self.export)

        self.show_notes(self.setup_notes())

    def setup_notes(self):
        return self.note_service.get_notes()

    def show_notes(self, notes):
        self.listview.clear()
        if notes is not None:
            for row in notes:
                time = row["time"][:16]
                item = QListWidgetItem(time + " " + row["text"])
                item.setData(Qt.UserRole, row["id"])
                self.listview.addItem(item)

    def add_note(self):
        text = self.textfield.toPlainText()
        if text == "":
            return
        self.note_service.create_note(text)
        self.show_notes(self.setup_notes())
        self.textfield.clear()

    def delete_note(self):
        note = self.listview.selectedItems()[0]
        id = int(note.data(Qt.UserRole))
        self.note_service.delete_note(id)
        self.show_notes(self.setup_notes())

    def search(self):
        if self.textfield.toPlainText() == "":
            return
        if self.search_button.text() == "Search":
            self.search_button.setText("Show Notes")
            text = self.textfield.toPlainText()
            if text and not text.isspace():

                # Search by tag
                if len(text.split()) == 1 and text[0] == "#":
                    self.show_notes(self.note_service.search_by_tag(text))
                else:
                    self.show_notes(self.note_service.search_by_keyword(text))
        else:
            self.search_button.setText("Search")
            self.textfield.setText("")
            self.show_notes(self.setup_notes())

    def export(self):
        #note_file = self.note_service.export_notes()
        filter = "Text Files (*.txt)"

        export_dialog = QFileDialog()
        export_dialog.setWindowTitle('Export')
        export_dialog.setAcceptMode(QFileDialog.AcceptSave)
        export_dialog.setNameFilter(filter)
        export_dialog.setDefaultSuffix('txt')

        if export_dialog.exec_() == QFileDialog.Accepted:
            self.note_service.export_notes(export_dialog.selectedFiles()[0])
