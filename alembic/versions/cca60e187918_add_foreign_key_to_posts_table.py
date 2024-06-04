"""add foreign key to posts table

Revision ID: cca60e187918
Revises: ca22a607ad66
Create Date: 2024-06-04 13:35:03.795425

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cca60e187918'
down_revision: Union[str, None] = 'ca22a607ad66'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('owner_id',sa.Integer,nullable=False))
    op.create_foreign_key('post_users_fk',source_table="posts",referent_table="users",local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk',table_name="posts")
    op.drop_column('posts','owner_id')
    pass
