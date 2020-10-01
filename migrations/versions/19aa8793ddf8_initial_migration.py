"""Initial Migration

Revision ID: 19aa8793ddf8
Revises: 9efe632c9da2
Create Date: 2020-10-01 11:27:10.886365

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19aa8793ddf8'
down_revision = '9efe632c9da2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cases', sa.Column('status_id', sa.Integer(), nullable=True))
    op.add_column('cases', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'cases', 'statuses', ['status_id'], ['id'])
    op.create_foreign_key(None, 'cases', 'users', ['user_id'], ['id'])
    op.add_column('users', sa.Column('role_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'roles', ['role_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'role_id')
    op.drop_constraint(None, 'cases', type_='foreignkey')
    op.drop_constraint(None, 'cases', type_='foreignkey')
    op.drop_column('cases', 'user_id')
    op.drop_column('cases', 'status_id')
    # ### end Alembic commands ###
