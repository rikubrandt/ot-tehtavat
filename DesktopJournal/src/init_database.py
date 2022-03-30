
from db_connection import get_database_connection


def clear_tables(conn):
    cursor = conn.cursor()
    cursor.executescript("""
    DROP TABLE IF EXISTS notes;
    DROP TABLE IF EXISTS tags;
    DROP TABLE IF EXISTS note_tags;
    """)
    conn.commit()

def init_tables(conn):
    cursor = conn.cursor()
    cursor.executescript("""
    CREATE TABLE notes(
    id SERIAL PRIMARY KEY,
    text TEXT,
    time TIMESTAMP,
    visible BOOLEAN DEFAULT TRUE
    )

    CREATE TABLE tags(
        id SERIAL PRIMARY KEY,
        name TEXT
    )

    CREATE TABLE note_tags(
        note_id INTEGER NOT NULL,
        tag_id INTEGER NOT NULL,
        PRIMARY KEY (note_id, tag_id)
    )
    """)
    conn.commit()

def execute_sql_file(file, conn):
    cursor = conn.cursor()
    sql_file = open(file)
    file = sql_file.read()
    cursor.executescript(file)
    conn.commit()
    
def init_db():
    conn = get_database_connection()
    execute_sql_file("schema.sql", conn)
    execute_sql_file("populate.sql", conn)


if __name__ == "__main__":
    init_db()
