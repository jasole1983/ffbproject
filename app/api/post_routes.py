from app.api.user_routes import validation_errors_to_error_messages
from flask import Blueprint, jsonify, request
from app.models import Post, db
from app.forms.post_form import MakePost
from app.api.comment_routes import delete_comment
import time

post_routes = Blueprint('posts', __name__)

@post_routes.route('/')
def posts():
    '''
    load all posts
    '''
    posts = Post.query.all()
    return {'posts': [{post.id: post.to_dict()} for post in posts]}

@post_routes.route('/', methods=['POST'])
def create_post():
    '''
    make new post
    '''
    form = MakePost()
    if form.validate_on_submit:
        post = Post(
            title=form.data['title'],
            body=form.data['body'],
            franchise_id=form.data['franchise'],
            modify_date=form.data['modify_date'],
            create_date=time.time(),            
        )
        db.session.add(post)
        db.session.commit()
        return {'post':{post.id: post.to_dict()}}
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401

@post_routes.route('/<int:id>', methods=['PUT', 'DELETE'])
def update_post(id):
    '''
    modify existing Post
    '''
    post = Post.query.get(id)
    if request.method == 'DELETE':
        list = [{'post': post.id}]
        for comment in post.comments:
            list.append(delete_comment(comment.id))
        db.session.delete(post)
        db.session.commit()
        return 
    elif request.method == 'PUT':
        for key, val in request.body:
            setattr(post, key, val)
        db.session.commit()
        return {'post': {post.id: post.to_dict()}}
    else:
        return {'errors': 'Error! Please double check fetch method'}, 401