from config import CONN, CURSOR
# from . import CURSOR
# from . import CURSOR


class Song:
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS songs(
        id INTEGER PRMARY KEY,
        name TEXT,
        album TEXT
        )
        
        """

        CURSOR.execute(sql)

    def save(self):
        sql = """
        INSERT INTO songs (name,album)
        VALUES(?,?)
        """

        CURSOR.execute(sql, (self.name, self.album))
        self.id = CURSOR.execute(
            "SELECT last_insert_rowid() FROM songs").fetchone()[0]
