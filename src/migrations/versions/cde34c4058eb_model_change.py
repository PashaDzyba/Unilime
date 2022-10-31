"""Model Change

Revision ID: cde34c4058eb
Revises: e94f179cfb3b
Create Date: 2022-10-31 10:48:48.808499

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cde34c4058eb'
down_revision = 'e94f179cfb3b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_product_review_id', table_name='product_review')
    op.drop_table('product_review')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product_review',
    sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('reviews_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], name='product_review_product_id_fkey'),
    sa.ForeignKeyConstraint(['reviews_id'], ['reviews.id'], name='product_review_reviews_id_fkey')
    )
    op.create_index('ix_product_review_id', 'product_review', ['id'], unique=False)
    # ### end Alembic commands ###