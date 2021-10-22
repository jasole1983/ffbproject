from typing import Sequence
from .db import db

class Roster(db.Model):
    __tablename__ = 'rosters'

    id = db.Column(db.Integer, primary_key=True)
    franchise_id = db.Column(db.Integer, db.ForeignKey('franchises.id'), nullable=False, unique=True)
    week = db.Column(db.String(3), nullable=True)
    player_id = db.Column(db.string(6), db.ForeignKey('players.player_id'))
    players = db.relationship("Player", backref=db.backref('rosters', lazy=True))

    def to_dict(self):
        players = self.players
        plyrs = [player.id for player in players if player.status != "INJURED_RESERVED"]
        # while len(plyrs) < 46:
        #     plyrs.append('EMPTY')
        reserves = [player.id for player in players if player.status == "INJURED_RESERVE"]
        # while len(reserves) < 2:
        #     reserves.append('EMPTY')
        return {
            'id': self.id,
            'week': self.week,
            'franchiseId': self.franchise_id,
            'players': plyrs,
            'injuredReserve': reserves,
            # 'playerOne': plyrs[0],
            # 'playerTwo': plyrs[1],
            # 'playerThree': plyrs[2],
            # 'playerFour': plyrs[3],
            # 'playerFive': plyrs[4],
            # 'playerSix': plyrs[5],
            # 'playerSeven': plyrs[6],
            # 'playerEight': plyrs[7],
            # 'playerNine': plyrs[8],
            # 'playerTen': plyrs[9],
            # 'playerEleven': plyrs[10],
            # 'playerTwelve': plyrs[11],
            # 'playerThirteen': plyrs[12],
            # 'playerFourteen': plyrs[13],
            # 'playerFifteen': plyrs[14],
            # 'playerSixteen': plyrs[15],
            # 'playerSeventeen': plyrs[16],
            # 'playerEighteen': plyrs[17],
            # 'playerNineteen': plyrs[18],
            # 'playerTwenty': plyrs[19],
            # 'playerTwentyOne': plyrs[20],
            # 'playerTwentyTwo': plyrs[21],
            # 'playerTwentyThree': plyrs[22],
            # 'playerTwentyFour': plyrs[23],
            # 'playerTwentyFive': plyrs[24],
            # 'playerTwentySix': plyrs[25],
            # 'playerTwentySeven': plyrs[26],
            # 'playerTwentyEight': plyrs[27],
            # 'playerTwentyNine': plyrs[28],
            # 'playerThirty': plyrs[29],
            # 'playerThirtyOne': plyrs[30],
            # 'playerThirtyTwo': plyrs[31],
            # 'playerThirtyThree': plyrs[32],
            # 'playerThirtyFour': plyrs[33],
            # 'playerThirtyFive': plyrs[34],
            # 'playerThirtySix': plyrs[35],
            # 'playerThirtySeven': plyrs[36],
            # 'playerThirtyEight': plyrs[37],
            # 'playerThirtyNine': plyrs[38],
            # 'playerForty': plyrs[39],
            # 'playerFortyOne': plyrs[40],
            # 'playerFortyTwo': plyrs[41],
            # 'playerFortyThree': plyrs[42],
            # 'playerFortyFour': plyrs[43],
            # 'playerFortyFive': plyrs[44],
            # 'playerFortySix': plyrs[45],
            # 'reserveOne': reserves[0],
            # 'reserveTwo': reserves[1],
        }