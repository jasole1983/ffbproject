from typing import Sequence
from .db import db

class PlayerScore(db.Model):
    __tablename__ = 'player_score'

    player_id = db.Column(db.String(76), db.ForeignKey('players.player_id'), primary_key=True)
    week = db.Column(db.String(35), primary_key=True)
    score = db.Column(db.String(35))
    available = db.Column(db.Boolean)
    
    def to_dict(self):

        return {
            'id': self.player_id,
            'week': self.week,
            'score': self.score,
            'available': self.available,
        }