"""empty message

Revision ID: 68c6aa3581bd
Revises: 0440054220fc
Create Date: 2021-03-19 02:18:22.300436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68c6aa3581bd'
down_revision = '0440054220fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('podcast', sa.Column('duration', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('podcast', 'duration')
    # ### end Alembic commands ###
