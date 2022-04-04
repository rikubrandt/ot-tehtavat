
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
        id = cursor.execute("""
        INSERT INTO notes (text, time) VALUES(?, ?);
        """, (text, datetime.datetime.now()))
        
        #TODO insert tags
        if note.tags:
            pass
        
        self.connection.commit()
        return cursor.lastrowid
    