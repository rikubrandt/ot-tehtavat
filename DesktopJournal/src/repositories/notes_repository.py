



class NotesRepository:
    
    def __init__(self, connection):
        self.connection = connection

    def get_all_notes(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, text, time FROM notes WHERE visible = 1")
        rows = cursor.fetchall()
        return rows
