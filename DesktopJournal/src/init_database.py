
from db_connection import get_database_connection


def clear_tables(conn):
    cursor = conn.cursor()
    cursor.execute("""
    DROP TABLE IF EXISTS notes CASCADE;
    DROP TABLE IF EXISTS tags CASCADE;
    DROP TABLE IF EXISTS note_tags CASCADE;
    """)
    conn.commit()

def init_tables(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE notes(
    id SERIAL PRIMARY KEY,
    text TEXT,
    time TIMESTAMP,
    visible BOOLEAN DEFAULT TRUE,
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

def init_db():
    conn = get_database_connection()
    clear_tables()
    init_tables()


if __name__ == "__main__":
    init_db()
    