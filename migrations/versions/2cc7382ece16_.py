"""empty message

Revision ID: 2cc7382ece16
Revises: 35ca503dc164
Create Date: 2020-10-15 16:15:57.489195

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2cc7382ece16'
down_revision = '35ca503dc164'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cliente', sa.Column('data_nascimento', sa.Date(), nullable=False))
    op.alter_column('cliente', 'nome_completo',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=50),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('cliente', 'nome_completo',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=50),
               nullable=True)
    op.drop_column('cliente', 'data_nascimento')
    # ### end Alembic commands ###
