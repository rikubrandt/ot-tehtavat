
from services.notes_service import NotesService
from db_connection import get_database_connection

#from ui.main_ui import MainUI


def main():

    # Gui not done this has to do.
    n = NotesService()
    rows = n.get_notes()
    for row in rows:
        print(row["id"], row["text"])

if __name__ == "__main__":
    main()

