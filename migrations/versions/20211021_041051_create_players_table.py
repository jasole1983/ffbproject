"""create players table

Revision ID: 36362e6e8cf5
Revises: 
Create Date: 2021-10-21 04:10:51.842175

"""
from sqlalchemy.sql.schema import PrimaryKeyConstraint
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36362e6e8cf5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('players',
    sa.Column('player_id', sa.String(6), primary_key=True),
    sa.Column('name', sa.String(75), nullable=False),
    sa.Column('position', sa.String(5), nullable=False),
    sa.Column('team', sa.String(5), nullable=False),
    sa.Column('draft_year', sa.String(4), nullable=False),
    sa.Column('draft_round', sa.String(5)),
    sa.Column('draft_team', sa.String(5)),
    sa.Column('draft_pick', sa.String(3)),
    sa.Column('college', sa.String(25)),
    sa.Column('height', sa.String(3)),
    sa.Column('weight', sa.String(3)),
    sa.Column('jersey', sa.String(2)),
    sa.Column('birthday', sa.String(12)),
    sa.Column('rotoworld_id', sa.String(15)),
    sa.Column('rotowire_id', sa.String(15)),
    sa.Column('stats_id', sa.String(15)),
    sa.Column('stats_global_id', sa.String(17)),
    sa.Column('espn_id', sa.String(18)),
    sa.Column('sportsdata_id', sa.String(75)),
    sa.Column('cbs_id', sa.String(25)),
    sa.Column('nfl_id', sa.String(35)),
    sa.Column('fleaflicker_id', sa.String(25)),
    sa.Column('twitter_username', sa.String(75)),
    sa.Column('status', sa.String(15)),
    sa.PrimaryKeyConstraint('player_id')
    )


def downgrade():
    op.drop_table('players')
