"""empty message

Revision ID: 89bc01020df5
Revises: 
Create Date: 2024-11-30 12:20:06.850459

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '89bc01020df5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('orderId', sa.Integer(), nullable=False),
    sa.Column('productId', sa.BigInteger(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('orderedAt', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['productId'], ['items.productId'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.userId'], ),
    sa.PrimaryKeyConstraint('orderId')
    )
    op.add_column('items', sa.Column('rating', sa.Float(), nullable=True))
    op.add_column('items', sa.Column('reviews', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('items', 'reviews')
    op.drop_column('items', 'rating')
    op.drop_table('orders')
    # ### end Alembic commands ###