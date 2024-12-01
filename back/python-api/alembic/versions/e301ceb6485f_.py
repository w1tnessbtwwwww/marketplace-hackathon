"""empty message

Revision ID: e301ceb6485f
Revises: eac68a9bac3e
Create Date: 2024-11-30 21:57:32.709056

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e301ceb6485f'
down_revision: Union[str, None] = 'eac68a9bac3e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product_categories',
    sa.Column('productCategoryId', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('productCategoryId')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_categories')
    # ### end Alembic commands ###