"""empty message

Revision ID: 3df46b8bf4ff
Revises: e5e5a7184121
Create Date: 2019-02-08 16:12:45.882731+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3df46b8bf4ff'
down_revision = 'e5e5a7184121'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('test')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='test_pkey'),
    sa.UniqueConstraint('name', name='test_name_key')
    )
    # ### end Alembic commands ###
