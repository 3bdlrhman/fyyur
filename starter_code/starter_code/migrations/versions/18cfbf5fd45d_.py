"""empty message

Revision ID: 18cfbf5fd45d
Revises: c30ccec9a827
Create Date: 2021-01-23 21:15:08.458492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18cfbf5fd45d'
down_revision = 'c30ccec9a827'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('show',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('show')
    # ### end Alembic commands ###