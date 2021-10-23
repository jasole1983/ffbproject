from typing import Sequence
from .db import db
from .posts import Post
from .comments import Comment

class Franchise(db.Model):
    __tablename__ = 'franchises'

    id = db.Column(db.String(65), primary_key=True)
    # user_id = db.Column(db.String(6), db.ForeignKey('users.id'), nullable=False)
    # users = db.relationship("User", backref=db.backref('franchises', lazy=True))
    roster_id = db.Column(db.String(75), db.ForeignKey('rosters.id'))
    roster = db.relationship("Roster", back_populates="franchise", uselist=False)
    # draft_results = db.Column(db.Integer, db.ForeignKey('drafts.id'))
    # future_picks = db.Column(db.Integer, db.ForeignKey('future_picks.id'))
    # watch_list = db.Column(db.Integer, db.ForeignKey('watch_lists.id'))
    posts = db.relationship("Post", order_by=Post.create_date, back_populates="franchise")
    comments = db.relationship("Comment", order_by=Comment.create_date, back_populates="franchise")
    # schedule_id = db.Column(db.Integer, db.ForeignKey('schedules.id'))
    # roster = db.relationship('Roster', backref=db.backref('franchises', lazy=True))
    name = db.Column(db.String(75))
    abbr = db.Column(db.String(35))
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
