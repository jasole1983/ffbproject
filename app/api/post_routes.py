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
    print(posts)
    return {"posts":[post.to_dict() for post in posts]}

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
        return {post.id: post.to_dict()}
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401

@post_routes.route('/<int:id>', methods=['PUT', 'DELETE'])
def update_post(id):
    '''
    modify existing Post
    '''
    p = Post.query.get(id)
    if request.method == 'DELETE':
        list = [{'post': p.id}]
        for comment in p.comments:
            list.append(delete_comment(comment.id))
        db.session.delete(p)
        db.session.commit()
        return {'Deleted Items': list}
    elif request.method == 'PUT':
        for key, val in request.body:
            setattr(p, key, val)
        db.session.commit()
        return {'post': p.to_dict()}
    else:
        return {'errors': 'Error! Please double check fetch method'}, 401