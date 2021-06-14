"""empty message

Revision ID: 340edc1fcec9
Revises: 2dd20b0337db
Create Date: 2021-06-14 14:53:24.736476

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '340edc1fcec9'
down_revision = '2dd20b0337db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dislikes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dislikes', sa.Integer(), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitch.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('likes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('likes', sa.Integer(), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitch.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('pitch', 'dislikes')
    op.drop_column('pitch', 'likes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitch', sa.Column('likes', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('pitch', sa.Column('dislikes', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_table('likes')
    op.drop_table('dislikes')
    # ### end Alembic commands ###