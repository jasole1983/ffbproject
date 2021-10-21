from typing import Sequence
from .db import db

class PlayerScore(db.Model):
    __tablename__ = 'player_score'

    player_id = db.Column(db.String(6), db.ForeignKey('players.player_id'), primary_key=True)
    one = db.Column(db.Integer, nullable=True, default=None)
    two = db.Column(db.Integer, nullable=True, default=None)
    three = db.Column(db.Integer, nullable=True, default=None)
    four = db.Column(db.Integer, nullable=True, default=None)
    five = db.Column(db.Integer, nullable=True, default=None)
    six = db.Column(db.Integer, nullable=True, default=None)
    seven = db.Column(db.Integer, nullable=True, default=None)
    eight = db.Column(db.Integer, nullable=True, default=None)
    nine = db.Column(db.Integer, nullable=True, default=None)
    ten = db.Column(db.Integer, nullable=True, default=None)
    eleven = db.Column(db.Integer, nullable=True, default=None)
    twelve = db.Column(db.Integer, nullable=True, default=None)
    thirteen = db.Column(db.Integer, nullable=True, default=None)
    forteen = db.Column(db.Integer, nullable=True, default=None)
    fifteen = db.Column(db.Integer, nullable=True, default=None)
    sixteen = db.Column(db.Integer, nullable=True, default=None)
    seventeen = db.Column(db.Integer, nullable=True, default=None)
    eighteen = db.Column(db.Integer, nullable=True, default=None)
    
    def to_dict(self):
        weeks = [self.one, self.two, self.three, self.four, self.five, self.six, self.seven, self.eight, self.nine, self.ten, self.eleven, self.twelve, self.thirteen, self.forteen, self.fifteen, self.sixteen, self.seventeen, self.eighteen]
        ytd = sum(weeks)
        return {
            'id': self.player_id,
            'one': self.one,
            'two': self.two,
            'three': self.three,
            'four': self.four,
            'five': self.five,
            'six': self.six,
            'seven': self.seven,
            'eight': self.eight,
            'nine': self.nine,
            'ten': self.ten,
            'eleven': self.eleven,
            'twelve': self.twelve,
            'thirteen': self.thirteen,
            'forteen': self.forteen,
            'fifteen': self.fifteen,
            'sixteen': self.sixteen,
            'seventeen': self.seventeen,
            'eighteen': self.eighteen,
            'ytd': ytd,
        }