"""Model Change

Revision ID: 82d3d9682ade
Revises: ce54b466f4b9
Create Date: 2022-10-31 14:34:22.330595

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82d3d9682ade'
down_revision = 'ce54b466f4b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('reviews_product_id_fkey', 'reviews', type_='foreignkey')
    op.drop_column('reviews', 'product_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('reviews_product_id_fkey', 'reviews', 'products', ['product_id'], ['id'])
    # ### end Alembic commands ###