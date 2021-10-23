from typing import Sequence
from .db import db
import datetime

class Player(db.Model):
    __tablename__ = 'players'

    player_id = db.Column(db.String(76), primary_key=True, unique=True)
    name = db.Column(db.String(75), nullable=False)
    position = db.Column(db.String(25), nullable=False)
    team = db.Column(db.String(25), nullable=False)
    draft_year = db.Column(db.String(74), nullable=False)
    draft_round = db.Column(db.String(25))
    draft_team = db.Column(db.String(25))
    draft_pick = db.Column(db.String(3))
    college = db.Column(db.String(25))
    height = db.Column(db.String(73))
    weight = db.Column(db.String(73))
    jersey = db.Column(db.String(72))
    birthdate = db.Column(db.String(70))
    rotoworld_id = db.Column(db.String(75))
    rotowire_id = db.Column(db.String(75))
    stats_id = db.Column(db.String(75))
    stats_global_id = db.Column(db.String(75))
    espn_id = db.Column(db.String(75))
    sportsdata_id = db.Column(db.String(75))
    cbs_id = db.Column(db.String(25))
    nfl_id = db.Column(db.String(35))
    fleaflicker_id = db.Column(db.String(25))
    twitter_username = db.Column(db.String(75))
    status = db.Column(db.Enum("FA", "ROSTER", "INJURED_RESERVE", "LOCKED", "PLAYED", name='STATUS'), default="FA")
    starter = db.Column(db.Boolean, nullable=True, default=None)
    roster_id = db.Column(db.String(75), db.ForeignKey('rosters.id'), nullable=True)
    roster = db.relationship("Roster", back_populates="rplayers")
    player_scores = db.relationship("PlayerScore", backref=db.backref('players', lazy=True))

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
            'starter': self.starter,
            'rosterId': self.roster_id,
        }
