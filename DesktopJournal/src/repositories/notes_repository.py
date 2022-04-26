
import datetime


class NotesRepository:

    def __init__(self, connection):
        self.connection = connection

    def get_all_notes(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, text, time FROM notes WHERE visible = 1")
        rows = cursor.fetchall()
        return rows

    def add_note(self, note):
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
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, name FROM tags")
        rows = cursor.fetchall()
        return rows

    def get_notes_by_tag(self, tag):
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
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT id, text, time FROM notes WHERE text LIKE ?", ("%"+keyword+"%",))
        return cursor.fetchall()

    def delete_note(self, note_id):
        cursor = self.connection.cursor()
        cursor.execute(
            "UPDATE notes SET visible = FALSE WHERE id = ?", (note_id,))
        self.connection.commit()
