from flask.cli import AppGroup
# from .players import seed_players, undo_players
# from .rosters import seed_rosters, undo_rosters
from .posts import seed_posts, undo_posts

seed_commands = AppGroup('seed')

@seed_commands.command('all')
def seed():
    # seed_players()
    # seed_rosters()
    seed_posts()
   
@seed_commands.command('undo')
def undo():
    # undo_players()
    # undo_rosters()
    undo_posts()
   