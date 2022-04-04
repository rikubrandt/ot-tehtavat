



class NotesRepository:
    
    def __init__(self, connection):
        self.connection = connection

    def get_all_notes(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, text, time FROM notes WHERE visible = 1")
        rows = cursor.fetchall()
        return rows


    def add_note(self, text, tags):
        cursor = self.connection.cursor()
        cursor.execute("""
        INSERT INTO notes(text, time) VALUES(?, DateTime("now"))
        """, text)
        
        #TODO insert tags
        if tags:
            pass
        
        self.connection.commit()

    