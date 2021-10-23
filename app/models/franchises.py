from typing import Sequence
from .db import db

class Franchise(db.Model):
    __tablename__ = 'franchises'

    id = db.Column(db.String(6), primary_key=True)
    # user_id = db.Column(db.String(6), db.ForeignKey('users.id'), nullable=False)
    # users = db.relationship("User", backref=db.backref('franchises', lazy=True))
    roster_id = db.Column(db.Integer, db.ForeignKey('rosters.id'), nullable=False)
    # draft_results = db.Column(db.Integer, db.ForeignKey('drafts.id'))
    # future_picks = db.Column(db.Integer, db.ForeignKey('future_picks.id'))
    # watch_list = db.Column(db.Integer, db.ForeignKey('watch_lists.id'))
    posts = db.relationship("Post", backref=db.backref('franchises', lazy=True))
    comments = db.relationship("Comment", backref=db.backref('franchises', lazy=True))
    # schedule_id = db.Column(db.Integer, db.ForeignKey('schedules.id'))
    name = db.Column(db.String(75), nullable=False)
    abbr = db.Column(db.String(3), nullable=False)
    # weekly_results_id = db.Column(db.Integer, db.ForeignKey('weekly_results.id'))
    wins = db.Column(db.Integer, nullable=True)
    losses = db.Column(db.Integer, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'rosterId': self.roster_id,
            'posts': self.posts,
            'comments': self.comments,
            'name': self.name,
            'abbr': self.abbr,
            'wins': self.wins,
            'losses': self.losses
        }
