"""add few columns to posts table

Revision ID: 929a221cc534
Revises: cca60e187918
Create Date: 2024-06-04 13:41:46.327209

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '929a221cc534'
down_revision: Union[str, None] = 'cca60e187918'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column(
        'published',sa.Boolean(),nullable=False,server_default='TRUE'
    ),)
    op.add_column('posts',sa.Column(
        'created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('NOW()')
    ),)
    pass


def downgrade() -> None:
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
