import sqlite3


class LunchDB(object):
    def __init__(self):
        self.curs = self.init_db()

    def init_db(self):
        conn = sqlite3.connect('lunchtime.db')
        conn.text_factory = str
        curs = conn.cursor()

        #curs.execute("DELETE FROM places;")

        places = [
            ('Troll', 'Trollownia', 1),
            ('Chińczyk', 'Chińczykownia', 1),
            ('Spacja', 'Na dole', 1),
        ]

        curs.executemany(
            "INSERT INTO places(name, description, open) VALUES(?, ?, ?)",
            places
        )
        return curs
