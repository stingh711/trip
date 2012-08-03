# -*- coding: utf-8 -*-

from flask.ext.sqlalchemy import SQLAlchemy
from trip import app

db = SQLAlchemy(app)

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(10))
    choice = db.Column(db.Integer)
    ip = db.Column(db.String(20))

    def __init__(self, name, choice, ip):
        self.name = name
        self.choice = choice
        self.ip = ip

    def __repr__(self):
        return "<Vote %r>" % self.name
