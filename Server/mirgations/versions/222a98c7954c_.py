"""empty message

Revision ID: 222a98c7954c
Revises: 
Create Date: 2024-07-05 14:12:38.073050

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '222a98c7954c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('game',
                    sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
                    sa.Column('player', sa.String(), nullable=False),
                    sa.Column('date', sa.String, server_default=sa.text("CURRENT_TIMESTAMP"),
                              nullable=False),
                    sa.Column('result', sa.Integer(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade() -> None:
    pass
