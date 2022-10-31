"""Minor Changes

Revision ID: 8daf634f0b32
Revises: d56cdc537086
Create Date: 2022-10-31 09:19:47.463903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8daf634f0b32'
down_revision = 'd56cdc537086'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('products_asin_key', 'products', type_='unique')
    op.drop_constraint('reviews_asin_key', 'reviews', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('reviews_asin_key', 'reviews', ['asin'])
    op.create_unique_constraint('products_asin_key', 'products', ['asin'])
    # ### end Alembic commands ###