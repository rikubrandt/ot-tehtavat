
from db_connection import get_database_connection
import os

def execute_sql_file(file, conn):
    cursor = conn.cursor()
    sql_file = open(file)
    file = sql_file.read()
    cursor.executescript(file)
    conn.commit()
    
def init_db():
    path = os.path.dirname(__file__)
    conn = get_database_connection()
    execute_sql_file(path + "/schema.sql", conn)

    # Adds some test data for now.
    execute_sql_file(path + "/populate.sql", conn)


if __name__ == "__main__":
    init_db()
