
from services.notes_service import NotesService




class MainView:
    def __init__(self, root):
        self.root = root
        self.notes_service = NotesService()


    def get_notes(self):
        return self.notes_service.get_notes()
