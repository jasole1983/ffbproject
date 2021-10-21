from flask import Blueprint, jsonify, request
from app.models import Roster, Player, db

roster_routes = Blueprint('rosters', __name__)

@roster_routes.route('/')
def rosters():
    rosters = Roster.query.all()
    return {'rosters': [{roster.id: roster.to_dict(), 'players': roster.players} for roster in rosters]}

@roster_routes.route('/add/<int:rid>/<int:id>', methods=['PUT'])
def add_player_roster(rid, id):
    player = Player.query.get(str(id))
    setattr(player, 'status', 'ROSTER')
    setattr(player, 'roster_id', rid)
    roster = Roster.query.get(rid)
    new_roster = roster.players.append(player)
    setattr(roster, 'players', new_roster)
    db.session.commit()
    return {roster.id: roster.to_dict()}

@roster_routes.route('/drop/<int:rid>/<int:id>', methods=['PUT'])
def drop_player_roster(rid, id):
    roster = Roster.query.get(rid)
    roster_player_ids = roster.to_dict().players
    pid = roster_player_ids.pop(roster_player_ids.find(str(id)))
    player = Player.query.get(pid)
    holder = roster.players.pop(roster.players.find(player))
    new_roster = roster.players
    setattr(player, 'status', 'LOCKED')
    setattr(player, 'roster_id', None)
    setattr(roster, 'players', new_roster)
    db.session.commit()
    return {roster.id: roster.to_dict()}

@roster_routes.route('/lineup/<int:id>', methods=['PUT'])
def set_lineup(id):
    roster = Roster.query.get(id)
    player_ids = roster.players
    starters = []
    nonstarters = []
    for pid in player_ids:
        player = Player.query.get(pid)
        if player.player_id in request.form:
            setattr(player, 'starter', True)
            starters.append(player)
        else:
            setattr(player, 'starter', False)
            nonstarters.append(player)
    db.session.commit()
            