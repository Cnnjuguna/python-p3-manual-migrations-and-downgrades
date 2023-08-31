"""Renaming students to scholars

Revision ID: 3f2547b881b5
Revises: 791279dd0760
Create Date: 2023-08-31 15:11:16.788360

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3f2547b881b5"
down_revision = "791279dd0760"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table("students", "scholars")


def downgrade() -> None:
    op.rename_table("scholars", "students")
