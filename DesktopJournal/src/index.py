
from repositories.notes_repository import NotesRepository
from db_connection import get_database_connection

from ui.main_ui import MainUi


def main():
    conn = get_database_connection()
    n = NotesRepository(conn)
    rows = n.get_all_notes()
    for row in rows:
        print(row["id"])

if __name__ == "__main__":
    main()

