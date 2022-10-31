"""empty message

Revision ID: ca018e16f0f7
Revises: 
Create Date: 2022-10-25 13:59:15.329938

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca018e16f0f7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('companies',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=140), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('war_name', sa.String(length=50), nullable=True),
    sa.Column('role', sa.String(length=50), nullable=True),
    sa.Column('identification', sa.String(length=13), nullable=True),
    sa.Column('admission', sa.String(length=10), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.Column('for_print', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employees')
    op.drop_table('companies')
    # ### end Alembic commands ###