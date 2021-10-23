from flask import Blueprint, jsonify, request
from app.models import Post, db
import time

post_routes = Blueprint('posts', __name__)

@post_routes.route('/')
def posts():
    posts = Post.query.all()
    return {'posts': [{post.id: post.to_dict()} for post in posts]}

@post_routes.route('/', methods=['POST'])
def create_post():
