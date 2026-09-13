import sqlite3

class DatabaseManager():
    def __init__(self, db_filepath: str):
        self._db_filepath = db_filepath
