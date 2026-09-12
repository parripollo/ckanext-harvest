"""add the harvest_queue table (database queue backend)

Revision ID: a1b2c3d4e5f6
Revises: 75d650dfd519
Create Date: 2026-09-12 20:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "a1b2c3d4e5f6"
down_revision = "75d650dfd519"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "harvest_queue",
        sa.Column("id", sa.UnicodeText, primary_key=True),
        sa.Column("routing_key", sa.UnicodeText, nullable=False),
        sa.Column("body", sa.UnicodeText, nullable=False),
        sa.Column("created", sa.DateTime),
        sa.Column("claimed", sa.DateTime, nullable=True),
    )
    op.create_index("ix_harvest_queue_routing_key", "harvest_queue",
                    ["routing_key"])


def downgrade():
    op.drop_index("ix_harvest_queue_routing_key", table_name="harvest_queue")
    op.drop_table("harvest_queue")
