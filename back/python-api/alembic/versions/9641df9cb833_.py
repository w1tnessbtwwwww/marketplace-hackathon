"""empty message

Revision ID: 9641df9cb833
Revises: 5ac29ce5453f
Create Date: 2024-11-30 22:04:48.405419

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9641df9cb833'
down_revision: Union[str, None] = '5ac29ce5453f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('items_productCategoryId_fkey', 'items', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('items_productCategoryId_fkey', 'items', 'product_categories', ['productCategoryId'], ['productCategoryId'])
    # ### end Alembic commands ###