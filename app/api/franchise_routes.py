from flask import Blueprint, jsonify, request
from app.models import Franchise, db

franchise_routes = Blueprint('franchises', __name__)

@franchise_routes.route('/')
def franchises():
    franchises = Franchise.query.all()
    return ('franchises': [{franchise.id: franchise.to_dict()} for franchise in franchises ])

@franchise_routes.route('/<int:id>')
def franchise(id):
    franchise = Franchise.query.get(id)
    return ('frinchise': {franchise.id: franchise.to_dict()}) 