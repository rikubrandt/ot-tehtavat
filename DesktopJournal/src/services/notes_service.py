
from repositories.notes_repository import NotesRepository
from db_connection import get_database_connection
from entities.note import Note




class NotesService:

    def __init__(self):
        self.connection = get_database_connection()
        self.notes_repository = NotesRepository(self.connection)


    def create_note(self, content):

        # Creates tags from the text
        tags = [tag.strip("#") for tag in content.split() if tag.startswith("#")]
        note = Note(content, tags)

        return self.notes_repository.add_note(note)

    def get_notes(self):
        return self.notes_repository.get_all_notes()
        
    def get_tags(self):
        return self.notes_repository.get_all_tags()