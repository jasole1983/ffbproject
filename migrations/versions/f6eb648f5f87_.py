"""empty message

Revision ID: f6eb648f5f87
Revises: 
Create Date: 2021-10-22 21:13:59.838281

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6eb648f5f87'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rosters',
    sa.Column('id', sa.String(length=75), nullable=False),
    sa.Column('week', sa.String(length=35), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('franchises',
    sa.Column('id', sa.String(length=65), nullable=False),
    sa.Column('roster_id', sa.String(length=75), nullable=True),
    sa.Column('name', sa.String(length=75), nullable=True),
    sa.Column('abbr', sa.String(length=35), nullable=True),
    sa.Column('wins', sa.Integer(), nullable=True),
    sa.Column('losses', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['roster_id'], ['rosters.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('players',
    sa.Column('player_id', sa.String(length=76), nullable=False),
    sa.Column('name', sa.String(length=75), nullable=False),
    sa.Column('position', sa.String(length=25), nullable=False),
    sa.Column('team', sa.String(length=25), nullable=False),
    sa.Column('draft_year', sa.String(length=74), nullable=False),
    sa.Column('draft_round', sa.String(length=25), nullable=True),
    sa.Column('draft_team', sa.String(length=25), nullable=True),
    sa.Column('draft_pick', sa.String(length=3), nullable=True),
    sa.Column('college', sa.String(length=25), nullable=True),
    sa.Column('height', sa.String(length=73), nullable=True),
    sa.Column('weight', sa.String(length=73), nullable=True),
    sa.Column('jersey', sa.String(length=72), nullable=True),
    sa.Column('birthdate', sa.String(length=70), nullable=True),
    sa.Column('rotoworld_id', sa.String(length=75), nullable=True),
    sa.Column('rotowire_id', sa.String(length=75), nullable=True),
    sa.Column('stats_id', sa.String(length=75), nullable=True),
    sa.Column('stats_global_id', sa.String(length=75), nullable=True),
    sa.Column('espn_id', sa.String(length=75), nullable=True),
    sa.Column('sportsdata_id', sa.String(length=75), nullable=True),
    sa.Column('cbs_id', sa.String(length=25), nullable=True),
    sa.Column('nfl_id', sa.String(length=35), nullable=True),
    sa.Column('fleaflicker_id', sa.String(length=25), nullable=True),
    sa.Column('twitter_username', sa.String(length=75), nullable=True),
    sa.Column('status', sa.Enum('FA', 'ROSTER', 'INJURED_RESERVE', 'LOCKED', 'PLAYED', name='STATUS'), nullable=True),
    sa.Column('starter', sa.Boolean(), nullable=True),
    sa.Column('roster_id', sa.String(length=75), nullable=True),
    sa.ForeignKeyConstraint(['roster_id'], ['rosters.id'], ),
    sa.PrimaryKeyConstraint('player_id'),
    sa.UniqueConstraint('player_id')
    )
    op.create_table('player_score',
    sa.Column('player_id', sa.String(length=76), nullable=False),
    sa.Column('week', sa.String(length=35), nullable=False),
    sa.Column('score', sa.String(length=35), nullable=True),
    sa.Column('available', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['player_id'], ['players.player_id'], ),
    sa.PrimaryKeyConstraint('player_id', 'week')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('player_score')
    op.drop_table('players')
    op.drop_table('franchises')
    op.drop_table('rosters')
    # ### end Alembic commands ###
