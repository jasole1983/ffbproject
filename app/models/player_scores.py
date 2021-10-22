from typing import Sequence
from .db import db

class PlayerScore(db.Model):
    __tablename__ = 'player_score'

    player_id = db.Column(db.String(6), db.ForeignKey('players.player_id'), primary_key=True)
    week = db.Column(db.String(3), primary_key=True)
    score = db.Column(db.String(3))
    available = db.Column(db.Boolean)
    
    def to_dict(self):
        pscores = PlayerScore.query.filter_by(player_id=self.player_id).all()
        weekly = [pscore.score for pscore in pscores if pscore.week <= self.week]        
        ytd = sum(weekly)
        return {
            'id': self.player_id,
            'week': self.week,
            'score': self.score,
            'available': self.available,
            'ytd': ytd,
        }