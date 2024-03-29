"""empty message

Revision ID: 35ca503dc164
Revises: dede0dae9ecc
Create Date: 2020-10-15 16:12:19.461510

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35ca503dc164'
down_revision = 'dede0dae9ecc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cliente',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome_completo', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('veiculo',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('modelo', sa.String(length=50), nullable=False),
    sa.Column('cor', sa.Enum('vermelho', 'preto', 'amarelo', 'prata', 'branco', 'azul', name='corescarro'), nullable=False),
    sa.Column('marca', sa.String(length=30), nullable=False),
    sa.Column('potencia', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('veiculo')
    op.drop_table('cliente')
    # ### end Alembic commands ###
