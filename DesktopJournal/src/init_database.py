import os
from db_connection import get_database_connection


def execute_sql_file(file, conn):
    """Executes given sql-files.

    Args:
        file: File's path.
        conn: Connection to the database.
    """
    cursor = conn.cursor()
    with open(file, encoding="utf_8") as sql_file:
        file = sql_file.read()
        cursor.executescript(file)
        conn.commit()


def init_db():
    """Initializes the database tables.
    """
    path = os.path.dirname(__file__)
    conn = get_database_connection()
    execute_sql_file(path + "/schema.sql", conn)

    # Adds some test data for now.
    execute_sql_file(path + "/populate.sql", conn)


if __name__ == "__main__":
    init_db()
