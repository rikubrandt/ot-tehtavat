
from repositories.notes_repository import NotesRepository
from db_connection import get_database_connection
from entities.note import Note


class NotesService:
    """Class that is responsible for the logic operations.
    """

    def __init__(self):
        """ Constructor that initializes the database connection
        and creates NotesRepository object.
        """
        self.connection = get_database_connection()
        self.notes_repository = NotesRepository(self.connection)

    def create_note(self, content):
        """ Creates new note.

        Args:
            content: String that contains the note text

        Returns:
            id: Note's id
        """
        # Creates tags from the text
        tags = [tag.strip("#")
                for tag in content.split() if tag.startswith("#")]
        note = Note(content, tags)

        return self.notes_repository.add_note(note)

    def get_notes(self):
        """Returns all notes from that are visible

        Returns:
            Notes: Object of all the notes.
        """
        return self.notes_repository.get_all_notes()

    def get_tags(self):
        """Returns all the tags in the database

        Returns:
            Tags: Object of all the tags.
        """
        return self.notes_repository.get_all_tags()

    def delete_note(self, note_id):
        """Deletes the note based on id.

        Args:
            note_id: Id of the note.
        """
        self.notes_repository.delete_note(note_id)


    def search(self, text):
        """Returns search by keyword or search by tags based on the text.

        Args:
            text: Given search parameter
        """
        # Search by tag if given one word that start with-#
        if len(text.split()) == 1 and text[0] == "#":
            return self.search_by_tag(text)
            
        return self.search_by_keyword(text)

    def search_by_tag(self, tag):
        """Returns all the notes with given tag.

        Args:
            tag: Tag in string format.

        Returns:
            Notes: All notes that have the given tag.
        """
        return self.notes_repository.get_notes_by_tag(tag)

    def search_by_keyword(self, keyword):
        """Returns all the notes that match the keyword.

        Args:
            keyword: keyword in string format.

        Returns:
            Notes: All notes that have the given keyword.
        """
        return self.notes_repository.get_notes_by_keyword(keyword)

    def export_notes(self, path):
        """Writes all the notes in the database to text file and saves it as txt.

        Args:
            path: Path where the file is to be saved.
        """
        notes = self.notes_repository.get_all_notes()
        string_notes = ""
        for row in notes:
            note = f"{row[2]} {row[1]} \n"
            string_notes += note

        with open(path, "w", encoding="utf_8") as file:
            file.write(string_notes)
            file.close()
