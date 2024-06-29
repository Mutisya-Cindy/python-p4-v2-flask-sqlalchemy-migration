"""rename department

Revision ID: b7bea126d452
Revises: 8990f60b5dab
Create Date: 2024-06-29 23:41:39.445062

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7bea126d452'
down_revision = '8990f60b5dab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
