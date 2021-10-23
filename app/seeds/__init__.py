from flask.cli import AppGroup
# from .players import seed_players, undo_players
from .rosters import seed_rosters, undo_rosters

seed_commands = AppGroup('seed')

@seed_commands.command('all')
def seed():
    # seed_players()
    seed_rosters()
   
@seed_commands.command('undo')
def undo():
    # undo_players()
    undo_rosters()
   