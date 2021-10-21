from flask import Blueprint, jsonify, request
from app.models import Player, db
from app.config import eng

player_routes = Blueprint('players', __name__)

@player_routes.route('/')
def players():
    players = Player.query.all()
    return {'players': [{player.player_id: player.to_dict()} for player in players]}

@player_routes.route('/<int:id>')
def player(id):
    player = Player.query.get(str(id))
    return {player.player_id: player.to_dict()}

@player_routes.route('/update/<int:id>', methods=['PUT'])
def update_player(id):
    player = Player.query.get(str(id))
    for key, value in request.form:
        setattr(player, key, value)
    db.session.commit()
    return {player.player_id: player.to_dict()}

# @player_routes.route('/add/<int:id>', methods=['PUT'])
# def roster_player(id):
#     player = Player.query.get(str(id))
#     player.status = 'ROSTER'
#     db.session.commit()
#     return {player.player_id: player.to_dict()}