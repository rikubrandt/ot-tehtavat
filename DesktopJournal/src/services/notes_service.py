
from repositories.notes_repository import NotesRepository
from db_connection import get_database_connection
from entities.note import Note


class NotesService:

    def __init__(self):
        self.connection = get_database_connection()
        self.notes_repository = NotesRepository(self.connection)

    def create_note(self, content):

        # Creates tags from the text
        tags = [tag.strip("#")
                for tag in content.split() if tag.startswith("#")]
        note = Note(content, tags)

        return self.notes_repository.add_note(note)

    def get_notes(self):
        return self.notes_repository.get_all_notes()

    def get_tags(self):
        return self.notes_repository.get_all_tags()

    def delete_note(self, note_id):
        return self.notes_repository.delete_note(note_id)

    def search_by_tag(self, tag):
        return self.notes_repository.get_notes_by_tag(tag)

    def search_by_keyword(self, keyword):
        return self.notes_repository.get_notes_by_keyword(keyword)


    def export_notes(self, path):
        notes = self.notes_repository.get_all_notes()
        string_notes = ""
        for row in notes:
            note = "{timestamp} {text} \n".format(timestamp=row[2], text=row[1])
            string_notes += note
            
        file = open(path, "w")
        file.write(string_notes)
        file.close()