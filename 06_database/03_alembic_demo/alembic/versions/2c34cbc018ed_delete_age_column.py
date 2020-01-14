"""delete age column

Revision ID: 2c34cbc018ed
Revises: 8a0638123e1f
Create Date: 2017-11-03 16:15:52.714645

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2c34cbc018ed'
down_revision = '8a0638123e1f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'age')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('age', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
