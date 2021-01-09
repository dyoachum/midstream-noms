"""empty message

Revision ID: 5d4a9ca351a1
Revises: 1728a1d15570
Create Date: 2021-01-09 16:34:03.982367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d4a9ca351a1'
down_revision = '1728a1d15570'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('role', sa.Boolean(), nullable=True))
    op.drop_column('user', 'admin')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('admin', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('user', 'role')
    # ### end Alembic commands ###
