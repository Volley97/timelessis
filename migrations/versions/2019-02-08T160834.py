"""empty message

Revision ID: e5e5a7184121
Revises: ce1494a8b1f3
Create Date: 2019-02-08 16:08:34.266608+00:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e5e5a7184121'
down_revision = 'ce1494a8b1f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('table_shapes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('picture', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('test',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('comments',
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('updated_on', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.Column('body', sa.String(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('employee', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['employee'], ['employees.id'], ),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dates',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('scheme_condition_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['scheme_condition_id'], ['scheme_conditions.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('date')
    )
    op.create_table('monthdays',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('monthday', sa.Integer(), nullable=False),
    sa.Column('scheme_condition_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['scheme_condition_id'], ['scheme_conditions.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('monthday')
    )
    op.create_table('weekdays',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('weekday', sa.Integer(), nullable=False),
    sa.Column('scheme_condition_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['scheme_condition_id'], ['scheme_conditions.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('weekday')
    )
    op.create_table('tables',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('floor_id', sa.Integer(), nullable=True),
    sa.Column('x', sa.Integer(), nullable=False),
    sa.Column('y', sa.Integer(), nullable=False),
    sa.Column('width', sa.Integer(), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('max_capacity', sa.Integer(), nullable=False),
    sa.Column('multiple', sa.Boolean(), nullable=True),
    sa.Column('playstation', sa.Boolean(), nullable=True),
    sa.Column('shape_id', sa.Integer(), nullable=True),
    sa.Column('min_capacity', sa.Integer(), nullable=True),
    sa.Column('deposit_hour', sa.Integer(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['deposit_hour'], ['scheme_types.id'], ),
    sa.ForeignKeyConstraint(['floor_id'], ['floors.id'], ),
    sa.ForeignKeyConstraint(['min_capacity'], ['scheme_types.id'], ),
    sa.ForeignKeyConstraint(['shape_id'], ['table_shapes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('companies', 'updated_on',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('employees', 'updated_on',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.add_column('locations', sa.Column('closed_days', sa.Integer(), nullable=True))
    op.add_column('locations', sa.Column('synchronized_on', sa.DateTime(), nullable=True))
    op.add_column('locations', sa.Column('working_hours', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'locations', 'scheme_types', ['closed_days'], ['id'])
    op.create_foreign_key(None, 'locations', 'scheme_types', ['working_hours'], ['id'])
    op.alter_column('reservation_settings', 'updated_on',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('reservation_settings', 'updated_on',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.drop_constraint(None, 'locations', type_='foreignkey')
    op.drop_constraint(None, 'locations', type_='foreignkey')
    op.drop_column('locations', 'working_hours')
    op.drop_column('locations', 'synchronized_on')
    op.drop_column('locations', 'closed_days')
    op.alter_column('employees', 'updated_on',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('companies', 'updated_on',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.drop_table('tables')
    op.drop_table('weekdays')
    op.drop_table('monthdays')
    op.drop_table('dates')
    op.drop_table('comments')
    op.drop_table('test')
    op.drop_table('table_shapes')
    # ### end Alembic commands ###
