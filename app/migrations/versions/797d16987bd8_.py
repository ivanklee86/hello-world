"""empty message

Revision ID: 797d16987bd8
Revises: 169c4c3be518
Create Date: 2018-08-15 09:01:39.558602

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '797d16987bd8'
down_revision = '169c4c3be518'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('publisher', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('book', 'publisher')
    # ### end Alembic commands ###
