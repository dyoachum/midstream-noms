"""empty message

Revision ID: 82b0d66a1419
Revises: 114ab22aea72
Create Date: 2021-01-11 19:26:22.816623

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82b0d66a1419'
down_revision = '114ab22aea72'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('nom', sa.Column('contract_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'nom', 'contract', ['contract_id'], ['contract_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'nom', type_='foreignkey')
    op.drop_column('nom', 'contract_id')
    # ### end Alembic commands ###
