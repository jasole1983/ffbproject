from app.api.user_routes import validation_errors_to_error_messages
from flask import Blueprint, jsonify, request
from app.models import Comment, db
from app.forms.comment_form import MakeComment
import time

comment_routes = Blueprint('comments', __name__)

@comment_routes.route('/')
def comments():
    '''
    load all comments
    '''
    comments = Comment.query.all()
    return {'comments': [{comment.id: comment.to_dict()} for comment in comments]}

@comment_routes.route('/', methods=['POST'])
def create_comment():
    '''
    make new comment
    '''
    form = MakeComment()
    if form.validate_on_submit:
        comment = Comment(
            post_id=form.data['post'],
            body=form.data['body'],
            franchise_id=form.data['franchise'],
            modify_date=form.data['modify_date'],
            create_date=time.time(),            
        )
        db.session.add(comment)
        db.session.commit()
        return {'comment':{comment.id: comment.to_dict()}}
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401

@comment_routes.route('/<int:id>', methods=['PUT'])
def update_comment(id):
    '''
    modify existing comment
    '''
    comment = Comment.query.get(id)
    for key, val in request.body:
        setattr(comment, key, val)
    db.session.commit()
    return {'comment': {comment.id: comment.to_dict()}}

@comment_routes.route('/<int:id>', methods=['DELETE'])
def delete_comment(id):
    '''
    delete existing comment
    '''
    comment = Comment.query.get(id)
    cid = {'comment': comment.id}
    db.session.delete(comment)
    db.session.commit()
    return cid
        
    
    