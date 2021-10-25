from typing import Sequence
from .db import db
from .comments import Comment

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    franchise_id = db.Column(db.String(65), db.ForeignKey('franchises.id'))
    franchise = db.relationship("Franchise", back_populates="posts")
    title = db.Column(db.String(225))
    body = db.Column(db.Text)
    comments = db.relationship("Comment", back_populates="post")
    create_date = db.Column(db.String(75))
    modify_date = db.Column(db.String(75))

    def to_dict(self):
        comments = [comment.id for comment in self.comments]
        franchise = self.franchise.name
        post = {
            "id": self.id,
            "franchise": franchise,
            "title": self.title,
            "body": self.body,
            "comments": comments,
            "created": self.create_date,
            "modified": self.modify_date,
        }
        return post