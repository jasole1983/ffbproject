from flask import Blueprint, jsonify, request
from app.models import PlayerScore, Player, db

pscore_routes = Blueprint('pscore', __name__)

@pscore_routes.route('/')
def player_scores():
    player_scores = PlayerScore.query.all()
    return {'pScores': [{player_score.player_id: player_score.to_dict} for player_score in player_scores]}

@pscore_routes.route('/update/<int:week>', methods=['PUT'])
def update_player_scores(week):    
    pscores = PlayerScore.query.filter_by(week='week').all()
    for key, value in request.form:
        for pscore in pscores:
            setattr(pscore, key, value)
    db.session.commit()
    return {'message': 'updated'}


        


    
    