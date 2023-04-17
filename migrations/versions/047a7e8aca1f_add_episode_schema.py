"""add episode schema

Revision ID: 047a7e8aca1f
Revises: 227403ad98ec
Create Date: 2023-04-17 20:54:32.305110

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '047a7e8aca1f'
down_revision = '227403ad98ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('episode',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('season_number', sa.Integer(), nullable=True),
    sa.Column('episode_number', sa.Integer(), nullable=True),
    sa.Column('first_aired', sa.Date(), nullable=True),
    sa.Column('director', sa.String(length=80), nullable=True),
    sa.Column('episode_name', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('episode')
    # ### end Alembic commands ###
