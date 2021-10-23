from typing import Sequence
from .db import db
import datetime

class Player(db.Model):
    __tablename__ = 'players'

    player_id = db.Column(db.String(6), primary_key=True)
    name = db.Column(db.String(75), nullable=False)
    position = db.Column(db.String(5), nullable=False)
    team = db.Column(db.String(5), nullable=False)
    draft_year = db.Column(db.String(4), nullable=False)
    draft_round = db.Column(db.String(5))
    draft_team = db.Column(db.String(5))
    draft_pick = db.Column(db.String(3))
    college = db.Column(db.String(25))
    height = db.Column(db.String(3))
    weight = db.Column(db.String(3))
    jersey = db.Column(db.String(2))
    birthdate = db.Column(db.String(10))
    rotoworld_id = db.Column(db.String(5))
    rotowire_id = db.Column(db.String(15))
    stats_id = db.Column(db.String(5))
    stats_global_id = db.Column(db.String(7))
    espn_id = db.Column(db.String(8))
    sportsdata_id = db.Column(db.String(75))
    cbs_id = db.Column(db.String(25))
    nfl_id = db.Column(db.String(35))
    fleaflicker_id = db.Column(db.String(25))
    twitter_username = db.Column(db.String(75))
    status = db.Column(db.String(15))

    def to_dict(self):
        name = self.name
        name_break_index = name.find(",")
        last_name = name[0:name_break_index]
        first_name = name[(name_break_index + 1):len(name)]
        birthday = int(self.birthdate)
        bday = datetime.date.fromtimestamp(birthday)
        h_int = int(self.height)
        height = str(h_int // 12) + "' " + str(h_int % 12) + '"'
        return {
            'id': self.player_id,
            'lastName': last_name,
            'firstName': first_name,
            'position': self.position,
            'birthday': bday,
            'height': height,
            'weight': self.weight,
            'jersey': self.jersey,
            'college': self.college,
            'team': self.team,
            'draftTeam': self.draft_team,
            'draftYear': self.draft_year,
            'draftRound': self.draft_round,
            'draftPick': self.draft_pick,
            'status': self.status,
            'twitter': self.twitter_username,
        }
