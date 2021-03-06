"""empty message

Revision ID: aa398a034551
Revises: 9aa173aec503
Create Date: 2018-04-07 08:54:26.217359

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'aa398a034551'
down_revision = '9aa173aec503'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mahasiswa',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nim', sa.String(length=50), nullable=False),
    sa.Column('nama', sa.String(length=1), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('ayam')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ayam',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('jenis', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('kelamin', mysql.VARCHAR(length=1), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('mahasiswa')
    # ### end Alembic commands ###
