from typing import Sequence
from .db import db

class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    franchise_id = db.Column(db.String(65), db.ForeignKey('franchises.id'))
    franchise = db.relationship("Franchise", back_populates="comments")
    body = db.Column(db.Text)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    post = db.relationship("Post", back_populates="comments")
    create_date = db.Column(db.String(75))
    modify_date = db.Column(db.String(75))

    def to_dict(self):
        return {
            "id": self.id,
            "franchise": self.franchise.name,
            "body": self.body,
            "postId": self.post_id,
            "created": self.create_date,
            "modified": self.modify_date,
        }