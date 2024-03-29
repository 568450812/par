"""empty message

Revision ID: 8e31d2fc6afd
Revises: 
Create Date: 2019-06-03 20:05:38.181619

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e31d2fc6afd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('parks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pname', sa.String(length=100), nullable=False),
    sa.Column('address', sa.String(length=100), nullable=False),
    sa.Column('pnum', sa.Integer(), nullable=False),
    sa.Column('price', sa.DECIMAL(precision=2, scale=1), nullable=True),
    sa.Column('coordi_x', sa.DECIMAL(precision=4, scale=2), nullable=False),
    sa.Column('coordi_y', sa.DECIMAL(precision=4, scale=2), nullable=False),
    sa.Column('addtime', sa.DateTime(), nullable=True),
    sa.Column('is_Active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('address'),
    sa.UniqueConstraint('coordi_y'),
    sa.UniqueConstraint('pname')
    )
    op.create_index(op.f('ix_parks_addtime'), 'parks', ['addtime'], unique=False)
    op.create_table('record',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uname', sa.String(length=100), nullable=False),
    sa.Column('pname', sa.String(length=100), nullable=False),
    sa.Column('addtime', sa.DateTime(), nullable=True),
    sa.Column('startT', sa.DateTime(), nullable=False),
    sa.Column('endT', sa.DateTime(), nullable=False),
    sa.Column('totalT', sa.String(length=100), nullable=False),
    sa.Column('spend', sa.DECIMAL(precision=5, scale=2), nullable=False),
    sa.Column('is_Delete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('pname'),
    sa.UniqueConstraint('uname')
    )
    op.create_table('tourist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('addtime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uname', sa.String(length=100), nullable=False),
    sa.Column('pwd1', sa.String(length=100), nullable=False),
    sa.Column('pwd2', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('phone', sa.String(length=11), nullable=False),
    sa.Column('ucard', sa.String(length=100), nullable=False),
    sa.Column('addtime', sa.DateTime(), nullable=True),
    sa.Column('is_Active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('ucard'),
    sa.UniqueConstraint('uname')
    )
    op.create_index(op.f('ix_users_addtime'), 'users', ['addtime'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_addtime'), table_name='users')
    op.drop_table('users')
    op.drop_table('tourist')
    op.drop_table('record')
    op.drop_index(op.f('ix_parks_addtime'), table_name='parks')
    op.drop_table('parks')
    # ### end Alembic commands ###
