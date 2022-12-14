"""Model Change

Revision ID: 4516b91ced1b
Revises: 34c6659c25c6
Create Date: 2022-10-31 16:37:34.123182

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4516b91ced1b'
down_revision = '34c6659c25c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product_review', sa.Column('id', sa.Integer(), nullable=False))
    op.create_index(op.f('ix_product_review_id'), 'product_review', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_product_review_id'), table_name='product_review')
    op.drop_column('product_review', 'id')
    # ### end Alembic commands ###
