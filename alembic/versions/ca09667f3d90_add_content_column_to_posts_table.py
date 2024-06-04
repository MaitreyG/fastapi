"""add content column to posts table

Revision ID: ca09667f3d90
Revises: 3090c0750bcc
Create Date: 2024-06-04 13:19:51.670205

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ca09667f3d90'
down_revision: Union[str, None] = '3090c0750bcc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
