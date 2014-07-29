#!/usr/bin/env python
# -*- coding: utf8 -*-


import sqlite3
from flask import Flask
from flask.ext import restful
from collections import defaultdict


app = Flask(__name__)
api = restful.Api(app)


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


class HelloWorld(restful.Resource, LunchDB):
    def get(self):
        places = defaultdict(tuple)
        for place in self.curs.execute('SELECT * FROM places;'):
            places[place[0]] = place[1:]
        return places


if __name__ == '__main__':
    api.add_resource(HelloWorld, '/')
    app.run(debug=True)
