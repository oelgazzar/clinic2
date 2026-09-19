import sqlite3
from pathlib import Path

class Database:
    def __init__(self, path):
        self.connection = sqlite3.connect(path)

    def init_schema(self):
        schema_path = Path(__file__).parent / "schema.sql"
        with open(schema_path) as f:
            schema = f.read()
            with self.connection as con:
                con.executescript(schema)


if __name__ == '__main__':
    db = Database("storage/clinic.db")
    db.init_schema()
    print(__file__)