import os
import sqlite3



def get_database_connection():
    dirname = os.path.dirname(__file__)
    connection = sqlite3.connect(os.path.join(dirname, "database.db"))
    connection.row_factory = sqlite3.Row
    return connection

