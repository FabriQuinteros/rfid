"""empty message

Revision ID: 0ba9a275769b
Revises: 
Create Date: 2019-09-06 14:19:55.648645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ba9a275769b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('respuesta',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pregunta', sa.Integer(), nullable=True),
    sa.Column('respuesta', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_respuesta_pregunta'), 'respuesta', ['pregunta'], unique=False)
    op.create_index(op.f('ix_respuesta_respuesta'), 'respuesta', ['respuesta'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_respuesta_respuesta'), table_name='respuesta')
    op.drop_index(op.f('ix_respuesta_pregunta'), table_name='respuesta')
    op.drop_table('respuesta')
    # ### end Alembic commands ###
