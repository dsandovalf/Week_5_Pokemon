"""empty message

Revision ID: 9d4f0209204a
Revises: 0380f303ed35
Create Date: 2021-10-28 16:08:11.061435

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d4f0209204a'
down_revision = '0380f303ed35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.String(length=200), nullable=True))
    op.drop_column('user', 'passwor')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('passwor', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    op.drop_column('user', 'password')
    # ### end Alembic commands ###
