
import datetime


class NotesRepository:
    """Class that is responsible for operations to the database.
    """

    def __init__(self, connection):
        """Initializes the connetion to database

        Args:
            connection: Sqlite3 database connection.
        """
        self.connection = connection

    def get_all_notes(self):
        """Returns all visible notes

        Returns:
            rows: Sqlite3 object containing all notes.
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, text, time FROM notes WHERE visible = 1")
        rows = cursor.fetchall()
        return rows

    def add_note(self, note):
        """Adds new note to the database.

        Args:
            note: Note object

        Returns:
            note_id: Id of the created note.
        """
        text = note.text

        cursor = self.connection.cursor()
        cursor.execute("""
        INSERT INTO notes (text, time) VALUES(?, ?);
        """, (text, datetime.datetime.now()))
        note_id = cursor.lastrowid
        if note.tags:
            for tag in note.tags:
                cursor.execute(
                    "SELECT id FROM tags WHERE name = ?", (tag,))
                tag_id = cursor.fetchone()

                if tag_id is None:
                    cursor.execute("INSERT INTO tags(name) VALUES (?)", (tag,))
                    tag_id = cursor.lastrowid
                else:
                    tag_id = tag_id["id"]
                cursor.execute(
                    "INSERT INTO note_tags(note_id, tag_id) VALUES (?, ?)", (note_id, tag_id))

        self.connection.commit()
        return note_id

    def get_all_tags(self):
        """Returns all created tags.

        Returns:
            rows: Sqlite3 object containing all tags.
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, name FROM tags")
        rows = cursor.fetchall()
        return rows

    def get_notes_by_tag(self, tag):
        """Returns all notes with given tag.

        Args:
            tag: Tag in string format

        Returns:
            notes: All notes that have the given tag.
        """
    
        cursor = self.connection.cursor()

        cursor.execute("SELECT id FROM tags WHERE name = ?", (tag[1:],))
        tag_id = cursor.fetchone()

        if tag_id:
            cursor.execute("""SELECT n.id, n.text, n.time FROM notes n, note_tags nt
                            WHERE n.id = nt.note_id AND n.visible = TRUE
                             AND nt.tag_id = ?""", (tag_id[0],))
            return cursor.fetchall()
        return None

    def get_notes_by_keyword(self, keyword):
        """Returns all notes with given keyword.

        Args:
            keyword: Keyword in string format

        Returns:
            notes: All notes that have the given keyword.
        """
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT id, text, time FROM notes WHERE text LIKE ?", ("%"+keyword+"%",))
        return cursor.fetchall()

    def delete_note(self, note_id):
        """Deletes the given note.

        Args:
            note_id: Id of the note to be deleted.
        """
        cursor = self.connection.cursor()
        cursor.execute(
            "UPDATE notes SET visible = FALSE WHERE id = ?", (note_id,))
        self.connection.commit()
